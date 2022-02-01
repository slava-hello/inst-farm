from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
import random
import generators
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://www.instagram.com/accounts/emailsignup/')  #getting signing up page

    #setting up sign in variables
    number = '+375295424962'
    name = generators.get_full_name()
    username = generators.get_nickname()
    password = generators.get_password()


    sleep(2)
    try:
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()   #trying to accept cookies
    except:
        print('a')
    sleep(2)

    try:
        driver.find_element(By.NAME, 'emailOrPhone').send_keys(number)   #inputting phone number
        sleep(2)
        driver.find_element(By.NAME, 'fullName').send_keys(name)   #inputting name
        sleep(2)
        driver.find_element(By.NAME, 'username').send_keys(username)   #inputting username
        sleep(2)
        driver.find_element(By.NAME, 'password').send_keys(password)   #inputting password
        sleep(2)
        # sleep(1000)
        driver.find_element(By.CLASS_NAME, 'XFYOY').find_elements(By.TAG_NAME, 'button')[-1].click()   #clicking 'next' button
        # print(a)
    except Exception as ex:
        try:
            print('a')
            ca = driver.find_element(By.ID, 'ssfErrorAlert').text    #locating error occured
            print(ca)
            print('a')
        except:
            sleep(1000)
        print(ex)
    sleep(2)
    # sleep(100)                          #/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span
                                        #/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span
                                        #qF0y9 Igw0E rBNOH eGOV_ _4EzTm yV-Ex HVWg4
    # b = driver.find_elements((By.CLASS_NAME, 'qF0y9'))
    # print(b)
    # print(len(b))
    try:
        b = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/main/div/div/div[1]/div/div[4]/div/div/span')    #locating span with all fields
    except:
        b = driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span')
    a = b.find_elements(By.TAG_NAME, 'select')   #list of input fields
    sleep(2)
    print(len(a))
    for i in range(len(a)):
        if i == 0:
            a[i].find_elements(By.TAG_NAME, 'option')[random.randint(0,11)].click()   #choosing random month
        if i == 1:
            a[i].find_elements(By.TAG_NAME, 'option')[random.randint(0,27)].click()   #choosing random day
        if i == 2:
            a[i].find_elements(By.TAG_NAME, 'option')[random.randint(19, 26)].click()   #choosing birth year

        sleep(2)
    try:
        driver.find_element(By.XPATH, '/html/body/div[1]/section/main/div/div/div[1]/div/div[6]/button').click()
    except:
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/section/main/div/div/div[1]/div/div[6]/button').click()

    sleep(100)
    sleep(100)
    # fullName
    # username
    # password