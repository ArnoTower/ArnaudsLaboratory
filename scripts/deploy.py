from brownie import accounts, config


def deploy_simple_storage():
    # account = accounts[0]
    # pass
    # print(account)
    # account = accounts.load("ArnaudsLaboratory")
    account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
