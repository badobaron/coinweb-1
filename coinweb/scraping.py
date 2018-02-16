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
oldvalue= {}

driver1 = webdriver.PhantomJS(PHANTOMJS_PATH)



#driver2 = webdriver.PhantomJS(PHANTOMJS_PATH)

#--------------------FEES VARIABLES----------------------------#

buyucoin_buy_fees = 0
buyucoin_sell_fees = 0

btcx_buy_fees = 1
btcx_sell_fees = 1

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
btcx_err = None
coindelta_err = None
coinome_err =  None
coinsecure_err = None
ethex_err =  None
koinex_err = None
pocketbits_err = None
unocoin_err = None
zebpay_err = None


def scrape_api(api):
	html = requests.get(api)
	soup = html.json()
	


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
#------------------------------ASSIGNING OLD VALUES----------------------------#        

		try:
		#---------------ERROR VALUES--------------------------#
			oldvalue['old_btcx_error'] = oldsoup['btcx_error']
			oldvalue['old_buyucoin_error'] = oldsoup['buyucoin_error']
			oldvalue['old_coindelta_error'] = oldsoup['coindelta_error']
			oldvalue['old_coinome_error'] = oldsoup['coinome_error']
			oldvalue['old_coinsecure_error'] = oldsoup['coinsecure_error']
			oldvalue['old_ethex_error'] = oldsoup['ethex_error']
			oldvalue['old_koinex_error'] = oldsoup['koinex_error']
			oldvalue['old_pocketbits_error'] = oldsoup['pocketbits_error']
			oldvalue['old_unocoin_error'] = oldsoup['unocoin_error']
			oldvalue['old_zebpay_error'] = oldsoup['zebpay_error']

		except Exception as e:
			oldvalue['old_btcx_error'] = 'false'
			oldvalue['old_buyucoin_error'] = 'false'
			oldvalue['old_coindelta_error'] = 'false'
			oldvalue['old_coinome_error'] = 'false'
			oldvalue['old_coinsecure_error'] = 'false'
			oldvalue['old_ethex_error'] = 'false'
			oldvalue['old_koinex_error'] = 'false'
			oldvalue['old_pocketbits_error'] = 'false'
			oldvalue['old_unocoin_error'] = 'false'
			oldvalue['old_zebpay_error'] = 'false'
			error(e)

		#------------------------BEST BUY FROM-------------------------#

		try:
			oldvalue['old_best_btc_buy_from'] = oldsoup['best_btc_buy_from']
			oldvalue['old_best_eth_buy_from'] = oldsoup['best_eth_buy_from']
			oldvalue['old_best_bch_buy_from'] = oldsoup['best_bch_buy_from']
			oldvalue['old_best_ltc_buy_from'] = oldsoup['best_ltc_buy_from']
			oldvalue['old_best_xrp_buy_from'] = oldsoup['best_xrp_buy_from']
			oldvalue['old_best_dash_buy_from'] = oldsoup['best_dash_buy_from']

			#------------------------BEST SELL TO-------------------------#
			oldvalue['old_best_btc_sell_to'] = oldsoup['best_btc_sell_to']
			oldvalue['old_best_eth_sell_to'] = oldsoup['best_eth_sell_to']
			oldvalue['old_best_bch_sell_to'] = oldsoup['best_bch_sell_to']
			oldvalue['old_best_ltc_sell_to'] = oldsoup['best_ltc_sell_to']
			oldvalue['old_best_xrp_sell_to'] = oldsoup['best_xrp_sell_to']
			oldvalue['old_best_dash_sell_to'] = oldsoup['best_dash_sell_to']
		
		except Exception as e:

			oldvalue['old_best_btc_buy_from'] = '---'
			oldvalue['old_best_eth_buy_from'] = '---'
			oldvalue['old_best_bch_buy_from'] = '---'
			oldvalue['old_best_ltc_buy_from'] = '---'
			oldvalue['old_best_xrp_buy_from'] = '---'
			oldvalue['old_best_btc_sell_to'] = '---'
			oldvalue['old_best_eth_sell_to'] = '---'
			oldvalue['old_best_bch_sell_to'] = '---'
			oldvalue['old_best_ltc_sell_to'] = '---'
			oldvalue['old_best_xrp_sell_to'] = '---'
			oldvalue['old_best_dash_sell_to'] = '---'
			error(e)


		#---------------------COINS BUY/SELL-------------------------#
		
		oldvalue['old_unocoin_btc_buy'] = oldsoup['unocoin_btc_buy']
		oldvalue['old_unocoin_btc_sell'] = oldsoup['unocoin_btc_sell']
		oldvalue['old_unocoin_timestamp'] = oldsoup['unocoin_timestamp']

		oldvalue['old_zebpay_btc_buy'] = oldsoup['zebpay_btc_buy']
		oldvalue['old_zebpay_btc_sell'] = oldsoup['zebpay_btc_sell']
		oldvalue['old_zebpay_timestamp'] = oldsoup['zebpay_timestamp']

		oldvalue['old_koinex_btc_buy'] = oldsoup['koinex_btc_buy']
		oldvalue['old_koinex_btc_sell'] = oldsoup['koinex_btc_sell']
		oldvalue['old_koinex_eth_buy'] = oldsoup['koinex_eth_buy']
		oldvalue['old_koinex_eth_sell'] = oldsoup['koinex_eth_sell']
		oldvalue['old_koinex_ltc_buy'] = oldsoup['koinex_ltc_buy']
		oldvalue['old_koinex_ltc_sell'] = oldsoup['koinex_ltc_sell']
		oldvalue['old_koinex_bch_buy'] = oldsoup['koinex_bch_buy']
		oldvalue['old_koinex_bch_sell'] = oldsoup['koinex_bch_sell']
		oldvalue['old_koinex_xrp_buy'] = oldsoup['koinex_xrp_buy']
		oldvalue['old_koinex_xrp_sell'] = oldsoup['koinex_xrp_sell']
		oldvalue['old_koinex_timestamp'] = oldsoup['koinex_timestamp']

		oldvalue['old_buyucoin_btc_buy'] = oldsoup['buyucoin_btc_buy']
		oldvalue['old_buyucoin_btc_sell'] = oldsoup['buyucoin_btc_sell']
		oldvalue['old_buyucoin_timestamp'] = oldsoup['buyucoin_timestamp']

		oldvalue['old_coinsecure_btc_buy'] = oldsoup['coinsecure_btc_buy']
		oldvalue['old_coinsecure_btc_sell'] = oldsoup['coinsecure_btc_sell']
		oldvalue['old_coinsecure_timestamp'] = oldsoup['coinsecure_timestamp']

		oldvalue['old_coinome_btc_buy'] = oldsoup['coinome_btc_buy']
		oldvalue['old_coinome_btc_sell'] = oldsoup['coinome_btc_sell']
		oldvalue['old_coinome_bch_buy'] = oldsoup['coinome_bch_buy']
		oldvalue['old_coinome_bch_sell'] = oldsoup['coinome_bch_sell']
		oldvalue['old_coinome_ltc_buy'] = oldsoup['coinome_ltc_buy']
		oldvalue['old_coinome_ltc_sell'] = oldsoup['coinome_ltc_sell']
		oldvalue['old_coinome_dash_buy'] = oldsoup['coinome_dash_buy']
		oldvalue['old_coinome_dash_sell'] = oldsoup['coinome_dash_sell']
		oldvalue['old_coinome_timestamp'] = oldsoup['coinome_timestamp']

		oldvalue['old_pocketbits_btc_buy'] = oldsoup['pocketbits_btc_buy']
		oldvalue['old_pocketbits_btc_sell'] = oldsoup['pocketbits_btc_sell']
		oldvalue['old_pocketbits_timestamp'] = oldsoup['pocketbits_timestamp']

		oldvalue['old_ethex_eth_buy'] = oldsoup['ethex_eth_buy']
		oldvalue['old_ethex_eth_sell'] = oldsoup['ethex_eth_sell']
		oldvalue['old_ethex_timestamp'] = oldsoup['ethex_timestamp']

		oldvalue['old_btcx_xrp_buy'] = oldsoup['btcx_xrp_buy']
		oldvalue['old_btcx_xrp_sell'] = oldsoup['btcx_xrp_sell']
		oldvalue['old_btcx_timestamp'] = oldsoup['btcx_timestamp']

		oldvalue['old_coindelta_btc_buy'] = oldsoup['coindelta_btc_buy']
		oldvalue['old_coindelta_btc_sell'] = oldsoup['coindelta_btc_sell']
		oldvalue['old_coindelta_eth_buy'] = oldsoup['coindelta_eth_buy']
		oldvalue['old_coindelta_eth_sell'] = oldsoup['coindelta_eth_sell']
		oldvalue['old_coindelta_ltc_buy'] = oldsoup['coindelta_ltc_buy']
		oldvalue['old_coindelta_ltc_sell'] = oldsoup['coindelta_ltc_sell']
		oldvalue['old_coindelta_bch_buy'] = oldsoup['coindelta_bch_buy']
		oldvalue['old_coindelta_bch_sell'] = oldsoup['coindelta_bch_sell']
		oldvalue['old_coindelta_xrp_buy'] = oldsoup['coindelta_xrp_buy']
		oldvalue['old_coindelta_xrp_sell'] = oldsoup['coindelta_xrp_sell']
		oldvalue['old_coindelta_timestamp'] = oldsoup['coindelta_timestamp']


		#-----------------BEST BUY SELL VALUE------------------#
		try: 
			oldvalue['old_best_btc_buy'] = oldsoup['best_btc_buy']
			oldvalue['old_best_btc_sell'] = oldsoup['best_btc_sell']
			oldvalue['old_best_eth_buy'] = oldsoup['best_eth_buy']
			oldvalue['old_best_eth_sell'] = oldsoup['best_eth_sell']
			oldvalue['old_best_bch_buy'] = oldsoup['best_bch_buy']
			oldvalue['old_best_bch_sell'] = oldsoup['best_bch_sell']
			oldvalue['old_best_ltc_buy'] = oldsoup['best_ltc_buy']
			oldvalue['old_best_ltc_sell'] = oldsoup['best_ltc_sell']
			oldvalue['old_best_xrp_buy'] = oldsoup['best_xrp_buy']
			oldvalue['old_best_xrp_sell'] = oldsoup['best_xrp_sell']
			oldvalue['old_best_dash_buy'] = oldsoup['best_dash_buy']
			oldvalue['old_best_dash_sell'] = oldsoup['best_dash_sell']
		
		except exception as e:
			oldvalue['old_best_btc_buy'] = 0
			oldvalue['old_best_btc_sell'] = 0
			oldvalue['old_best_eth_buy'] = 0
			oldvalue['old_best_eth_sell'] = 0
			oldvalue['old_best_bch_buy'] = 0
			oldvalue['old_best_bch_sell'] = 0
			oldvalue['old_best_ltc_buy'] = 0
			oldvalue['old_best_ltc_sell'] = 0
			oldvalue['old_best_xrp_buy'] = 0
			oldvalue['old_best_xrp_sell'] = 0
			oldvalue['old_best_dash_buy'] = 0
			oldvalue['old_best_dash_sell'] = 0
			error(e)

	
