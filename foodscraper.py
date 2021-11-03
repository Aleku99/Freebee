from shared.city import City

class FoodScraper:

    def __init__(self, service_name):
        self.service_name = service_name
        self.cities = [City("Timisoara", "21.226788", "45.760696"), City("Bucuresti", "26.102538", "44.426767")]


    def update(self): #get_prices(oras) --> nume restaurant si pret (tuplu)
        pass

    def scrape(self) -> dict:
        pass


