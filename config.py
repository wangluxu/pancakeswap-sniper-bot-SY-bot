
walletAddress = "0x0000000000000000000000000000000000000000"                     #Your Wall address From trustwallet or another wallet.
private_key = "0x00000000000000000000000000000000000000000000000000000000000000" #Wallet private_key

spend = "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"  # WBNB OR OTHER contract for buy the token

AmountForSnipe = 0.0024  # Amount how much you want buy the token in WBNB OR OTHER.
MinLiquidityAdded = 5  # Set how much minimum liquidity added in pair address that you want to buy. set in WBNB OR OTHER. (eg : 2, 4, 7). 2 mean 2 BNB liquidity added.

SellToken = 0   # 0 = Not Sell after buy, 1 = Sell token after buy by take profit
Takeprofit = 150 # On percent

transactionRevertTime = 1000 #Limit for make transaction
gasAmount = 400000 #Minimul limit is 210000, more much more better.
gasPrice = 5 #Customize your GWEI (gas fee) here, cannot decimal. (eg : 5, 10, 25).

bscScanAPIKey= "NYBZQ1DI6FMBTQRJBV9YKRXAJHGY1N2HYE" #Your BSC API Key Get From https://bscscan.com

pancakeSwapRouterAddress = "0x10ED43C718714eb63d5aA57B78B54704E256024E"          #pancakeSwapRouterAddress
pancakeSwapFactoryAddress = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"         #pancakeSwapFactoryAddress
bsc = "https://bsc-dataseed.binance.org/"                                        #BSC JSON-RPC