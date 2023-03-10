"""This python will handle some extra functions."""
import sys
from os.path import exists

import yaml
from yaml import SafeLoader


def config_file_generator():
    """Generate the template of config file"""
    with open('config.yml', 'w', encoding="utf8") as f:
        f.write("""# ++--------------------------------++
# | MEI_HSING_Auto_Video             |
# | Made by KXX (MIT License)        |
# ++--------------------------------++
# 輸入你的Etherscan api key :          
ether_api_key : ''
#-------------------------------------
# 輸入你希望的gas值(Gwei)
enter_gwei : ''
#-------------------------------------
# 輸入你的line_channel
line_notify_token: ''
#-------------------------------------
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
                'ether_api_key': data['ether_api_key'],
                'enter_gwei': data['enter_gwei'],
                'line_notify_token': data['line_notify_token']
            }
            return config
    except (KeyError, TypeError):
        print(
            "An error occurred while reading config.yml, please check if the file is corrected filled.\n"
            "If the problem can't be solved, consider delete config.yml and restart the program.\n")
        sys.exit()
