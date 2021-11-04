from foodscraper import FoodScraper
from selenium import webdriver
import time

class TazzScraper(FoodScraper):
    def __init__(self):
        super().__init__('tazz')

    def update(self):
        pass
    def scrape(self,city)->dict:
        name = city.name.strip().lower()
        url = "https://tazz.ro/"+name+"/restaurante"
        driver = webdriver.Chrome("C:/Users/aleku/Desktop/UPT/SMA/resources/chromedriver.exe")
        driver.get(url)

        time.sleep(5)

        scraped_restaurants = driver.find_elements_by_class_name('store-name');
        scraped_prices = driver.find_elements_by_class_name('store-description');

        restaurants = list()
        prices = list()

        for restaurant in scraped_restaurants:
            restaurants.append(restaurant.text)
        for price in scraped_prices:
            price = price.text.split()
            new_price = price[4] + "." + price[5];
            prices.append(new_price)

        return_dict = {}
        for (i,j) in zip(restaurants,prices):
            return_dict.update({i:j})
        print(return_dict)
        driver.close()
