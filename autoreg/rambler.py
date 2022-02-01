from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import random
import generators
from webdriver_manager.chrome import ChromeDriverManager
from twocaptcha import TwoCaptcha


def captcha(section, form):
    config = {
        'server':           'RuCaptcha.com',
        'apiKey':           '7010f8fed13ad3fde52528cdd956729d',
    }
    solver = TwoCaptcha(**config)
    balance = solver.balance()
    if balance >= 0.5:

        with open('captcha.png', 'wb') as file:
            file.write(section.find_element(By.TAG_NAME, 'img').screenshot_as_png)
        sleep(2)
        config = {
            'server':           'RuCaptcha.com',
            'apiKey':           '7010f8fed13ad3fde52528cdd956729d',
        }
        solver = TwoCaptcha(**config)

        # id = solver.send(file='captcha.png')
        # sleep(10)
        # code = solver.get_result(id)

        result = solver.normal('captcha.png', language=1, lang = 'ru')
        section.find_element(By.TAG_NAME, 'input').send_keys(result['code'])
        sleep(2)
        form.find_elements(By.TAG_NAME, 'button')[1].click()
    else:
        print('Not enough money on rucaptcha account')


if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://id.rambler.ru/login-20/mail-registration?rname=mail&back=undefined&')  #opening registration page
    sleep(2)
    password = generators.get_password()     #generating password
    form = driver.find_element(By.TAG_NAME, 'form')   #locating form
    a = form.find_elements(By.TAG_NAME, 'section')


    a[0].find_element(By.ID, 'login').send_keys(generators.get_mailname())  #generating and inserting mail name
    sleep(2)
    a[1].find_element(By.ID, 'newPassword').send_keys(password) #inputting password
    sleep(2)
    a[2].find_element(By.ID, 'confirmPassword').send_keys(password) #confirming password
    sleep(2)
    # a[3].find_element(By.ID, 'login').send_keys(generators.get_mailname())
    # sleep(2)
    a[3].find_element(By.TAG_NAME, 'input').click()
    b = a[3].find_element(By.CLASS_NAME, 'rui-RelativeOverlay-content')
    c = b.find_element(By.CLASS_NAME, 'rui-Menu-content')
    variants = c.find_elements(By.TAG_NAME, 'div')
    variants[random.randint(0,11)].click()  #choosing random question
    sleep(2)
    a[4].find_element(By.ID, 'answer').send_keys(generators.answer_for_rambler()) #inputting random answer
                  #-----------------CARTCHA------------------------------
    try:
        captcha(a[5], form)
    except Exception as ex:
        print(ex)
        a[5].find_element(By.TAG_NAME, 'button').click() #кнопка смены капчи
        captcha(a[5], form)
        # ----------------Final step----------------------
    sleep(2)
    sleep(1000)
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/footer/div/a').click()
    print('страница создана')
    sleep(1000)

