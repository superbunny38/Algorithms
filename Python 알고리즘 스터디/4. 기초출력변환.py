#4. 기초-출력 변환

'''
#31 10진수를 입력받아 8진수(octal)로 출력해보자

octal = int(input())
print(oct(octal)[2:])

#32
hexa = int(input())
print(hex(hexa)[2:])


#33** 10진수 입력후 16진수를 대문자로 출력

hexa = int(input())
hexConv = hex(hexa)[2:]
print(hexConv.upper())
#print(hex(hexa)[2:].upper())



#34*****
#10진수로 변환하고자 할 때는 int()를 이용하면 된다.
#첫번째 파라미터로는 변환하고자하는 숫자의 문자열('0o12')을,
#두번째 파라미터로는 첫번째 값이 몇 진수인지를 정수로 입력하면 된다

octal = '0o' + input()
print(int(octal,8))


#35
#16진수로 입력된 정수 1개를 8진수로 바꾸어 출력해보자
#Tip:
#16진수 >> 10진수 >> 8진수 순서대로 변환

hexadecimal = '0x' + input()
integer = int(hexadecimal, 16)
print(oct(integer)[2:])


#36***아스키->정수
askii = input()
print(ord(askii))



#37***정수->아스키

askii = int(input())
print(chr(askii))

'''













