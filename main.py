import json
import time
from etherscan import Etherscan
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import utilities as utils
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

config = utils.read_config()
driver = webdriver.Chrome()
eth = Etherscan(config.get('ether_api_key'))
wallet_address = config.get('wallet_address')
enter_gwei = config.get('enter_gwei')
gas_oracle = eth.get_gas_oracle()
safe_gas = gas_oracle["SafeGasPrice"]
proposed_gas = gas_oracle["ProposeGasPrice"]
fast_gas = gas_oracle["FastGasPrice"]
suggest_base_fee = gas_oracle["suggestBaseFee"]


def gas_info():
    safe_message = "Safe : " + safe_gas + " gwei"
    proposed_gas_message = "Proposed : " + proposed_gas + " gwei"
    fast_gas_message = "Fast : " + fast_gas + " gwei"
    suggest_message = "Suggest base fee : " + suggest_base_fee + " gwei"
    print("-----------------------")
    print(safe_message)
    print(proposed_gas_message)
    print(fast_gas_message)
    print(suggest_message)
    print("-----------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gas_info()
