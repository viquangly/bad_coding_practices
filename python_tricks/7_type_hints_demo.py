
import functools
import pandas as pd

from typing import List


# Show this in Spyder
def merge_many(dfs: List[pd.DataFrame], **kwargs) -> pd.DataFrame:
    return functools.reduce(
        lambda x, y: pd.merge(x, y, **kwargs), dfs
    )
