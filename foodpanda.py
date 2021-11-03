from foodscraper import FoodScraper
from selenium import webdriver
import time


class FoodPandaScraper(FoodScraper):
    def __init__(self):
        super().__init__('foodpanda')

    def update(self):
        for city in self.cities:
           pass

    def scrape(self,city)->dict: #TODO: finish scraping; wait for unlock
        name = city.name.strip().lower()
        longitude = city.longitude.strip()
        latitude = city.latitude.strip()
        url = "https://www.foodpanda.ro/restaurants/new?lat="+latitude+"&lng="+longitude+"&vertical=restaurants"
        driver = webdriver.Chrome("C:/Users/aleku/Desktop/UPT/SMA/resources/chromedriver.exe")
        driver.get(url)

        scraped_restaurants = driver.find_elements_by_class_name('headline');
        scraped_prices = driver.find_elements_by_class_name('extra-info mov-df-extra-info');

        restaurants = list()
        prices = list()

        for restaurant in scraped_restaurants:
            # restaurants.append(restaurant.text)
            print(restaurant)
        for price in scraped_prices:
            pass
            #print(price)
            # price = price.text.split()
            # new_price = price[4] + "." + price[5];
            # prices.append(new_price)

        return_dict = {}
        # for (i,j) in zip(restaurants,prices):
        #     return_dict.update({i:j})
        # print(return_dict)
        driver.close()
