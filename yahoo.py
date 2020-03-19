import requests
from bs4 import BeautifulSoup



def dow_price():
    dow = 'https://finance.yahoo.com/quote/%5EDJI?p=^DJI'
    r = requests.get(dow)
    soup = BeautifulSoup(r.text, 'html.parser')
    price_span = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('span')
    price_td = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('td')

    previous_close_raw = price_span[1]
    last_open_raw = price_span[3]
    previous_close = previous_close_raw.text.replace(',', '')
    last_open = last_open_raw.text.replace(',', '')

    today = price_td[9].text.split('-')
    lowest = today[0].replace(',','')
    highest = today[1].replace(',','')

    opening_res = float(last_open) - float(previous_close)
    opening_change = ( float(last_open) / float(previous_close) ) * 100 - 100
    print('----------------------------------------------------')
    print('DOW')
    print('Previous close: '+previous_close)
    print('Open: '+last_open)
    print('Lowest: '+lowest)
    print('Highest: '+highest)
    print('Opening res: '+str(round(opening_res, 2)))
    print('Opening change: '+ str(round(opening_change, 2)) + '%')


def nasdaq_price():
    nasdaq = 'https://finance.yahoo.com/quote/%5EIXIC?p=^IXIC'
    r = requests.get(nasdaq)
    soup = BeautifulSoup(r.text, 'html.parser')
    price_span = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('span')
    price_td = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('td')

    previous_close_raw = price_span[1]
    last_open_raw = price_span[3]
    previous_close = previous_close_raw.text.replace(',', '')
    last_open = last_open_raw.text.replace(',', '')

    today = price_td[9].text.split('-')
    lowest = today[0].replace(',','')
    highest = today[1].replace(',','')

    opening_res = float(last_open) - float(previous_close)
    opening_change = ( float(last_open) / float(previous_close) ) * 100 - 100
    print('----------------------------------------------------')
    print('NASDAQ')
    print('Previous close: '+previous_close)
    print('Open: '+last_open)
    print('Lowest: '+lowest)
    print('Highest: '+highest)
    print('Opening res: '+str(round(opening_res, 2)))
    print('Opening change: '+ str(round(opening_change, 2)) + '%')

def apple_price():
    aapl = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'
    r = requests.get(aapl)
    soup = BeautifulSoup(r.text, 'html.parser')
    price_span = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('span')
    price_td = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('td')

    previous_close_raw = price_span[1]
    last_open_raw = price_span[3]
    previous_close = previous_close_raw.text.replace(',', '')
    last_open = last_open_raw.text.replace(',', '')

    today = price_td[9].text.split('-')
    lowest = today[0].replace(',','')
    highest = today[1].replace(',','')

    opening_res = float(last_open) - float(previous_close)
    opening_change = ( float(last_open) / float(previous_close) ) * 100 - 100
    print('----------------------------------------------------')
    print('AAPL')
    print('Previous close: '+previous_close)
    print('Open: '+last_open)
    print('Lowest: '+lowest)
    print('Highest: '+highest)
    print('Opening res: '+ str(round(opening_res, 2)))
    print('Opening change: '+ str(round(opening_change, 2)) + '%')


def google_price():
    googl = 'https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch'
    r = requests.get(googl)
    soup = BeautifulSoup(r.text, 'html.parser')
    price_span = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('span')
    price_td = soup.find_all('div', {'id' : 'quote-summary'})[0].find_all('td')

    previous_close_raw = price_span[1]
    last_open_raw = price_span[3]
    previous_close = previous_close_raw.text.replace(',', '')
    last_open = last_open_raw.text.replace(',', '')

    today = price_td[9].text.split('-')
    lowest = today[0].replace(',','')
    highest = today[1].replace(',','')

    opening_res = float(last_open) - float(previous_close)
    opening_change = ( float(last_open) / float(previous_close) ) * 100 - 100
    print('----------------------------------------------------')
    print('GOOGL')
    print('Previous close: '+previous_close)
    print('Open: '+last_open)
    print('Lowest: '+lowest)
    print('Highest: '+highest)
    print('Opening res: '+ str(round(opening_res, 2)))
    print('Opening change: '+ str(round(opening_change, 2)) + '%')

dow_price()
nasdaq_price()
apple_price()
google_price()
 #[0].find('span').text
 