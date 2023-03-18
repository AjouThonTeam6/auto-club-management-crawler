from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import time
import csv
import requests
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
data = []

def find_btn_menu_1():
    try:
        btn_menu_1 = driver.find_element(By.XPATH, "//a[contains(text(), '학생생활신청')]")
        time.sleep(2);
        btn_menu_1.click()
    except:
        print("Error: <a> 태그 중에서 텍스트가 '학생생활신청'인 요소가 없음")
    return;

def find_btn_menu_2(flag):
    try:
        if(flag == 0):
            btn_menu_2 = driver.find_element(By.XPATH, "//a[contains(text(), '동아리상세정보신청')]")
        elif(flag == 1):
            btn_menu_2 = driver.find_element(By.XPATH, "//a[contains(text(), '소학회상세정보신청')]")
        time.sleep(2);
        btn_menu_2.click()
    except:
        print("Error: <a> 태그 중에서 요소가 없음")
    return;

def find_btn_menu_3():
    try:
        time.sleep(2)
        btn_detail = driver.find_elements('id', 'btnDetail') 
        time.sleep(2)
        driver.execute_script("arguments[0].click();", btn_detail[10])
        #btn_detail.click()
        #btn_detail.send_keys(Keys.ENTER)
        #driver.execute_script("arguments[0].click();", btn_detail)
    except Exception as e:
        print(e)
    return;

def find_btn_menu_add_for_user():
    try:
        time.sleep(2)
        btn_add = driver.find_element(By.XPATH, "//button[contains(text(), '추가')]")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", btn_add)
    except Exception as e:
        print(e)
    return;


def find_btn_menu_add_for_activity():
    try:
        time.sleep(2)
        btn_add = driver.find_elements(By.XPATH, "//button[contains(text(), '추가')]")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", btn_add[1])
    except Exception as e:
        print(e)
    return;

def parse_csv():
    try:
        with open('data.csv', newline='', encoding='cp949') as csvfile:
            reader = csv.reader(csvfile)
            flag = 0
            for row in reader:
                if(flag==0):
                    flag += 1
                    continue;
                else:
                    data.append(row);
            # print(data)
    except Exception as e:
        print(e)
    return;

def apply_data_user(position, student_id):
    try:
            time.sleep(1)
            select_position = Select(driver.find_element(by=By.CSS_SELECTOR, value='select[key="cmmnCd"][key-name="korNm"]'))
            select_position.select_by_index(position)
            select_student_id = driver.find_element(by=By.CSS_SELECTOR, value='input[ng-model="pc.popData.row.stdNo"]')
            select_student_id.send_keys(student_id)
            select_submit_btn = driver.find_element(by=By.CSS_SELECTOR, value='button[ng-click="pc.clickBtn(\'save\', saveForm)"]')
            driver.execute_script("arguments[0].click();", select_submit_btn)
            select_submit2_btn = driver.find_element(by=By.CSS_SELECTOR, value='button[ng-click="modal.ok()"]')
            driver.execute_script("arguments[0].click();", select_submit2_btn)
            time.sleep(0.5)
            select_submit3_btn = driver.find_element(by=By.CSS_SELECTOR, value='button[ng-click="modal.close()"]')
            driver.execute_script("arguments[0].click();", select_submit3_btn)
    except Exception as e:
        print(e)
    return;

def apply_data_activity(activity_name, description):
    try:
            wait = WebDriverWait(driver, 10)
            input_activity_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='text'][ng-model='pc.popData.row.actNm'][required]")))
            input_activity_name.send_keys(activity_name)

            activity_description = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'textarea[ng-model="pc.popData.row.actCtnt"]'))
            )
            activity_description.send_keys(description)

            save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@ng-click=\"pc.clickBtn('save', saveForm)\"]")))
            driver.execute_script("arguments[0].click();", save_button)

            save_button_2 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '확인')]"))
            )
            driver.execute_script("arguments[0].click();", save_button_2)

            save_button_3 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), '확인')]"))
            )
            driver.execute_script("arguments[0].click();", save_button_3)
    except Exception as e:
        print(e)
    return;

def login():
    driver.get('https://mhaksa.ajou.ac.kr:30443/index.html')
    driver.maximize_window()
    input_id = driver.find_element('name', 'userId')
    input_pw = driver.find_element('name', 'password')
    btn_login = driver.find_element('id', 'loginSubmit')
    input_id.send_keys('nhle0217')
    input_pw.send_keys('030217nana')
    btn_login.click()
    time.sleep(2)

def change_menu_into_activity_report():
    try:
        time.sleep(1)
        btn_activity_report = driver.find_element(By.XPATH, "//em[contains(text(), '활동내역')]").find_element(By.XPATH, '..').find_element(By.XPATH, '..')
        time.sleep(1)
        driver.execute_script("arguments[0].click();", btn_activity_report)
    except Exception as e:
        print(e)

# 1차 기능 함수 구역

def register_general_club():
    find_btn_menu_1()
    find_btn_menu_2(0)
    find_btn_menu_3()

    for i in data:
        find_btn_menu_add_for_user()
        apply_data_user(i[0], i[1])

def register_inner_club():
    find_btn_menu_1()
    find_btn_menu_2(1)
    find_btn_menu_3()
    parse_csv()

    for i in data:
        find_btn_menu_add_for_user()
        apply_data_user(i[0], i[1])

def generate_inner_club_activity_report(data):
    find_btn_menu_1()
    find_btn_menu_2(1)
    find_btn_menu_3()
    change_menu_into_activity_report()
    
    for i in data:
        find_btn_menu_add_for_activity()
        apply_data_activity(i[0], i[1])

test_data_for_activity_report = [['개강총회', '개강을 했다.'], ['종강총회', '종강을 했다.']]

if __name__ == '__main__':
    login()
    generate_inner_club_activity_report(test_data_for_activity_report)


while(True):
        pass