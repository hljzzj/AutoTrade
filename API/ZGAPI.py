import json
import websocket
import requests
import time

ws = websocket.WebSocket()
# API地址
tickersURL = 'https://www.zg.com/api/v1/tickers'

def tickers():
	starttime = time.time()
	rq = requests.get('https://www.zg.com/api/v1/tickers')
	tickersData = rq.json()
	endtime = time.time()
	print(tickersData)
	print('运行时长：'+str(endtime-starttime))
	print('第'+str(a)+"次")
	time.sleep(1)





if __name__ == '__main__':
	a = 0
	while(True):
		a += 1
		tickers()

