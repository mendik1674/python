num_inst = int(input("Введите целое положительное число :"))
greatest_dig = 0
num = num_inst
while num > 0:
    digit = num % 10
    if digit < greatest_dig:
        greatest_dig = digit
        if greatest_dig == 9:
            break
    # num = num // 10
    print(f"Наибольшая цифра в числе {num_inst} равна {greatest_dig}")