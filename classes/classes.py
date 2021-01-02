# creating basic classes for every element used

class Depot:
    def __init__(self, name, lon, lat):
        self.name = name
        self.lat = lon
        self.lon = lat



##########################################################################

class Plant:
    def __init__(self, name, lan, lon):
        self.name = name
        self.lon = lan
        self.lat = lon


##########################################################################

class Site:
    def __init__(self, zipcode, lon, lat):
        self.name = str(zipcode) + str(lon) + str(lat) #concat key
        self.zip = zipcode
        self.lon = lon
        self.lat = lat


##########################################################################

class Job:
    def __init__(self, id, key, plant, silo, material, start, duration, site):
        self.id = id
        self.key = key
        self.plant = plant
        self.silo = silo
        self.material = material
        self.start = start
        self.duration = duration
        self.site = site
