from urllib import request
import json
from django.shortcuts import render

def getResponse(url):
    res = request.urlopen(url)
    if (res.getcode() == 200):
        data = res.data()
        jsonData = json.loads(data)
        return jsonData
    else:
        print("Url not found\n")
    
def main():
    data = getResponse("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north")

    return render()
