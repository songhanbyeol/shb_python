#--팁 계산기--
#총 얼마를 주문했을까?
#팁은 몇%
#팁을 포함해서 총 얼마를 내야할까?
#몇명이 지불 해야될까?
#1인당 지불 금액은?

print("팁 계산기!")

order=float(input("총 얼마를 주문했을까?"))
tip= int(input("팁을 얼마나 주면 좋을까? 10, 12,or,15?"))
people =int(input("몇몇이서 나눠서 낼까?"))

tip_as_percent = tip/100
total_tip = order * tip_as_percent
total_bill = total_tip + order
bill_per_person = total_bill / people
final_bill = round(bill_per_person, 2)
print(f"팁 포함해서 각자 내야되는 금액은:{final_bill}$")