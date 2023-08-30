from http.client import http

#? GET 메소드 요청예제

#* 1. 연결 객체 생성
conn = http.client.HTTPConnection("www.python.org") 

#* 2. 요청 보내기
conn.request("GET", "/index.html")

#* 3. 응답 객체 생성
response = conn.getresponse()

#* 4. 응답 데이터를 읽음
date = response.read()

#* 5. 연결을 닫음
conn.close()