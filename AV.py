#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:48:32 2018

@author: shaydineen
"""

import requests
import alpha_vantage


API_URL = "https://www.alphavantage.co/query"

data = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "^GSPC",
    "outputsize" : "full",
    "datatype" : "csv",
    "apikey" : "0ZSSUD2LJQV6MK6M",
    }


outFile = 'Data/testData.csv'

page = requests.get(url = API_URL, params = data)

with open(outFile, 'w') as oF:
    oF.write(page.text)
    
macd = {
       'function' : 'MACD',
       'symbol' : '^GSPC',
       "outputsize" : "full",
       "datatype" : "csv",
       'interval' : 'daily',
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

macd_request = requests.get(url = API_URL, params = macd)

macd_file = 'Data/macd.json' 
with open(macd_file, 'w') as oF:
    oF.write(macd_request.text)
    
#RSI and stochastic

cci = {
       'function' : 'CCI',
       'symbol' : '^GSPC',
       'interval' : 'daily',
       'time_period' : '30', #investopedia says this is a standard value
       'apikey' : '0ZSSUD2LJQV6MK6M'}

cci_request = requests.get(url = API_URL, params = cci)
cci_file = 'Data/cci.json'

with open(cci_file, 'w') as oF:
    oF.write(cci_request.text)
    
atr = {
       'function' : 'ATR',
       'symbol' : '^GSPC',
       'interval' : 'daily',
       'time_period' : '14', #investopedia says this is a standard value
       'apikey' : '0ZSSUD2LJQV6MK6M'}

atr_request = requests.get(url = API_URL, params = atr)
atr_file = 'Data/atr.json'

with open(atr_file, 'w') as oF:
    oF.write(atr_request.text)
    
boll = {
        'function' : 'BBANDS',
        'symbol' : '^GSPC',
        'interval' : 'daily',
        'time_period' : '20', #investopedia says this is a standard value
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

boll_request = requests.get(url = API_URL, params = boll)
boll_file = 'Data/boll.json'

with open(boll_file, 'w') as oF:
    oF.write(boll_request.text)
    
ema20 = {
        'function' : 'EMA',
        'symbol' : '^GSPC',
        'interval' : 'daily',
        'time_period' : '20', #what was used in actual paper
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

ema20_request = requests.get(url = API_URL, params = ema20)
ema20_file = 'Data/ema20.json'

with open(ema20_file, 'w') as oF:
    oF.write(ema20_request.text)
    
ma5 = {
       'function' : 'sma', 
       'symbol' : '^GSPC',
       'interval' : 'daily',
       'time_period' : '5', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma5_request = requests.get(url = API_URL, params = ma5)
ma5_file = 'Data/ma5.json'

with open(ma5_file, 'w') as oF:
    oF.write(ma5_request.text)
    
ma10 = {
       'function' : 'sma', 
       'symbol' : '^GSPC',
       'interval' : 'daily',
       'time_period' : '10', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma10_request = requests.get(url = API_URL, params = ma10)
ma10_file = 'Data/ma10.json'

with open(ma10_file, 'w') as oF:
    oF.write(ma10_request.text)

mom6 = {
        'function' : 'MOM',
        'symbol' : '^GSPC',
        'interval' : 'daily',
        'time_period' : '127', #they said they used six months and on average there are 252 trading days in a year so half of that is 127
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

mom6_request = requests.get(url = API_URL, params = mom6)
mom6_file = 'Data/mom6.json'

with open(mom6_file, 'w') as oF:
    oF.write(mom6_request.text)

mom12 = {
        'function' : 'MOM',
        'symbol' : '^GSPC',
        'interval' : 'daily',
        'time_period' : '252', #they said they used twelve months and on average there are 252 trading days in a year
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

mom12_request = requests.get(url = API_URL, params = mom12)
mom12_file = 'Data/mom12.json'

with open(mom12_file, 'w') as oF:
    oF.write(mom12_request.text)
    
roc = {
        'function' : 'ROC',
        'symbol' : '^GSPC',
        'interval' : 'daily',
        'time_period' : '127', #using the same value as six month momentum
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

roc_request = requests.get(url = API_URL, params = roc)
roc_file = 'Data/roc.json'

with open(roc_file, 'w') as oF:
    oF.write(roc_request.text)
    
wvad = {
        'function' : 'WILLR',
        'symbol' : '^GSPC',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

wvad_request = requests.get(url = API_URL, params = wvad)
wvad_file = 'Data/wvad.json'

with open(wvad_file, 'w') as oF:
    oF.write(wvad_request.text)

stoch = {
        'function' : 'STOCH',
        'symbol' : '^GSPC',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

stoch_request = requests.get(url = API_URL, params = stoch)
stoch_file = 'Data/stoch.json'

with open(stoch_file, 'w') as oF:
    oF.write(stoch_request.text)
    
us_dollar = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "DXY",
    "outputsize" : "full",
    "datatype" : "csv",
    "apikey" : "0ZSSUD2LJQV6MK6M",
    }


usdx_file = 'Data/usdx.csv'

usdx_request = requests.get(url = API_URL, params = us_dollar)

with open(usdx_file, 'w') as oF:
    oF.write(usdx_request.text)
    
tnx = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "^TNX",
    "outputsize" : "full",
    "datatype" : "csv",
    "apikey" : "0ZSSUD2LJQV6MK6M",
    }


tnx_file = 'Data/tnx.csv'

tnx_request = requests.get(url = API_URL, params = tnx)

with open(tnx_file, 'w') as oF:
    oF.write(tnx_request.text)

vix = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "VIX",
    "outputsize" : "full",
    "datatype" : "csv",
    "apikey" : "0ZSSUD2LJQV6MK6M",
    }


vix_file = 'Data/VIX.csv'

vix_request = requests.get(url = API_URL, params = vix)

with open(vix_file, 'w') as oF:
    oF.write(vix_request.text)

rsi= {
       'function' : 'RSI',
       'symbol' : '^GSPC',
       'interval' : 'daily',
       'time_period' : '14',
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

rsi_file = 'Data/rsi.json'
rsi_request = requests.get(url = API_URL, params = rsi)

with open(rsi_file, 'w') as oF:
    oF.write(rsi_request.text)
    
    
spy = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "SPY",
    "outputsize" : "full",
    "datatype" : "csv",
    "apikey" : "0ZSSUD2LJQV6MK6M",
    }


spy_file = 'ETF Opportunity Set/spy.csv'

spy_request = requests.get(url = API_URL, params = spy)

with open(spy_file, 'w') as oF:
    oF.write(spy_request.text)

stoch_spy = {
        'function' : 'STOCH',
        'symbol' : 'SPY',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

stoch_spy_request = requests.get(url = API_URL, params = stoch_spy)
stoch_spy_file = 'ETF Opportunity Set/SPY/stoch_spy.json'

with open(stoch_spy_file, 'w') as oF:
    oF.write(stoch_spy_request.text)

ema20_spy = {
        'function' : 'EMA',
        'symbol' : 'SPY',
        'interval' : 'daily',
        'time_period' : '20', #what was used in actual paper
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

ema20_spy_request = requests.get(url = API_URL, params = ema20_spy)
ema20_spy_file = 'ETF Opportunity Set/SPY/ema20_spy.json'

with open(ema20_spy_file, 'w') as oF:
    oF.write(ema20_spy_request.text)

ma5_spy = {
       'function' : 'sma', 
       'symbol' : 'SPY',
       'interval' : 'daily',
       'time_period' : '5', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma5_spy_request = requests.get(url = API_URL, params = ma5_spy)
ma5_spy_file = 'ETF_Opportunity_Set/SPY/ma5_spy.json'

with open(ma5_spy_file, 'w') as oF:
    oF.write(ma5_spy_request.text)
    
ma10_spy = {
       'function' : 'sma', 
       'symbol' : 'SPY',
       'interval' : 'daily',
       'time_period' : '10', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma10_spy_request = requests.get(url = API_URL, params = ma10_spy)
ma10_spy_file = 'ETF_Opportunity_Set/SPY/ma10_spy.json'

with open(ma10_spy_file, 'w') as oF:
    oF.write(ma10_spy_request.text)

wvad_spy = {
        'function' : 'WILLR',
        'symbol' : 'SPY',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

wvad_spy_request = requests.get(url = API_URL, params = wvad_spy)
wvad_spy_file = 'ETF_Opportunity_Set/SPY/wvad_spy.json'

with open(wvad_spy_file, 'w') as oF:
    oF.write(wvad_spy_request.text)


rsi_spy= {
       'function' : 'RSI',
       'symbol' : 'SPY',
       'interval' : 'daily',
       'time_period' : '14',
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

rsi_spy_file = 'ETF_Opportunity_Set/SPY/rsi_spy.json'
rsi_spy_request = requests.get(url = API_URL, params = rsi_spy)

with open(rsi_spy_file, 'w') as oF:
    oF.write(rsi_spy_request.text)

#ma5 ma10 and RSI
    
# =============================================================================
# IWM
# =============================================================================
iwm = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "IWM",
    "outputsize" : "full",
    "datatype" : "csv",
    "apikey" : "0ZSSUD2LJQV6MK6M",
    }


iwm_file = 'ETF_Opportunity_Set/IWN/iwn.csv'

iwn_request = requests.get(url = API_URL, params = iwm)

with open(iwm_file, 'w') as oF:
    oF.write(iwn_request.text)

stoch_iwm = {
        'function' : 'STOCH',
        'symbol' : 'IWM',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

stoch_iwm_request = requests.get(url = API_URL, params = stoch_iwm)
stoch_iwm_file = 'ETF_Opportunity_Set/IWN/stoch_iwn.json'

with open(stoch_iwm_file, 'w') as oF:
    oF.write(stoch_iwm_request.text)

ema20_iwm = {
        'function' : 'EMA',
        'symbol' : 'IWM',
        'interval' : 'daily',
        'time_period' : '20', #what was used in actual paper
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

ema20_iwm_request = requests.get(url = API_URL, params = ema20_iwm)
ema20_iwm_file = 'ETF_Opportunity_Set/IWN/ema20_iwm.json'

with open(ema20_iwm_file, 'w') as oF:
    oF.write(ema20_iwm_request.text)

ma5_iwm = {
       'function' : 'sma', 
       'symbol' : 'IWM',
       'interval' : 'daily',
       'time_period' : '5', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma5_iwm_request = requests.get(url = API_URL, params = ma5_iwm)
ma5_iwm_file = 'ETF_Opportunity_Set/IWN/ma5_iwm.json'

with open(ma5_iwm_file, 'w') as oF:
    oF.write(ma5_iwm_request.text)
    
ma10_iwm = {
       'function' : 'sma', 
       'symbol' : 'IWM',
       'interval' : 'daily',
       'time_period' : '10', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma10_iwm_request = requests.get(url = API_URL, params = ma10_iwm)
ma10_iwm_file = 'ETF_Opportunity_Set/IWN/ma10_iwm.json'

with open(ma10_iwm_file, 'w') as oF:
    oF.write(ma10_iwm_request.text)

wvad_iwm = {
        'function' : 'WILLR',
        'symbol' : 'IWM',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

wvad_iwm_request = requests.get(url = API_URL, params = wvad_iwm)
wvad_iwm_file = 'ETF_Opportunity_Set/IWN/wvad_iwm.json'

with open(wvad_iwm_file, 'w') as oF:
    oF.write(wvad_iwm_request.text)


rsi_iwm= {
       'function' : 'RSI',
       'symbol' : 'IWM',
       'interval' : 'daily',
       'time_period' : '14',
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

rsi_iwm_file = 'ETF_Opportunity_Set/IWN/rsi_iwm.json'
rsi_iwm_request = requests.get(url = API_URL, params = rsi_iwm)

with open(rsi_iwm_file, 'w') as oF:
    oF.write(rsi_iwm_request.text)


# =============================================================================
# EEM
# =============================================================================

eem = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : "EEM",
    "outputsize" : "full",
    "datatype" : "csv",
    "apikey" : "0ZSSUD2LJQV6MK6M",
    }


eem_file = 'ETF_Opportunity_Set/EEM/eem.csv'

eem_request = requests.get(url = API_URL, params = eem)

with open(eem_file, 'w') as oF:
    oF.write(eem_request.text)

stoch_eem = {
        'function' : 'STOCH',
        'symbol' : 'EEM',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

stoch_eem_request = requests.get(url = API_URL, params = stoch_eem)
stoch_eem_file = 'ETF_Opportunity_Set/EEM/stoch_eem.json'

with open(stoch_eem_file, 'w') as oF:
    oF.write(stoch_eem_request.text)

ema20_eem = {
        'function' : 'EMA',
        'symbol' : 'EEM',
        'interval' : 'daily',
        'time_period' : '20', #what was used in actual paper
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

ema20_eem_request = requests.get(url = API_URL, params = ema20_eem)
ema20_eem_file = 'ETF_Opportunity_Set/EEM/ema20_eem.json'

with open(ema20_eem_file, 'w') as oF:
    oF.write(ema20_eem_request.text)

ma5_eem = {
       'function' : 'sma', 
       'symbol' : 'EEM',
       'interval' : 'daily',
       'time_period' : '5', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma5_eem_request = requests.get(url = API_URL, params = ma5_eem)
ma5_eem_file = 'ETF_Opportunity_Set/EEM/ma5_eem.json'

with open(ma5_eem_file, 'w') as oF:
    oF.write(ma5_eem_request.text)
    
ma10_eem = {
       'function' : 'sma', 
       'symbol' : 'EEM',
       'interval' : 'daily',
       'time_period' : '10', #what was used in actual paper
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

ma10_eem_request = requests.get(url = API_URL, params = ma10_eem)
ma10_eem_file = 'ETF_Opportunity_Set/EEM/ma10_eem.json'

with open(ma10_eem_file, 'w') as oF:
    oF.write(ma10_eem_request.text)

wvad_eem = {
        'function' : 'WILLR',
        'symbol' : 'EEM',
        'interval' : 'daily',
        'time_period' : '14', #according to investopedia, 14 is usually used
        'series_type' : 'close',
        'apikey' : '0ZSSUD2LJQV6MK6M'}

wvad_eem_request = requests.get(url = API_URL, params = wvad_eem)
wvad_eem_file = 'ETF_Opportunity_Set/EEM/wvad_eem.json'

with open(wvad_eem_file, 'w') as oF:
    oF.write(wvad_eem_request.text)


rsi_eem= {
       'function' : 'RSI',
       'symbol' : 'EEM',
       'interval' : 'daily',
       'time_period' : '14',
       'series_type' : 'close',
       'apikey' : '0ZSSUD2LJQV6MK6M'}

rsi_eem_file = 'ETF_Opportunity_Set/EEM/rsi_eem.json'
rsi_eem_request = requests.get(url = API_URL, params = rsi_eem)

with open(rsi_eem_file, 'w') as oF:
    oF.write(rsi_eem_request.text)


