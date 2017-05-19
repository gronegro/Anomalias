#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 04:50:23 2017

@author: Anomalias
"""



import os
import pandas as pd




#os.chdir('/Users/juan/Documents/Gurufocus/Data/csv')
os.chdir('/home/juang/Documents/Python Scripts/Mercados GURU')

tp = pd.read_csv('output.csv',iterator=True, chunksize=1000)
Market = pd.concat(tp, ignore_index=True)


Market1=Market[0:50000]

percentil=15;
#price to earnings
P2E=Market1.loc[Market1['Fiscal Period']=="PE Ratio(TTM)",['Ticker','TTM/current']]
#price to earnings positivos
P2Epos=P2E[P2E['TTM/current']>0]
#p/e bajos - "mejores"
P2Eupper=P2Epos[P2Epos['TTM/current']<np.percentile(np.array(P2Epos['TTM/current']), percentil)]

Market = pd.read_csv('output.csv')