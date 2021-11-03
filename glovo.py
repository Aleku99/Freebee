from foodscraper import FoodScraper
from selenium import webdriver

class GlovoScraper(FoodScraper):
    def __init__(self):
        super().__init__('glovo')

    def update(self):
        for city in self.cities:
           pass
           #webscraping
           #
           # url = "https://tazz.ro/timisoara/restaurante"
           # driver = webdriver.Chrome("C:/Users/aleku/Desktop/UPT/SMA/resources/chromedriver.exe")
           # driver.get(url)
           #
           # restaurants = driver.find_elements_by_class_name("store-info")
           #
           # for i in restaurants:
           #     j = i.find_element_by_class_name('store-name').text
           #     print(j)
           #
           # driver.close()

