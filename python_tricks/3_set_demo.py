
big_list = list(range(1_000_000))
big_set = set(big_list)

%%timeit
500_000 in big_list

%%timeit
500_000 in big_set

bills = {'Josh Allen', 'Jordan Poyer', 'Stefon Diggs', 'Micah Hyde', 'Sean McDermott', 'Damar Hamlin'}
golfers = {'Josh Allen', 'Jordan Poyer', 'Stefon Diggs', 'Tiger Woods', 'Jack Nicklaus', 'Kevin Chang', 'Tyler Rinker'}

bills - golfers
golfers - bills

bills.intersection(golfers)
bills & golfers

bills.union(golfers)
bills | golfers

bills.symmetric_difference(golfers)

