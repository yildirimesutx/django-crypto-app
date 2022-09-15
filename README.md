```
ekrana arama sonucu aldık, db yazdırıp cekmemiz lazim

def home(request):
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
    

    coin = request.GET.get("coin_name")
    print(coin)

    response = requests.get(url)
    content = response.json()
    pprint(content[0])
    # pprint(content[0]["image"])
    # pprint(content[0]["market_cap"])
    # pprint(content[0]["price_change_24h"])
    
    context = {
        "coin" : coin,
        "content" : content,
        # "image" : content["image"],
        # "cap" : content["market_cap"],
        # "change" :content["price_change_24h"]
        # "name"  : content["coin"]
     
    }



    return render(request, "app/home.html", context)

```


```
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
```


