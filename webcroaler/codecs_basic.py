

'''
* 표준 모듈 codecs

- 웹이나 다른 프로그램의 텍스트 데이터와 파이선 내부의
텍스트 데이터의 인코딩 방식이 다를 경우 내장함수 open()이
제대로 인코딩을 적용할 수 없어서 예외가 발생합니다.
(UnicodeEncodeError)

- 파일 입/출력시 인코딩 코덱을 변경하고 싶다면
codecs 모듈을 활용합니다.
'''
import codecs

file_path = "d:/py1230/codecs_test.txt"

try:
    f = codecs.open(file_path, mode="w", encoding="utf-8")
    f.write("안뇽안뇽~~")
    f.write("바이바이~~")
    f.write("멜롱멜롱~~")
    print("파일 저장 완료~!")
except:
    print("파일 저장 실패!")
finally:
    f.close()






































