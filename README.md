# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> tokenB-> tokenA(amountIn:5B,amountOut:5.6497A)  
> tokenA-> tokenD(amountIn:5.6497A,amountOut:2.4550D)  
> tokenD-> tokenC(amountIn:2.4550D,amountOut:5.0798C)  
> tokenC-> tokenB(amountIn:5.0798C,amountOut:20.0802B)  

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

>  Slippage is the difference between the expected price and the actual price of a trade, Uniswap V2 address this by setting slippage tolerance.
>  Slippage=(expected_amount-actual_amount)/expected_amount, which expected_amount=amount exchange by the rate of two token in the pool. Once slippage is higher than slippage tolerance the transaction wil revert.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

>   It will first caculate the value you send into the pool by subtracting the before amount and after amount of the pool, after that it will calculate the percentage of the amount you send to the amount that is initially in the pool, then it choose the smaller percentage between the two token, and send you the liquidity token, the amount of it is the percentage of the total supply.
>   The reason of it is to prevent inflation attack. 


## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

>   It is design this way to keep the balance of the two token. 

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

>   Due to the swapping formula, swapping the same pair will raise the swapping price, sandwich attack is to buy the token before a big trade then sell it after the big trade is finished, and profit from the price different.
>   It might impact the buying price when you are swapping, you'll swap less token then expact. 

