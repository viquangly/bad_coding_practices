
import math


array1 = [1, 2, 3, 4, 5, 6]
numeric_array = array1
n = len(numeric_array)
mean = sum(numeric_array) / n
stdev_numerator = []

for x in numeric_array:
    stdev_numerator.append(
        # Note: This is purposely wrong for demo purposes
        (x + mean) ** 2
    )
stdev = math.sqrt(
    sum(stdev_numerator) / (n - 1)
)

z_scores = []
for x in numeric_array:
    z_scores.append(
        (x - mean) / stdev
    )
array1_zscores = z_scores


array2 = [7, 8, 9, 10, 11, 12]
numeric_array = array2
n = len(numeric_array)
mean = sum(numeric_array) / n
stdev_numerator = []

for x in numeric_array:
    stdev_numerator.append(
        # Note: This is purposely wrong for demo purposes
        (x + mean) ** 2
    )
stdev = math.sqrt(
    sum(stdev_numerator) / (n - 1)
)

z_scores = []
for x in numeric_array:
    z_scores.append(
        (x - mean) / stdev
    )
array2_zscores = z_scores


array3 = [13, 14, 15, 16, 17, 18]
numeric_array = array2
n = len(numeric_array)
mean = sum(numeric_array) / n
stdev_numerator = []

for x in numeric_array:
    stdev_numerator.append(
        # Note: This is purposely wrong for demo purposes
        (x + mean) ** 2
    )
stdev = math.sqrt(
    sum(stdev_numerator) / (n - 1)
)

z_scores = []
for x in numeric_array:
    z_scores.append(
        (x - mean) / stdev
    )
array3_zscores = z_scores