from coinapi_v1 import CoinAPIv1
import datetime

test_key = 'B46B2E49-7E7C-4571-AC14-2424D3D2D8F5'
#B46B2E49-7E7C-4571-AC14-2424D3D2D8F5  disconnected
#905F969E-29DB-4456-9BBC-C3BA445C1033  Texas
#F0895A26-3F04-4761-AD5C-745B2FF2B43D  California
#8B2744D7-C2EB-4919-9727-61F9A560458F  East
#4B575B6C-2F32-4E6B-9151-49D871BE4E68  Midwest

api = CoinAPIv1(test_key)
exchanges = api.metadata_list_exchanges()

#print('Exchanges')
#for exchange in exchanges:
#    print('Exchange ID: %s' % exchange['exchange_id'])
#    print('Exchange website: %s' % exchange['website'])
#    print('Exchange name: %s' % exchange['name'])

assets = api.metadata_list_assets()
myAssets = {'BTC':0.09477632,
         #   'BCH':0.63513097,
         #   'SAFEX':22900,
            'HTMLCOIN':78550,
         #   'BTCP':8.2005408,
            'XMR':0.919,
         #   'ETH':6.3193777,
         #   'LTC':14.0045,
         #   'ZCL':23.93923833,
         #   'NEO':4.01044135,
         #   'NXS':43.3720439,
         #   'MCO':11,
         #   'SIB':30,
         #   'STEEM':21.93029234,
         #   'LGD':75,
         #   'QTUM':2,
         #   'XRP':43.38303529,
         #   'ARK':10,
         #  '2GIVE':3000,
         #   'CVC':75,
         #   'OMG':1.47986606,
            'GEO':10,
            'PAY':10,
         #   'IOP':5,
         #   'EGC':50,
         #   'XEM':50,
            'WINGS':21.78128547,
         #   'VTR':23.032674,
            'BTG':0.14038045,
            'ABY':1000,
         #   'XEL':30,
            'ADX':5,
            'DCT':6.77293432,
            'ADA':145.0334,
         #   'BNB':5.07078433,
            'ICN':400,
         #   'NANO':21.085,
            'DENT':3114.3857967,
         #   'REF':17.12166107,
         #   'AVT':30.06468235
            }

myAssetsA = {'SAFEX':22900}

print('Assets')
#for asset in assets:
for asset in assets:
    if(asset['asset_id'] in myAssets):
        if(asset['type_is_crypto'] == 1):
            print('Asset ID: %s' % asset['asset_id'])
            print('Asset name: %s' % asset['name'])
         #   print('Asset type (crypto?): %s' % asset['type_is_crypto'])

#symbols = api.metadata_list_symbols()
#print('Symbols')
#for symbol in symbols:
#    print('Symbol ID: %s' % symbol['symbol_id'])
#    print('Exchange ID: %s' % symbol['exchange_id'])
#    print('Symbol type: %s' % symbol['symbol_type'])
#    print('Asset ID base: %s' % symbol['asset_id_base'])
#    print('Asset ID quote: %s' % symbol['asset_id_quote'])
#
#    if (symbol['symbol_type'] == 'FUTURES'):
#        print('Future delivery time: %s' % symbol['future_delivery_time'])
#
#    if (symbol['symbol_type'] == 'OPTION'):
#        print('Option type is call: %s' % symbol['option_type_is_call'])
#        print('Option strike price: %s' % symbol['option_strike_price'])
#        print('Option contract unit: %s' % symbol['option_contract_unit'])
#        print('Option exercise style: %s' % symbol['option_exercise_style'])
#        print('Option expiration time: %s' % symbol['option_expiration_time'])
#
##exchange_rate = api.exchange_rates_get_specific_rate('BTC', 'USD')
#print('Time: %s' % exchange_rate['time'])
##print('Base: %s' % exchange_rate['asset_id_base'])
#print('Quote: %s' % exchange_rate['asset_id_quote'])
##print('Rate: %s' % exchange_rate['rate'])

print('Total Assets:')
total_assets = 0.0

