from http.client import http

#* 1. 연결 객체 생성
conn = http.client.HTTPConnection("www.python.org") 

#* 2. 요청 보내기
conn.request("GET", "/index.html")

