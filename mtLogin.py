import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime
import pytz

# # acocount number
# LOGIN = 1# ACCOUNT NUMBER 
# # password
# PASSWORD = ""# ACCOUNT PASSWORD 

SERVER = "ICMarketsSC-Demo"

# acocount number
LOGIN = 51535169
# password
PASSWORD = "Cdm9I@7hsU"

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)


class MT5Class:

    def __init__(self):
        self.mt5_result = None
        self.account_info = None

    def login_to_metatrader(self, login=LOGIN, password=PASSWORD) -> None:
        # Connect to the MetaTrader 5 terminal
        mt5.initialize()

        # Log in to the terminal with your account credentials
        account_server = SERVER

        self.mt5_result = mt5.login(login, password, account_server)

        if not self.mt5_result:
            print("Login failed. Check your credentials.")
            quit()

    def get_acc_info(self) -> None:

        if mt5.account_info() is None:
            print("Account info is None!")
        else:
            account_info_dict = mt5.account_info()._asdict()
            self.account_info = pd.DataFrame(list(account_info_dict.items()), columns=['property', 'value'])
            print(self.account_info)
            
    def get_all_orders(self) -> None:
        """
        This function get the number of current active orders
        """
        orders = mt5.orders_total()
        
        if orders > 0:
            print("Total order = ", orders)
        else:
            print("No orders")
        
        return orders
    
    def get_orders_total_by_symbol(self, symbol: str="USDJPY") -> int:
        """
        This function get the number of current active orders filter for a given symbol
        """
        orders = mt5.orders_get(symbol=symbol)
        
        if len(orders) > 0:
            print(f"USDJPY orders = {orders}")
        else:
            print(f"No orders for {symbol}")
        
        return orders
    
    def get_symbol_info(self, symbol: str="USDJPY"):
        """
        This function gets information for a given symbol
        """
        symbol_info = mt5.symbol_info(symbol)
        
        if symbol_info is None:
            print(f"{symbol} not found")
        if not symbol_info.visible:
            print(f"{symbol} is not visible")
        else:
            print(symbol)


def get_historic_data(fx_symbol, fx_timeframe, fx_count):

    rates = mt5.copy_rates_from_pos(fx_symbol, fx_timeframe, 0, fx_count)
    # dataframe
    historic_df = pd.DataFrame(rates)
    # changing the time to datetime
    historic_df['time'] = pd.to_datetime(historic_df['time'], unit='s')

    return historic_df


if __name__ == "__main__":
    mt5_obj = MT5Class()
    mt5_obj.login_to_metatrader()
    mt5_obj.get_acc_info()

    # timeframe objects https://www.mql5.com/en/docs/python_metatrader5/mt5copyratesfrom_py
    timeframe = mt5.TIMEFRAME_D1
    symbol = 'USDJPY'
    # set time zone to UTC
    timezone = pytz.timezone("Etc/UTC")
    # create 'datetime' objects in UTC time zone to avoid the implementation of a local time zone offset
    utc_from = datetime(2010, 1, 10, tzinfo=timezone)
    utc_to = datetime(2020, 1, 11, tzinfo=timezone)
    count = 13500

    df = get_historic_data(symbol, timeframe, count)

    print(df)
    # Disconnect from the terminal
    mt5.shutdown()
