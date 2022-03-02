# import time
# from smsactivateru import Sms, SmsTypes, SmsService, GetBalance, GetFreeSlots, GetNumber, SetStatus, GetStatus
#
# """
# create wrapper with secret api-key
# search here: http://sms-activate.ru/index.php?act=profile)
# """
# wrapper = Sms('2254efc35fd07b884e13Ad18Afb02Af8')
#
# # getting balance
# balance = GetBalance().request(wrapper)
# # show balance
# a = balance
# print(a)
# print('На счету {} руб.'.format(balance))
#
# # getting free slots (count available phone numbers for each services)
# available_phones = GetFreeSlots(country='0').request(wrapper)
# # show for instagram
# print('insta.com: {} номеров'.format(available_phones.Instagram.count))
#
#
# # try get phone for youla.io
# activation = GetNumber(
#     service=SmsService().Instagram,
#     country=SmsTypes.Country.RU
# ).request(wrapper)
# # show activation id and phone for reception sms
# print('id: {} phone: {}'.format(str(activation.id), str(activation.phone_number)))
# #
# # getting and show current activation status
# response = GetStatus(id=activation.id).request(wrapper)
# print(response)
#
# # .. send phone number to you service
# user_action = input('Press enter if you sms was sent or type "cancel": ')
# if user_action == 'cancel':
#     set_as_cancel = SetStatus(
#         id=activation.id,
#         status=SmsTypes.Status.Cancel
#     ).request(wrapper)
#     print(set_as_cancel)
#     exit(1)
#
# # set current activation status as SmsSent (code was sent to phone)
# set_as_sent = SetStatus(
#     id=activation.id,
#     status=SmsTypes.Status.SmsSent
# ).request(wrapper)
# print(set_as_sent)
#
# # .. wait code
# while True:
#     time.sleep(1)
#     response = GetStatus(id=activation.id).request(wrapper)
#     if response['code']:
#         print('Your code:{}'.format(response['code']))
#         break
#
# # set current activation status as End (you got code and it was right)
# set_as_end = SetStatus(
#     id=activation.id,
#     status=SmsTypes.Status.End
# ).request(wrapper)
# print(set_as_end)









from smsactivate.api import SMSActivateAPI # SMSActivateAPI Содержит все основные инструменты для работы с API SMSActivate
from time import sleep

def get_number():
    sa = SMSActivateAPI('16378162fB33723f93276c0f8B283e6B')

    print(sa.getBalance())
    prices = sa.getPrices(service='ig', country=0)
    try:
        print(prices['0'])  # {'fb': {'cost': 9, 'count': 27934}}
    except:
        print(prices['message'])  # Текст ошибки

    number = sa.getNumber(service='ig', country=0)  # {'order_id': 000000000, 'phone': 79999999999}
    try:
        print(number['phone'])  # 79999999999
    except:
        print(number['message'])  # Текст ошибки
    return [sa,number]


def ver_code(sa, number):
        a = True
        while a:
            status = sa.getStatus(id=number['order_id'])
            print(status)
            if 'STATUS_OK' in status:
                a = False
                sms = sa.getFullSms(id=number['order_id'])
                print(sms)
                sleep(5)
            else:
                sleep(5)

        return status[status.index(':') + 1:]

# try:
#     print(status['price']) # 4.00
# except:
#     print(status['message']) # Текст ошибки

# sa.debug_mode = True # Используется для отладки. При активном debug_mode все ответы от сервера и класса будут выводиться в консоль