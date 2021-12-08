import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/coronavirus/country/india/'

res = rq.get(url)
res_data = res.text
res.close()

soup = BeautifulSoup(res_data,'lxml')

cases = soup.find_all('div',class_= 'maincounter-number')

data = []

for case in cases:
    span = case.find('span')
    data.append(span.string)

# print(data)

data_frame = pd.DataFrame({"Covid Data Count":data})

#naming the columns
data_frame.index = ['Total No. of Cases','No.of Deaths','No. of Recovered cases']

# print(data_frame)
#                        Covid Data Count
# Total No. of Cases          34,656,822 
# No.of Deaths                    473,952
# No. of Recovered cases       34,089,137

data_frame.to_csv('Covid Status.csv')