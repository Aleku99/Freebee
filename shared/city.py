class City:
    def __init__(self,name,longitude,latitude):
        self.name = name
        self.longitude = longitude
        self.latitude = latitude
        self.restaurants_tazz = {}
        self.restaurants_foodpanda = {}
        self.restaurants = {}

