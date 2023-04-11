
import functools
import time
import pandas as pd

from datasets import ages, bp1, bp2, bp3, bp4, bp5, bp6
pd.set_option('display.max_columns', 10)


def uncached_add(x: int, y: int) -> int:
    time.sleep(3)
    return x + y


@functools.lru_cache(2)
def cached_add(x: int, y: int) -> int:
    time.sleep(3)
    return x + y


uncached_add(1, 1)

cached_add(1, 1)
cached_add(1, 2)
cached_add(1, 3)

ages
bp1
bp2
bp3
bp4
bp5
bp6

bp_flattened = pd.merge(ages, bp1, on='MEMBER')
bp_flattened = pd.merge(bp_flattened, bp2, on='MEMBER')
bp_flattened = pd.merge(bp_flattened, bp3, on='MEMBER')
bp_flattened = pd.merge(bp_flattened, bp4, on='MEMBER')
bp_flattened = pd.merge(bp_flattened, bp5, on='MEMBER')
bp_flattened = pd.merge(bp_flattened, bp6, on='MEMBER')
bp_flattened


for i, df in enumerate([ages, bp1, bp2, bp3, bp4, bp5, bp6]):
    if i == 0:
        bp_flattened_for = df
    else:
        bp_flattened_for = pd.merge(bp_flattened_for, df, on='MEMBER')
bp_flattened.equals(bp_flattened_for)


bp_flattened2 = functools.reduce(
    lambda x, y: pd.merge(x, y, on='MEMBER'),
    [ages, bp1, bp2, bp3, bp4, bp5, bp6]
)
bp_flattened2

bp_flattened.equals(bp_flattened2)
