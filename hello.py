print("Enter -1 to stop")
total_fare =0 
fare=0

distance = 0
while distance!=-1 :
    distance = int(input("Enter the distance to be travelled (in kms): "))
    if distance <=5 :
        fare = 10
    elif 6<=distance<=15 :
        fare = 10 + 2*(distance-5)
    elif 16<=distance<=25:
        fare=30+ 3*(distance-15)
    elif distance>25:
        fare = 60 + 5*(distance-25)
    fare = fare+100
    total_fare = total_fare+fare
    print(f"Fare for this passenger(including fee):{fare}")
    fare =0

print(f"Total Fare = {total_fare}")