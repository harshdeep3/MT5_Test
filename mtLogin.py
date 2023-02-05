import MetaTrader5 as mt5

LOGIN = 51104994
SERVER = "ICMarketsSC-Demo"
# password
PASSWORD = "Q1VqLHUs"

# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)


def login_to_metatrader():
    # Connect to the MetaTrader 5 terminal
    mt5.initialize()

    # Log in to the terminal with your account credentials
    account_server = SERVER
    # this needs to be an integer
    login = LOGIN
    password = PASSWORD
    result = mt5.login(login, password, account_server)

    if not result:
        print("Login failed. Check your credentials.")
    else:
        print("Login successful.")
        return result

if __name__ == "__main__":
    result = login_to_metatrader()


    # Disconnect from the terminal
    mt5.shutdown()
