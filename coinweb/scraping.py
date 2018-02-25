import platform
import traceback
import time
import json
import pytz
import os
import requests
import cfscrape
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

tz = pytz.timezone('Asia/Kolkata')
datefmt = '%d-%m-%Y'
timefmt = '%H:%M:%S'

fulltime = datetime.datetime.now()

PHANTOMJS_PATH = 'phantomjs'



coinsoup = {} 
oldsoup= {}

driver1 = webdriver.PhantomJS(PHANTOMJS_PATH)

#driver2 = webdriver.PhantomJS(PHANTOMJS_PATH)

#--------------------FEES VARIABLES----------------------------#

buyucoin_buy_fees = 0
buyucoin_sell_fees = 0



coindelta_buy_fees = 0.3
coindelta_sell_fees = 0

coinome_buy_fees = 0.3
coinome_sell_fees = 0.1

coinsecure_buy_fees = 0.4
coinsecure_sell_fees = 0.4

ethex_buy_fees = 1
ethex_sell_fees = 1

koinex_buy_fees = 0.25
koinex_sell_fees = 0.2


pocketbits_buy_fees = 0
pocketbits_sell_fees = 0

unocoin_buy_fees = 0.826
unocoin_sell_fees = 0.826

zebpay_buy_fees = 0
zebpay_sell_fees = 0


buyucoin_err = None

coindelta_err = None
coinome_err =  None
coinsecure_err = None
ethex_err =  None
koinex_err = None
pocketbits_err = None
unocoin_err = None
zebpay_err = None
bitbns_err = None



	
def error(e):
	with open('./log.txt', 'a') as f:
		fulltime = datetime.datetime.now()
		f.write('DateTime : ' + str(fulltime))
		f.write('\n')
		
		f.write(str(e))
		f.write('\n')
		f.write(traceback.format_exc() + '\n')

def scrape_data():

	with open('./coinprice.json','r+',encoding='utf-8') as file:
		oldsoup = json.load(file)
       
#--------------------------FEES IN JSON---------------------------------------#
		try:
			coinsoup['buyucoin_buy_fees'] = buyucoin_buy_fees
			coinsoup['buyucoin_sell_fees'] = buyucoin_sell_fees

			coinsoup['coindelta_buy_fees'] = coindelta_buy_fees
			coinsoup['coindelta_sell_fees'] = coindelta_sell_fees

			coinsoup['coinome_buy_fees'] = coinome_buy_fees
			coinsoup['coinome_sell_fees'] = coinome_sell_fees

			coinsoup['coinsecure_buy_fees'] = coinsecure_buy_fees
			coinsoup['coinsecure_sell_fees'] = coinsecure_sell_fees

			coinsoup['ethex_buy_fees'] = ethex_buy_fees
			coinsoup['ethex_sell_fees'] = ethex_sell_fees

			coinsoup['koinex_buy_fees'] = koinex_buy_fees
			coinsoup['koinex_sell_fees'] = koinex_sell_fees

			coinsoup['pocketbits_buy_fees'] = pocketbits_buy_fees
			coinsoup['pocketbits_sell_fees'] = pocketbits_sell_fees

			coinsoup['unocoin_buy_fees'] = unocoin_buy_fees
			coinsoup['unocoin_sell_fees'] = unocoin_sell_fees

			coinsoup['zebpay_buy_fees'] = zebpay_buy_fees
			coinsoup['zebpay_sell_fees'] = zebpay_sell_fees

		except Exception as e:
			coinsoup['buyucoin_buy_fees'] = 0
			coinsoup['buyucoin_sell_fees'] = 0
			
			coinsoup['coindelta_buy_fees'] = 0 
			coinsoup['coindelta_sell_fees'] = 0
			coinsoup['coinome_buy_fees'] = 0
			coinsoup['coinome_sell_fees'] = 0
			coinsoup['coinsecure_buy_fees'] =0 
			coinsoup['coinsecure_sell_fees'] =0 
			coinsoup['ethex_buy_fees'] = 0
			coinsoup['ethex_sell_fees'] = 0
			coinsoup['koinex_buy_fees'] = 0
			coinsoup['koinex_sell_fees'] = 0
			coinsoup['pocketbits_buy_fees'] = 0
			coinsoup['pocketbits_sell_fees'] = 0
			coinsoup['unocoin_buy_fees'] = 0
			coinsoup['unocoin_sell_fees'] = 0
			coinsoup['zebpay_buy_fees'] = 0
			coinsoup['zebpay_sell_fees'] = 0

