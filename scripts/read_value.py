from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]
    # go take the index thats one less than the length
    # ABI whenever interacting with smart contract (brownie already knows this)
    # Address (Brownie already knows your contract address)
    print(simple_storage.retrieve())


def main():
    read_contract()
