def calculatePay():
    # Implement your solution in between the two comment blocks
    print("calculating pay")
    # This first line is provided for you
    hours = float(input("Enter Hours:"))
    hourly_rate = float(input('Enter Rate:'))
    
    total_pay = (hours * hourly_rate)

    print(total_pay)
    



    # end assignment


## If you want to test locally before you try to sync
## Open your terminal and run > python payCalculator.py

#Ignore this for now. 
if __name__ == "__main__":
    calculatePay()