#----------------------- BEST DICTS-----------------------------#

	btc_buy_dict = {}
	eth_buy_dict = {}
	bch_buy_dict = {}
	ltc_buy_dict = {}
	xrp_buy_dict = {}
	dash_buy_dict = {}
	neo_buy_dict = {}
	xlm_buy_dict = {}
	omg_buy_dict = {}
	req_buy_dict = {}

	btc_sell_dict = {}
	eth_sell_dict = {}
	bch_sell_dict = {}
	ltc_sell_dict = {}
	xrp_sell_dict = {}
	dash_sell_dict = {}
	neo_sell_dict = {}
	xlm_sell_dict = {}
	omg_sell_dict = {}
	req_sell_dict = {}


	#--------------------------FETCHING APIS-----------------------------#

	try:
		driver1.get('https://www.unocoin.com/trade?all')
		html1 = driver1.page_source
		soup1 = BeautifulSoup(html1, "html.parser")
		
		json_soup = json.loads(soup1.get_text())
		unocoin_btc_buy = float(json_soup.pop('buy'))
		unocoin_btc_sell = float(json_soup.pop('sell'))
		coinsoup['unocoin_btc_buy'] = float(unocoin_btc_buy)
		coinsoup['unocoin_btc_sell'] = float(unocoin_btc_sell)
		coinsoup['unocoin_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('unocoin working')
	except Exception as e:
		print('some exception occured in unocoin')
		unocoin_btc_buy = float(oldsoup['unocoin_btc_buy'])
		unocoin_btc_sell = float(oldsoup['unocoin_btc_sell'])
		coinsoup['unocoin_btc_buy'] = float(oldsoup['unocoin_btc_buy'])
		coinsoup['unocoin_btc_sell'] = float(oldsoup['unocoin_btc_sell'])
		coinsoup['unocoin_timestamp'] = int(oldsoup['unocoin_timestamp'])
		error(e)

	try:
		bscraper = cfscrape.create_scraper()
		html_bit = bscraper.get("https://bitbns.com/order/getTickerAll")
		soup_bit = html_bit.json()
		bitbns_btc_buy = float(soup_bit[0]['BTC']['buyPrice'])
		bitbns_btc_sell = float(soup_bit[0]['BTC']['sellPrice'])
		bitbns_xrp_buy = float(soup_bit[1]['XRP']['buyPrice'])
		bitbns_xrp_sell = float(soup_bit[1]['XRP']['sellPrice'])
		bitbns_neo_buy = float(soup_bit[2]['NEO']['buyPrice'])
		bitbns_neo_sell = float(soup_bit[2]['NEO']['sellPrice'])
		bitbns_eth_buy = float(soup_bit[4]['ETH']['buyPrice'])
		bitbns_eth_sell = float(soup_bit[4]['ETH']['sellPrice'])
		bitbns_xlm_buy = float(soup_bit[5]['XLM']['buyPrice'])
		bitbns_xlm_sell = float(soup_bit[5]['XLM']['sellPrice'])
		coinsoup['bitbns_btc_buy'] = float(bitbns_btc_buy)
		coinsoup['bitbns_btc_sell'] = float(bitbns_btc_sell)
		coinsoup['bitbns_xrp_buy'] = float(bitbns_xrp_buy)
		coinsoup['bitbns_xrp_sell'] = float(bitbns_xrp_sell)
		coinsoup['bitbns_neo_buy'] = float(bitbns_neo_buy)
		coinsoup['bitbns_neo_sell'] = float(bitbns_neo_sell)
		coinsoup['bitbns_eth_buy'] = float(bitbns_eth_buy)
		coinsoup['bitbns_eth_sell'] = float(bitbns_eth_sell)
		coinsoup['bitbns_xlm_buy'] = float(bitbns_xlm_buy)
		coinsoup['bitbns_xlm_sell'] = float(bitbns_xlm_sell)
		coinsoup['bitbns_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print("bitbns working")
	
	except Exception as e:
		print("some exception occured in bitbns")
		bitbns_btc_buy = float(oldsoup['bitbns_btc_buy'])
		bitbns_btc_sell = float(oldsoup['bitbns_btc_sell'])
		bitbns_eth_buy = float(oldsoup['bitbns_eth_buy'])
		bitbns_eth_sell = float(oldsoup['bitbns_eth_sell'])
		bitbns_neo_buy = float(oldsoup['bitbns_neo_buy'])
		bitbns_neo_sell = float(oldsoup['bitbns_neo_sell'])
		bitbns_xrp_buy = float(oldsoup['bitbns_xrp_buy'])
		bitbns_xrp_sell = float(oldsoup['bitbns_xrp_sell'])
		bitbns_xlm_buy = float(oldsoup['bitbns_xlm_buy'])
		bitbns_xlm_sell = float(oldsoup['bitbns_xlm_sell'])
		coinsoup['bitbns_btc_buy'] = float(oldsoup['bitbns_btc_buy'])
		coinsoup['bitbns_btc_sell'] = float(oldsoup['bitbns_btc_sell'])
		coinsoup['bitbns_eth_buy'] = float(oldsoup['bitbns_eth_buy'])
		coinsoup['bitbns_eth_sell'] = float(oldsoup['bitbns_eth_sell'])
		coinsoup['bitbns_neo_buy'] = float(oldsoup['bitbns_neo_buy'])
		coinsoup['bitbns_neo_sell'] = float(oldsoup['bitbns_neo_sell'])
		coinsoup['bitbns_xrp_buy'] = float(oldsoup['bitbns_xrp_buy'])
		coinsoup['bitbns_xrp_sell'] = float(oldsoup['bitbns_xrp_sell'])
		coinsoup['bitbns_xlm_buy'] = float(oldsoup['bitbns_xlm_buy'])
		coinsoup['bitbns_xlm_sell'] = float(oldsoup['bitbns_xlm_sell'])
		coinsoup['bitbns_timestamp'] = int(oldsoup['bitbns_timestamp'])
		error(e)




	try:
		html22 = requests.get('https://www.zebapi.com/api/v1/market/ticker-new/BTC/INR')
		zbpy_ltc = requests.get('https://www.zebapi.com/api/v1/market/ticker-new/LTC/INR')
		zbpy_bch = requests.get('https://www.zebapi.com/api/v1/market/ticker-new/BCH/INR')
		zbpy_xrp = requests.get('https://www.zebapi.com/api/v1/market/ticker-new/XRP/INR')
		soup_zebpay = html22.json()
		soup_zebpay_ltc = zbpy_ltc.json()
		soup_zebpay_bch = zbpy_bch.json()
		soup_zebpay_xrp = zbpy_xrp.json()
		zebpay_btc_buy=float(soup_zebpay['buy'])
		zebpay_btc_sell=float(soup_zebpay['sell'])
		zebpay_ltc_buy=float(soup_zebpay_ltc['buy'])
		zebpay_ltc_sell=float(soup_zebpay_ltc['sell'])
		zebpay_bch_buy=float(soup_zebpay_bch['buy'])
		zebpay_bch_sell=float(soup_zebpay_bch['sell'])
		zebpay_xrp_buy=float(soup_zebpay_xrp['buy'])
		zebpay_xrp_sell=float(soup_zebpay_xrp['sell'])
		coinsoup['zebpay_btc_buy'] = float(zebpay_btc_buy)
		coinsoup['zebpay_btc_sell'] = float(zebpay_btc_sell)
		coinsoup['zebpay_ltc_buy'] = float(zebpay_ltc_buy)
		coinsoup['zebpay_ltc_sell'] = float(zebpay_ltc_sell)
		coinsoup['zebpay_bch_buy'] = float(zebpay_bch_buy)
		coinsoup['zebpay_bch_sell'] = float(zebpay_bch_sell)
		coinsoup['zebpay_xrp_buy'] = float(zebpay_xrp_buy)
		coinsoup['zebpay_xrp_sell'] = float(zebpay_xrp_sell)
		coinsoup['zebpay_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('zebpay working')
	except Exception as e:
		print('some exception occured in zebpay')
		zebpay_btc_buy = float(oldsoup['zebpay_btc_buy'])
		zebpay_btc_sell = float(oldsoup['zebpay_btc_sell'])
		zebpay_ltc_buy = float(oldsoup['zebpay_ltc_buy'])
		zebpay_ltc_sell = float(oldsoup['zebpay_ltc_sell'])
		zebpay_bch_buy = float(oldsoup['zebpay_bch_buy'])
		zebpay_bch_sell = float(oldsoup['zebpay_bch_sell'])
		zebpay_xrp_buy = float(oldsoup['zebpay_xrp_buy'])
		zebpay_xrp_sell = float(oldsoup['zebpay_xrp_sell'])
		coinsoup['zebpay_btc_buy'] = float(oldsoup['zebpay_btc_buy'])
		coinsoup['zebpay_btc_sell'] = float(oldsoup['zebpay_btc_sell'])
		coinsoup['zebpay_ltc_buy'] = float(oldsoup['zebpay_ltc_buy'])
		coinsoup['zebpay_ltc_sell'] = float(oldsoup['zebpay_ltc_sell'])
		coinsoup['zebpay_bch_buy'] = float(oldsoup['zebpay_bch_buy'])
		coinsoup['zebpay_bch_sell'] = float(oldsoup['zebpay_bch_sell'])
		coinsoup['zebpay_xrp_buy'] = float(oldsoup['zebpay_xrp_buy'])
		coinsoup['zebpay_xrp_sell'] = float(oldsoup['zebpay_xrp_sell'])
		coinsoup['zebpay_timestamp'] = int(oldsoup['zebpay_timestamp'])
		error(e)

	try:
		
		kscraper = cfscrape.create_scraper()
		html_koinex = kscraper.get("https://koinex.in/api/ticker")
		soup_koinex = html_koinex.json()
		
		koinex_eth = (soup_koinex['stats']['ETH'])
		koinex_btc = (soup_koinex['stats']['BTC'])
		koinex_ltc = (soup_koinex['stats']['LTC'])
		koinex_bch = (soup_koinex['stats']['BCH'])
		koinex_xrp = (soup_koinex['stats']['XRP'])
		koinex_omg = (soup_koinex['stats']['OMG'])
		koinex_req = (soup_koinex['stats']['REQ'])

		koinex_eth_buy = float(koinex_eth['lowest_ask'])
		koinex_eth_sell = float(koinex_eth['highest_bid'])
		koinex_btc_buy = float(koinex_btc['lowest_ask'])
		koinex_btc_sell = float(koinex_btc['highest_bid'])
		koinex_ltc_buy = float(koinex_ltc['lowest_ask'])
		koinex_ltc_sell = float(koinex_ltc['highest_bid'])
		koinex_bch_buy = float(koinex_bch['lowest_ask'])
		koinex_bch_sell = float(koinex_bch['highest_bid'])
		koinex_xrp_buy = float(koinex_xrp['lowest_ask'])
		koinex_xrp_sell = float(koinex_xrp['highest_bid'])
		koinex_omg_buy = float(koinex_omg['lowest_ask'])
		koinex_omg_sell = float(koinex_omg['highest_bid'])
		koinex_req_buy = float(koinex_req['lowest_ask'])
		koinex_req_sell = float(koinex_req['highest_bid'])

		coinsoup['koinex_eth_buy'] = float(koinex_eth_buy)
		coinsoup['koinex_eth_sell'] = float(koinex_eth_sell)
		coinsoup['koinex_btc_buy'] = float(koinex_btc_buy)
		coinsoup['koinex_btc_sell'] = float(koinex_btc_sell)
		coinsoup['koinex_ltc_buy'] = float(koinex_ltc_buy)
		coinsoup['koinex_ltc_sell'] = float(koinex_ltc_sell) 
		coinsoup['koinex_bch_buy'] = float(koinex_bch_buy)
		coinsoup['koinex_bch_sell'] = float(koinex_bch_sell) 
		coinsoup['koinex_xrp_buy'] = float(koinex_xrp_buy)
		coinsoup['koinex_xrp_sell'] = float(koinex_xrp_sell)  
		coinsoup['koinex_omg_buy'] = float(koinex_omg_buy)
		coinsoup['koinex_omg_sell'] = float(koinex_omg_sell) 
		coinsoup['koinex_req_buy'] = float(koinex_req_buy)
		coinsoup['koinex_req_sell'] = float(koinex_req_sell) 
		print('koinex working')
		coinsoup['koinex_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())

	except Exception as e:
		print('some exception occured in koinex')
		koinex_btc_buy = float(oldsoup['koinex_btc_buy'])
		koinex_btc_sell = float(oldsoup['koinex_btc_sell'])
		koinex_eth_buy = float(oldsoup['koinex_eth_buy'])
		koinex_eth_sell = float(oldsoup['koinex_eth_sell'])
		koinex_bch_buy = float(oldsoup['koinex_bch_buy'])
		koinex_bch_sell = float(oldsoup['koinex_bch_sell'])
		koinex_ltc_buy = float(oldsoup['koinex_ltc_buy'])
		koinex_ltc_sell = float(oldsoup['koinex_ltc_sell'])
		koinex_xrp_buy = float(oldsoup['koinex_xrp_buy'])
		koinex_xrp_sell = float(oldsoup['koinex_xrp_sell'])
		koinex_omg_buy = float(oldsoup['koinex_omg_buy'])
		koinex_omg_sell = float(oldsoup['koinex_omg_sell'])
		koinex_req_buy = float(oldsoup['koinex_req_buy'])
		koinex_req_sell = float(oldsoup['koinex_req_sell'])

		coinsoup['koinex_btc_buy'] = float(oldsoup['koinex_btc_buy'])
		coinsoup['koinex_btc_sell'] = float(oldsoup['koinex_btc_sell'])
		coinsoup['koinex_eth_buy'] = float(oldsoup['koinex_eth_buy'])
		coinsoup['koinex_eth_sell'] = float(oldsoup['koinex_eth_sell'])
		coinsoup['koinex_bch_buy'] = float(oldsoup['koinex_bch_buy'])
		coinsoup['koinex_bch_sell'] = float(oldsoup['koinex_bch_sell'])
		coinsoup['koinex_ltc_buy'] = float(oldsoup['koinex_ltc_buy'])
		coinsoup['koinex_ltc_sell'] = float(oldsoup['koinex_ltc_sell'])
		coinsoup['koinex_xrp_buy'] = float(oldsoup['koinex_xrp_buy'])
		coinsoup['koinex_xrp_sell'] = float(oldsoup['koinex_xrp_sell'])
		coinsoup['koinex_omg_buy'] = float(oldsoup['koinex_omg_buy'])
		coinsoup['koinex_omg_sell'] = float(oldsoup['koinex_omg_sell'])
		coinsoup['koinex_req_buy'] = float(oldsoup['koinex_req_buy'])
		coinsoup['koinex_req_sell'] = float(oldsoup['koinex_req_sell'])
		coinsoup['koinex_timestamp'] = int(oldsoup['koinex_timestamp'])

		error(e)    

	try:
		bscraper = cfscrape.create_scraper()
		html_buyucoin = bscraper.get("https://www.buyucoin.com/api/v1/btc")
		
		soup_buyucoin = html_buyucoin.json()

	
		
		for sub_obj in soup_buyucoin["BuyUcoin_data"]:
			buyucoin_btc_buy=float(sub_obj.pop('btc_buy_price'))
			buyucoin_btc_sell=float(sub_obj.pop('btc_sell_price'))
		coinsoup['buyucoin_btc_buy'] = float(buyucoin_btc_buy)
		coinsoup['buyucoin_btc_sell'] = float(buyucoin_btc_sell)
		coinsoup['buyucoin_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('buyucoin working')
	except Exception as e:
		print('some exception occured in buyucoin')
		buyucoin_btc_buy = float(oldsoup['buyucoin_btc_buy'])
		buyucoin_btc_sell = float(oldsoup['buyucoin_btc_sell'])
		coinsoup['buyucoin_btc_buy'] = float(oldsoup['buyucoin_btc_buy'])
		coinsoup['buyucoin_btc_sell'] = float(oldsoup['buyucoin_btc_sell'])
		coinsoup['buyucoin_timestamp'] = int(oldsoup['buyucoin_timestamp'])

		error(e)

	try:
		csscraper = cfscrape.create_scraper()
		html_coinsecure = csscraper.get("https://api.coinsecure.in/v1/exchange/ticker")
		soup_coinsecure = html_coinsecure.json()
		
	
		#soup_coinsecure = xmltodict.parse(html5,process_namespaces=True)
		
		coinsecure_btc_buy = float(soup_coinsecure['message']['ask']/100)    
		coinsecure_btc_sell = float(soup_coinsecure['message']['bid']/100)
		coinsoup['coinsecure_btc_buy'] = float(coinsecure_btc_buy)
		coinsoup['coinsecure_btc_sell'] = float(coinsecure_btc_sell)
		coinsoup['coinsecure_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('coinsecure working')
	except Exception as e:
		print('some exception occured in coinsecure')
		coinsecure_btc_buy = float(oldsoup['coinsecure_btc_buy'])
		coinsecure_btc_sell = float(oldsoup['coinsecure_btc_sell'])
		coinsoup['coinsecure_btc_buy'] = float(oldsoup['coinsecure_btc_buy'])
		coinsoup['coinsecure_btc_sell'] = float(oldsoup['coinsecure_btc_sell'])
		coinsoup['coinsecure_timestamp'] = int(oldsoup['coinsecure_timestamp'])
		curtime= datetime.datetime.now(tz)
		fulltime = datetime.datetime.now()

		error(e)

	try:    
		html6 = requests.get('https://api.ethexindia.com/ticker')
		soup6 = html6.json()

		json_soup6 = soup6
		ethex_eth_buy = float(json_soup6.pop('ask')) 
		ethex_eth_sell = float(json_soup6.pop('bid'))
		coinsoup['ethex_eth_buy'] = float(ethex_eth_buy)
		coinsoup['ethex_eth_sell'] = float(ethex_eth_sell)
		coinsoup['ethex_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('ethex working')
	except Exception as e:
		print('some exception occured in ethex')
		ethex_eth_buy = float(oldsoup['ethex_eth_buy'])
		ethex_eth_sell = float(oldsoup['ethex_eth_sell'])
		coinsoup['ethex_eth_buy'] = float(oldsoup['ethex_eth_buy'])
		coinsoup['ethex_eth_sell'] = float(oldsoup['ethex_eth_sell'])
		coinsoup['ethex_timestamp'] = int(oldsoup['ethex_timestamp'])

		error(e)

	

	try:    
		html8 = requests.get('https://www.coinome.com/api/v1/ticker.json')
		soup8 = html8.json()
		json_soup8 = soup8
		coinome_btc_buy = float(json_soup8['btc-inr']['lowest_ask'])
		coinome_btc_sell = float(json_soup8['btc-inr']['highest_bid'])
		coinome_bch_buy = float(json_soup8['bch-inr']['lowest_ask'])
		coinome_bch_sell = float(json_soup8['bch-inr']['highest_bid'])
		coinome_ltc_buy = float(json_soup8['ltc-inr']['lowest_ask'])
		coinome_ltc_sell = float(json_soup8['ltc-inr']['highest_bid'])
		coinome_dash_buy = float(json_soup8['dash-inr']['lowest_ask'])
		coinome_dash_sell = float(json_soup8['dash-inr']['highest_bid'])

		coinsoup['coinome_btc_buy']=float(coinome_btc_buy)
		coinsoup['coinome_btc_sell']=float(coinome_btc_sell)
		coinsoup['coinome_bch_buy']=float(coinome_bch_buy)
		coinsoup['coinome_bch_sell']=float(coinome_bch_sell)
		coinsoup['coinome_ltc_buy']=float(coinome_ltc_buy)
		coinsoup['coinome_ltc_sell']=float(coinome_ltc_sell)
		coinsoup['coinome_dash_buy']=float(coinome_dash_buy)
		coinsoup['coinome_dash_sell']=float(coinome_dash_sell)
		coinsoup['coinome_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('coinome working')
		
	except Exception as e:
		print('some exception occured in coinome')
		coinome_btc_buy = float(oldsoup['coinome_btc_buy'])
		coinome_btc_sell = float(oldsoup['coinome_btc_sell'])
		coinome_bch_buy = float(oldsoup['coinome_bch_buy'])
		coinome_bch_sell = float(oldsoup['coinome_bch_sell'])
		coinome_ltc_buy = float(oldsoup['coinome_ltc_buy'])
		coinome_ltc_sell = float(oldsoup['coinome_ltc_sell'])

		coinsoup['coinome_btc_buy'] = float(oldsoup['coinome_btc_buy'])
		coinsoup['coinome_btc_sell'] = float(oldsoup['coinome_btc_sell'])
		coinsoup['coinome_bch_buy'] = float(oldsoup['coinome_bch_buy'])
		coinsoup['coinome_bch_sell'] = float(oldsoup['coinome_bch_sell'])
		coinsoup['coinome_ltc_buy'] = float(oldsoup['coinome_ltc_buy'])
		coinsoup['coinome_ltc_sell'] = float(oldsoup['coinome_ltc_sell'])
		coinsoup['coinome_dash_buy'] = float(oldsoup['coinome_dash_buy'])
		coinsoup['coinome_dash_sell'] = float(oldsoup['coinome_dash_sell'])
		coinsoup['coinome_timestamp'] = int(oldsoup['coinome_timestamp'])

		error(e)

	try:    
		html9 = requests.get('https://pocketbits.in/api/ticker')
		soup9 = html9.json()
		json_soup9 = soup9
		pocketbits_btc_buy=float(json_soup9.pop('buy'))
		pocketbits_btc_sell=float(json_soup9.pop('sell'))
		coinsoup['pocketbits_btc_buy'] = float(pocketbits_btc_buy)
		coinsoup['pocketbits_btc_sell'] = float(pocketbits_btc_sell)
		coinsoup['pocketbits_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('pocketbits working')
	except Exception as e:
		print('some exception occured in pocketbits')
		pocketbits_btc_buy = float(oldsoup['pocketbits_btc_buy'])
		pocketbits_btc_sell = float(oldsoup['pocketbits_btc_sell'])
		coinsoup['pocketbits_btc_buy'] = float(oldsoup['pocketbits_btc_buy'])
		coinsoup['pocketbits_btc_sell'] = float(oldsoup['pocketbits_btc_sell'])
		coinsoup['pocketbits_timestamp'] = int(oldsoup['pocketbits_timestamp'])

		error(e)

	try:
		cscraper = cfscrape.create_scraper()
		cdrbtc = cscraper.get('https://coindelta.com/api/v1/public/getticker/?market=btc-inr')
		cdreth = cscraper.get('https://coindelta.com/api/v1/public/getticker/?market=eth-inr')
		cdrltc = cscraper.get('https://coindelta.com/api/v1/public/getticker/?market=ltc-inr')
		cdrbch = cscraper.get('https://coindelta.com/api/v1/public/getticker/?market=bch-inr')
		cdrxrp = cscraper.get('https://coindelta.com/api/v1/public/getticker/?market=xrp-inr')

		cdrbtc_soup = cdrbtc.json()
		coindelta_buy_btc = float(cdrbtc_soup[0]['Ask'])
		coinsoup['coindelta_btc_buy'] = float(coindelta_buy_btc)
		coindelta_sell_btc = float(cdrbtc_soup[0]['Bid'])
		coinsoup['coindelta_btc_sell'] = float(coindelta_sell_btc)
		

		cdreth_soup = cdreth.json()
		coindelta_buy_eth = float(cdreth_soup[0]['Ask'])
		coinsoup['coindelta_eth_buy'] = float((coindelta_buy_eth))
		coindelta_sell_eth = float(cdreth_soup[0]['Bid'])
		coinsoup['coindelta_eth_sell'] = float(coindelta_sell_eth)

		cdrltc_soup = cdrltc.json()
		coindelta_buy_ltc = float(cdrltc_soup[0]['Ask'])
		coinsoup['coindelta_ltc_buy'] = float(coindelta_buy_ltc)
		coindelta_sell_ltc = float(cdrltc_soup[0]['Bid'])
		coinsoup['coindelta_ltc_sell'] = float(coindelta_sell_ltc)

		cdrbch_soup = cdrbch.json()
		coindelta_buy_bch = float(cdrbch_soup[0]['Ask'])
		coinsoup['coindelta_bch_buy'] = float(coindelta_buy_bch)
		coindelta_sell_bch = float(cdrbch_soup[0]['Bid'])
		coinsoup['coindelta_bch_sell'] = float(coindelta_sell_bch)

		cdrxrp_soup = cdrxrp.json()
		coindelta_buy_xrp = float(cdrxrp_soup[0]['Ask'])
		coinsoup['coindelta_xrp_buy'] = float(coindelta_buy_xrp)
		coindelta_sell_xrp = float(cdrxrp_soup[0]['Bid'])
		coinsoup['coindelta_xrp_sell'] = float(coindelta_sell_xrp)

		coinsoup['coindelta_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('coindelta working')
	except Exception as e:
		print('some exception occured in coindelta')
		coindelta_buy_btc = float(oldsoup['coindelta_btc_buy'])
		coindelta_sell_btc = float(oldsoup['coindelta_btc_sell'])
		coindelta_buy_eth = float(oldsoup['coindelta_eth_buy'])
		coindelta_sell_eth = float(oldsoup['coindelta_eth_sell'])
		coindelta_buy_bch = float(oldsoup['coindelta_bch_buy'])
		coindelta_sell_bch = float(oldsoup['coindelta_bch_sell'])
		coindelta_buy_ltc = float(oldsoup['coindelta_ltc_buy'])
		coindelta_sell_ltc = float(oldsoup['coindelta_ltc_sell'])
		coindelta_buy_xrp = float(oldsoup['coindelta_xrp_buy'])
		coindelta_sell_xrp = float(oldsoup['coindelta_xrp_sell'])

		coinsoup['coindelta_btc_buy'] = float(oldsoup['coindelta_btc_buy'])
		coinsoup['coindelta_btc_sell'] = float(oldsoup['coindelta_btc_sell'])
		coinsoup['coindelta_eth_buy'] = float(oldsoup['coindelta_eth_buy'])
		coinsoup['coindelta_eth_sell'] = float(oldsoup['coindelta_eth_sell'])
		coinsoup['coindelta_bch_buy'] = float(oldsoup['coindelta_bch_buy'])
		coinsoup['coindelta_bch_sell'] = float(oldsoup['coindelta_bch_sell'])
		coinsoup['coindelta_ltc_buy'] = float(oldsoup['coindelta_ltc_buy'])
		coinsoup['coindelta_ltc_sell'] = float(oldsoup['coindelta_ltc_sell'])
		coinsoup['coindelta_xrp_buy'] = float(oldsoup['coindelta_xrp_buy'])
		coinsoup['coindelta_xrp_sell'] = float(oldsoup['coindelta_xrp_sell'])
		coinsoup['coindelta_timestamp'] = int(oldsoup['coindelta_timestamp'])

		error(e)


	with open('./coinprice.json', 'w',encoding='utf-8') as f:
			
			json.dump(coinsoup,f)


	current_time= int(datetime.datetime.now().timestamp())
	json_content = json.load(open('coinprice.json'))
	
	
	try:

		if(int(current_time - json_content['bitbns_timestamp']<=120)):
			bitbns_err = False
			
			btc_buy_dict['bitbns'] = bitbns_btc_buy
			btc_sell_dict['bitbns'] = bitbns_btc_sell
			xrp_buy_dict['bitbns'] = bitbns_xrp_buy
			xrp_sell_dict['bitbns'] = bitbns_xrp_sell
			eth_buy_dict['bitbns'] = bitbns_eth_buy
			eth_sell_dict['bitbns'] = bitbns_eth_sell
			xlm_buy_dict['bitbns'] = bitbns_xlm_buy
			xlm_sell_dict['bitbns'] = bitbns_xlm_sell
			neo_buy_dict['bitbns'] = bitbns_neo_buy
			neo_sell_dict['bitbns'] = bitbns_neo_sell
		else:
			bitbns_err = True	


		
		if(int(current_time - json_content['coindelta_timestamp']<=120)):
			
			coindelta_err = False
			

			btc_buy_dict['coindelta'] = coindelta_buy_btc
			eth_buy_dict['coindelta'] = coindelta_buy_eth
			bch_buy_dict['coindelta'] = coindelta_buy_bch
			ltc_buy_dict['coindelta'] = coindelta_buy_ltc
			xrp_buy_dict['coindelta'] = coindelta_buy_xrp

			btc_sell_dict['coindelta'] = coindelta_sell_btc
			eth_sell_dict['coindelta'] = coindelta_sell_eth
			bch_sell_dict['coindelta'] = coindelta_sell_bch
			ltc_sell_dict['coindelta'] = coindelta_sell_ltc
			xrp_sell_dict['coindelta'] = coindelta_sell_xrp
			

		else:
			coindelta_err = True

		if(int(current_time - json_content['coinome_timestamp']<=120)):
			coinome_err = False
			

			btc_buy_dict['coinome'] = coinome_btc_buy
			bch_buy_dict['coinome'] = coinome_bch_buy
			ltc_buy_dict['coinome'] = coinome_ltc_buy
			dash_buy_dict['coinome'] = coinome_dash_buy

			btc_buy_dict['coinome'] = coinome_btc_sell
			bch_sell_dict['coinome'] = coinome_bch_sell
			ltc_sell_dict['coinome'] = coinome_ltc_sell
			dash_sell_dict['coinome'] = coinome_dash_sell
			
		else:
			coinome_err = True	

		if(int(current_time - json_content['coinsecure_timestamp']<=120)):
			coinsecure_err = False
			
			btc_buy_dict['coinsecure'] = coinsecure_btc_buy
			btc_sell_dict['coinsecure'] = coinsecure_btc_sell

		else:
			coinsecure_err = True

		if(int(current_time - json_content['ethex_timestamp']<=120)):
			ethex_err = False
			

			eth_buy_dict['ethexindia'] = ethex_eth_buy
			eth_sell_dict['ethexindia'] = ethex_eth_sell


		else:
			ethex_err = True

		if(int(current_time - json_content['koinex_timestamp']<=120)):
			koinex_err = False
			

			btc_buy_dict['koinex'] = koinex_btc_buy
			bch_buy_dict['koinex'] = koinex_bch_buy
			ltc_buy_dict['koinex'] = koinex_ltc_buy
			eth_buy_dict['koinex'] = koinex_eth_buy
			xrp_buy_dict['koinex'] = koinex_xrp_buy
			omg_buy_dict['koinex'] = koinex_omg_buy
			req_buy_dict['koinex'] = koinex_req_buy

			btc_buy_dict['koinex'] = koinex_btc_sell
			bch_sell_dict['koinex'] = koinex_bch_sell
			ltc_sell_dict['koinex'] = koinex_ltc_sell
			eth_sell_dict['koinex'] = koinex_eth_sell
			xrp_sell_dict['koinex'] = koinex_xrp_sell
			omg_sell_dict['koinex'] = koinex_omg_sell
			req_sell_dict['koinex'] = koinex_req_sell

		else:
			koinex_err = True

		if(int(current_time - json_content['pocketbits_timestamp']<=120)):
			pocketbits_err = False
			
			btc_buy_dict['pocketbits'] = pocketbits_btc_buy
			btc_sell_dict['pocketbits'] = pocketbits_btc_sell
		else:
			pocketbits_err = True

		if(int(current_time - json_content['buyucoin_timestamp']<=120)):
			buyucoin_err = False
			
			btc_buy_dict['buyucoin'] = buyucoin_btc_buy
			btc_sell_dict['buyucoin'] = buyucoin_btc_sell

		else:
			buyucoin_err = True

		if(int(current_time - json_content['unocoin_timestamp']<=120)):
			unocoin_err = False
			
			btc_buy_dict['unocoin'] = unocoin_btc_buy
			btc_sell_dict['unocoin'] = unocoin_btc_sell
		else:
			unocoin_err = True

		if(int(current_time - json_content['zebpay_timestamp']<=120)):
			zebpay_err = False
			
			btc_buy_dict['zebpay'] = zebpay_btc_buy
			btc_sell_dict['zebpay'] = zebpay_btc_sell
			ltc_buy_dict['zebpay'] = zebpay_ltc_buy
			ltc_sell_dict['zebpay'] = zebpay_ltc_sell
			bch_buy_dict['zebpay'] = zebpay_bch_buy
			bch_sell_dict['zebpay'] = zebpay_bch_sell
			xrp_buy_dict['zebpay'] = zebpay_xrp_buy
			xrp_sell_dict['zebpay'] = zebpay_xrp_sell
		else:
			zebpay_err = True
	except Exception as e :

		buyucoin_err = oldsoup['buyucoin_error']
		
		coindelta_err = oldsoup['coindelta_error']
		coinome_err = oldsoup['coinome_error']
		coinsecure_err = oldsoup['coinsecure_error']
		ethex_err = oldsoup['ethex_error']
		koinex_err = oldsoup['koinex_error']
		pocketbits_err = oldsoup['pocketbits_error']
		unocoin_err = oldsoup['unocoin_error']
		zebpay_err = oldsoup['zebpay_error']
		bitbns_err = oldsoup['bitbns_error']

		error(e)

	
	try:
		best_btc_buy = min(btc_buy_dict.values())
		best_btc_sell = max(btc_sell_dict.values())

		best_eth_buy = min(eth_buy_dict.values())
		best_eth_sell = max(eth_sell_dict.values())

		best_bch_buy = min(bch_buy_dict.values())
		best_bch_sell = max(bch_sell_dict.values())

		best_ltc_buy = min(ltc_buy_dict.values())
		best_ltc_sell = max(ltc_sell_dict.values())

		best_xrp_buy = min(xrp_buy_dict.values())
		best_xrp_sell = max(xrp_sell_dict.values())

		best_dash_buy = min(dash_buy_dict.values())
		best_dash_sell = max(dash_sell_dict.values())

		best_neo_buy = min(neo_buy_dict.values())
		best_neo_sell = max(neo_sell_dict.values())

		best_xlm_buy = min(xlm_buy_dict.values())
		best_xlm_sell = max(xlm_sell_dict.values())

		best_omg_buy = min(omg_buy_dict.values())
		best_omg_sell = max(omg_sell_dict.values())

		best_req_buy = min(req_buy_dict.values())
		best_req_sell = max(req_sell_dict.values())
		 
		
	except Exception as e:
		print("some exception occ in best values")

		best_btc_buy = oldsoup['best_btc_buy']
		best_eth_buy = oldsoup['best_eth_buy']
		best_bch_buy = oldsoup['best_bch_buy']
		best_ltc_buy = oldsoup['best_ltc_buy']
		best_xrp_buy = oldsoup['best_xrp_buy']
		best_dash_buy = oldsoup['best_dash_buy']
		best_neo_buy = oldsoup['best_neo_buy']
		best_xlm_buy = oldsoup['best_xlm_buy']
		best_omg_buy = oldsoup['best_omg_buy']
		best_req_buy = oldsoup['best_req_buy']
		best_btc_sell = oldsoup['best_btc_sell']
		best_eth_sell = oldsoup['best_eth_sell']
		best_bch_sell = oldsoup['best_bch_sell']
		best_ltc_sell = oldsoup['best_ltc_sell']
		best_xrp_sell = oldsoup['best_xrp_sell']
		best_dash_sell = oldsoup['best_dash_sell']
		best_neo_sell = oldsoup['best_neo_sell']
		best_xlm_sell = oldsoup['best_xlm_sell']
		best_omg_sell = oldsoup['best_omg_sell']
		best_req_sell = oldsoup['best_req_sell']

		error(e)

	try:
		best_btc_buy_from = (min(btc_buy_dict, key=btc_buy_dict.get))
		best_btc_sell_to = (max(btc_sell_dict, key=btc_sell_dict.get))

		best_eth_buy_from = (min(eth_buy_dict, key=eth_buy_dict.get))
		best_eth_sell_to = (max(eth_sell_dict, key=eth_sell_dict.get))

		best_bch_buy_from = (min(bch_buy_dict, key=bch_buy_dict.get))
		best_bch_sell_to = (max(bch_sell_dict, key=bch_sell_dict.get))

		best_ltc_buy_from = (min(ltc_buy_dict, key=ltc_buy_dict.get))
		best_ltc_sell_to = (max(ltc_sell_dict, key=ltc_sell_dict.get))

		best_xrp_buy_from = (min(xrp_buy_dict, key=xrp_buy_dict.get))
		best_xrp_sell_to = (max(xrp_sell_dict, key=xrp_sell_dict.get))

		best_dash_buy_from = (min(dash_buy_dict, key = dash_buy_dict.get))
		best_dash_sell_to = max(dash_sell_dict, key=dash_sell_dict.get)

		best_neo_buy_from = (min(neo_buy_dict, key=neo_buy_dict.get))
		best_neo_sell_to = (max(neo_sell_dict, key=neo_sell_dict.get))

		best_xlm_buy_from = (min(xlm_buy_dict, key=xlm_buy_dict.get))
		best_xlm_sell_to = (max(xlm_sell_dict, key=xlm_sell_dict.get))

		best_omg_buy_from = (min(omg_buy_dict, key=xlm_buy_dict.get))
		best_omg_sell_to = (max(omg_sell_dict, key=xlm_sell_dict.get))

		best_req_buy_from = (min(req_buy_dict, key=xlm_buy_dict.get))
		best_req_sell_to = (max(req_sell_dict, key=xlm_sell_dict.get))
	except Exception as e:

		best_btc_buy_from = oldsoup['best_btc_buy_from']
		best_eth_buy_from = oldsoup['best_eth_buy_from']
		best_bch_buy_from = oldsoup['best_bch_buy_from']
		best_ltc_buy_from = oldsoup['best_ltc_buy_from']
		best_xrp_buy_from = oldsoup['best_xrp_buy_from']
		best_neo_buy_from = oldsoup['best_neo_buy_from']
		best_xlm_buy_from = oldsoup['best_xlm_buy_from']
		best_omg_buy_from = oldsoup['best_omg_buy_from']
		best_req_buy_from = oldsoup['best_req_buy_from']
		best_dash_buy_from = oldsoup['best_dash_buy_from']
		best_btc_sell_to = oldsoup['best_btc_sell_to']
		best_eth_sell_to = oldsoup['best_eth_sell_to']
		best_bch_sell_to = oldsoup['best_bch_sell_to']
		best_ltc_sell_to = oldsoup['best_ltc_sell_to']
		best_xrp_sell_to = oldsoup['best_xrp_sell_to']
		best_neo_sell_to = oldsoup['best_neo_sell_to']
		best_xlm_sell_to = oldsoup['best_xlm_sell_to']
		best_omg_sell_to = oldsoup['best_omg_sell_to']
		best_req_sell_to = oldsoup['best_req_sell_to']
		best_dash_sell_to = oldsoup['best_dash_sell_to']
	
		error(e)


	
	coinsoup['buyucoin_error'] = buyucoin_err
	coinsoup['coindelta_error'] = coindelta_err
	coinsoup['coinome_error'] = coinome_err
	coinsoup['coinsecure_error'] = coinsecure_err
	coinsoup['ethex_error'] =  ethex_err
	coinsoup['koinex_error'] = koinex_err
	coinsoup['pocketbits_error'] = pocketbits_err
	coinsoup['unocoin_error'] = unocoin_err
	coinsoup['zebpay_error'] = zebpay_err
	coinsoup['bitbns_error'] = bitbns_err

	coinsoup['best_btc_buy'] = best_btc_buy
	coinsoup['best_btc_sell'] = best_btc_sell
	coinsoup['best_eth_buy'] = best_eth_buy
	coinsoup['best_eth_sell'] = best_eth_sell
	coinsoup['best_bch_buy'] = best_bch_buy
	coinsoup['best_bch_sell'] = best_bch_sell
	coinsoup['best_ltc_buy'] = best_ltc_buy
	coinsoup['best_ltc_sell'] = best_ltc_sell
	coinsoup['best_xrp_buy'] = best_xrp_buy
	coinsoup['best_xrp_sell'] = best_xrp_sell
	coinsoup['best_dash_buy'] = best_dash_buy
	coinsoup['best_dash_sell'] = best_dash_sell
	coinsoup['best_neo_buy'] = best_neo_buy
	coinsoup['best_neo_sell'] = best_neo_sell
	coinsoup['best_xlm_buy'] = best_xlm_buy
	coinsoup['best_xlm_sell'] = best_xlm_sell
	coinsoup['best_omg_buy'] = best_omg_buy
	coinsoup['best_omg_sell'] = best_omg_sell
	coinsoup['best_req_buy'] = best_req_buy
	coinsoup['best_req_sell'] = best_req_sell


	coinsoup['best_btc_buy_from'] = best_btc_buy_from
	coinsoup['best_btc_sell_to'] = best_btc_sell_to
	coinsoup['best_eth_buy_from'] = best_eth_buy_from
	coinsoup['best_eth_sell_to'] = best_eth_sell_to
	coinsoup['best_bch_buy_from'] = best_bch_buy_from
	coinsoup['best_bch_sell_to'] = best_bch_sell_to
	coinsoup['best_ltc_buy_from'] = best_ltc_buy_from
	coinsoup['best_ltc_sell_to'] = best_ltc_sell_to
	coinsoup['best_xrp_buy_from'] = best_xrp_buy_from
	coinsoup['best_xrp_sell_to'] = best_xrp_sell_to
	coinsoup['best_dash_buy_from'] = best_dash_buy_from
	coinsoup['best_dash_sell_to'] = best_dash_sell_to
	coinsoup['best_neo_buy_from'] = best_neo_buy_from
	coinsoup['best_neo_sell_to'] = best_neo_sell_to
	coinsoup['best_xlm_buy_from'] = best_xlm_buy_from
	coinsoup['best_xlm_sell_to'] = best_xlm_sell_to
	coinsoup['best_omg_buy_from'] = best_omg_buy_from
	coinsoup['best_omg_sell_to'] = best_omg_sell_to
	coinsoup['best_req_buy_from'] = best_req_buy_from
	coinsoup['best_req_sell_to'] = best_req_sell_to




	try:
		with open('./coinprice.json', 'w',encoding='utf-8') as f:
			
			json.dump(coinsoup,f)
		cur_time = datetime.datetime.now(tz)
		print(cur_time.strftime(timefmt)) 
		#print(best_btc_sell_to)
		
		
			
	except Exception as e:
		print('some exception occured in writing in file')
		error(e)    
	

while True:
		
			scrape_data()
			time.sleep(5)


	