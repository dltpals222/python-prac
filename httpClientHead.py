from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
# 첫번째 인자가 url이 아니라 host이기 때문에 
# 'Http://www.example.com'로 입력하면 에러가 발생한다.

conn.request('HEAD','/')
resp = conn.getresponse()
print(resp.status, resp.reason)

data = resp.read()
print(len(data))
# 위 요청에 head는 있지만 body는 없기 때문에 길이는 0이 나온다.

print(data == b'')
