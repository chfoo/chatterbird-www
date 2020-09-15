import argparse
import fcntl
import glob
import logging
import os
import re
import subprocess
import sys
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import signal

_logger = logging.getLogger()


def main():
    logging.basicConfig(level=logging.INFO)

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('screenshots_dir')
    arg_parser.add_argument('--s3config', required=True)
    arg_parser.add_argument('--dry-run', action='store_true')

    args = arg_parser.parse_args()

    try:
        lock_file = open('/var/tmp/chatterbird_image_uploader.lock', 'wb')
        fcntl.flock(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        _logger.exception("failed to lock")
        sys.exit(1)

    exit_code = 0
    try:
        process_files(args)
    except Exception:
        _logger.exception('processing error')
        exit_code = 1
        fcntl.flock(lock_file, fcntl.LOCK_UN)
        lock_file.close()

    _logger.info("exiting.")
    sys.exit(exit_code)


def process_files(args):
    os.chdir(args.screenshots_dir)

    pattern = '*/????-??-??/*.jpg'
    running = True

    def handler(signum, frame):
        _logger.info('exit requested')
        nonlocal running
        running = False

    def upload(name):
        if not running:
            raise OSError("task stopping")

        destination = f's3://meme/chatterbird/{name}'
        _logger.info('upload %s to %s', name, destination)
        upload_args = [
            's3cmd', 'put', name, destination, '--recursive',
            '--acl-public', '-c', args.s3config]

        if args.dry_run:
            upload_args.append('--dry-run')

        subprocess.check_call(upload_args)

        if '_thumb.' not in name:
            placeholder_filename = re.sub(r'\.jpg$', '.placeholder', name)
            _logger.info('write placeholder %s', placeholder_filename)

            if args.dry_run:
                _logger.info('  (dry run)')
            else:
                with open(placeholder_filename, "wb") as file:
                    pass

        if not args.dry_run:
            backup_filename = f'{name}.bak'
            os.rename(name, backup_filename)

    old_int_handler = signal.signal(signal.SIGINT, handler)
    old_term_handler = signal.signal(signal.SIGTERM, handler)

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(upload, name) for name in sorted(glob.glob(pattern))]

        for future in concurrent.futures.as_completed(futures):
            future.result()

    signal.signal(signal.SIGINT, old_int_handler)
    signal.signal(signal.SIGTERM, old_term_handler)

if __name__ == "__main__":
    main()
