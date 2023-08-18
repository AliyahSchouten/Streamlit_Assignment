import requests
import pandas as pd

class Base:
    

        
    
    
    def get_data(self):
        ''' Scraping data from the API and creatin a DataFrame from it.'''
        response = requests.pd.read_csv(r'C:\Users\ALIYA\OneDrive\Documents\Coding_Temple\Week 6\Day2\Streamlit_Assignment\src\data\student-mat.csv')
        response1 = requests.get(response.json()['data'][0]['download_uri'])
        self.df = pd.DataFrame.from_dict(response1.json())
        return self.df
        

