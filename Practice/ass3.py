import multiprocessing as mp

def calculate_local_sum(chunk):

    local_sum = sum(chunk)


    print(f"{mp.current_process().name} received {chunk} and local_sum = {local_sum}")

    return local_sum

if __name__ == "__main__":

    arr = [10,20,30,40,50,60,70,80]
    print("Original Array is: ", arr)


    num_processes = 4

    chunks = [arr[i::num_processes] for i in range(num_processes)]


    with mp.Pool(processes=num_processes) as pool:
        all_sum = pool.map(calculate_local_sum,chunks)

    total = sum(all_sum)

    print(f"Intermediate sum is {all_sum}")
    print(f"Toal sum is: {total}")