import json

from selenium import webdriver
from tazz import TazzScraper
from shared.city import City
from foodpanda import FoodPandaScraper
from shared.country import Country
from glovo import GlovoScraper
from getpass import getpass
import time
if __name__ == "__main__":
    cities = [City("Timisoara", "21.226788", "45.760696"), City("Bucuresti", "26.10626", "44.43225")]
    romania = Country("Romania", cities)

    tazz = TazzScraper()
    for city in romania.cities:
        time.sleep(30)
        city.restaurants_tazz = tazz.scrape(city)


    foodpanda = FoodPandaScraper()
    for city in romania.cities:
        time.sleep(30)
        city.restaurants_foodpanda = foodpanda.scrape(city)


    for city in romania.cities:
        #insert tazz restaurants
        for key, value in city.restaurants_tazz.items():
            found = 0
            for key2, value2 in city.restaurants_foodpanda.items():
                if key.lower().strip() in key2.lower().strip():
                    city.restaurants.update({key:(value, value2)})
                    found = 1
            if found == 0:
                city.restaurants.update({key: (value, -1)})
        #insert foodpanda restaurants
        for key2, value2 in city.restaurants_foodpanda.items():
            found = 0
            for key, value in city.restaurants.items():
                if key2.lower().strip() in key.lower().strip():
                    found = 1
            if found == 0:
                city.restaurants.update({key2: (-1, value2)})

    #print all restaurants
    for city in romania.cities:
        firebase_object = {}
        firebase_object['name'] = city.name
        firebase_object['restaurants'] = city.restaurants
        with open("out.json","w") as file:
            json.dump(firebase_object,file, indent=4,sort_keys=True);








