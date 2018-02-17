from bots.gainer import Gainer


config = {
    'coin': 'LTC',
    'market' : 'BTC-LTC',
    'algorithm': 'MVA',
    'exchange': 'Binance',
    'interval' : 2
}

bot = Gainer(config)

bot.trade()