for asset in assets:
    if(asset['asset_id'] in myAssets):
    #    id = 'asset_id'
    #    print(id)
        print('Base: %s' % asset['asset_id'])
        exchange_rate = api.exchange_rates_get_specific_rate(asset['asset_id'], 'USD')
        print('Rate: %s' % exchange_rate['rate'])
        print("Current Asset Value: %s" %  (exchange_rate['rate'] * myAssets[asset['asset_id']]))
        total_assets += (exchange_rate['rate'] * myAssets[asset['asset_id']])
        print('Total Assets: %s\r\n' % total_assets)

VTRrate = float(input('Price of VTR? '))
total_assets += VTRrate * 23.032674
print('Total Assets: %s' % total_assets)

LGDrate = float(input('Price of LGD? '))
total_assets += LGDrate * 75
print('Total Assets: %s' % total_assets)

BTCPrate = float(input('Price of BTCP? '))
total_assets += BTCPrate * 8.2005408
print('Total Assets: %s' % total_assets)

IOPrate = float(input('Price of IOP? '))
total_assets += IOPrate * 5.0
print('Total Assets: %s' % total_assets)

NXSrate = float(input('Price of NXS? '))
total_assets += NXSrate * 43.3720439
print('Total Assets: %s' % total_assets)

ZCLrate = float(input('Price of ZCL? '))
total_assets += ZCLrate * 23.93923833
print('Total Assets: %s' % total_assets)

SIBrate = float(input('Price of SIB? '))
total_assets += SIBrate * 30.0
print('Total Assets: %s' % total_assets)

SAFEXrate = float(input('Price of SAFEX? '))
total_assets += SAFEXrate * 22900.0
print('Total Assets: $%s' % total_assets)

#Save to file
file = open("TotalAssets.txt", "a+")#str(total_assets))
file.write("TimeStamp: %s" % exchange_rate['time'])
file.write("     Total Assets: %s     \r\n" % str(total_assets))
file.close()

#last_week = datetime.date(2017, 5, 16).isoformat()

#exchange_rate_last_week = api.exchange_rates_get_specific_rate('BTC', 'USD', {'time': last_week})
#print('Time: %s' % exchange_rate_last_week['time'])
#print('Base: %s' % exchange_rate_last_week['asset_id_base'])
#print('Quote: %s' % exchange_rate_last_week['asset_id_quote'])
#print('Rate: %s' % exchange_rate_last_week['rate'])
#
#current_rates = api.exchange_rates_get_all_current_rates('BTC')

#print("Asset ID Base: %s" % current_rates['asset_id_base'])
#for rate in current_rates['rates']:
#    print('Time: %s' % rate['time'])
#    print('Quote: %s' % rate['asset_id_quote'])
#    print('Rate: %s' % rate['rate'])

#periods = api.ohlcv_list_all_periods()
#
#for period in periods:
#    print('ID: %s' % period['period_id'])
#    print('Seconds: %s' % period['length_seconds'])
#    print('Months: %s' % period['length_months'])
#    print('Unit count: %s' % period['unit_count'])
#    print('Unit name: %s' % period['unit_name'])
#    print('Display name: %s' % period['display_name'])
#
#ohlcv_latest = api.ohlcv_latest_data('BITSTAMP_SPOT_BTC_USD', {'period_id': '1MIN'})

#for period in ohlcv_latest:
#    print('Period start: %s' % period['time_period_start'])
#    print('Period end: %s' % period['time_period_end'])
#    print('Time open: %s' % period['time_open'])
#    print('Time close: %s' % period['time_close'])
#    print('Price open: %s' % period['price_open'])
#    print('Price close: %s' % period['price_close'])
#    print('Price low: %s' % period['price_low'])
#    print('Price high: %s' % period['price_high'])
#    print('Volume traded: %s' % period['volume_traded'])
#    print('Trades count: %s' % period['trades_count'])

#start_of_2016 = datetime.date(2016, 1, 1).isoformat()
#ohlcv_historical = api.ohlcv_historical_data('BITSTAMP_SPOT_BTC_USD', {'period_id': '1MIN', 'time_start': start_of_2016})

