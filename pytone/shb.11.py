print("1부터 45번까지 숫자를 입력하세요")

num1 = int(input("첫번째 숫자:"))
num2 = int(input("두번째 숫자:"))
num3 = int(input("세번째 숫자:"))
num4 = int(input("네번째 숫자:"))
num5 = int(input("다섯번째 숫자:"))
num6 = int(input("여섯번째 숫자:"))

my_nums =[num1,num2,num3,num4,num5,num6]
my_nums.sort()

print("당신이 선택한 로또 번호는" ,my_nums,"입니다.")
