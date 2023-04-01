from priceTrendCapture import priceCapture
from accessConfig import read_config_file

config_contents = read_config_file()

hist_nav = priceCapture(config_contents["fund_list"])

hist_nav.joinFundNAVs()
