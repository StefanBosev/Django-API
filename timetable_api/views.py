from urllib import request
import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getResponse(url):
    res = request.urlopen(url)
    if (res.getcode() == 200):
        data = res.data()
        jsonData = json.loads(data)
        return jsonData
    else:
        print("Url not found\n")

def table(request):
    return HttpResponse(getResponse("https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=-departure_time&filter%5Bstop%5D=place-north"))
    