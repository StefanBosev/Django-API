from django.shortcuts import render
import requests


def index(request):
    api = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time'
                       '&include=schedule%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north')

    json_data = api.json()

    print('TIME - DESTINATION - TRAIN# - STATUS', end='\n \n')
    for x in range(0, 10):
        print(json_data['data'][x]['attributes']['departure_time'], end=" - ")
        print(json_data['included'][x]['attributes']['headsign'], end=" - ")
        print(json_data['included'][x]['attributes']['name'], end=" - ")
        print(json_data['data'][x]['attributes']['status'])

    return render(request, 'home.html')
