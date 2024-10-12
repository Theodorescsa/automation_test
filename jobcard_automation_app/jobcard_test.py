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


def __selectStartOrEndDate(browser,date: dict,type):
    # select_time_btn = browser.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[3]/div[2]/div[2]/div/smart-datetime/button")
    # select_time_btn.click()
    # time.sleep(sleeping_time)
    if type == "start":
        date_element = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[3]/div[2]/div[2]/div/smart-datetime/button')
    else:
        date_element = browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[3]/div[2]/div[3]/div/smart-datetime/button')
            
    date_element.click()
    time.sleep(2)
    ion_datetime_shadow = browser.find_element(By.TAG_NAME,'ion-datetime').shadow_root

    # select day
    next_month_btn = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="calendar-next-prev"]')

    ion_button_ele = next_month_btn.find_elements(By.TAG_NAME,'ion-button')
    print(ion_button_ele[0].tag_name)
    ion_button_ele[1].click()
    time.sleep(0.5)
    group_day_dad_ele = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="calendar-month-grid"]')
    list_days_btn = group_day_dad_ele.find_elements(By.TAG_NAME,'button')
    print(len(list_days_btn))
    for element in list_days_btn:
        print(element.text, int(date['day']))
        if element.text == None or element.text == '':
            continue
        if int(element.text) == int(date['day']):
            print(element.tag_name)
            # Nhấn nút
            # element.click()
            
            time.sleep(sleeping_time)
            break
        

    # select month and year
    test = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="calendar-month-year"]')
    ion_item_ele = test.find_element(By.TAG_NAME,'ion-item')
    ion_label_btn = ion_item_ele.find_element(By.TAG_NAME,'ion-label')
    ion_label_btn.click()
    time.sleep(0.5)
    group_month_element = ion_datetime_shadow.find_element(By.CSS_SELECTOR,'[class="month-column ion-color ion-color-primary md hydrated"]').shadow_root
    list_month_btn = group_month_element.find_elements(By.CSS_SELECTOR,'[class="picker-item"]')
    print(len(list_month_btn))
    
    



def __select_tabjob(browser, tabjob_name):
    tabjob_selection_ele = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[1]/ion-item/ionic-selectable/div/button')
    tabjob_selection_ele.click()
    time.sleep(0.5)
    group_selection_tabjob = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
    
    list_selection_tabjob = group_selection_tabjob.find_elements(By.TAG_NAME,'ion-label')
    for element in list_selection_tabjob:
        print(element.text)
        element.click()
        time.sleep(0.5)
        break
        if tabjob_name == element.text:
            element.click()
            break
    list_job_ele = browser.find_element(By.XPATH,'//*[@id="main-content"]/app-create-card-job/ion-content/div/div[2]/ion-item/ionic-selectable/div/button')
    list_job_ele.click()
    time.sleep(0.5)
    group_selection_list_tabjob = browser.find_element(By.XPATH,'/html/body/app-root/ion-app/ion-modal/ionic-selectable-modal/ion-content/ion-list/ion-item-group')
    
    list_selection_list_tabjob = group_selection_list_tabjob.find_elements(By.TAG_NAME,'ion-label')
    for element in list_selection_list_tabjob:
        print(element.text)
        element.click()
        time.sleep(0.5)
        break
        if tabjob_name == element.text:
            element.click()
            break
    move_to_add_job_card_ele = browser.find_element(By.XPATH, "/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[3]/i")
    move_to_add_job_card_ele.click()
    time.sleep(0.25)

def __finJobCard(browser,list_jobcards,list_staffs,list_tasks):

    for i in range(len(list_jobcards)):
        add_jobcard_element =  browser.find_element(By.XPATH, '/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-time-keeping/ion-header/ion-toolbar/div/div/a[1]')
        add_jobcard_element.click()
        time.sleep(sleeping_time)
        __select_tabjob(browser, list_jobcards[i].tab_job)
        time.sleep(0.5)
        if list_jobcards[i].name is None:
            i = 2
        cardname_input = browser.find_element(By.XPATH,"/html/body/app-root/ion-app/ion-split-pane/ion-router-outlet/app-create-card-job/ion-content/div/div[1]/div/input")
        print(list_jobcards[i].name)
        cardname_input.clear()
        cardname_input.send_keys(list_jobcards[i].name)

        start_date = list_jobcards[i].start_date

        day = start_date.strftime('%d') 
        month = start_date.strftime('%B')  # Lấy tháng dưới dạng tên tiếng Anh đầy đủ
        year = start_date.strftime('%Y') 
        start_date_compile = {
            "day":day,
            "month":month,
            "year":year
        }
        __selectStartOrEndDate(browser,start_date_compile, "start")
        time.sleep(0.25)
        break
        
    
