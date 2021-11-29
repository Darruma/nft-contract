from brownie import * 

def main():
    ContractContainer.publish_source(
        NFTControl.at("0xb2589F8b4924A1E183b0071BB68d2aA725570499")
    )