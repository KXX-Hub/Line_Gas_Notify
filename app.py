import time
import requests
import line_notify
import utilities as utils

config = utils.read_config()
wallet_address = config.get('wallet_address')
target_gas = config.get('target_gas')
token = config.get("line_notify_token")


time_counter = {
    'too_high_gas_msg': 0,
    'high_gas_msg': 0,
    'ok_gas_msg': 0,
    'prefect_msg': 0
}


def get_gas_notify():
    url = "https://api.etherscan.io/api?module=gastracker&action=gasoracle"
    response = requests.get(url)
    print("+---------------------------+\n"
          "|Welcome come to Gas Notify!|\n"
          "-----------------------------")
    while True:
        data = response.json()
        safe_gas = int(data['result']['SafeGasPrice'])
        proposed_gas = int(data['result']['ProposeGasPrice'])
        fast_gas = int(data['result']['FastGasPrice'])
        base_fee = proposed_gas
        suggest_gas = base_fee + proposed_gas
        if float(suggest_gas) > float(target_gas) + 10:
            if time_counter.get('too_high_gas_msg') == 1:
                print('Skip (too high)')
                time.sleep(3)
                continue
            else:
                message = "Gas is too high\n"
                line_notify.send_message(message)
                message = "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_gas} Gwei\n" \
                          f"Your target gas : {target_gas} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                time_counter['too_high_gas_msg'] = 1
                time_counter['high_gas_msg'] = 0
                time_counter['ok_gas_msg'] = 0
                time_counter['prefect_msg'] = 0
                print('+---------------+\n'
                      '|Gas is too high|\n'
                      '+---------------+')
                continue
        elif float(target_gas) + 3 <= float(suggest_gas) <= float(target_gas) + 10:
            if time_counter.get('high_gas_msg') == 1:
                print('Skip (higher)')
                time.sleep(3)
                continue
            else:
                message = "Gas is out of safe range\n"
                line_notify.send_message(message)
                message = "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_gas} Gwei\n" \
                          f"Your target gas : {target_gas} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                time_counter['too_high_gas_msg'] = 0
                time_counter['high_gas_msg'] = 1
                time_counter['ok_gas_msg'] = 0
                time_counter['prefect_msg'] = 0
                print('+------------------------+\n'
                      '|Gas is out of safe range|\n'
                      '+------------------------+')
                continue

        elif float(target_gas) - 3 <= float(suggest_gas) <= float(target_gas) + 3:
            if time_counter.get('ok_gas_msg') == 1:
                print('Skip (safe)')
                time.sleep(3)
                continue
            else:
                message = "Gas is in the safe range\n"
                line_notify.send_message(message)
                message = "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_gas} Gwei\n" \
                          f"Your target gas : {target_gas} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                time_counter['too_high_gas_msg'] = 0
                time_counter['high_gas_msg'] = 0
                time_counter['ok_gas_msg'] = 1
                time_counter['prefect_msg'] = 0
                print('+--------------------+\n'
                      '|Gas is in safe range|\n'
                      '+--------------------+')
                continue
        elif float(target_gas) - 3 >= float(suggest_gas):
            if time_counter.get('prefect_msg') == 1:
                print('Skip (prefect)')
                time.sleep(3)
                continue
            else:
                message = "Gas is prefect for you!!!"
                line_notify.send_message(message)
                message = "\n----------------------------------\n" \
                          f"Safe Gas : {safe_gas} Gwei\n" \
                          f"Proposed Gas : {proposed_gas} Gwei\n" \
                          f"Fast Gas : {fast_gas} Gwei\n" \
                          f"----------------------------------\n" \
                          f"Suggest Base Fee : {suggest_gas} Gwei\n" \
                          f"Your target gas : {target_gas} Gwei\n" \
                          f"----------------------------------"
                line_notify.send_message(message)
                time_counter['too_high_gas_msg'] = 0
                time_counter['high_gas_msg'] = 0
                time_counter['ok_gas_msg'] = 0
                time_counter['prefect_msg'] = 1
                print('+--------------+\n'
                      '|Gas is prefect|\n'
                      '+--------------+')
                continue
        else:
            continue


if __name__ == "__main__":
    get_gas_notify()
