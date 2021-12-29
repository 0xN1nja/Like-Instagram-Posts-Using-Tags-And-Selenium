# Copyright Abhimanyu Sharma, https://github.com/N1nja0p
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support import expected_conditions as EC
    import os
    from csv import DictReader
    import time
except:
    print("Modules Not Installed. Run pip install -r requirements.txt To Continue")
options = Options()
options.add_argument("--start-maximized")


class Bot():
    def __init__(self, username: str, password: str, tag: str, count: int, chrome_driver_path: str):
        self.username = username
        self.password = password
        self.tag = tag
        self.count = int(count)
        self.chrome_driver_path = chrome_driver_path
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        self.driver.get("https://instagram.com")

    def login(self):
        WebDriverWait(self.driver, 10000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')))
        username_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_field.send_keys(self.username)
        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(self.password)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

    def explore_tag(self):
        time.sleep(5)
        self.driver.get(f"https://instagram.com/explore/tags/{self.tag}")
        WebDriverWait(self.driver, 100000).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/article')))
        first_post = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]')
        first_post.click()
        time.sleep(2)
        WebDriverWait(self.driver, 10000).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')))
        WebDriverWait(self.driver, 10000).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')))
        like_button = self.driver.find_element_by_xpath(
            '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
        like_button.click()
        WebDriverWait(self.driver, 10000).until(EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[6]/div[1]/div/div/div/button')))
        next_post_button = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div/button')
        next_post_button.click()
        i = 0
        while True:
            WebDriverWait(self.driver, 1000).until(EC.visibility_of_element_located(
                (By.XPATH, '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')))
            like_button = self.driver.find_element_by_xpath(
                '/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button')
            like_button.click()
            WebDriverWait(self.driver, 10000).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div/div/div[2]/button')))
            next_post_button = self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/div[2]/button')
            next_post_button.click()
            i += 1
            print(f"Liked Another Post! Post URL : {self.driver.current_url} Like Count : {i}")
            time.sleep(2)
            if i == self.count:
                self.driver.quit()
                break


if __name__ == '__main__':
    with open("config.csv", "r") as f:
        reader = DictReader(f)
        for i in reader:
            USERNAME = i.get("username")
            PASSWORD = i.get("password")
            TAG = i.get("tag")
            COUNT = i.get("count")
            CHROME_DRIVER_PATH = i.get("chrome_driver_path")
        bot = Bot(USERNAME, PASSWORD, TAG, COUNT, CHROME_DRIVER_PATH)
        bot.login()
        bot.explore_tag()
