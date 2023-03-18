from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.common.by import By
import time

def find_btn_menu_1():
    try:
        btn_menu_1 = driver.find_element(By.XPATH, "//a[contains(text(), '학생생활신청')]")
        time.sleep(1);
        btn_menu_1.click()
    except:
        print("Error: <a> 태그 중에서 텍스트가 '학생생활신청'인 요소가 없음")
    return;

def find_btn_menu_2():
    try:
        btn_menu_2 = driver.find_element(By.XPATH, "//a[contains(text(), '소학회상세정보신청')]")
        time.sleep(1);
        btn_menu_2.click()
    except:
        print("Error: <a> 태그 중에서 텍스트가 '소학회상세정보신청'인 요소가 없음")
    return;




driver.get('https://mhaksa.ajou.ac.kr:30443/index.html')
driver.maximize_window()
input_id = driver.find_element('name', 'userId')
input_pw = driver.find_element('name', 'password')
btn_login = driver.find_element('id', 'loginSubmit')
input_id.send_keys('nhle0217')
input_pw.send_keys('030217nana')
btn_login.click()

find_btn_menu_1()

find_btn_menu_2()

while(True):
    	pass
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
data = []

def find_btn_menu_1():
    try:
        btn_menu_1 = driver.find_element(By.XPATH, "//a[contains(text(), '학생생활신청')]")
        time.sleep(1);
        btn_menu_1.click()
    except:
        print("Error: <a> 태그 중에서 텍스트가 '학생생활신청'인 요소가 없음")
    return;

def find_btn_menu_2():
    try:
        btn_menu_2 = driver.find_element(By.XPATH, "//a[contains(text(), '소학회상세정보신청')]")
        time.sleep(1);
        btn_menu_2.click()
    except:
        print("Error: <a> 태그 중에서 텍스트가 '소학회상세정보신청'인 요소가 없음")
    return;

def find_btn_menu_3():
    try:
        time.sleep(1)
        btn_detail = driver.find_elements('id', 'btnDetail') 
        time.sleep(1)
        driver.execute_script("arguments[0].click();", btn_detail[10])
        #btn_detail.click()
        #btn_detail.send_keys(Keys.ENTER)
        #driver.execute_script("arguments[0].click();", btn_detail)
    except Exception as e:
        print(e)
    return;

def find_btn_menu_add():
    try:
        time.sleep(2)
        btn_add = driver.find_element(By.XPATH, "//button[contains(text(), '추가')]")
        time.sleep(1)
        driver.execute_script("arguments[0].click();", btn_add)
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

def apply_data(position, student_id):
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

def login():
    driver.get('https://mhaksa.ajou.ac.kr:30443/index.html')
    driver.maximize_window()
    input_id = driver.find_element('name', 'userId')
    input_pw = driver.find_element('name', 'password')
    btn_login = driver.find_element('id', 'loginSubmit')
    input_id.send_keys('nhle0217')
    input_pw.send_keys('030217nana')
    btn_login.click()

def register_inner_club():
    find_btn_menu_1()
    find_btn_menu_2()
    find_btn_menu_3()
    parse_csv()

    for i in data:
        find_btn_menu_add()
        apply_data(i[0], i[1])

def register_general_club():
    find_btn_menu_1()
    find_btn_menu_2()
    find_btn_menu_3()

if __name__ == '__main__':
    login()
    register_inner_club()


while(True):
        pass

