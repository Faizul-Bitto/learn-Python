my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i = 0
while i < 3:
    for j in my_list:
        if j == "Monday":
            continue
        print(j)
    i += 1
