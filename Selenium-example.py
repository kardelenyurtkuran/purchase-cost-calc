from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from concurrent.futures import ThreadPoolExecutor

# Tarayıcıyı başlatma
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Headless modu etkinleştir
browser = webdriver.Chrome(options=options)

# İşlenecek ürün URL'lerini belirtin
urls = ['https://ozdisan.com/pasif-komponentler/kapasitorler/tantal-kapasitorler/T491A106M016AT/461255']  # işlenecek ürün URL'lerini içeren bir liste

# Her bir ürünün bilgisini işleyen bir fonksiyon tanımlama
def process_product(product_url):
    browser.get(product_url)
    # Belirli bir elementin yüklenmesini bekleyelim
    element = WebDriverWait(browser, 0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table-hover")))
    # İşlem yapılacak diğer kodlar buraya gelebilir
    print(element.text)  # Örnek olarak elementin metnini yazdırma

# ThreadPoolExecutor kullanarak iş parçacıklarını yönetme
# with ThreadPoolExecutor(max_workers=5) as executor:
#     executor.map(process_product, urls)

for i in urls:
    process_product(i)
# Tarayıcıyı kapatma
browser.quit()