#for period in ohlcv_historical:
#    print('Period start: %s' % period['time_period_start'])
#    print('Period end: %s' % period['time_period_end'])
#    print('Time open: %s' % period['time_open'])
#    print('Time close: %s' % period['time_close'])
#    print('Price open: %s' % period['price_open'])
#    print('Price close: %s' % period['price_close'])
#    print('Price low: %s' % period['price_low'])
#    print('Price high: %s' % period['price_high'])
#    print('Volume traded: %s' % period['volume_traded'])
#    print('Trades count: %s' % period['trades_count'])

#latest_trades = api.trades_latest_data_all()
#
#for data in latest_trades:
#    print('Symbol ID: %s' % data['symbol_id'])
#    print('Time Exchange: %s' % data['time_exchange'])
#    print('Time CoinAPI: %s' % data['time_coinapi'])
#    print('UUID: %s' % data['uuid'])
#    print('Price: %s' % data['price'])
#    print('Size: %s' % data['size'])
#    print('Taker Side: %s' % data['taker_side'])

#latest_trades_doge = api.trades_latest_data_symbol('BITTREX_SPOT_BTC_DOGE')

#for data in latest_trades_doge:
#    print('Symbol ID: %s' % data['symbol_id'])
#    print('Time Exchange: %s' % data['time_exchange'])
#    print('Time CoinAPI: %s' % data['time_coinapi'])
#    print('UUID: %s' % data['uuid'])
#    print('Price: %s' % data['price'])
#    print('Size: %s' % data['size'])
#    print('Taker Side: %s' % data['taker_side'])

#historical_trades_btc = api.trades_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})

#for data in historical_trades_btc:
#    print('Symbol ID: %s' % data['symbol_id'])
#    print('Time Exchange: %s' % data['time_exchange'])
#    print('Time CoinAPI: %s' % data['time_coinapi'])
#    print('UUID: %s' % data['uuid'])
#    print('Price: %s' % data['price'])
#    print('Size: %s' % data['size'])
#    print('Taker Side: %s' % data['taker_side'])

#current_quotes = api.quotes_current_data_all()
#print(current_quotes)
#for quote in current_quotes:
#    print('Symbol ID: %s' % quote['symbol_id'])
#    print('Time Exchange: %s' % quote['time_exchange'])
#    print('Time CoinAPI: %s' % quote['time_coinapi'])
#    print('Ask Price: %s' % quote['ask_price'])
#    print('Ask Size: %s' % quote['ask_size'])
#    print('Bid Price: %s' % quote['bid_price'])
#    print('Bid Size: %s' % quote['bid_size'])
#    if 'last_trade' in quote:
#        print('Last Trade: %s' % quote['last_trade'])

#current_quote_btc_usd = api.quotes_current_data_symbol('BITSTAMP_SPOT_BTC_USD')

#print('Symbol ID: %s' % current_quote_btc_usd['symbol_id'])
#print('Time Exchange: %s' % current_quote_btc_usd['time_exchange'])
#print('Time CoinAPI: %s' % current_quote_btc_usd['time_coinapi'])
#print('Ask Price: %s' % current_quote_btc_usd['ask_price'])
#print('Ask Size: %s' % current_quote_btc_usd['ask_size'])
#print('Bid Price: %s' % current_quote_btc_usd['bid_price'])
#print('Bid Size: %s' % current_quote_btc_usd['bid_size'])
#if 'last_trade' in current_quote_btc_usd:
#    last_trade = current_quote_btc_usd['last_trade']
#    print('Last Trade:')
#    print('- Taker Side: %s' % last_trade['taker_side'])
#    print('- UUID: %s' % last_trade['uuid'])
#    print('- Time Exchange: %s' % last_trade['time_exchange'])
#    print('- Price: %s' % last_trade['price'])
#    print('- Size: %s' % last_trade['size'])
#    print('- Time CoinAPI: %s' % last_trade['time_coinapi'])

#quotes_latest_data = api.quotes_latest_data_all()

#for quote in quotes_latest_data:
#    print('Symbol ID: %s' % quote['symbol_id'])
#    print('Time Exchange: %s' % quote['time_exchange'])
#    print('Time CoinAPI: %s' % quote['time_coinapi'])
#    print('Ask Price: %s' % quote['ask_price'])
#    print('Ask Size: %s' % quote['ask_size'])
#    print('Bid Price: %s' % quote['bid_price'])
#    print('Bid Size: %s' % quote['bid_size'])

