import requests
import json
import pandas as pd
r = requests.get(url = 'http://127.0.0.1:8000/api/dataProcess/single_inquire/?poi_dbname=cinema_poi&poly_dbname=bussiness_poly&type=3&poly_dbname_ids=[9,35,111]')

result = json.loads(r.text)
result['result']
json = json.dumps(result['result'])
b = pd.read_json(json,orient='split')
print(b)