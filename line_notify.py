import requests

import utilities as utils

config = utils.read_config()
token = config.get('line_notify_token')


def send_message(message):
    """Send message to LINE Notify.
    :param int sub_num: Subscribed sync channels num.
    :param str message: Message to send.
    """
    headers = {"Authorization": "Bearer " + token}
    data = {'message': message}
    requests.post("https://notify-api.line.me/api/notify",
                  headers=headers, data=data, timeout=5)

