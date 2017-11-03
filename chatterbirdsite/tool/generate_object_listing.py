import argparse

import os


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('run_dir')

    args = arg_parser.parse_args()

    run_dir = args.run_dir

    for name in sorted(os.listdir(run_dir)):
        date_dir = os.path.join(run_dir, name)

        if os.path.isdir(date_dir):
            text_file = os.path.join(run_dir, name + '.txt')
            with open(text_file, 'w') as file:
                for filename in sorted(os.listdir(date_dir)):
                    file.write(filename)
                    file.write('\n')


if __name__ == '__main__':
    main()
