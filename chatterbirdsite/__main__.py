import argparse
import json
import tornado.ioloop

from chatterbirdsite.app import App


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('config_file')
    args = arg_parser.parse_args()

    with open(args.config_file, 'r') as file:
        config = json.load(file)

    app = App(config)
    app.listen(config['port'])
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
