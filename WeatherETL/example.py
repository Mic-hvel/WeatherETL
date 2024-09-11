import pandas as pd
import json
import openpyxl
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

json_data = response.json()

data = pd.DataFrame(json_data)
print(data)

data.to_excel('output.xlsx', index=False)