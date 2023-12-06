# 引入 selenium 的 webdriver
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 初始化 webdriver 並開啟瀏覽器
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.get("https://dev.egroup-infocenter.com/login")
# 等待一段時間讓頁面載入結果
time.sleep(3)
# 透過 xpath 找到帳號、密碼輸入框
account_input = driver.find_element(By.XPATH, "//*[@id='mui-6']")
password_input = driver.find_element(By.XPATH, "//*[@id='mui-7']")
# 輸入帳號、密碼
account_input.send_keys("test03@gmail.com")
password_input.send_keys("123456")
# 按下登入按鈕
password_input.send_keys(Keys.ENTER)
time.sleep(5)

setting_button = driver.find_element(By.XPATH, "//*[@id='__next']/div/header/div[1]/div/span")
setting_button.click()
time.sleep(5)

press_darking = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/div[2]/button[2]")
press_darking.click()
time.sleep(5)

close_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[1]/button[2]")
close_button.click()
time.sleep(5)

click_head = driver.find_element(By.XPATH, "//*[@id='__next']/div/header/div[1]/div/button[2]")
click_head.click()
time.sleep(5)

logout_button = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div[2]/li[3]/div")
logout_button.click()
time.sleep(5)



expect_url = "https://dev.egroup-infocenter.com/login"
assert driver.current_url == expect_url, "未正常登出"

# 關閉瀏覽器
driver.close()