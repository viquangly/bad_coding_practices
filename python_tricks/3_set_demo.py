
big_list = list(range(1_000_000))
big_set = set(big_list)

%%timeit
500_000 in big_list

%%timeit
500_000 in big_set

