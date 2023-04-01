from priceTrendCapture import priceCapture
from configParser import read_config_file

config_contents = read_config_file()

fund_details = config_contents["fund_details"]
# hist_nav = priceCapture(config_contents["fund_details"])

# print(config_contents["fund_details"].keys())


fund_name_dict = {fund_details[fund_name]['code'] : fund_details[fund_name]['name'] for fund_name in fund_details.keys() if fund_details[fund_name]['code']  }

fund_alias_dict = {fund_details[fund_name]['code'] : fund_details[fund_name]['alias'] for fund_name in fund_details.keys() if fund_details[fund_name]['code']  }

# for fund_code, fund_alias in fund_alias_dict.items():
#     print(fund_code, fund_alias)






hist_nav = priceCapture(
    dict(
        zip(fund_alias_dict.values(), fund_alias_dict.keys())
        )
    )

nav = hist_nav.joinFundNAVs()
print(nav)


