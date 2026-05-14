n = int(input("Enter number of machines (including master): "))

clocks = []
sum_time = 0

print("Enter clock times (in seconds) for each machine:")

for i in range(n):
    t = int(input(f"Machine {i}: "))
    clocks.append(t)
    sum_time += t

avg = sum_time // n

print("\nCalculated Average Time:", avg, "seconds")

print("\nClock Adjustments:")

for i in range(n):
    offset = avg - clocks[i]
    print(f"Machine {i}: Adjust by {offset:+d} seconds")
    clocks[i] += offset

print("\nSynchronized Clock Times:")

for i in range(n):
    print(f"Machine {i}: {clocks[i]} seconds")