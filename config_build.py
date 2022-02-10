# import configparser
import logging
import os

logging.basicConfig(filename=rf'./.debug.log',
                    level=logging.DEBUG,
                    format='%(asctime)s: %(message)s',
                    )

CONFIG_VERSION = 0.1
USERNAME = os.environ['USERNAME']


def read_config():
    logging.debug(f'loading config: {USERNAME}')
    return USERNAME


if __name__ == '__main__':
    print('test')
