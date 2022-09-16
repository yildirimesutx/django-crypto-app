from django.shortcuts import render, redirect,get_object_or_404
import requests
from pprint import pprint
from .models import Coin

from django.contrib import messages



def home(request):
    coin = request.GET.get("coin_name") # lower methodu bosa düsmesin diye or "hello" yanına da yazabiliriz
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    response = requests.get(url)
    content = response.json()
    # pprint(content)
    text =""
    for i in content:
        if coin:  # bu kisimi coin ilk etapta boş geldiği için lower method hata veriyor
            if i["name"].lower() == coin.lower():
                name_c = i["name"]
                
                if  Coin.objects.filter(name=name_c):
                    # messages.warning(request, 'Coin already exists!')
                    # text = 'Coin already exists!'
                    continue
                
                else:
                    Coin.objects.create(name=name_c)
                    # messages.success(request, 'Coin created!')
                    # text = 'Coin created!'

                    
            else:
                # messages.error(request, 'There is no coin!')
                # text = 'There is no coin!'
                continue



    # messages.success(request, text)
    # pprint(content[0])

                         

    coin_data = []

    coins = Coin.objects.all().order_by("-id")
  
    # print(coins)

    for k in coins:
        # print(k)
        for n in range(0,100):
            # print(n)
            if content[n]["name"]== str(k):
            #    print("hello")
               data = {
                 "k" :k, #DB ICINDEKI NAME ID ALMAK ICIN
                 "name":content[n]["name"],
                 "image":content[n]["image"],
                 "market":content[n]["current_price"],
                 "change":content[n]["price_change_24h"],
                 } 
            #    print(data) 
               coin_data.append(data)  
    
 
    context ={
         "coin_data" : coin_data
    }    
        
   
    return render(request, "app/home.html", context)


def delete_coin(request, id):
    coin = get_object_or_404(Coin, id=id)
    coin.delete()
    messages.success(request, 'City deleted!')
    return redirect('home')
