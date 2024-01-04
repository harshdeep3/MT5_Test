
from mtLogin import MT5Class

if __name__ == "__main__":
    
    # get the custom MT5 class
    mt5_obj = MT5Class()
    # log into mt5 using the account info provided
    # pass in the account number and password for different account
    mt5_obj.login_to_metatrader()
    # get account info
    mt5_obj.get_acc_info()
    
    # get total number of orders 
    num_of_order = mt5_obj.get_all_orders()
    # get total number of order for a given symbol
    num_of_order = mt5_obj.get_orders_total_by_symbol("USDJPY")
    
    mt5_obj.get_symbol_info("USDJPY")