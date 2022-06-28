
from random import random
from xxlimited import Null
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

dumy = [["https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379543998", [3,1,2,4,2,2]],["https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379511719", [5,4,2,5,5,2]],["https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379564318", [5,4,4,2,3,2]], ["https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379580731", [3,3,3,4,5,4,3,5]],["https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379613916", [4,5,3,4,3,2,5,5,2,2,5,4,5]],["https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379642496", [5,3,4,3,4,4,4,4,2,2,2,3]],["https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379670817", [5,5,4,3,4,2,4,5]]]

print("이름을 입력해주세요")
name = input()
print("번호는 선택해주세요")
num = int(input())

driver = webdriver.Chrome("/Users/seonghun/Downloads/chromedriver 2")
driver.get(dumy[num-1][0])
time.sleep(5)

# element = driver.find_elements(By.TAG_NAME,'li')
choose = driver.find_element(By.ID, "nickname")
choose.send_keys(name)

run = driver.find_element(By.CSS_SELECTOR, "button[type=submit]")
run.click()

time.sleep(13)

for i in dumy[num-1][1]:

    a = False
    while(a == False):
        try:
            button = driver.find_elements(By.TAG_NAME, "button")
            if len(button) <= 1:
                a = False
            else:
                a = True
        except :
            a = False

    button[i].click()

    time.sleep(2)
    for i in [0,1]:
        next = driver.find_element(By.CSS_SELECTOR, "button[type=button]")
        next.click()


# for i in element:
#     if("강" in i.text or "한" in i.text or "세" in i.text):
#         print(i.text)

time.sleep(20)

# https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379543998
# 3,1,2,4,2,2 -> 1

# https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379511719
# 5,4,2,5,5,2 -> 2

# https://kahoot.it/challenge/cd9367e1-2f6b-4002-abfb-9d94cd7159f6_1656379564318
# 5,4,4,2,3,2 -> 3