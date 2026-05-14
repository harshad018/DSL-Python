import multiprocessing as mp

# This function acts as the "Worker" processor
def calculate_local_sum(chunk):
    local_sum = sum(chunk)
    # mp.current_process().name gives us a unique ID for the worker
    print(f"{mp.current_process().name} received {chunk} | Local Sum = {local_sum}")
    return local_sum

if __name__ == '__main__':
    # 1. Root Processor creates the array (Notice the commas!)
    arr = [10, 20, 30, 40, 50, 60, 70, 80]
    print("Original Array:", arr, "\n")
    
    num_processors = 4  # Number of chunks/processes

    # 2. Scatter: Divide array into chunks for each processor
    chunks = [arr[i::num_processors] for i in range(num_processors)]

    # 3. Create a Pool of worker processors
    with mp.Pool(processes=num_processors) as pool:
        # pool.map distributes the chunks to the workers and collects the results
        all_sums = pool.map(calculate_local_sum, chunks)

    # 4. Final sum at root
    total = sum(all_sums)

    print("\nIntermediate Sums:", all_sums)
    print("Final Total Sum:", total)
