import requests


LOCATION_LIST = ["Лондон", "Шереметьево", "Череповец"]


def get_weather(location_list):
    weather_info = []
    lang = 'ru'
    for location in location_list:
        url = f"https://wttr.in/{location}"
        params = {'nTqu': '', 'lang': lang}
        response = requests.get(url, params=params)
        response.raise_for_status()
        weather_info.append(response.text)
    return weather_info

def main():
    weather_data = get_weather(LOCATION_LIST)
    for weather in weather_data:
        print(weather)


if __name__ == "__main__":
    main()