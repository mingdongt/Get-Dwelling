import pandas as pd

y = pd.read_csv('data.csv')
x = pd.read_hdf('data.h5', 'table')

x['Dwelling number class'] = ''
x['Dwelling number class'][(x['Dwelling number'] >= 0) & (x['Dwelling number'] < 5)] = '000 - 005'
x['Dwelling number class'][(x['Dwelling number'] >= 5) & (x['Dwelling number'] < 10)] = '005 - 010'
x['Dwelling number class'][(x['Dwelling number'] >= 10) & (x['Dwelling number'] < 15)] = '010 - 015'
x['Dwelling number class'][(x['Dwelling number'] >= 15) & (x['Dwelling number'] < 20)] = '015 - 020'
x['Dwelling number class'][(x['Dwelling number'] >= 20) & (x['Dwelling number'] < 25)] = '020 - 025'
x['Dwelling number class'][(x['Dwelling number'] >= 25) & (x['Dwelling number'] < 30)] = '025 - 030'
x['Dwelling number class'][(x['Dwelling number'] >= 30) & (x['Dwelling number'] < 35)] = '030 - 035'
x['Dwelling number class'][(x['Dwelling number'] >= 35) & (x['Dwelling number'] < 40)] = '035 - 040'
x['Dwelling number class'][(x['Dwelling number'] >= 40) & (x['Dwelling number'] < 45)] = '040 - 045'
x['Dwelling number class'][(x['Dwelling number'] >= 45) & (x['Dwelling number'] < 50)] = '045 - 050'
x['Dwelling number class'][(x['Dwelling number'] >= 50) & (x['Dwelling number'] < 100)] = '050 - 100'


x['Dwelling number class'][(x['Dwelling number'] >= 100) & (x['Dwelling number'] < 200)] = '100 - 200'
x['Dwelling number class'][(x['Dwelling number'] >= 200) & (x['Dwelling number'] < 300)] = '200 - 300'
x['Dwelling number class'][(x['Dwelling number'] >= 300) & (x['Dwelling number'] < 400)] = '300 - 400'
x['Dwelling number class'][(x['Dwelling number'] >= 400) & (x['Dwelling number'] < 500)] = '400 - 500'
x['Dwelling number class'][(x['Dwelling number'] >= 500) & (x['Dwelling number'] < 600)] = '500 - 600'
x['Dwelling number class'][(x['Dwelling number'] >= 600) & (x['Dwelling number'] <= 700)] = '600 - 700'


x.to_hdf('data.h5', 'table')




