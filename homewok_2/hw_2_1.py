my_list = [(-2 + 3j), 3, 4.4, False, [5, 6], {5: 'five', 6: 'six'}, range(6)]
for i, val in enumerate (my_list, 1):
    print(f"{i}) {val} - {type(val)}")

