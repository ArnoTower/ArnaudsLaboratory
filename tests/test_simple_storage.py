from brownie import SimpleStorage, accounts


def test_deploy():  # creating test crontract #seperated in 3 categories: arrange, act, assets
    # arrange - getting account
    account = accounts[0]
    # act - deploy simplestorage smart contract, call retrieve to see starting value, then compare to see if it it 0
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # assert - green dot means test passed
    assert starting_value == expected

    # test update with 15 to see if it works


def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # act
    expected = 15
    simple_storage.store(expected, {"from": account})
    # assert (we want to store 15 in our smart contract, then retrieve shows thats)
    assert expected == simple_storage.retrieve()
