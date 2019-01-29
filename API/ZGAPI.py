import json
import websocket
import requests
import time

ws = websocket.WebSocket()
# API地址
tickersURL = 'https://www.zg.com/api/v1/tickers'

def ZGtickers():
	rq = requests.get('https://www.zg.top/API/api/v1/ticker?symbol=36')
	tickersData = rq.json()
	return tickersData['data']






if __name__ == '__main__':
	a = 0
	while(True):
		a += 1
		ZGtickers()

