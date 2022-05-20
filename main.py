# indicators
crypto_market_up = True
tech_stocks_up = True # tech stocks
bitcoin_dominance_up = False

# reusable independent tests
def altcoin_season():
    return not bitcoin_dominance_up

# independent tests
def bull_market():
    return crypto_market_up and tech_stocks_up

def bull_market_ending():
    return crypto_market_up and not tech_stocks_up

# reusable tests
def buy_altcoins():
    return altcoin_season() and crypto_market_up

# sanity checks
assert not ( altcoin_season() and not crypto_market_up ), "bitcoin dominance always goes up in a bear market"
assert not ( altcoin_season() and not crypto_market_up ), "altcoins don't pump in a crypto bear market"

if altcoin_season() and bull_market_ending():
    print("take profit on altcoins into bitcoin")
elif buy_altcoins():
    print("sell all bitcoin and buy back into altcoins to get more coins with the same or slightly increased cost basis")
else:
    print("buy bitcoin")
