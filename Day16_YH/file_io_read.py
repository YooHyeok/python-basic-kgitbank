

'''
* 파일 읽기 기능 (read)

- 파일로부터 데이터를 읽어들일 때는 분량에 따라
적당한 메서드를 사용합니다.

1. read(): 파일 전체 데이터를 통째로 읽어서 리턴.
2. readline(): 파일 데이터를 한 줄씩 읽어러 리턴.
3. readlines(): 파일 전체를 읽어서 한 줄씩 분리한 후에
리스트에 담아서 리턴.
'''
file_path = "d:/py1230/애국가.txt"
'''
try:
    f = open(file_path, "r")
    text = f.read()
    print(text)
except:
    print("파일 로드 실패")
finally:
    f.close
'''

'''
- readline() 메서드는 자동으로 \n을 기준으로 하여
데이터를 줄 단위로 읽어들이기 때문에 메모리 부담을
줄일 수 있습니다.
'''
    
'''
try:
    f = open("d:/py1230/애국가.txt", "r")
    while True:
        text = f.readline()
        if len(text) == 0: break
        print(text)
except:
    print("파일 로드 실패")
finally:
    f.close    
''' 

'''
- readlines()는 파일 데이터를 한줄씩 읽어서 리스트에
담아 리턴하기 때문에 읽은 데이터를 리스트 문법을 통해
처리할 수 있습니다.
'''   
    
try:
    f = open(file_path, "r")
    text = f.readlines()
#     print(text)
    text.reverse() # 역순 정렬
    for t in text:
        print(t, end="")
        
except:
    print("파일 로드 실패")
finally:
    f.close    
    
    
    
    
    
    
    
    
    
    
    
    