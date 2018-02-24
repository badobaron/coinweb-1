from django.urls import path
from . import views

urlpatterns =[
	path('',views.index, name='index'),
	path('api',views.api, name='api'),
	path('uc_btc_by/', views.uc_btc_by, name='uc_btc_by'),
	path('uc_btc_sl/', views.uc_btc_sl, name='uc_btc_sl'),
	path('zp_btc_by/', views.zp_btc_by, name='zp_btc_by'),
	path('zp_btc_sl/', views.zp_btc_sl, name='zp_btc_sl'),
	path('kx_eth_by/', views.kx_eth_by, name='kx_eth_by'),
	path('kx_eth_sl/', views.kx_eth_sl, name='kx_eth_sl'),
	path('kx_btc_by/', views.kx_btc_by, name='kx_btc_by'),
	path('kx_btc_sl/', views.kx_btc_sl, name='kx_btc_sl'),
	path('kx_ltc_by/', views.kx_ltc_by, name='kx_ltc_by'),
	path('kx_ltc_sl/', views.kx_ltc_sl, name='kx_ltc_sl'),
	path('kx_bch_by/', views.kx_bch_by, name='kx_bch_by'),
	path('kx_bch_sl/', views.kx_bch_sl, name='kx_bch_sl'),
	path('kx_xrp_by/', views.kx_xrp_by, name='kx_xrp_by'),
	path('kx_xrp_sl/', views.kx_xrp_sl, name='kx_xrp_sl'),
	path('bu_btc_by/', views.bu_btc_by, name='bu_btc_by'),
	path('bu_btc_sl/', views.bu_btc_sl, name='bu_btc_sl'),
	path('cs_btc_by/', views.cs_btc_by, name='cs_btc_by'),
	path('cs_btc_sl/', views.cs_btc_sl, name='cs_btc_sl'),
	path('ex_eth_by/', views.ex_eth_by, name='ex_eth_by'),
	path('ex_eth_sl/', views.ex_eth_sl, name='ex_eth_sl'),
	path('bx_xrp_by/', views.bx_xrp_by, name='bx_xrp_by'),
	path('bx_xrp_sl/', views.bx_xrp_sl, name='bx_xrp_sl'),
	path('cn_btc_by/', views.cn_btc_by, name='cn_btc_by'),
	path('cn_btc_sl/', views.cn_btc_sl, name='cn_btc_sl'),
	path('cn_bch_by/', views.cn_bch_by, name='cn_bch_by'),
	path('cn_bch_sl/', views.cn_bch_sl, name='cn_bch_sl'),
	path('cn_ltc_by/', views.cn_ltc_by, name='cn_ltc_by'),
	path('cn_ltc_sl/', views.cn_ltc_sl, name='cn_ltc_sl'),
	path('pb_btc_by/', views.pb_btc_by, name='pb_btc_by'),
	path('pb_btc_sl/', views.pb_btc_sl, name='pb_btc_sl'),
	path('cd_btc_by/', views.cd_btc_by, name='cd_btc_by'),
	path('cd_btc_sl/', views.cd_btc_sl, name='cd_btc_sl'),
	path('cd_eth_by/', views.cd_eth_by, name='cd_eth_by'),
	path('cd_eth_sl/', views.cd_eth_sl, name='cd_eth_sl'),
	path('cd_ltc_by/', views.cd_ltc_by, name='cd_ltc_by'),
	path('cd_ltc_sl/', views.cd_ltc_sl, name='cd_ltc_sl'),
	path('cd_bch_by/', views.cd_bch_by, name='cd_bch_by'),
	path('cd_bch_sl/', views.cd_bch_sl, name='cd_bch_sl'),
	path('cd_xrp_by/', views.cd_xrp_by, name='cd_xrp_by'),
	path('cd_xrp_sl/', views.cd_xrp_sl, name='cd_btc_sl'),
	path('bt_btc_by/', views.bt_btc_by, name='bt_btc_by'),
	path('bt_btc_sl/', views.bt_btc_sl, name='bt_btc_sl'),
	path('bt_eth_by/', views.bt_eth_by, name='bt_eth_by'),
	path('bt_eth_sl/', views.bt_eth_sl, name='bt_eth_sl'),
	path('bt_bch_by/', views.bt_bch_by, name='bt_bch_by'),
	path('bt_bch_sl/', views.bt_bch_sl, name='bt_bch_sl'),
	path('bt_ltc_by/', views.bt_ltc_by, name='bt_ltc_by'),
	path('bt_ltc_sl/', views.bt_ltc_sl, name='bt_ltc_sl'),
	path('bt_xrp_by/', views.bt_xrp_by, name='bt_xrp_by'),
	path('bt_xrp_sl/', views.bt_xrp_sl, name='bt_xrp_sl'),
	path('bt_btc_by_fr/', views.bt_btc_by_fr, name='bt_btc_by_fr'),
	path('bt_btc_sl_fr/', views.bt_btc_sl_fr, name='bt_btc_sl_fr'),
	path('bt_eth_by_fr/', views.bt_eth_by_fr, name='bt_eth_by_fr'),
	path('bt_eth_sl_fr/', views.bt_eth_sl_fr, name='bt_eth_sl_fr'),
	path('bt_bch_by_fr/', views.bt_bch_by_fr, name='bt_bch_by_fr'),
	path('bt_bch_sl_fr/', views.bt_bch_sl_fr, name='bt_bch_sl_fr'),
	path('bt_ltc_by_fr/', views.bt_ltc_by_fr, name='bt_ltc_by_fr'),
	path('bt_ltc_sl_fr/', views.bt_ltc_sl_fr, name='bt_ltc_sl_fr'),
	path('bt_xrp_by_fr/', views.bt_xrp_by_fr, name='bt_xrp_by_fr'),
	path('bt_xrp_sl_fr/', views.bt_xrp_sl_fr, name='bt_xrp_sl_fr'),


]