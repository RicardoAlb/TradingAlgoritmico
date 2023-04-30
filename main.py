from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("API_KEY")

SECRET_KEY = os.environ.get("SECRET_KEY")

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)

account = trading_client.get_account()

market_order_data = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )

market_order = trading_client.submit_order(market_order_data)

positions = trading_client.get_all_positions()
