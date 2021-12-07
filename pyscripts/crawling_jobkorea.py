from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd

driver = webdriver.Chrome()

URL = 'https://www.jobkorea.co.kr/recruit/joblist'

driver.get(url=URL)
wait = WebDriverWait(driver, 10)

df = pd.DataFrame(columns=["직무명", "회사명", "위치", "조건텍스트"])

option_jobtype = driver.find_element(By.ID, "duty_10016")
webdriver.ActionChains(driver).click(option_jobtype).perform()

job_name_list = ['웹프로그래머','응용프로그래머','시스템프로그래머','DBA·데이터베이스']
for job_name in job_name_list:
  css_selector = f"input[data-name='{job_name}']"
  option_job_name = driver.find_element(By.CSS_SELECTOR, css_selector)
  webdriver.ActionChains(driver).click(option_job_name).perform()


option_locationtype = driver.find_element(By.CSS_SELECTOR, "dl.dev-local>dt>p")
webdriver.ActionChains(driver).click(option_locationtype).perform()
location_id_list = ['I000', 'B000', 'K000']
for location_id in location_id_list :
  option_location = driver.find_element(By.CSS_SELECTOR, f"label[for='local_step1_{location_id}']>span.radiWrap>span")
  webdriver.ActionChains(driver).click(option_location).perform()

option_careertype = driver.find_element(By.CSS_SELECTOR, "dl.dev-career>dt>p")
webdriver.ActionChains(driver).click(option_careertype).perform()

carrer_id = 'career1' # 신입
option_career = driver.find_element(By.CSS_SELECTOR, f"label[for='{carrer_id}']>span.radiWrap>span")
webdriver.ActionChains(driver).click(option_career).perform()

search_btn = driver.find_element(By.ID, "dev-btn-search")
webdriver.ActionChains(driver).click(search_btn).perform()

el = WebDriverWait(driver).until(lambda d: d.find_element(By.ID, "dev-btn-search"))
assert el.text == "검색완료"

recruit_list = driver.find_elements(By.CSS_SELECTOR, ".tplJobList tbody tr")
webdriver.ActionChains(driver).click(option_career).perform()


