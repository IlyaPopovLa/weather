import requests


def get_weather(location):
    lang = 'ru'
    url = f"https://wttr.in/{location}"
    params = {'nTqu': '', 'lang': lang}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text


def main():
    locations = ["Лондон", "Шереметьево", "Череповец"]
    for location in locations:
        weather = get_weather(location)
        print(weather)


if __name__ == "__main__":
    main()