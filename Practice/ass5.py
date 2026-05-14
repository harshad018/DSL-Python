n = int(input("Enter the no of processes: "))


processes = []

for i in range(n):
    processes.append(i)

token = int(input("Enter the process intially holding the token: "))

while True:

    request = int(input("Enter the process wanting to enter the critical section( 0 to exit): "))

    if request == 0:
        print("Program ended")
        break

    while token != request:

        print("Process", token, "passes token")

        token = token + 1

        if token > n:
            token = 1

    print("process", request, "enters critical section")
    print("process", request, "exits critical section")