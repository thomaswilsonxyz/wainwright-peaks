from hill import Hill
import pandas as pd

class HillSet:    
    def __init__(self, filename):
        df = pd.read_csv(filename, low_memory=False)
        self.hills_dict = df.to_dict('records')
        self.all_hills = []
        self.wainwrights = []
        
        for entry in self.hills_dict:
            hill = Hill(
                    number=entry['Number'],
                    name=entry['Name'],
                    classification=entry['Classification'],
                    height_metres=entry['Metres'],
                    height_feet=entry['Feet'],
                    drop_metres=entry['Drop'],
                    col_metres=entry['Col height'],
                    os_grid_ref=entry['Grid ref'],
                    latitude=entry['Latitude'],
                    longitude=entry['Longitude'],
                )
            
            self.all_hills.append(hill)
            
            if hill.is_wainwright():
                self.wainwrights.append(hill)

    def get_hills(self):
        return self.all_hills

    def get_wainwrights(self):
        return self.wainwrights

    def to_csv(self, hills, filename):
        hills_as_records = map(lambda hill: hill.to_record(), self.wainwrights)
        df = pd.DataFrame.from_records(hills_as_records)
        df.to_csv(filename, index=False)

    def to_json(self, hills, filename):
        hills_as_records = map(lambda hill: hill.to_record(), self.wainwrights)
        df = pd.DataFrame.from_records(hills_as_records)
        df.to_json(filename, orient='records')