#--------------------------FEES IN JSON---------------------------------------#
		try:
			coinsoup['buyucoin_buy_fees'] = buyucoin_buy_fees
			coinsoup['buyucoin_sell_fees'] = buyucoin_sell_fees

			coinsoup['btcx_buy_fees'] = btcx_buy_fees
			coinsoup['btcx_sell_fees'] = btcx_sell_fees

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
			coinsoup['btcx_buy_fees'] = 0
			coinsoup['btcx_sell_fees'] = 0
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

	btc_sell_dict = {}
	eth_sell_dict = {}
	bch_sell_dict = {}
	ltc_sell_dict = {}
	xrp_sell_dict = {}
	dash_sell_dict = {}



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
		unocoin_btc_buy = float(oldvalue['old_unocoin_btc_buy'])
		unocoin_btc_sell = float(oldvalue['old_unocoin_btc_sell'])
		coinsoup['unocoin_btc_buy'] = float(oldvalue['old_unocoin_btc_buy'])
		coinsoup['unocoin_btc_sell'] = float(oldvalue['old_unocoin_btc_sell'])
		coinsoup['unocoin_timestamp'] = int(oldvalue['old_unocoin_timestamp'])
		error(e)



	try:
		html22 = requests.get('https://www.zebapi.com/api/v1/market/ticker-new/BTC/INR')
		soup22 = html22.json()
		soup_zebpay = html22.json()
		zebpay_btc_buy=float(soup_zebpay['buy'])
		zebpay_btc_sell=float(soup_zebpay['sell'])
		coinsoup['zebpay_btc_buy'] = float(zebpay_btc_buy)
		coinsoup['zebpay_btc_sell'] = float(zebpay_btc_sell)
		coinsoup['zebpay_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
		print('zebpay working')
	except Exception as e:
		print('some exception occured in zebpay')
		zebpay_btc_buy = float(oldvalue['old_zebpay_btc_buy'])
		zebpay_btc_sell = float(oldvalue['old_zebpay_btc_sell'])
		coinsoup['zebpay_btc_buy'] = float(oldvalue['old_zebpay_btc_buy'])
		coinsoup['zebpay_btc_sell'] = float(oldvalue['old_zebpay_btc_sell'])
		coinsoup['zebpay_timestamp'] = int(oldvalue['old_zebpay_timestamp'])
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
		print('koinex working')
		coinsoup['koinex_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())

	except Exception as e:
		print('some exception occured in koinex')
		koinex_btc_buy = float(oldvalue['old_koinex_btc_buy'])
		koinex_btc_sell = float(oldvalue['old_koinex_btc_sell'])
		koinex_eth_buy = float(oldvalue['old_koinex_eth_buy'])
		koinex_eth_sell = float(oldvalue['old_koinex_eth_sell'])
		koinex_bch_buy = float(oldvalue['old_koinex_bch_buy'])
		koinex_bch_sell = float(oldvalue['old_koinex_bch_sell'])
		koinex_ltc_buy = float(oldvalue['old_koinex_ltc_buy'])
		koinex_ltc_sell = float(oldvalue['old_koinex_ltc_sell'])
		koinex_xrp_buy = float(oldvalue['old_koinex_xrp_buy'])
		koinex_xrp_sell = float(oldvalue['old_koinex_xrp_sell'])

		coinsoup['koinex_btc_buy'] = float(oldvalue['old_koinex_btc_buy'])
		coinsoup['koinex_btc_sell'] = float(oldvalue['old_koinex_btc_sell'])
		coinsoup['koinex_eth_buy'] = float(oldvalue['old_koinex_eth_buy'])
		coinsoup['koinex_eth_sell'] = float(oldvalue['old_koinex_eth_sell'])
		coinsoup['koinex_bch_buy'] = float(oldvalue['old_koinex_bch_buy'])
		coinsoup['koinex_bch_sell'] = float(oldvalue['old_koinex_bch_sell'])
		coinsoup['koinex_ltc_buy'] = float(oldvalue['old_koinex_ltc_buy'])
		coinsoup['koinex_ltc_sell'] = float(oldvalue['old_koinex_ltc_sell'])
		coinsoup['koinex_xrp_buy'] = float(oldvalue['old_koinex_xrp_buy'])
		coinsoup['koinex_xrp_sell'] = float(oldvalue['old_koinex_xrp_sell'])
		coinsoup['koinex_timestamp'] = int(oldvalue['old_koinex_timestamp'])

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
		buyucoin_btc_buy = float(oldvalue['old_buyucoin_btc_buy'])
		buyucoin_btc_sell = float(oldvalue['old_buyucoin_btc_sell'])
		coinsoup['buyucoin_btc_buy'] = float(oldvalue['old_buyucoin_btc_buy'])
		coinsoup['buyucoin_btc_sell'] = float(oldvalue['old_buyucoin_btc_sell'])
		coinsoup['buyucoin_timestamp'] = int(oldvalue['old_buyucoin_timestamp'])

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
		coinsecure_btc_buy = float(oldvalue['old_coinsecure_btc_buy'])
		coinsecure_btc_sell = float(oldvalue['old_coinsecure_btc_sell'])
		coinsoup['coinsecure_btc_buy'] = float(oldvalue['old_coinsecure_btc_buy'])
		coinsoup['coinsecure_btc_sell'] = float(oldvalue['old_coinsecure_btc_sell'])
		coinsoup['coinsecure_timestamp'] = int(oldvalue['old_coinsecure_timestamp'])
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
		ethex_eth_buy = float(oldvalue['old_ethex_eth_buy'])
		ethex_eth_sell = float(oldvalue['old_ethex_eth_sell'])
		coinsoup['ethex_eth_buy'] = float(oldvalue['old_ethex_eth_buy'])
		coinsoup['ethex_eth_sell'] = float(oldvalue['old_ethex_eth_sell'])
		coinsoup['ethex_timestamp'] = int(oldvalue['old_ethex_timestamp'])

		error(e)

	try:
		bscraper = cfscrape.create_scraper()
		html_btcx = bscraper.get("https://api.btcxindia.com/ticker/")
		soup_btcx = html_btcx.json()
		btcx_xrp_buy = float(soup_btcx['ask'])
		btcx_xrp_sell = float(soup_btcx['bid'])
		coinsoup['btcx_xrp_buy'] = float(btcx_xrp_buy)
		coinsoup['btcx_xrp_sell'] = float(btcx_xrp_sell)        
		print('Btcx Working')
		coinsoup['btcx_timestamp'] = int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1, 0, 0, 0, 0)).total_seconds())
	except Exception as e:
		print('some exception occured in  btcx')
		btcx_xrp_buy = float(oldvalue['old_btcx_xrp_buy'])
		btcx_xrp_sell = float(oldvalue['old_btcx_xrp_sell'])
		coinsoup['btcx_xrp_buy'] = float(oldvalue['old_btcx_xrp_buy'])
		coinsoup['btcx_xrp_sell'] = float(oldvalue['old_btcx_xrp_sell'])
		coinsoup['btcx_timestamp'] = int(oldvalue['old_btcx_timestamp'])

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
		print(coinome_dash_buy)
		print(coinome_dash_sell)
	except Exception as e:
		print('some exception occured in coinome')
		coinome_btc_buy = float(oldvalue['old_coinome_btc_buy'])
		coinome_btc_sell = float(oldvalue['old_coinome_btc_sell'])
		coinome_bch_buy = float(oldvalue['old_coinome_bch_buy'])
		coinome_bch_sell = float(oldvalue['old_coinome_bch_sell'])
		coinome_ltc_buy = float(oldvalue['old_coinome_ltc_buy'])
		coinome_ltc_sell = float(oldvalue['old_coinome_ltc_sell'])

		coinsoup['coinome_btc_buy'] = float(oldvalue['old_coinome_btc_buy'])
		coinsoup['coinome_btc_sell'] = float(oldvalue['old_coinome_btc_sell'])
		coinsoup['coinome_bch_buy'] = float(oldvalue['old_coinome_bch_buy'])
		coinsoup['coinome_bch_sell'] = float(oldvalue['old_coinome_bch_sell'])
		coinsoup['coinome_ltc_buy'] = float(oldvalue['old_coinome_ltc_buy'])
		coinsoup['coinome_ltc_sell'] = float(oldvalue['old_coinome_ltc_sell'])
		coinsoup['coinome_dash_buy'] = float(oldvalue['old_coinome_dash_buy'])
		coinsoup['coinome_dash_sell'] = float(oldvalue['old_coinome_dash_sell'])
		coinsoup['coinome_timestamp'] = int(oldvalue['old_coinome_timestamp'])

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
		pocketbits_btc_buy = float(oldvalue['old_pocketbits_btc_buy'])
		pocketbits_btc_sell = float(oldvalue['old_pocketbits_btc_sell'])
		coinsoup['pocketbits_btc_buy'] = float(oldvalue['old_pocketbits_btc_buy'])
		coinsoup['pocketbits_btc_sell'] = float(oldvalue['old_pocketbits_btc_sell'])
		coinsoup['pocketbits_timestamp'] = int(oldvalue['old_pocketbits_timestamp'])

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
		coindelta_buy_btc = float(oldvalue['old_coindelta_btc_buy'])
		coindelta_sell_btc = float(oldvalue['old_coindelta_btc_sell'])
		coindelta_buy_eth = float(oldvalue['old_coindelta_eth_buy'])
		coindelta_sell_eth = float(oldvalue['old_coindelta_eth_sell'])
		coindelta_buy_bch = float(oldvalue['old_coindelta_bch_buy'])
		coindelta_sell_bch = float(oldvalue['old_coindelta_bch_sell'])
		coindelta_buy_ltc = float(oldvalue['old_coindelta_ltc_buy'])
		coindelta_sell_ltc = float(oldvalue['old_coindelta_ltc_sell'])
		coindelta_buy_xrp = float(oldvalue['old_coindelta_xrp_buy'])
		coindelta_sell_xrp = float(oldvalue['old_coindelta_xrp_sell'])

		coinsoup['coindelta_btc_buy'] = float(oldvalue['old_coindelta_btc_buy'])
		coinsoup['coindelta_btc_sell'] = float(oldvalue['old_coindelta_btc_sell'])
		coinsoup['coindelta_eth_buy'] = float(oldvalue['old_coindelta_eth_buy'])
		coinsoup['coindelta_eth_sell'] = float(oldvalue['old_coindelta_eth_sell'])
		coinsoup['coindelta_bch_buy'] = float(oldvalue['old_coindelta_bch_buy'])
		coinsoup['coindelta_bch_sell'] = float(oldvalue['old_coindelta_bch_sell'])
		coinsoup['coindelta_ltc_buy'] = float(oldvalue['old_coindelta_ltc_buy'])
		coinsoup['coindelta_ltc_sell'] = float(oldvalue['old_coindelta_ltc_sell'])
		coinsoup['coindelta_xrp_buy'] = float(oldvalue['old_coindelta_xrp_buy'])
		coinsoup['coindelta_xrp_sell'] = float(oldvalue['old_coindelta_xrp_sell'])
		coinsoup['coindelta_timestamp'] = int(oldvalue['old_coindelta_timestamp'])

		error(e)


	with open('./coinprice.json', 'w',encoding='utf-8') as f:
			
			json.dump(coinsoup,f)


	current_time= int(datetime.datetime.now().timestamp())
	json_content = json.load(open('coinprice.json'))
	
	
	try:
		if(int(current_time - json_content['btcx_timestamp']<=120)):
			btcx_err = False
			
			xrp_buy_dict['btcxindia'] = btcx_xrp_buy
			xrp_sell_dict['btcxindia'] = btcx_xrp_sell
		else:
			btcx_err = True	
		
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

			btc_buy_dict['koinex'] = koinex_btc_sell
			bch_sell_dict['koinex'] = koinex_bch_sell
			ltc_sell_dict['koinex'] = koinex_ltc_sell
			eth_sell_dict['koinex'] = koinex_eth_sell
			xrp_sell_dict['koinex'] = koinex_xrp_sell

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
		else:
			zebpay_err = True
	except Exception as e :

		buyucoin_err = oldvalue['old_buyucoin_error']
		btcx_err = oldvalue['old_btcx_error']
		coindelta_err = oldvalue['old_coindelta_error']
		coinome_err = oldvalue['old_coinome_error']
		coinsecure_err = oldvalue['old_coinsecure_error']
		ethex_err = oldvalue['old_ethex_error']
		koinex_err = oldvalue['old_koinex_error']
		pocketbits_err = oldvalue['old_pocketbits_error']
		unocoin_err = oldvalue['old_unocoin_error']
		zebpay_err = oldvalue['old_zebpay_error']

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
		 
		print(best_dash_buy)
		print(best_dash_sell)
	except Exception as e:
		print("some exception occ in best values")

		best_btc_buy = oldvalue['old_best_btc_buy']
		best_eth_buy = oldvalue['old_best_eth_buy']
		best_bch_buy = oldvalue['old_best_bch_buy']
		best_ltc_buy = oldvalue['old_best_ltc_buy']
		best_xrp_buy = oldvalue['old_best_xrp_buy']
		best_dash_buy = oldvalue['old_best_dash_buy']
		best_btc_sell = oldvalue['old_best_btc_sell']
		best_eth_sell = oldvalue['old_best_eth_sell']
		best_bch_sell = oldvalue['old_best_bch_sell']
		best_ltc_sell = oldvalue['old_best_ltc_sell']
		best_xrp_sell = oldvalue['old_best_xrp_sell']
		best_dash_sell = oldvalue['old_best_dash_sell']

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
	except Exception as e:


		best_btc_buy_from = oldvalue['old_best_btc_buy_from']
		best_eth_buy_from = oldvalue['old_best_eth_buy_from']
		best_bch_buy_from = oldvalue['old_best_bch_buy_from']
		best_ltc_buy_from = oldvalue['old_best_ltc_buy_from']
		best_xrp_buy_from = oldvalue['old_best_xrp_buy_from']
		best_dash_buy_from = oldvalue['old_best_dash_buy_from']
		best_btc_sell_to = oldvalue['old_best_btc_sell_to']
		best_eth_sell_to = oldvalue['old_best_eth_sell_to']
		best_bch_sell_to = oldvalue['old_best_bch_sell_to']
		best_ltc_sell_to = oldvalue['old_best_ltc_sell_to']
		best_xrp_sell_to = oldvalue['old_best_xrp_sell_to']
		best_dash_sell_to = oldvalue['old_best_dash_sell_to']
	
		error(e)


	coinsoup['btcx_error'] = btcx_err
	coinsoup['buyucoin_error'] = buyucoin_err
	coinsoup['coindelta_error'] = coindelta_err
	coinsoup['coinome_error'] = coinome_err
	coinsoup['coinsecure_error'] = coinsecure_err
	coinsoup['ethex_error'] =  ethex_err
	coinsoup['koinex_error'] = koinex_err
	coinsoup['pocketbits_error'] = pocketbits_err
	coinsoup['unocoin_error'] = unocoin_err
	coinsoup['zebpay_error'] = zebpay_err

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


	