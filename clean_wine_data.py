import pandas as pd
import numpy as np

wine_data = pd.read_csv('./Wine.csv')
wine_data.columns = [  'name',
                'alcohol',
             	'malicAcid',
             	'ash',
            	'ashalcalinity',
             	'magnesium',
            	'totalPhenols',
             	'flavanoids',
             	'nonFlavanoidPhenols',
             	'proanthocyanins',
            	'colorIntensity',
             	'hue',
             	'od280_od315',
             	'proline'
                ]

wine_data = wine_data[[  'name',
                'alcohol',
             	'malicAcid',
             	'ash',
            	'ashalcalinity',
             	'magnesium',
            	'totalPhenols',
             	'flavanoids',
             	'nonFlavanoidPhenols',
             	'proanthocyanins',
            	'colorIntensity',
             	'hue'
                ]]

wine_data.to_csv('wine_data.csv', index = False, sep=',', )