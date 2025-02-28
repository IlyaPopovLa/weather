import requests


LOCATIONS = ["Лондон", "Шереметьево", "Череповец"]


def get_weather(location_list):
    for location in location_list:
        lang = 'ru'
        params = {'nTqu': '', 'lang': lang}
        url = f"https://wttr.in/{location}"
        response = requests.get(url, params=params)
        print(response.text)


def main():
    get_weather(LOCATIONS)


if __name__ == "__main__":
    main()