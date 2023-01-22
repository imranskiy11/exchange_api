from conf.conf import apiKey, secretKey
from binance import Client, ThreadedDepthCacheManager, ThreadedWebsocketManager
import pandas as pd

class BinanceAPI:
    
    def __init__(self) -> None:
        self.client = Client(apiKey, secretKey)
    
    def get_info(self, pair: str='BTSUSDT') -> None:
        pass