from API.ZAPI import ZApi

access_key = 'e3073eb6-945c-4ae3-9482-8bf4bdeeb296'
secret_key = '6071dd9c-9652-4300-968b-6f89790754c3'
# ZBData = ZApi(apiKey,secretKey).ticker('eth_usdt')
#ZBData = ZApi(access_key, secret_key)
#ZBData.ticker('eth_usdt')
#print(ZBData)








if __name__ == '__main__':
    zb = ZApi(access_key=access_key, secret_key=secret_key)
    # a = zb.all_ticker()
    a = zb.order( "bts_usdt", 1, 0.1, 0.1)
    print(a)