
nums = list(range(5))
x1, x2, x3, x4, x5 = nums
x1
x2
x3
x4
x5

first_only, *not_needed = nums
first_only
not_needed

*also_not_needed, last_only = nums
also_not_needed
last_only

first, *middle, last = nums
first
middle
last

first, second, *remaining, last = nums
first
second
remaining
last