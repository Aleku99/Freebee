from foodscraper import FoodScraper
from selenium import webdriver
import time


class FoodPandaScraper(FoodScraper):
    def __init__(self):
        super().__init__('foodpanda')

    def update(self):
        for city in self.cities:
           pass

    def scrape(self, city)->dict:
        name = city.name.strip().lower()
        longitude = city.longitude.strip()
        latitude = city.latitude.strip()
        url = "https://www.foodpanda.ro/restaurants/new?lat="+latitude+"&lng="+longitude+"&vertical=restaurants"
        # driver = webdriver.Chrome("C:/Users/aleku/Desktop/UPT/SMA/resources/chromedriver.exe")
        driver = webdriver.Firefox(executable_path=r"C:/Users/aleku/Desktop/UPT/SMA/resources/geckodriver.exe")
        driver.get(url)

        time.sleep(10)

        scraped_restaurants = driver.find_elements_by_css_selector(".name.fn")
        scraped_prices = driver.find_elements_by_css_selector('.extra-info.mov-df-extra-info');

        restaurants = list()
        prices = list()

        for restaurant in scraped_restaurants:
            restaurants.append(restaurant.text)

        for price in scraped_prices:
            price = price.text.split()
            price_string_length = len(price)
            if price_string_length > 4:
                if price[4].isnumeric():
                    new_price = price[4]
                elif "gratuita" in price[4]:
                    new_price = str(0)
                else:
                    new_price = price[3].replace("minima","")


            else:
                if price[3].isnumeric():
                    new_price = price[3]
                elif "gratuita" in price[3]:
                    new_price = str(0)
                else:
                    new_price = price[2].replace("minima", "")
            new_price = new_price.replace(",",".")
            new_price = new_price.replace(" ", "")

            try:
                new_price = float(new_price)
            except:
                new_price = float(0)
            finally:
                prices.append(new_price)


        return_dict = {}
        for (i,j) in zip(restaurants,prices):
            return_dict.update({i:j})
        driver.close()
        return return_dict
