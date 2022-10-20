# dollar = 300
# exchange_rate = 100
#
# bdt = dollar * exchange_rate
# print(dollar,"dollar is equal to",bdt)
#
# # Samsung rate
#
# samsumg_phone_price = 200
# samsung_bdt = samsumg_phone_price * exchange_rate
# print(samsumg_phone_price,"dollar is equal to",samsung_bdt)
#
# # Xaiomi price
#
# xaiomi_phone_price = 150
# xaiomi_bdt = xaiomi_phone_price * exchange_rate
# print(xaiomi_phone_price,"dollar is equal to",xaiomi_bdt)

# Don't repeat same work (function)

def mobile_price_bdt(usd_price, exchange_rate):
    bdt_price = usd_price * exchange_rate
    return bdt_price

xaiomi_price = mobile_price_bdt(180,101.91)
samsung_price = mobile_price_bdt(200,103.52)
print(xaiomi_price)
print(round(samsung_price))

