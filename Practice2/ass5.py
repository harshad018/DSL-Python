n = int(input("Enter the number of processes: "))\

processes = []

for i in range(n):
    processes.append(i)


token = int(input("Enter the process initially hoding the token: "))


while True:

    request = int(input("Enter the process requesting the token ( 0 to exit): "))

    if request == 0:
        print("Program has finished.")
        break

    while token != request:
        print("process", token , "passes token")
        token += 1

        if token > n:
            token = 1

    print(f"process {request} enters critical section")
    print(f"process {request} exists critical section")