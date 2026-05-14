n = int(input("Enter the number of clocks(including the master): "))

clocks = []
sum_all = 0

for i in range(n):

    t = int(input(f"Enter the time in seconds for clock {i}"))

    clocks.append(t)
    sum_all += t

avg = sum_all // n

for i in range(n):

    offset = avg-clocks[i]

    print(f"Clock {i} has the offeset of {offset:+d}")

    clocks[i]+=offset

for i in range(n):

    print(f"clock {i} has {clocks[i]} seconds")