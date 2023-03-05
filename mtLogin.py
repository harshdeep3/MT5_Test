import MetaTrader5 as mt5
import pandas as pd

LOGIN = 51104994
SERVER = "ICMarketsSC-Demo"
# password
PASSWORD = "Q1VqLHUs"

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)


class MT5Class:

    def __init__(self):
        self.mt5_result = None
        self.account_info = None

    def login_to_metatrader(self):
        # Connect to the MetaTrader 5 terminal
        mt5.initialize()

        # Log in to the terminal with your account credentials
        account_server = SERVER
        # this needs to be an integer
        login = LOGIN
        password = PASSWORD
        self.mt5_result = mt5.login(login, password, account_server)

        if not self.mt5_result:
            print("Login failed. Check your credentials.")
            quit()

    def get_acc_info(self):

        if mt5.account_info() is None:
            print("Account info is None!")
        else:
            account_info_dict = mt5.account_info()._asdict()
            self.account_info = pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])
            print(self.account_info)


if __name__ == "__main__":

    mt5_obj = MT5Class()
    mt5_obj.login_to_metatrader()
    mt5_obj.get_acc_info()
    # Disconnect from the terminal
    mt5.shutdown()
