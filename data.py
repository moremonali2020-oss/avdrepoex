import pandas as pd
import requests


Data = {
    'name': ['A', 'B', 'C'],
     'age': [30, 20, 20],
     'address': ['pune', 'mumbai', 'CSN']

}

print('Student Details')
df = pd.DataFrame(Data)
print(df)

print('API data')
response = requests.get('https://jsonplaceholder.typicode.com/users')
print(response.json())
