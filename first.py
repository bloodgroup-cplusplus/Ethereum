from web3 import Web3

# converting ether to wei 
# 1 ether = 10000000000000000000 wei 
# 1 wei = 0.00000000000000000001 ether 

print(Web3.toWei(1,'ether'))

print(Web3.fromWei(5000000,'gwei'))

w3 = Web3(Web3.EthereumTesterProvider())

# to check whether ethereum is connected to the test net 

print(w3.isConnected())

# see the associated accounts with the object 


print(w3.eth.accounts)


# get balance from the first account 


print(w3.eth.get_balance(w3.eth.accounts[0]))


