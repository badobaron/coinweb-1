import os
from coinweb.settings import PROJECT_ROOT
import json
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'coinapp/index.html', {})


def uc_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["unocoin_btc_buy"]
    return HttpResponse(results)


def uc_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["unocoin_btc_sell"]
    return HttpResponse(results)


def zp_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["zebpay_btc_buy"]
    return HttpResponse(results)


def zp_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["zebpay_btc_sell"]
    return HttpResponse(results)


def kx_eth_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_eth_buy"]
    return HttpResponse(results)


def kx_eth_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_eth_sell"]
    return HttpResponse(results)


def kx_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_btc_buy"]
    return HttpResponse(results)


def kx_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_btc_sell"]
    return HttpResponse(results)


def kx_ltc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_ltc_buy"]
    return HttpResponse(results)


def kx_ltc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_ltc_sell"]
    return HttpResponse(results)


def kx_bch_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_bch_buy"]
    return HttpResponse(results)


def kx_bch_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_bch_sell"]
    return HttpResponse(results)


def kx_xrp_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_xrp_buy"]
    return HttpResponse(results)


def kx_xrp_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["koinex_xrp_sell"]
    return HttpResponse(results)


def bu_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["buyucoin_btc_buy"]
    return HttpResponse(results)


def bu_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["buyucoin_btc_sell"]
    return HttpResponse(results)


def cs_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinsecure_btc_buy"]
    return HttpResponse(results)


def cs_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinsecure_btc_sell"]
    return HttpResponse(results)


def ex_eth_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["ethex_eth_buy"]
    return HttpResponse(results)


def ex_eth_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["ethex_eth_sell"]
    return HttpResponse(results)


def bx_xrp_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["btcx_xrp_buy"]
    return HttpResponse(results)


def bx_xrp_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["btcx_xrp_sell"]
    return HttpResponse(results)


def cn_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinome_btc_buy"]
    return HttpResponse(results)


def cn_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinome_btc_sell"]
    return HttpResponse(results)


def cn_bch_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinome_bch_buy"]
    return HttpResponse(results)


def cn_bch_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinome_bch_sell"]
    return HttpResponse(results)


def cn_ltc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinome_ltc_buy"]
    return HttpResponse(results)


def cn_ltc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coinome_ltc_sell"]
    return HttpResponse(results)


def pb_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["pocketbits_btc_buy"]
    return HttpResponse(results)


def pb_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["pocketbits_btc_sell"]
    return HttpResponse(results)


def cd_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_btc_buy"]
    return HttpResponse(results)


def cd_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_btc_sell"]
    return HttpResponse(results)


def cd_eth_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_eth_buy"]
    return HttpResponse(results)


def cd_eth_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_eth_sell"]
    return HttpResponse(results)


def cd_ltc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_ltc_buy"]
    return HttpResponse(results)


def cd_ltc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_ltc_sell"]
    return HttpResponse(results)



def cd_bch_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_bch_buy"]
    return HttpResponse(results)


def cd_bch_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_bch_sell"]
    return HttpResponse(results)


def cd_xrp_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_xrp_buy"]
    return HttpResponse(results)


def cd_xrp_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["coindelta_xrp_sell"]
    return HttpResponse(results)


def bt_btc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_btc_buy"]
    return HttpResponse(results)


def bt_btc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_btc_sell"]
    return HttpResponse(results)


def bt_eth_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_eth_buy"]
    return HttpResponse(results)


def bt_eth_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_eth_sell"]
    return HttpResponse(results)


def bt_bch_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_bch_buy"]
    return HttpResponse(results)


def bt_bch_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_bch_sell"]
    return HttpResponse(results)


def bt_ltc_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_ltc_buy"]
    return HttpResponse(results)


def bt_ltc_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_ltc_sell"]
    return HttpResponse(results)


def bt_xrp_by(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_xrp_buy"]
    return HttpResponse(results)


def bt_xrp_sl(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_xrp_sell"]
    return HttpResponse(results)


def bt_btc_by_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_btc_buy_from"]
    return HttpResponse(results)


def bt_btc_sl_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_btc_sell_to"]
    return HttpResponse(results)


def bt_eth_by_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_eth_buy_from"]
    return HttpResponse(results)


def bt_eth_sl_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_eth_sell_to"]
    return HttpResponse(results)


def bt_bch_by_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_bch_buy_from"]
    return HttpResponse(results)


def bt_bch_sl_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_bch_sell_to"]
    return HttpResponse(results)


def bt_ltc_by_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_ltc_buy_from"]
    return HttpResponse(results)


def bt_ltc_sl_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_ltc_sell_to"]
    return HttpResponse(results)


def bt_xrp_by_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_xrp_buy_from"]
    return HttpResponse(results)

def bt_xrp_sl_fr(request):
    with open(os.path.join(PROJECT_ROOT, 'coinprice.json')) as json_file:
    	data=json.load(json_file)
    results = data["best_xrp_sell_to"]
    return HttpResponse(results)

