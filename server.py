from urllib.request import urlopen, Request
from urllib.parse import urlencode 

#* Get 처리
# f = urlopen("http://www.example.com")
# print(f.read(500).decode('utf-8'))

#* POST방식 요청
# data = "language=python&framework=django"
# f = urlopen("http://127.0.0.1:8000", bytes(data, encoding='utf-8'))
# print(f.read(500).decode('utf-8'))

#* Request 클래스로 요청 헤더 지정
url = "http://127.0.0.1:8000"
data = {
    'name' : "BlahBlah",
    'email' : "blah@example.com",
    'url' : "http://www.naver.com"
}
encData = urlencode(data)
postData = bytes(encData, encoding='utf-8')
req = Request(url, data=postData)
req.add_header('Content-Type', 'application/x-www-form-urlencoded')
f = urlopen(req)
print(f.info())
print(f.read(500).decode('utf-8'))