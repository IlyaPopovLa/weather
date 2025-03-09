import requests


def get_weather(location):
    lang = 'ru'
    url = f"https://wttr.in/{location}"
    params = {'nTqu': '', 'lang': lang}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text

def main():
    LOCATION_LIST = ["Лондон", "Шереметьево", "Череповец"]
    for location in LOCATION_LIST:
        weather = get_weather(location)
        print(weather)


if __name__ == "__main__":
    main()