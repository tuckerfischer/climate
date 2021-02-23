from bs4 import BeautifulSoup
from urllib.request import urlopen

city = input("What city are you in? ")
state = input("What state are you in? ")
month = int(input('What month is it?[1-12] '))
month_py = month - 1

link_to_city = urlopen('https://www.usclimatedata.com/climate/{}/{}/united-states'.format(city, state))
state_soup = BeautifulSoup(link_to_city.read(), 'html.parser')
temp_high = state_soup.find_all('td', {'class': 'high text-right'})
temp_low = state_soup.find_all('td', {'class': 'low text-right'})

high = temp_high[month_py]
low = temp_low[month_py]

high_txt= high.getText()
low_txt = low.getText()

print('the normal high for this month is {}, and the normal low is {}'.format(high_txt, low_txt))



