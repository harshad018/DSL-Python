n = int(input("Enter the total number of machines(including master): "))


clocks = []
sum_time = 0


for i in range(n):

    t = int(input(f"Enter the time for Machine {i} in seconds: "))

    clocks.append(t)

    sum_time += t

avg = sum_time//n

for i in range(n):
    offset = avg - clocks[i]

    print(f"machine {i} is adjusted with {offset:+d} seconds")
    clocks[i]+=offset

for i in range(n):

    print(f"machine {i} new time is {clocks[i]}")