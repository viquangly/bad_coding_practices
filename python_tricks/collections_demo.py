
from collections import deque, Counter
from copy import deepcopy


def list_pop_left(collection):
    collection = deepcopy(collection)
    while collection:
        collection.pop(0)


def list_pop_right(collection):
    collection = deepcopy(collection)
    while collection:
        collection.pop()


def deque_pop_left(collection):
    collection = deque(collection)
    while collection:
        collection.popleft()


def deque_pop_right(collection):
    collection = deque(collection)
    while collection:
        collection.pop()


collection = list(range(1000))

%%timeit
list_pop_right(collection)

%%timeit
list_pop_left(collection)

%%timeit
deque_pop_right(collection)

%%timeit
deque_pop_left(collection)


Counter('hello world')
