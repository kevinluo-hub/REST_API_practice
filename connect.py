from pip._vendor import requests
import pprint
# import pandas as pd

# version 3
api_key = "7e008c185440c2d75519e80298a48aae"

# HTTP requests

# what's our endpoint (or an url)

# what is the HTTP method that we need?
"""
Endpoint
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=7e008c185440c2d75519e80298a48aae
"""
movie_id = 550
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/movie/{movie_id}"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
print(endpoint)
r = requests.get(endpoint) # json={"api_key": api_key})
print(r.status_code)
print(r.text)
# HTTP requests
"""
GET -> grab data
POST -> add/update data

PATCH
PUT
DELETE
"""

# version 4
# access_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3ZTAwOGMxODU0NDBjMmQ3NTUxOWU4MDI5OGE0OGFhZSIsInN1YiI6IjVmZWEyZWE4ZjEyY2Y0MDA0MWQ0NjkyOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.nZ7Fn5xZswuAJxPW6Oz2HStuQpV0fgRJ_EtNP8hsLFQ"
# movie_id = 550
# api_version = 4
# api_base_url = f"https://api.themoviedb.org/{api_version}"
# endpoint_path = f"/movie/{movie_id}"
# endpoint = f"{api_base_url}{endpoint_path}"
# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json;charset=utf-8'
#
# }
# print(endpoint)
# r = requests.get(endpoint, headers=headers)
# print(r.status_code)
# print(r.text)

# using search
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = "/search/movie"
query = "Rush Hour"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={query}"
#print(endpoint)
r = requests.get(endpoint)
#print(r.status_code)
#pprint.pprint(r.json())

# finding out about ids
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        print(results[0].keys())
        movie_ids = set()
        for result in results:
            _id = result['id']
            movie_ids.add(_id)
            print(result['title'], _id)
        print(list(movie_ids))

output = 'movies.csv'
movie_data = []

for m_id in movie_ids:
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{m_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
        data = r.json()
        movie_data.append(data)
    pprint.pprint(r.json())

# df = pd.DataFrame(movie_data)
# df.to_csv(output)
