import requests


def get_wether():
    lang = 'ru'
    params = {'MnTq': '', 'lang': lang}
    location_list = ["Лондон", "svo", "Череповец"]
    for location in location_list:
        url = f"https://wttr.in/{location}"
        response = requests.get(url, params=params)
        print (response.text)


def main():
    get_wether()


if __name__ == "__main__":
    main()