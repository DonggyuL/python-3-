# def 함수이름(매개변수):
# 실행할 명령
# return 반환값

# gotcha 매개변수x, 반환값x
def gotcha():
    print("잡았다")

gotcha()

# add 매개변수 2개, 반환값 o
def add(num1, num2):
    return num1+num2

print(add(1,3))

# add_mul 매개변수o, 반환값 2개
def add_mul(num1, num2):
    return num1+num2, num1*num2

print(add_mul(2, 4))

# attack 매개변수o, 반환값x
def attack(name):
    print(name,"100만볼트")

attack("pikachu")

# practice
def add(num1, num2):
    print(num1 + num2)
    return num1-num2

add(1,3)
print(add(1,3))
