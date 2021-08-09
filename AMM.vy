from vyper.interfaces import ERC20

tokenAQty: public(uint256) #Quantity of tokenA held by the contract
tokenBQty: public(uint256) #Quantity of tokenB held by the contract

invariant: public(uint256) #The Constant-Function invariant (tokenAQty*tokenBQty = invariant throughout the life of the contract)
tokenA: ERC20 #The ERC20 contract for tokenA
tokenB: ERC20 #The ERC20 contract for tokenB
owner: public(address) #The liquidity provider (the address that has the right to withdraw funds and close the contract)

@external
def get_token_address(token: uint256) -> address:
    if token == 0:
        return self.tokenA.address
    if token == 1:
        return self.tokenB.address
    return ZERO_ADDRESS 

# Sets the on chain market maker with its owner, and initial token quantities
@external
def provideLiquidity(tokenA_addr: address, tokenB_addr: address, tokenA_quantity: uint256, tokenB_quantity: uint256):
    assert self.invariant == 0 #This ensures that liquidity can only be provided once
    #Your code here
    self.tokenAQty += tokenA_Quantity
    self.tokenBQty += tokenBQuantity
    tokenA.transferFrom(tokenA.address, self.owner, tokenA_quantity)
    tokenB.transferFrom(tokenB.address, self.owner, tokenB_quantity)
    assert self.invariant > 0

# Trades one token for the other
@external
def tradeTokens(sell_token: address, sell_quantity: uint256):
    assert sell_token == self.tokenA.address or sell_token == self.tokenB.address
    #Your code here
    if sell_token == self.tokenA.address:
        tokensToTrade = self.tokenBQty - self.invariant / (self.tokenAQty - sell_quantity)
        tokenAQty += sell_quantity
        tokenBQty -= tokensToTrade
        tokenA.transferFrom(sell_token, self.owner,sell_quantity)
        tokenB.transferFrom(self.owner,sell_token,tokensToTrade)
    if sell_token == self.tokenB.address:
        tokensToTrade = self.tokenAQty - self.invariant / (self.tokenBQty - sell_quantity)
        tokenBQty += sell_quantity
        tokenAQty -= tokensToTrade
        tokenB.transferFrom(sell_token, self.owner,sell_quantity)
        tokenA.transferFrom(self.owner,sell_token,tokensToTrade)

# Owner can withdraw their funds and destroy the market maker
@external
def ownerWithdraw():
    assert self.owner == msg.sender
    #Your code here
    tokenA.transferFrom(self.owner,tokenA.address, self.tokenAQty)
    tokenB.transferFrom(self.owner,tokenB.address, self.tokenBQty)
    self.tokenAQty = 0
    self.tokenBQty = 0
