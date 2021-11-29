from brownie import *

def main():
    acct = accounts.load("main")
    nft_control = NFTControl.deploy(acct, {'from': acct},publish_source=True)
    print(nft_control.nftWeightSchedules)