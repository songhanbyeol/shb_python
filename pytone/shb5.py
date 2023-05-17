height = input("당신의 키는 몇 m :")
weight = input("당신의 몸무게는 몇 kg :")

bmi = int (weight) / float(height)**2
bmi = round(bmi,2)
print(bmi)
2
if bmi < 18.5:
    print("당신의 저체중입니다.")
elif bmi <= 24:
    print("당신은 정상체중입니다.")
elif bmi < 30:
    print("당신은 과체중입니다")
elif bmi <= 35:
    print("당신은 비만입니다.")
else: 
    print("당신은 고도비만입니다.")