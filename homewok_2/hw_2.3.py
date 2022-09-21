month = int(input("Enter the month from 1 till 12: "))

month_dict = {1: "Jan", 2: "Feb", 3: "March", 4: "April", 5: "May", 6: "June", 7: "july", 8: "Aug", 9: "Sep", 10:
    "Oct", 11: "Nov", 12: "Dec"}

month_list =['Jan', 'Feb', 'March', 'April', 'May', 'June','July', 'Aug', 'Sep', 'Oct''Nov', 'Dec']

if month in month_dict:
    print(f"{month} - month of year - this {month_dict[month]}")
    print(f"{month} - month of year - this {month_list[month - 1]}")
else:
    print("Wrong number.")