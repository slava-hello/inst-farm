from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

#делать все действия в новой открытой вкладке и закрывать её
class parser:
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def faces_parser(self):
        self.driver.get('https://thispersondoesnotexist.com/image')
        with open('filename.png', 'wb') as file:
            file.write(self.driver.find_element(By.XPATH, '/html/body/img').screenshot_as_png)

    def quotes_parser(self):
        self.driver.get('http://freegenerator.ru/citat')
        self.driver.refresh()
        a = self.driver.find_element(By.ID, 'main').text
        print(a)

    def photo_parser(self):
        self.driver.get('https://realisticshots.com/')
        list_of_photos = self.driver.find_element(By.ID, 'posts')
        a = list_of_photos.find_elements(By.TAG_NAME, 'article')
        b = \
            a[0].find_element(By.CLASS_NAME, 'photo-post').find_element(By.CLASS_NAME, 'captions').find_element(
                By.TAG_NAME, 'p').find_elements(By.TAG_NAME, 'a')[1].get_attribute('href')
        self.driver.get(b)
        sleep(3)
        with open('photo.png', 'wb') as file:
            file.write(self.driver.find_element(By.TAG_NAME, 'img').screenshot_as_png)


a = parser()
