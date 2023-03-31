

'''
* 표준 모듈 datetime

- 운영체제의 현재 시간과 날짜 정보를 파이썬 내부로 읽어오는
기능을 제공하는 모듈입니다.
'''

from datetime import datetime

#오늘 날짜와 현재 시간정보를 가지고 있는 객체를 리턴.

d = datetime.today()
print(d)

print("지금은 %d년 %d월 %d일 %d시 %d분 %d초 입니다."
      % (d.year, d.month, d.day, d.hour, d.minute, d.second))






































