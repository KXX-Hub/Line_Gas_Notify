import time

from etherscan import Etherscan

import line_notify
import utilities as utils

config = utils.read_config()
eth = Etherscan(config.get('ether_api_key'))
wallet_address = config.get('wallet_address')
enter_gwei = config.get('enter_gwei')
gas_oracle = eth.get_gas_oracle()
safe_gas = gas_oracle["SafeGasPrice"]
proposed_gas = gas_oracle["ProposeGasPrice"]
fast_gas = gas_oracle["FastGasPrice"]
suggest_base_fee = gas_oracle["suggestBaseFee"]
token = config.get("line_notify_token")


def get_gas_notify():
    while True:
        if int(enter_gwei) < int(fast_gas):
            message = "\nGas is too high\n" \
                      f"Your target gas : {enter_gwei} Gwei" \
                      "\n----------------------------------------\n" \
                      f"Safe Gas : {safe_gas} Gwei\n" \
                      f"Proposed Gas : {proposed_gas} Gwei\n" \
                      f"Fast Gas : {fast_gas} Gwei\n" \
                      f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                      f"------------------------------------------"
            line_notify.send_message(message)
            time.sleep(30)
        elif int(enter_gwei) >= int(safe_gas):
            if int(enter_gwei) >= int(proposed_gas):
                message = "\nGas is high\n" \
                          f"Your target gas : {enter_gwei} Gwei" \
                          "\n----------------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                          f"------------------------------------------"
                line_notify.send_message(message)
                time.sleep(30)
            elif int(safe_gas) <= int(enter_gwei) <= int(proposed_gas):
                message = "\nGas is ok\n" \
                          f"Your target gas : {enter_gwei} Gwei" \
                          "\n----------------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                          f"------------------------------------------"
                line_notify.send_message(message)
                time.sleep(30)
            elif int(enter_gwei) >= int(suggest_base_fee):
                message = "\nGas is prefect!!!\n" \
                          f"Your target gas : {enter_gwei} Gwei" \
                          "\n----------------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                          f"------------------------------------------"
                line_notify.send_message(message)
                time.sleep(30)


if __name__ == "__main__":
    get_gas_notify()
