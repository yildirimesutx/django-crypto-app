# Crypto App


Belirlediğimiz API den veriyi almak için  `requests` paketini kullanıyoruz.

```
import requests
from pprint import pprint

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false"
response = requests.get(url)
content = response.json()


print(content) # terminalde veriyi gördük

pprint(content) #  gelen veriyi düzenli görebilmek için pprint kullandık


```

---

Yukarıda sorguladığımız veriyi input ile client dan alabilmek için template form yapısı oluşturuk "GET" methodu ile

```
home.html =>

<form>


<input class="coin-input" type="text" name="coin_name" placeholder='Provide the coin name'>

# name="coin_name"   ile yakalıyoruz


<button type="button" class="btn btn-primary">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-plus-circle-fill" viewBox="0 0 16 16">
        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z"/>
      </svg>
</button>

</form>


coin = request.GET.get("coin_name") 
#burada get("input name")



```

```
1- aldığımız veriyi DB kaydediyoruz.
2- db mükerrer kayıt olmaması içinde tedbir aldık 

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

```
---

```
DB sadece api den aldığımız name attributunu kaydettik,

name attributu kullanarak diğer güncel değişkenklere ulaşacağız.

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
               print(data) 
               coin_data.append(data)  


```

- DB aldığımız veri queryset olarak geliyor, apiden aldığımız string olduğu için db alıp döndüğümüz veriyi stringe çevirdik


