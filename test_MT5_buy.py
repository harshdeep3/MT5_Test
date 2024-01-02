
from mtLogin import MT5Class

if __name__ == "__main__":
    
    # get the custom MT5 class
    mt5_obj = MT5Class()
    # log into mt5 using the account info provided
    # pass in the account number and password for different account
    mt5_obj.login_to_metatrader()
    # get account info
    account_info = mt5_obj.get_acc_info()

    print(account_info)
    