def fibonacci_sum_evens():
    first = 1
    second = 2
    sum = 0
    while second < 4000000:
        if second % 2 == 0:
            sum += second
        temp = second
        second += first
        first = temp
    return sum



print(fibonacci_sum_evens())