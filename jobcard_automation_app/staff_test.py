import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# from Task import TaskSimpleData
from selenium.common.exceptions import *
# from Bom import Warehouse
from datetime import datetime
sleeping_time = 0.25




def __findToStaff(browser, list_staffs):
    apps_btn = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-footer/app-menu-footer/div/div[2]')
    apps_btn.click()
    time.sleep(sleeping_time)
    add_staff_app_btn = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-footer/app-menu-footer/div[1]/div/div[5]/div/div')
    add_staff_app_btn.click()
    time.sleep(sleeping_time)