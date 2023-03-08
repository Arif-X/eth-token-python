from brownie import accounts, config, TokenERC20, JancokToken
from scripts.helpful_scripts import get_account

initial_supply = 100000000  # 1000
token_name = "Jancok Token"
token_symbol = "JT"

def main():
    account = accounts.add(config['wallets']['from_key'])
    erc20 = TokenERC20.deploy(
        initial_supply, token_name, token_symbol, {"from": account}
    )
