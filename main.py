import bs4
import requests

url= 'http://www.jadwalsholat.pkpu.or.id/?id=308'
contents = requests.get (url)

response = bs4.BeautifulSoup(contents.text, "html.parser")
print (response)
data = response.find_all('tr', 'table_highlight')
data = data[0]

sholat ={}
i = 0
for d in data:
    if i == 1:
        sholat['shubuh'] = d.get_text()
    elif i == 2:
        sholat['dzuhur'] = d.get_text()
    elif i == 3:
        sholat['ashar'] = d.get_text()
    elif i == 4:
        sholat['maghrib'] = d.get_text()
    elif i == 5:
        sholat['isya'] = d.get_text()
    i += 1

print(sholat)
