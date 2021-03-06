#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 15:11:30 2018

@author: shaydineen
"""


  
import json
import numpy as np
import pandas as pd

# =============================================================================
# Converting MACD JSON file to CSV
# =============================================================================

macd_list = []
with open('Data/macd.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            print(j)
            print(tech_analysis[j])
            macd_list.append([j, tech_analysis[j]]) #where j is the date and tech_analysis[j] is the data at date j

macd = []
for i in range(9, len(macd_list)):
    date = macd_list[i][0]
    macd_value = macd_list[i][1]['MACD']
    macd_signal = macd_list[i][1]['MACD_Signal']
    macd_hist = macd_list[i][1]['MACD_Hist']

    macd.append([date, macd_value, macd_signal, macd_hist])
    
macd = np.array(macd)

filepath = 'macd.csv'

macdDF = pd.DataFrame(macd)

macdDF.to_csv(filepath, index=False)

# =============================================================================
# Converting CCI JSON file to CSV
# =============================================================================

cci_list = []
with open('Data/cci.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            cci_list.append([j, tech_analysis[j]])

cci = []
for i in range(6, len(cci_list)):
    date = cci_list[i][0]
    cci_value = cci_list[i][1]['CCI']

    cci.append([date, cci_value])
    
cci = np.array(cci)

filepath = 'Data/cci.csv'

cciDF = pd.DataFrame(cci)

cciDF.to_csv(filepath, index=False)

# =============================================================================
# Converting ATR JSON file to CSV
# =============================================================================

atr_list = []
with open('Data/atr.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            atr_list.append([j, tech_analysis[j]])

atr = []
for i in range(6, len(atr_list)):
    date = atr_list[i][0]
    atr_value = atr_list[i][1]['ATR']

    atr.append([date, atr_value])
    
atr = np.array(atr)

filepath = 'atr.csv'

atrDF = pd.DataFrame(atr)

atrDF.to_csv(filepath, index=False)

# =============================================================================
# Converting BOLL JSON file to CSV
# =============================================================================

boll_list = []
with open('Data/boll.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            boll_list.append([j, tech_analysis[j]])

boll = []
for i in range(10, len(boll_list)):
    date = boll_list[i][0]
    boll_mid_band = boll_list[i][1]['Real Middle Band']
    boll_up_band = boll_list[i][1]['Real Upper Band']
    boll_lower_band = boll_list[i][1]['Real Lower Band']

    boll.append([date, boll_mid_band, boll_up_band, boll_lower_band])
    
boll = np.array(boll)

filepath = 'boll.csv'

bollDF = pd.DataFrame(boll)

bollDF.to_csv(filepath, index=False)

# =============================================================================
# Converting EMA20 JSON file to CSV
# =============================================================================

ema20_list = []
with open('Data/ema20.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ema20.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)

# =============================================================================
# Converting 5 Day Moving Average JSON file to CSV
# =============================================================================

ma5_list = []
with open('Data/ma5.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ma5.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)

# =============================================================================
# Converting 5 Day Moving Average JSON file to CSV
# =============================================================================

ma10_list = []
with open('Data/ma10.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ma10.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)

# =============================================================================
# Converting 6 month momentum JSON file to CSV
# =============================================================================

mom6_list = []
with open('Data/mom6.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            mom6_list.append([j, tech_analysis[j]])

mom6 = []
for i in range(7, len(mom6_list)):
    date = mom6_list[i][0]
    mom6_value = mom6_list[i][1]['MOM']

    mom6.append([date, mom6_value])
    
mom6 = np.array(mom6)

filepath = 'mom6.csv'

mom6DF = pd.DataFrame(mom6)

mom6DF.to_csv(filepath, index=False)

# =============================================================================
# Converting 10 month momentum JSON file to CSV
# =============================================================================

mom12_list = []
with open('Data/mom12.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            mom12_list.append([j, tech_analysis[j]])

mom12 = []
for i in range(7, len(mom12_list)):
    date = mom12_list[i][0]
    mom12_value = mom12_list[i][1]['MOM']

    mom12.append([date, mom12_value])
    
mom12 = np.array(mom12)

filepath = 'mom12.csv'

mom12DF = pd.DataFrame(mom12)

mom12DF.to_csv(filepath, index=False)

# =============================================================================
# Converting ROC JSON file to CSV
# =============================================================================

roc_list = []
with open('Data/roc.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            roc_list.append([j, tech_analysis[j]])

roc = []
for i in range(7, len(roc_list)):
    date = roc_list[i][0]
    roc_value = roc_list[i][1]['ROC']

    roc.append([date, roc_value])
    
roc = np.array(roc)

filepath = 'roc.csv'

rocDF = pd.DataFrame(roc)

rocDF.to_csv(filepath, index=False)

# =============================================================================
# Converting STOCH JSON file to CSV
# =============================================================================

stoch_list = []
with open('Data/stoch.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'stoch.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# Converting WVAD JSON file to CSV
# =============================================================================


wvad_list = []
with open('Data/wvad.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'Data/wvad.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)

# =============================================================================
# Converting RSI JSON File to CSV
# =============================================================================

rsi_list = []
with open('Data/rsi.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'Data/rsi.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

# =============================================================================
# All the stuff for SPY
# =============================================================================
ema20_list = []
with open('ETF Opportunity Set/SPY/ema20_spy.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF Opportunity Set/SPY/ema20_spy.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/SPY/ma5_spy.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/SPY/ma5_spy.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/SPY/ma10_spy.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/SPY/ma10_spy.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF Opportunity Set/SPY/wvad_spy.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF Opportunity Set/SPY/wvad_spy.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/SPY/rsi_spy.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/SPY/rsi_spy.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF Opportunity Set/SPY/stoch_spy.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF Opportunity Set/SPY/stoch_spy.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# All the stuff for IWM
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/IWM/ema20_iwm.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/IWM/ema20_iwm.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/IWM/ma5_iwm.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/IWM/ma5_iwm.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/IWM/ma10_iwm.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/IWM/ma10_iwm.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/IWM/wvad_iwm.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/IWM/wvad_iwm.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/IWM/rsi_iwm.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/IWM/rsi_iwm.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/IWM/stoch_iwn.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/IWM/stoch_iwm.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# EEM
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/EEM/ema20_eem.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/EEM/ema20_eem.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/EEM/ma5_eem.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/EEM/ma5_eem.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/EEM/ma10_eem.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/EEM/ma10_eem.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/EEM/wvad_eem.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/EEM/wvad_eem.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/EEM/rsi_eem.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/EEM/rsi_eem.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/EEM/stoch_eem.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/EEM/stoch_eem.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# TLT
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/TLT/ema20_tlt.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/TLT/ema20_tlt.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/TLT/ma5_tlt.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/TLT/ma5_tlt.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/TLT/ma10_tlt.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/TLT/ma10_tlt.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/TLT/wvad_tlt.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/TLT/wvad_tlt.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/TLT/rsi_tlt.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/TLT/rsi_tlt.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/TLT/stoch_tlt.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/TLT/stoch_tlt.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# LQD
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/LQD/ema20_lqd.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/LQD/ema20_lqd.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/LQD/ma5_lqd.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/LQD/ma5_lqd.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/LQD/ma10_lqd.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/LQD/ma10_lqd.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/LQD/wvad_lqd.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/LQD/wvad_lqd.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/LQD/rsi_lqd.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/LQD/rsi_lqd.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/LQD/stoch_lqd.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/LQD/stoch_lqd.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# TIP
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/TIP/ema20_tip.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/TIP/ema20_tip.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/TIP/ma5_tip.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/TIP/ma5_tip.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/TIP/ma10_tip.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/TIP/ma10_tip.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/TIP/wvad_tip.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/TIP/wvad_tip.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/TIP/rsi_tip.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/TIP/rsi_tip.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/TIP/stoch_tip.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/TIP/stoch_tip.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# IYR
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/IYR/ema20_iyr.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/IYR/ema20_iyr.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/IYR/ma5_iyr.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/IYR/ma5_iyr.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/IYR/ma10_iyr.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/IYR/ma10_iyr.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/IYR/wvad_iyr.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/IYR/wvad_iyr.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/IYR/rsi_iyr.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/IYR/rsi_iyr.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/IYR/stoch_iyr.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/IYR/stoch_iyr.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# GLD
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/GLD/ema20_gld.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/GLD/ema20_gld.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/GLD/ma5_gld.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/GLD/ma5_gld.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/GLD/ma10_gld.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/GLD/ma10_gld.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/GLD/wvad_gld.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/GLD/wvad_gld.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/GLD/rsi_gld.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/GLD/rsi_gld.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/GLD/stoch_gld.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/GLD/stoch_gld.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# OIH
# =============================================================================

ema20_list = []
with open('ETF_Opportunity_Set/OIH/ema20_oih.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/OIH/ema20_oih.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/OIH/ma5_oih.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/OIH/ma5_oih.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/OIH/ma10_oih.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/OIH/ma10_oih.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/OIH/wvad_oih.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/OIH/wvad_oih.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/OIH/rsi_oih.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/OIH/rsi_oih.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/OIH/stoch_oih.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/OIH/stoch_oih.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)

# =============================================================================
# FXE
# =============================================================================


ema20_list = []
with open('ETF_Opportunity_Set/FXE/ema20_fxe.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ema20_list.append([j, tech_analysis[j]])

ema20 = []
for i in range(7, len(ema20_list)):
    date = ema20_list[i][0]
    ema20_value = ema20_list[i][1]['EMA']

    ema20.append([date, ema20_value])
    
ema20 = np.array(ema20)

filepath = 'ETF_Opportunity_Set/FXE/ema20_fxe.csv'

ema20DF = pd.DataFrame(ema20)

ema20DF.to_csv(filepath, index=False)


ma5_list = []
with open('ETF_Opportunity_Set/FXE/ma5_fxe.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma5_list.append([j, tech_analysis[j]])

ma5 = []
for i in range(7, len(ma5_list)):
    date = ma5_list[i][0]
    ma5_value = ma5_list[i][1]['SMA']

    ma5.append([date, ma5_value])
    
ma5 = np.array(ma5)

filepath = 'ETF_Opportunity_Set/FXE/ma5_fxe.csv'

ma5DF = pd.DataFrame(ma5)

ma5DF.to_csv(filepath, index=False)



ma10_list = []
with open('ETF_Opportunity_Set/FXE/ma10_fxe.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            ma10_list.append([j, tech_analysis[j]])

ma10 = []
for i in range(7, len(ma10_list)):
    date = ma10_list[i][0]
    ma10_value = ma10_list[i][1]['SMA']

    ma10.append([date, ma10_value])
    
ma10 = np.array(ma10)

filepath = 'ETF_Opportunity_Set/FXE/ma10_fxe.csv'

ma10DF = pd.DataFrame(ma10)

ma10DF.to_csv(filepath, index=False)


wvad_list = []
with open('ETF_Opportunity_Set/FXE/wvad_fxe.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            wvad_list.append([j, tech_analysis[j]])

wvad = []
for i in range(6, len(wvad_list)):
    date = wvad_list[i][0]
    willr = wvad_list[i][1]['WILLR']

    wvad.append([date, willr])
    
wvad = np.array(wvad)

filepath = 'ETF_Opportunity_Set/FXE/wvad_fxe.csv'

wvadDF = pd.DataFrame(wvad)

wvadDF.to_csv(filepath, index=False)


rsi_list = []
with open('ETF_Opportunity_Set/FXE/rsi_fxe.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            rsi_list.append([j, tech_analysis[j]])

rsi = []
for i in range(7, len(rsi_list)):
    date = rsi_list[i][0]
    rsi_value = rsi_list[i][1]['RSI']

    rsi.append([date, rsi_value])
    
rsi = np.array(rsi)

filepath = 'ETF_Opportunity_Set/FXE/rsi_fxe.csv'

rsiDF = pd.DataFrame(rsi)

rsiDF.to_csv(filepath, index=False)

stoch_list = []
with open('ETF_Opportunity_Set/FXE/stoch_fxe.json') as data_file:    
    data = json.load(data_file)
    for tech_analysis in data.values(): #.values()
        for j in tech_analysis:
            stoch_list.append([j, tech_analysis[j]])

stoch = []
for i in range(10, len(stoch_list)):
    date = stoch_list[i][0]
    slowK = stoch_list[i][1]['SlowK']
    slowD = stoch_list[i][1]['SlowD']

    stoch.append([date, slowK, slowD])
    
stoch = np.array(stoch)

filepath = 'ETF_Opportunity_Set/FXE/stoch_fxe.csv'

stochDF = pd.DataFrame(stoch)

stochDF.to_csv(filepath, index=False)