import time

#Function to measure time complexity of non-recursive algorithm
#using step-counting method
def step_count_non_recursive(func,*args,**kwargs):
    start_time=time.time()
    print("st_recursive",start_time)
    result=func(*args,**kwargs)
    end_time=time.time()
    elapsed_time=end_time-start_time
    return elapsed_time,result

#function to measure time complexity of recursive algorithm
#using step-counting method
def step_count_recursive(func,*args,**kwargs):
    start_time=time.time()
    print("st_nonrecursive",start_time)
    result=func(*args,**kwargs)
    end_time=time.time()
    elapsed_time=end_time-start_time
    return elapsed_time,result
#Non-recursive function (linear search)
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1

#Recursive function (factorial)
def factorial(n):
    #base case step
    if n==0:
        return 1
    #recursive step
    else:
        return n * factorial(n-1)

#Test cases
data=list(range(1000))
target_value=999

#Analyze non-recursive algorithm
time_non_recursive,result_non_recursive=step_count_non_recursive(linear_search,data,target_value)
print(f"Non_recursive(linear_search):")
print(f"Elapsed time:{time_non_recursive:.6f}seconds")
print(f"Result:{result_non_recursive}")

#Analyze recursive algorithm
num=10
time_recursive,result_recursive=step_count_recursive(factorial,num)
print(f"\nRecursive(factorial):")
print(f"Elapsed time:{time_recursive:.6f}seconds")
print(f"Result:{result_recursive}")

 


