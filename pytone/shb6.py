print("***피자 주문하는 자판기***")
size = input('피자사이즈를 선택하세요(S,M,L):').upper()
price =0
if  size =='S':
    price = 15000
elif size== 'M':
    price = 20000
elif size == 'L':
    price = 30000
print("선택한 피자의 크기",size)
print("피자가격",price,"원")