import argparse
import fcntl
import glob
import logging
import os
import re
import subprocess
import sys

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

    for name in glob.glob(pattern):
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

                backup_filename = f'{name}.bak'
                os.rename(name, backup_filename)


if __name__ == "__main__":
    main()
