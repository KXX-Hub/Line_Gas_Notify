"""This python will handle some extra functions."""
import sys
from os.path import exists

import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | Ethereum Gas Notify              |
# | Made by KXX (MIT License)        |
# ++--------------------------------++
# 輸入你希望的gas值(Gwei)
target_gas : ''
#-------------------------------------
# 輸入你的line_notify_token
# 網址：https://notify-bot.line.me/zh_TW/
line_notify_token: ''
#-------------------------------------
# 輸入你的ether_api_key
# 網址：https://etherscan.io/myapikey
ether_api_key: ''
"""
                )
    sys.exit()


def read_config():
    """Read config file.
    Check if config file exists, if not, create one.
    if exists, read config file and return config with dict type.
    :rtype: dict
    """
    if not exists('./config.yml'):
        print("Config file not found, create one by default.\nPlease finish filling config.yml")
        with open('config.yml', 'w', encoding="utf8"):
            config_file_generator()

    try:
        with open('config.yml', 'r', encoding="utf8") as f:
            data = yaml.load(f, Loader=SafeLoader)
            config = {
                'target_gas': data['target_gas'],
                'line_notify_token': data['line_notify_token'],
                'ether_api_key': data['ether_api_key']
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()
