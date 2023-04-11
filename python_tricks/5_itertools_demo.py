
import itertools

list(itertools.chain(list('abc'), list('def'), list('ghi')))

nested_lists = [[1, 2, 3], [4, 5, 6], [7, 8]]
flattened = list(itertools.chain(*nested_lists))

list(itertools.combinations(flattened, 2))
list(itertools.combinations(flattened, 3))

list(itertools.permutations(flattened, 3))

letters = list('abcd')
list(itertools.product(flattened, letters))
