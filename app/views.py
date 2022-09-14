from django.shortcuts import render
import requests
from pprint import pprint
from .models import Coin

from django.contrib import messages

# Create your views here.


# def home(request):
#     url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    
#     coin = request.GET.get("coin_name")
#     print(coin)

#     response = requests.get(url)
#     content = response.json()
#     pprint(content[0])

#     # for i in content:
#     #     print(i)
#     #     if i.name == coin:
#     #         pass
#     #     return


    
#     context = {
#         "coin" : coin,
#         "content" : content,
#         # "image" : content["image"],
#         # "cap" : content["market_cap"],
#         # "change" :content["price_change_24h"]
#         # "name"  : content["coin"]
     
#     }



#     # return render(request)
#     return render(request, "app/home.html", context)

def home(request):
    coin = request.GET.get("coin_name")
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(url)
    content = response.json()
    

    for i in content:
        # print(i["name"])
        if i["name"] == coin:
            name_c = i["name"]

            if Coin.objects.filter(name=name_c):
                messages.warning(request, 'Coin already exists!')
            else:
                Coin.objects.create(name=name_c)
                messages.success(request, 'Coin created!')

        else:
            messages.error(request, 'There is no coin!')


    coin_data = []

    coins = Coin.objects.all()
    
    


    for k in content:

        for y in coins:
            print(k["name"])
            # print(y)
            
            if y == k["name"]:
               print("hello")
               data = {
                 "name":k["name"],
                 "image":k["image"]
                 } 
               print(data) 
               coin_data.append(data)
               

    context ={
         "coin_data" : coin_data
    }    
        
    # print(coin_data)    
    return render(request, "app/test.html", context)
# https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false