import pandas as pd



class Hill:
    def __init__(self, number, name, classification, height_metres, height_feet, drop_metres, col_metres, os_grid_ref, latitude, longitude):
        self.number = number
        self.name = name
        self.classification = classification
        self.height_metres = height_metres
        self.drop_metres = drop_metres
        self.col_metres = col_metres
        self.height_feet = height_feet
        self.os_grid_ref = os_grid_ref
        self.latitude = latitude
        self.longitude = longitude

    def is_wainwright(self):
        classifications = self.classification.split(',')
        return 'W' in classifications

    def to_record(self):
        return {
            'number': self.number,
            'name': self.name,
            'classification': self.classification,
            'isWainwright': self.is_wainwright(),
            'heightMetres': self.height_metres,
            'heightFeet': self.height_feet,
            'dropMetres': self.drop_metres,
            'colMetres': self.col_metres,
            'osGridRef': self.os_grid_ref,
            'latitude': self.latitude,
            'longitude': self.longitude,
        }
