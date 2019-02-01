import time
from threading import Lock
from flask import Flask, render_template
from flask_socketio import SocketIO
from API.HuobiServices import *
from API.ZGAPI import ZGtickers
from API.GATEAPI import GateIO
from API.ZAPI import ZApi

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()


# 后台线程 产生数据，即刻推送至前端
def background_thread():
    while True:
        socketio.sleep(1)
        # 第一步：调用API获取平台实时价格数据
        try:
            # 火币
            ticker = get_ticker("ethusdt")
            HuoBiData = ticker['tick']
        except:
            HuoBiData = {}
            pass
        try:
            # ZG
            ZGData = ZGtickers()
        except:
            ZGData = {}
            pass
        try:
            # GATE.IO
            GATEIOData = GateIO.ticker("eth_usdt")
        except:
            GATEIOData = {}
            pass
        try:
            # ZB    https://www.bitkk.com/
            ZBData = ZApi.ticker('eth_usdt')
            print(ZBData)
        except:
            ZBData = {}
            pass
        # 第二步：处理各平台的数据
        print(GATEIOData)
        GATEIOData['name'] = 'GATEIO'
        ZBData['name'] = 'ZB'
        ZGData['name'] = 'ZG'
        if ZGData and HuoBiData and GATEIOData and ZBData:
            Data = {
                'HuoBiData': HuoBiData,
                'ZGData': ZGData,
                'GATEIOData': GATEIOData,
                'ZBData': ZBData
            }
        elif ZGData and ZBData:
            Data = {'ZGData': ZGData, 'GATEIOData': GATEIOData, 'ZBData': ZBData}
        elif HuoBiData:
            Data = {'HuoBiData': HuoBiData}
        print(Data)
        # 第三步：将数据发到前端
        socketio.emit('server_response',
                      {'Data': Data},
                      namespace='/test')
        # 注意：这里不需要客户端连接的上下文，默认 broadcast = True


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)


@socketio.on('connect', namespace='/test')
def test_connect():
    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(target=background_thread)


if __name__ == '__main__':
    socketio.run(app, debug=True)
