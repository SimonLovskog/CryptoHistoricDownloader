from binance.client import Client
import pandas as pd
import argparse
import os

client = Client()

def sortData(data, ticker):
    sortedData = {
        "openTime": [],
        "openPrice": [],
        "highPrice": [],
        "lowPrice": [],
        "closePrice": [],
        "closeTime": [],
        "numberOfTrades": []
    }

    for x in data:
        sortedData['openTime'].append(x[0])
        sortedData['openPrice'].append(x[1])
        sortedData['highPrice'].append(x[2])
        sortedData['lowPrice'].append(x[3])
        sortedData['closePrice'].append(x[4])
        sortedData['closeTime'].append(x[6])
        sortedData['numberOfTrades'].append(x[8])
    
    df = pd.DataFrame(sortedData)
    print("Saving to %s.csv" % ticker)

    if os.path.exists('%s.csv' % ticker):
        print("Removing old %s.csv" % ticker)
        os.remove('%s.csv' % ticker)

    df.to_csv('%s.csv' % ticker)

def getData(ticker, startDate, endDate, interval):
    if interval == '1m':
        interval = Client.KLINE_INTERVAL_1MINUTE
    elif interval == '5m':
        interval = Client.KLINE_INTERVAL_5MINUTE

    data = client.get_historical_klines(ticker, interval, startDate, endDate)
    sortData(data, ticker)

if __name__  == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", "-t", help="The tickers that should be downloaded.", required=True)
    parser.add_argument("--startDate", "-s", help="The date from to start downloading.", required=True)
    parser.add_argument("--endDate", "-e", help="The date from to stop downloading.", required=True)
    parser.add_argument("--interval", "-i", help="The interval to download data in.", required=True, choices=['1m', '5m'])

    args = parser.parse_args()

    if "," in args.ticker:
        tickers = args.ticker.split(",")
    else:
        tickers = [args.ticker]

    for ticker in tickers:
        print("Downloading {}, starting at {}, ending at {}, using {}".format(ticker, args.startDate, args.endDate, args.interval))
        getData(ticker, args.startDate, args.endDate, args.interval)