## CryptoHistoricDownloader

This program can automatize downloading multiple tickers from Binance to CSV files.

#### Installation

```
pip3 install -r requirements.txt
```

#### Usage

```
python3 main.py -t ETHUSDT,LTCUSDT --startDate 2020-01-01 --endDate 2020-01-7 --interval 5m
```

``` -t ``` : Which tickers you want to download, for example ``` -t ETHUSDT ```, you can download multiple by using a command between your tickers.

``` --startDate ``` : Where you want to start downloading.

``` --endDate ``` : Where you want to stop downloading.

``` --interval ``` : The interval which you want to download at.

This information can be accessed by running: ``` python3 main.py --help ```