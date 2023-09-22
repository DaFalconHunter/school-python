print("************** WELCOME TO THE TIME TABLES GRINDER **************")
print("This TORUROUS GRIND will drill those time tables into your lousy mind!")

table = int(input("Enter your chosen times table: "))
if type(table) != "int":
    table = int(input("Can't you just enter a table? Enter it: "))

right_qs_count = 0
right_qs_list = []
wrong_qs_count = 0
wrong_qs_list = []
for i in range(0, table):
    for j in range(0, 13):
        response = input(f"{table} × {j} = ")

        if response.lower() == "done":
            table += 1
            break
        elif response.lower() == "finished":
            break

        calc = int(response)
        if calc == (table * j):
            right_qs_count += 1
            right_qs_list.append(f"{table} * {j} = {calc}")
        else:
            wrong_qs_count += 1
            wrong_qs_list.append(f"{table} * {j} = {calc}")
        
