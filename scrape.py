import bs4
import requests

link = "https://boxnovel.com/novel/reincarnation-of-the-strongest-sword-god-webnovel/chapter-"

br = "-----------------------------------------------------------------------------------------\n"

fil = open("RSSD.txt","a+")

i=1214

while(i<=2000):
    print(f"{i}\n")
    page = requests.get(f"{link}{i}")
    soup = bs4.BeautifulSoup(page.text,'lxml')
    div = soup.find_all("div",class_="text-left")
    para = div[0].find_all("p")
    for stuff in para:
        fil.write("%s\n"%stuff.text)
    fil.write("%s"%br)
    i=i+1
fil.close()
print("done")
