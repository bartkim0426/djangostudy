from django.http.response import HttpResponse
import requests


def room(request, room_id):
    url = "https://api.zigbang.com/v1/items?detail=true&item_ids=" + room_id
    response = requests.get(url)
    return HttpResponse(response.content)

def home(request):
    url = "https://watcha.net/home/news.json?page=1&per=50"
    response = requests.get(url)
    return HttpResponse(response.content)
