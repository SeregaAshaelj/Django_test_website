import requests

token = '5466047405:AAEHahFfina35bJWTruYI0o96L3fF0kSJ8w'
chat_id = '-663231049'
text = 'Test_2'


def sendTelegram():
    api = 'https://api.telegram.org/bot'
    method = api + token + '/sendMessage'

    req = requests.post(method, data={
        'chat_id': chat_id,
        'text': text
    })

    sendTelegram()
