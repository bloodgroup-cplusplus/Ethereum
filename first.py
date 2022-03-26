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


# let's take a peek atht the state of this simulated blockchain 


print(w3.eth.get_block('latest'))



# send a few test ether from one account to another 

tx_hash = w3.eth.send_transaction (
        {
            'from':w3.eth.accounts[0],
            'to':w3.eth.accounts[1],
            'value':w3.toWei(3,'ether')
            })


print(f'this prints the transaction hash {tx_hash}')


# wait for the transaction to be mined 

#w3.eth.wait_for_transaction_receipt(tx_hash)

#continue applicaton logic. to view the successful transactoin :
#w3.eth.get_transaction(tx_hash)

print(w3.eth.get_balance(w3.eth.accounts[0]))

print(w3.eth.get_balance(w3.eth.accounts[1]))




