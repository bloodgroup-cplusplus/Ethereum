from web3 import Web3 

# connect to ethereum test net 

w3 = Web3(Web3.EthereumTesterProvider())


# to check whether the ethereum is connected

print(w3.isConnected())

#see the connected accounts 
print(w3.eth.accounts)


# create a new account 

acct_two = w3.eth.account.create()


#printing the address of second account
print(acct_two.address)


print(acct_two.key)

acct_one = w3.eth.accounts[0]
#Then send one of those fake ether over to new account:

tx_hash = w3.eth.send_transaction({
    'from':acct_one,
    'to':acct_two.address,
    'value':Web3.toWei(1,'ether')


    })


#manually build a transactrion


tx = {
        'to':acct_one,
        'value':100000,
        'gas':21000,
        'gasPrice':w3.eth.get_block('pending')['baseFeePerGas'],
        'nonce':0
        }

#sign the transaction with the sender's private key 

signed = w3.eth.account.sign_transaction(tx,acct_two.key)

#send the "raw" transaction 

tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)





