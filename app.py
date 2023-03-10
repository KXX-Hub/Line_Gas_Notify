import time

from etherscan import Etherscan

import line_notify
import utilities as utils

config = utils.read_config()
eth = Etherscan(config.get('ether_api_key'))
wallet_address = config.get('wallet_address')
enter_gwei = config.get('enter_gwei')
token = config.get("line_notify_token")
gas_oracle = eth.get_gas_oracle()
safe_gas = gas_oracle["SafeGasPrice"]
proposed_gas = gas_oracle["ProposeGasPrice"]
fast_gas = gas_oracle["FastGasPrice"]
suggest_base_fee = gas_oracle["suggestBaseFee"]
minute_counter = {
    'too_high_gas_msg': 0,
    'high_gas_msg': 0,
    'ok_gas_msg': 0,
    'prefect_msg': 0
}


def get_gas_notify():
    while True:
        gas_oracle = eth.get_gas_oracle()
        safe_gas = gas_oracle["SafeGasPrice"]
        proposed_gas = gas_oracle["ProposeGasPrice"]
        fast_gas = gas_oracle["FastGasPrice"]
        suggest_base_fee = gas_oracle["suggestBaseFee"]
        if float(suggest_base_fee) > float(enter_gwei) + 10:
            if minute_counter.get('too_high_gas_msg') == 1:
                continue
            else:
                message = "\nGas is too high\n" \
                          f"Your target gas : {enter_gwei} Gwei" \
                          "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                minute_counter['too_high_gas_msg'] = 1
                minute_counter['high_gas_msg'] = 0
                minute_counter['ok_gas_msg'] = 0
                minute_counter['prefect_msg'] = 0
                time.sleep(5)
                continue
        elif float(enter_gwei) + 1 <= float(suggest_base_fee) <= float(enter_gwei)+10:
            if minute_counter.get('high_gas_msg') == 1:
                continue
            else:
                message = "\nGas is high\n" \
                          f"Your target gas : {enter_gwei} Gwei" \
                          "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                minute_counter['too_high_gas_msg'] = 0
                minute_counter['high_gas_msg'] = 1
                minute_counter['ok_gas_msg'] = 0
                minute_counter['prefect_msg'] = 0
                time.sleep(5)
                continue

        elif float(enter_gwei) - 1 <= float(suggest_base_fee) <= float(enter_gwei) + 1:
            if minute_counter.get('ok_gas_msg') == 1:
                continue
            else:
                message = "\nGas is ok\n" \
                          f"Your target gas : {enter_gwei} Gwei" \
                          "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                minute_counter['too_high_gas_msg'] = 0
                minute_counter['high_gas_msg'] = 0
                minute_counter['ok_gas_msg'] = 1
                minute_counter['prefect_msg'] = 0
                time.sleep(5)
                continue
        elif float(enter_gwei)-1 >= float(suggest_base_fee):
            if minute_counter.get('prefect_msg') == 1:
                continue
            else:
                message = "\nGas is prefect for you!!!\n" \
                          f"Your target gas : {enter_gwei} Gwei" \
                          "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_base_fee} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                minute_counter['too_high_gas_msg'] = 0
                minute_counter['high_gas_msg'] = 0
                minute_counter['ok_gas_msg'] = 0
                minute_counter['prefect_msg'] = 1
                time.sleep(5)
                continue
        else:
            continue


def test_while():
    while True:
        safe_gas = gas_oracle["SafeGasPrice"]
        proposed_gas = gas_oracle["ProposeGasPrice"]
        fast_gas = gas_oracle["FastGasPrice"]
        suggest_base_fee = gas_oracle["suggestBaseFee"]
        message = suggest_base_fee
        line_notify.send_message(message)
        continue


if __name__ == "__main__":
    get_gas_notify()
