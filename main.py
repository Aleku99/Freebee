from selenium import webdriver
from tazz import TazzScraper
from shared.city import City
from foodpanda import FoodPandaScraper
if __name__ == "__main__":
    # tazz = TazzScraper()
    # tazz.scrape(City("Timisoara", "21.226788", "45.760696"))
    foodpanda = FoodPandaScraper()
    foodpanda.scrape(City("Timisoara", "21.226788", "45.760696"))



