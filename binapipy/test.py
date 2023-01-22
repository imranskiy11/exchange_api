import requests
import pandas as pd

class BinanceAPI:
    
    def __init__(self) -> None:
        self.base_url = "https://api.binance.com"
        self.end_point = "/api/v3/exchangeInfo"
    
    def get_info(self, pair: str='BTSUSDT') -> None:
        req = requests.get(f"{self.base_url}{self.end_point}?symbol={pair}")
        # print(f'request answer :\n {req.text}')
        print(type(req.text))
        

if __name__ == "__main__":
    api_class = BinanceAPI()
    api_class.get_info(pair='BTSUSDT')