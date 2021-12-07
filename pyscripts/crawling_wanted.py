from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver = webdriver.Chrome()

URL = 'https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all'

driver.get(url=URL)
original_window = driver.current_window_handle
wait = WebDriverWait(driver, 10)

df = pd.DataFrame(columns=["직무명", "회사명", "위치", "조건텍스트"])

list_links = driver.find_elements(By.CSS_SELECTOR, "*[data-cy='job-card']>a")
count = 0

while (len(list_links) > count):
  print(f"current progress = {count} / {len(list_links)}")
  list_links[count].click()
  info_section = WebDriverWait(driver,10).until(lambda d: d.find_element(By.CLASS_NAME, "Bfoa2bzuGpxK9ieE1GxhW"))
  position_name = info_section.find_element(By.TAG_NAME,"h2").text
  company_name = info_section.find_element(By.TAG_NAME,"h6").text
  location_name = info_section.find_element(By.CLASS_NAME,"uLnE9Osvd9TVfXzywpsK_").text
  condition_txt = WebDriverWait(driver,10).until(lambda d: d.find_element(By.CLASS_NAME, "_3_gsSnQyvwrqCAjw47hjWK")).text
  df.loc[count] = [position_name, company_name, location_name, condition_txt]
  count += 1
  if (count % 10) == 0 :
    df.to_csv("../data/data.csv", encoding="utf-8-sig")
  driver.back()
  list_links = driver.find_elements(By.CSS_SELECTOR, "*[data-cy='job-card']>a")
  # print(df)
df.to_csv("../data/data.csv", encoding="utf-8-sig")

# 0~458번까지 크롤링 완료