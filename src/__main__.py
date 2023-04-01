from priceTrendCapture import priceCapture
from configParser import read_config_file

config_contents = read_config_file()

fund_details = config_contents["fund_details"]
# hist_nav = priceCapture(config_contents["fund_details"])

# print(config_contents["fund_details"].keys())


fund_dict = {fund_details[fund_name]['code'] : fund_details[fund_name]['name'] for fund_name in fund_details.keys() if fund_details[fund_name]['code']  }


print(list(fund_dict.keys()))



