* 现在这个机器人适用于币安链上的: Pancakeswap (默认)
  你可以使用它去操作任何相似的defi应用，例如Uniswap或者Pancakeswap V2, 但是你需要去更改Pairabi, pancakeABI和pancakeSwapFactoryABI

 
*运行本机器人之前的重要提示
检查你想狙击的令牌，确保它不是貔貅或者没有杀科学家函数 (90%的新币是可以被扫描的)

* 新的更新
1. 在新的版本中你可以使用BNB代替WBNB，这将更有助于你使用。


*Demo for SY bot:
1. 你可以授权
2. 检查流动性，购买和卖出
3. 检查真实价格
4. 你不能发送转录
5. 卖出令牌

*Real for SY bot:
You can Use full
1. SY Developer : https://t.me/seng55
2. website : 

<img src="./assets/01.PNG">

*What's will you get
To avoid scam, I will invite you to my private repository, aTo avoid scam, I will invite you to my private repository, and you will get whole of code, and any update if I push new update. Please only contact to Telegrame:<code>@Seng55</code> or <code>eeyang5@gmail.com</code> with subject <b>SY Bot Info</b> for more info. For error or problem questions please open issues in GitHub, don't email me. Maybe I'll slow response on weekend. Thanks!nd you will get whole of code, and any update if I push new update. Please only contact to Discord : <code>countdown#4008</code> or <code>nafidinara@gmail.com</code> with subject <b>PancakeSwap Bot Info</b> for more info. For error or problem questions please open issues in GitHub, don't email me. Maybe I'll slow response on weekend. Thanks!

*Bot future
1. You can snipe new listing token on pancakeswap v2 or any defi like pancakeswap v2 (See how to on above)
2. Sell ALL you token 
3. Sell you token by TakeProfit or Selllimt (Capital is AmountForSnipe)
3. Approve 
4. Check Real price

*How sniper work ?
1. When liquidity added Bot will auto buy and sell when profit more than takeprofit (Please Approve before Sniper)


* HOW TO RUN
1. set up your config.py to with this explanation : 
----------------------------------------------------------
walletAddress = "0x0000000000000000000000000000000000000000"                     #Your Wall address From trustwallet or another wallet.
private_key = "x000000000000000000000000000000000000000000000000000000000000000" #Wallet private_key

spend = "0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c"  # WBNB OR OTHER contract for buy the token

AmountForSnipe = 0.0024  # Amount how much you want buy the token in WBNB OR OTHER.
MinLiquidityAdded = 5  # Set how much minimum liquidity added in pair address that you want to buy. set in WBNB OR OTHER. (eg : 2, 4, 7). 2 mean 2 BNB liquidity added.

SellToken = 0   # 0 = Not Sell after buy, 1 = Sell token after buy by take profit
Takeprofit = 150 # On percent

transactionRevertTime = 1000 #Limit for make transaction
gasAmount = 400000 #Minimul limit is 210000, more much more better.
gasPrice = 5 #Customize your GWEI (gas fee) here, cannot decimal. (eg : 5, 10, 25).

bscScanAPIKey= "XXXXXXXXXXXXXXXXXXXXXXXXX" #Your BSC API Key Get From https://bscscan.com

pancakeSwapRouterAddress = "0x10ED43C718714eb63d5aA57B78B54704E256024E"          #pancakeSwapRouterAddress
pancakeSwapFactoryAddress = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"         #pancakeSwapFactoryAddress
bsc = "https://bsc-dataseed.binance.org/"                                        #BSC JSON-RPC
-------------------------------------------------

2. run with <code>SBot.exe</code> include Insert and console windows.

3. Insert Token Contract you want to sniper, than press "Sniper Start" You will see any working on console windows<br>
   <img src="./assets/02.PNG">
   
8. Stop bot with "Stop Running".

## WARNING
The not guarantee make profit every token you snipe, do you research token info before run

## TROUBLESHOOT
* there are some reason if your tx failed :
- you haven't approve your WBNB or Any Token you want to buy or sell
- your gas price are to small
- your GWEI are to small (BSC use 7+ for fast)

