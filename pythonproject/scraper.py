from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_product_details(product_url: str) -> dict:
    product_details = {}

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--log-level=3')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_experimental_option("useAutomationExtension", False)

    service = Service(ChromeDriverManager().install())
    service.creation_flags = 0x08000000
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(product_url)
        time.sleep(3)

        try:
            title = driver.find_element(By.ID, "productTitle").text.strip()
        except:
            title = "Title not found"

        try:
            soup = BeautifulSoup(driver.page_source, 'lxml')
            price_tag = soup.find('span', class_='a-offscreen')
            price = price_tag.get_text().strip() if price_tag else "Price not found"
        except:
            price = "Price not found"

        product_details = {
            'title': title,
            'price': price,
            'product_url': product_url
        }

    except Exception as e:
        product_details = {
            'title': 'Error',
            'price': 'Error',
            'product_url': product_url
        }

    driver.quit()
    return product_details
