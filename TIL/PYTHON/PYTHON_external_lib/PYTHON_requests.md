# PYTHON requests
- 서버에 requets를 보낼 때 사용하는 library.
```python
import requests

URL = 'https://random-data-api.com/api/v2/users'

response = requests.get(URL)
```
## requests methods
### get
```python
requests.get(URL)
```
- returns response object

## RESP methods
### resp.json
- resp를 json 형식으로 불러온다.
- python 내에서는 list 형식.
```python
resp.json
```
### resp.text
- resp를 text 형식으로
```python
resp.text
```
### resp.headers
- resp의 headers를 가져옴
```python
resp.headers
```
### resp.status_code
- resp의 status_code를 가져옴
```python
resp.status_code
```