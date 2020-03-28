import requests
from bs4 import BeautifulSoup
import xlwt 
from xlwt import Workbook

url = 'https://www.worldometers.info/coronavirus/'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.87 Chrome/80.0.3987.87 Safari/537.36"}
page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find_all("table", { "id":"main_table_countries_today" })
file = open('data.csv','w')
for mytable in table:
    table_body = mytable.find('tbody')
    try:
        rows = table_body.find_all('tr')
        for tr in rows:
            cols = tr.find_all('td')
            for td in cols:
                file.write(td.text)
                file.write("\n")
    except:
        print("no tbody")

file.close()

f = open("data.csv",'r')
lines = f.readlines()
wb = Workbook() 
sheet1 = wb.add_sheet('Sheet 1')
i = 1
j = 1
for line in lines:
    print(line)
    if j%13 == 0 or j == 1 or j%12 == 0:
        cell = line

    else:
        line = line.replace(",","")
        line = line.replace("+","")
        if line == "" or line == "\n":
            cell = line
        
        else:
            line = line[:-1]
            try:
                cell = float(line)

            except:
                pass

    sheet1.write(i, j, cell)
    j+=1
    if j%13 == 0:
        j = 1
        i+=1

wb.save('data.xls')

