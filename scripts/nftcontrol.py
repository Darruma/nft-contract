from brownie import *

def main():
    nft_control = NFTControl.deploy(accounts[0], {'from': accounts[0]})
    nft_control.setNFTWeight(
        "0xe1e546e25A5eD890DFf8b8D005537c0d373497F8",
        1,
        200 * 1e18
    )
    result = nft_control.nftWeight["0xe1e546e25A5eD890DFf8b8D005537c0d373497F8"][1]
    print(result)