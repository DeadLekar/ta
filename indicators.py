import talib
import xml.etree.ElementTree as ET
import sqlite3 as lite
import numpy as np
import pandas as pd
import requests
import json
import time
from scripts import *

def get_quotes(ticker):
    url = 'http://iss.moex.com/iss/history/engines/stock/markets/shares/boards/tqbr/securities/{}/?from=2019-10-17'.format(ticker)
    r = requests.get(url).text
    tree = ET.ElementTree(ET.fromstring(r))

    root = tree.getroot()
    for child in root:
        els = child.find('row')
        print (child.tag, child.attrib)
    return tree

def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.append(y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1))


if __name__ == '__main__':
    quotes = get_quotes('SBER')
    db_name = 'ta.db'
    db_path = get_right_path(db_paths)
    if not db_path: exit(-1)
    db_path += db_name
    conn = lite.connect(db_path)
    c = conn.cursor()
    n = 14
    # df_sber = pd.read_sql('SELECT close FROM sber', conn)
    # df_sber['SMA_14'] = df_sber.close.rolling(14).mean()
    df_total = pd.read_sql('SELECT Close FROM bsms', conn)
    df_total['sma'] = df_total.close.rolling(n).mean()

    # df_total['RSI'] = talib.RSI(np.asarray(df_total.Close))

    # restore the RSI formula

    df_total['change'] = df_total.close.diff()
    df_total['gain'] = df_total.change.mask(df_total.change < 0, 0.0)
    df_total['loss'] = -df_total.change.mask(df_total.change > 0, -0.0)
    # df_total.loc[n:, 'avg_gain'] = rma(df_total.gain[n + 1:].values, n, df_total.loc[:n, 'gain'].mean())
    # df_total.loc[n:, 'avg_loss'] = rma(df_total.loss[n + 1:].values, n, df_total.loc[:n, 'loss'].mean())
    # df_total['rs'] = df_total.avg_gain / df_total.avg_loss
    # df_total['rsi_14'] = 100 - (100 / (1 + df_total.rs))
    df_total.to_sql('bsms1', conn)
    pass



