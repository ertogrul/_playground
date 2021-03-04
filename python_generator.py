def gen_nums():
    n = 0
    while n < 4:
        print('hello ' +str(n))
        yield n
        n += 1

nums = gen_nums()
print(type(nums))

for num in nums:
    print(num)


more_nums = gen_nums()

next(more_nums)
next(more_nums)
next(more_nums)