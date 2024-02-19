import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = 'https://ozdisan.com/pasif-komponentler/kapasitorler/tantal-kapasitorler/T491A106M016AT/461255'
    # 'https://ozdisan.com/led-ve-aydinlatma-cozumleri/cob-ledler-ve-led-moduller/ac-led-moduller/SMJE-3V12W1P3-E-Z4E2/396716' #Bu Ürünü Yeniden İncele

browser.get(url)
time.sleep(0.5)

elements = browser.find_elements(By.CSS_SELECTOR, ".table-hover")
# elements = browser.find_elements(By.CSS_SELECTOR, ".yeniUrunFiyat") Bu ürünü yeniden incele

for element in elements:
    print(element.text)

browser.close()
