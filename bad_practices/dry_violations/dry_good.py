
import math


def calculate_zscore(numeric_array):
    n = len(numeric_array)
    mean = sum(numeric_array) / n
    # stdev_numerator = [(x + mean) ** 2 for x in numeric_array]
    stdev_numerator = [(x - mean) ** 2 for x in numeric_array]

    stdev = math.sqrt(
        sum(stdev_numerator) / (n - 1)
    )
    return [(x - mean) / stdev for x in numeric_array]


# Good, but still some duplication in that we are calling calculate_zscore 3X)
array1 = [1, 2, 3, 4, 5, 6]
array1_zscores = calculate_zscore(array1)

array2 = [7, 8, 9, 10, 11, 12]
array2_zscores = calculate_zscore(array2)

array3 = [13, 14, 15, 16, 17, 18]
array3_zscores = calculate_zscore(array3)

# Even better - call calculate_zscore once using a loop
array1_zscores, array2_zscores, array3_zscores = [calculate_zscore(x) for x in (array1, array2, array3)]