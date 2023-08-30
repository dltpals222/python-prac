from http.client import HTTPConnection

#* 첫번쨰 요청
host = 'www.example.com'
conn = HTTPConnection(host)
conn.request('GET','/')
r1 = conn.getresponse()
print(r1.status, r1.reason)

data1 = r1.read()
