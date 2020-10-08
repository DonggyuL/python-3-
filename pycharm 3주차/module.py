# 모듈: 함수 or 변수 or 클래스 모아 놓은 파일
# import 모듈이름 or from 모듈이름
# 로또 번호 뽑기
import random

numbers = range(1,46)
# 1에서 45까지의 정수를 저장

lotto = random.sample(numbers,6)
#random.sample(a,n) : a에서 랜덤한 n개의 데이터를 추출하는 함수

print(lotto)