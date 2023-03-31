

'''
* 사용자 정의 모듈

- 하나의 모듈 파일에 너무 많은 코드가 들어있으면
편집이 힘들어지고 코드를 유지보수하는 데 어려움이
생깁니다.

- 관리 편의상 비슷한 기능들을 가진 코드를 여러 개의
모듈에 나눠서 작성하는 것이 좋습니다.
'''

import calculator as cal
from calculator import info

print("1인치: %2fcm" % cal.inch)
print("1~10까지 누적합:", cal.calc_sum(10))

info()
info()
info()












































