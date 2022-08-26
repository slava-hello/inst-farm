from smsactivate.api import SMSActivateAPI # SMSActivateAPI Содержит все основные инструменты для работы с API SMSActivate
from time import sleep
from config import sms_key

def get_number():
    sa = SMSActivateAPI(sms_key)

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
