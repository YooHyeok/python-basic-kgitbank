
# 삼각형 별 피라미드 그리기.
'''
*
**
***
****
*****
'''

for x in range(1,6):  #[1,2,3,4,5]
    for y in range(x):#range(0,1,1)-> [0]
        print("*",end="")
    print()
    
print("_" * 40)

'''
*****
****
***
**
*
'''

for x in range(1,6):
    for y in range(6-x): #range(0,5,1) -> [0,1,2,3,4]
        print("*",end="")
    print()

print("_" * 40)

'''
    *
   **
  ***
 ****
*****
'''

for x in range(1,6):
    for y in range(5-x):
        print(" ",end="")
    for y in range(x):
        print("*", end="")
    print()
    
print("_" * 40)

'''
*****
 ****
  ***
   **
    *
'''

for x in range(1,6):
    for y in range(x-1):
        print(" ", end="")
    for y in range(6-x):
        print("*", end="")
    print()

print("_" * 40)

'''
    *
   ***
  *****
 *******
*********
'''

for x in range(1,6):
    for y in range(5-x):
        print(" ", end="")
    for y in range(x*2-1):
        print("*", end="")
    print()
    
print("_" * 40)

'''
*********
 *******
  *****
   ***
    *
'''
    
for x in range(1,6):
    for y in range(x-1):
        print(" ", end="")
    for y in range(11-x*2):
        print("*", end="")
    print()
       
    
    
    
    
    
    
    
    
    
    
    
    
    

