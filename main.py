
import requests
from pynput.keyboard import Controller
from voice2text import Listen

def translate_hindi_to_english(text):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=hi&tl=en&dt=t&q=" + text
    response = requests.get(url)
    data = response.json()
    return data[0][0][0]

if __name__ == "__main__":
    while 1:
        input = Listen()
        translated_text = translate_hindi_to_english(input)
        keyboard = Controller()
        keyboard.type(translated_text)