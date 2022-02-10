import os
import logging
import config_build
from dotenv import load_dotenv

USERNAME = config_build.read_config()

logging.debug(f'finished reading config for user: {USERNAME}')

# load the env file, see .env.example for possible env variables
load_dotenv('./.env')


def main():
    print(os.environ['test'])


if __name__ == '__main__':
    main()
