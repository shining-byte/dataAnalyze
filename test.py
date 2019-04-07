import requests

url = 'http://s.tuniu.com/search_complex/whole-shz-0-%E4%B8%8A%E6%B5%B7/'

response = requests.get(url=url)

print(response.text)