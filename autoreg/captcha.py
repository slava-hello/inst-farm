
from twocaptcha import TwoCaptcha


config = {
    'server':           'RuCaptcha.com',
    'apiKey':           '7010f8fed13ad3fde52528cdd956729d',
}
solver = TwoCaptcha(**config)
balance = solver.balance()
import time


# id = solver.send(file='captcha.png')
# time.sleep(10)
#
# code = solver.get_result(id)
result = solver.normal('captcha.png', language=1, lang = 'ru')
print(result['code'])
print(balance) 





# import asyncio
# import concurrent.futures
# from twocaptcha import TwoCaptcha
#
#
#
# async def captchaSolver(image):
#     loop = asyncio.get_running_loop()
#     with concurrent.future.ThreadPoolExecutor() as pool:
#         result = await loop.run_in_executor(pool, lambda: TwoCaptcha('7010f8fed13ad3fde52528cdd956729d').normal(image))
#         return result
#
# captcha_result = captchaSolver('/captcha.png')