#quotes_latest_data_btc_usd = api.quotes_latest_data_symbol('BITSTAMP_SPOT_BTC_USD')

#for quote in quotes_latest_data_btc_usd:
#    print('Symbol ID: %s' % quote['symbol_id'])
#    print('Time Exchange: %s' % quote['time_exchange'])
#    print('Time CoinAPI: %s' % quote['time_coinapi'])
#    print('Ask Price: %s' % quote['ask_price'])
#    print('Ask Size: %s' % quote['ask_size'])
#    print('Bid Price: %s' % quote['bid_price'])
#    print('Bid Size: %s' % quote['bid_size'])
#
#quotes_historical_data_btc_usd = api.quotes_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})

#for quote in quotes_historical_data_btc_usd:
#    print('Symbol ID: %s' % quote['symbol_id'])
#    print('Time Exchange: %s' % quote['time_exchange'])
#    print('Time CoinAPI: %s' % quote['time_coinapi'])
#    print('Ask Price: %s' % quote['ask_price'])
#    print('Ask Size: %s' % quote['ask_size'])
#    print('Bid Price: %s' % quote['bid_price'])
#    print('Bid Size: %s' % quote['bid_size'])

#orderbooks_current_data = api.orderbooks_current_data_all()

#for data in orderbooks_current_data:
#    print('Symbol ID: %s' % data['symbol_id'])
#    print('Time Exchange: %s' % data['time_exchange'])
#    print('Time CoinAPI: %s' % data['time_coinapi'])
#    print('Asks:')
#    for ask in data['asks']:
#        print('- Price: %s' % ask['price'])
#        print('- Size: %s' % ask['size'])
#    print('Bids:')
#    for bid in data['bids']:
#        print('- Price: %s' % bid['price'])
#        print('- Size: %s' % bid['size'])

#orderbooks_current_data_btc_usd = api.orderbooks_current_data_symbol('BITSTAMP_SPOT_BTC_USD')

#print('Symbol ID: %s' % orderbooks_current_data_btc_usd['symbol_id'])
#print('Time Exchange: %s' % orderbooks_current_data_btc_usd['time_exchange'])
#print('Time CoinAPI: %s' % orderbooks_current_data_btc_usd['time_coinapi'])
#print('Asks:')
#for ask in orderbooks_current_data_btc_usd['asks']:
#    print('- Price: %s' % ask['price'])
#    print('- Size: %s' % ask['size'])
#print('Bids:')
#for bid in orderbooks_current_data_btc_usd['bids']:
#    print('- Price: %s' % bid['price'])
#    print('- Size: %s' % bid['size'])

#orderbooks_latest_data_btc_usd = api.orderbooks_latest_data('BITSTAMP_SPOT_BTC_USD')

#for data in orderbooks_latest_data_btc_usd:
#    print('Symbol ID: %s' % data['symbol_id'])
#    print('Time Exchange: %s' % data['time_exchange'])
#    print('Time CoinAPI: %s' % data['time_coinapi'])
#    print('Asks:')
#    for ask in data['asks']:
#        print('- Price: %s' % ask['price'])
#        print('- Size: %s' % ask['size'])
#    print('Bids:')
#    for bid in data['bids']:
#        print('- Price: %s' % bid['price'])
#        print('- Size: %s' % bid['size'])

#orderbooks_historical_data_btc_usd = api.orderbooks_historical_data('BITSTAMP_SPOT_BTC_USD', {'time_start': start_of_2016})

#for data in orderbooks_historical_data_btc_usd:
#    print('Symbol ID: %s' % data['symbol_id'])
#    print('Time Exchange: %s' % data['time_exchange'])
#    print('Time CoinAPI: %s' % data['time_coinapi'])
#    print('Asks:')
#    for ask in data['asks']:
#        print('- Price: %s' % ask['price'])
#        print('- Size: %s' % ask['size'])
#    print('Bids:')
#    for bid in data['bids']:
#        print('- Price: %s' % bid['price'])
#        print('- Size: %s' % bid['size'])

#twitter_latest_data = api.twitter_latest_data()
#twitter_historical_data = api.twitter_historical_data({'time_start': start_of_2016})
