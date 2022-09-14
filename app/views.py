from django.shortcuts import render
import requests
from pprint import pprint
from .models import Coin

from django.contrib import messages

# Create your views here.


# def home(request):
#     coin = request.GET.get("coin_name")
#     if coin :
#         url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
#         response = requests.get(url)
#         if response.ok : 
#             content = response.json()
#             u_coin = content["name"]
#             if Coin.objects.filter(name=u_coin):
#               messages.warring(request, "Coin already exists!")
#             else:
#                 Coin.objects.create(name=u_coin)
#                 messages.success(request, "Coin created!")  

#         else:
#             messages.error(request, "There is no coin")

#     url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"

#     response = requests.get(url)
#     content = response.json()

#     pprint(content["name"])
#     # pprint(content[0]["image"])
#     # pprint(content[0]["market_cap"])
#     # pprint(content[0]["price_change_24h"])
    
#     context = {
#         "coin" : coin,
#         "content" : content,
#         # "image" : content["image"],
#         # "cap" : content["market_cap"],
#         # "change" :content["price_change_24h"]
#         # "name"  : content["coin"]
     
#     }



#     return render(request, "app/home.html", context)

def home(request):
    # coin = request.GET.get("coin_name")
    # url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    # response = requests.get(url)
    # content = response.json()

    for i in content:
        coin = request.GET.get("coin_name")
        url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD& order=market_cap_desc&per_page=100&page=1&sparkline=false"
        response = requests.get(url)
        content = response.json()
        if content[i]["name"] == coin:
            name_c = content[i]["name"]

            if Coin.objects.filter(name=name_c):
                messages.warning(request, 'Coin already exists!')
            else:
                Coin.objects.create(name=name_c)
                messages.success(request, 'Coin created!')

        else:
            messages.error(request, 'There is no city!')


    coin_data = []

    coins = Coin.objects.all()

    for y in coins:

       if y == coin:

           data = {
           "name":name

           } 

       coin_data.append(data) 


         


    context ={
         "coin_data" : coin_data
    }    
        
        
    return render(request, "app/test.html", context)
# https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false