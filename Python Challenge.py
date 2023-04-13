# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:35:06 2023

@author: sjnam
"""
# 조건문

#https://www.acmicpc.net/problem/1330

a,b = map(int, input().split())

if a < b:
    print('<')
elif a > b:
    print('>')
else:
    print('=')
    

#https://www.acmicpc.net/problem/9498
score = int(input('점수를 입력하세요 : '))

if 90 <= score <= 100:
    print('A')
elif 80 <= score <90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')


#https://www.acmicpc.net/problem/2753

year = int(input("연도를 입력하세요 : "))

if year % 4 == 0:
    if year % 100 != 0 or year % 400 == 0:
        print('1')
    else:
        print('0')

#https://www.acmicpc.net/problem/14681

x = float(input("x좌표를 입력하세요 : "))
y = float(input("y좌표를 입력하세요 : "))

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
elif x >= 1000 and x < -1000 and y >= 1000 and y < -1000:
    print("잘못 입력하셨습니다.")

#https://www.acmicpc.net/problem/2884

hour = float(input('시간을 입력하세요 : '))
minute = float(input('분을 입력하세요 : '))

if minute - 45 > 0:
    print(int(hour),int(minute-45))
elif minute - 45 < 0:
    hour = hour - 1
    if hour < 0:
        print(23,int(60+(minute-45)))
    else:
        print(int(hour-1),int(60+(minute-45)))


#https://www.acmicpc.net/problem/2525

hour, minute = map(int, input().split())
time = int(input())

hour = hour + (time // 60)
minute = minute + (time % 60)

if hour >= 24:
    print(hour - 24, minute)

if minute >= 60:
    hour += 1
    minute -= 60
    print(hour,minute)
    
# 반복문

#https://www.acmicpc.net/problem/2739

dan = int(input("단을 입력하세요 : "))

for i in range(1,10):
    print(dan, '*', i, '=', dan * i)

# 4/11

#https://www.acmicpc.net/problem/10950

count = int(input('테스트 케이스의 개수를 입력하세요 : '))

for i in range(count):
    A,B = map(int, input().split())
    hap = A + B
    print(hap) 

#https://www.acmicpc.net/problem/8393

number = int(input("숫자를 입력하세요 : "))
a = 0

for i in range(number + 1):
    a  += i 
    
print(a)

#https://www.acmicpc.net/problem/25304

total = int(input('총 금액을 입력하세요 : '))
count = int(input('구매한 물건 종류의 수를 입력하세요 : '))
A = 0

for i in range(count):
    price, number = map(int, input().split())
    A = A + (price*number)   
    
if A == total:
    print('Yes')
else:
    print("No")

#https://www.acmicpc.net/problem/25314

number = int(input("숫자를 입력하세요 : "))

print('long ' * int(number // 4) + 'int')

#https://www.acmicpc.net/problem/11021

number = int(input("테스트 케이스 개수를 입력하세요 : "))

for i in range(number):
    a,b = map(int, input().split())
    print(f'Case #{i+1} : {a+b}')

#https://www.acmicpc.net/problem/2438

number = int(input("숫자를 입력하세요 : "))

for i in range(number):
    print(" " * (5 - (i+1)) + '*' * (i+1), end="\n")
 
#https://www.acmicpc.net/problem/10952

while True:
    a,b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)

# 1차원 배열

cou = int(input("숫자 개수를 입력하세요 : "))

count_list = list(map(int, input().split()))

if len(count_list) > cou:
    print("너무 많이 입력했습니다.")
else:
    target = int(input("찾으려는 숫자를 입력하세요 : "))
    print(count_list.count(target))

#4/12

#https://www.acmicpc.net/problem/10871

a,b = map(int, input().split())
x = list(map(int, input().split()))
    
for i in range(a):
    if x[i] < b:
        print(x[i], end =" ")
    
#https://www.acmicpc.net/problem/10818

a = int(input("정수의 개수를 입력하세요 : "))
b = list(map(int, input().split()))

print(max(b), min(b))


#https://www.acmicpc.net/problem/2562






























