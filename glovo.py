from foodscraper import FoodScraper
from selenium import webdriver
import time

class GlovoScraper(FoodScraper):
    def __init__(self):
        super().__init__('glovo')

    def update(self):
        pass

    def scrape(self,city)->dict: #TODO: try changing cookies to display prices?
        name = city.name.strip().lower()
        longitude = city.longitude.strip()
        latitude = city.latitude.strip()
        base_url = "https://glovoapp.com/ro/ro/"+name+"/restaurante_1?page="
        driver = webdriver.Chrome("C:/Users/aleku/Desktop/UPT/SMA/resources/chromedriver.exe")
        driver.delete_all_cookies()
        page = 1
        url = base_url + str(page)
        driver.get(url)
        driver.add_cookie({"name": "glovo_user_city", "value": "TIM"})
        driver.add_cookie({"name": "glovo_user_latlng", "value": latitude + "|" + longitude})
        driver.add_cookie({"name": "glovo_user_cities", "value": "[%22TIM%22]"})

        time.sleep(5)
        total_pages = int(driver.find_element_by_class_name('current-page-text').text.split()[2])
        print(total_pages)


        while(page <= total_pages):
            url = base_url + str(page)
            driver.delete_all_cookies()
            driver.get(url)
            driver.add_cookie({"name": "glovo_user_city", "value": "TIM"})
            driver.add_cookie({"name": "glovo_user_latlng", "value": latitude + "|" + longitude})
            driver.add_cookie({"name": "glovo_user_cities", "value": "[%22TIM%22]"})

            time.sleep(5)
            scraped_restaurants = scraped_restaurants + driver.find_elements_by_class_name('card-title')
            scraped_prices = scraped_prices+ driver.find_elements_by_css_selector('.service-fee__label.dark-text')
            page+=1

        restaurants = list()
        prices = list()

        for restaurant in scraped_restaurants:
            restaurants.append(restaurant.text)
            print(restaurant.text)
        for price in scraped_prices:
            price = price.text.split()
            new_price = price[0].replace(",",".")
            prices.append(new_price)
            print(price)
            print(new_price)

        return_dict = {}
        for (i,j) in zip(restaurants,prices):
            return_dict.update({i:j})
        print(return_dict)
        driver.close()

