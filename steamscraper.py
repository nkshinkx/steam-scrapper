from bs4 import BeautifulSoup as bs
import requests


url = "https://store.steampowered.com/specials#p=0&tab=NewReleases"

r = requests.get(url)
htmlcontent = r.content
soup = bs(htmlcontent,"html.parser")
newgames = soup.find_all("div", { "class" : "tab_item_name"})
games =[]
for i in newgames:
    gnames=i.string
    games.append(gnames)

newprices = soup.find_all("div",{"class":"discount_final_price"})
prices = []
for i in newprices:
    nprices = i.string
    prices.append(nprices)
k = 2 
res = prices[:len(prices)-k]


dict = {"Name":games,"Prices":res}
df = pd.DataFrame(dict)
df.to_csv("SteamGamesWithPrices.csv")

