import random
import pandas as pd
import numpy as np
import cProfile
import pstats
import time
from io import StringIO
from functools import wraps


raw_data = {k: random.randint(1, 200) for k in range(30)}
data = [raw_data for i in range(100000)]
df = pd.DataFrame.from_dict(data)
num_iter = 10000


def timeit_deep(f):
    ''' This decorator will show all timings for
        all the methods called within a function'''
    @wraps(f)
    def estimate_time(*args, **kwargs):
        print(f'Timings for function={f.__name__}')
        profiler = cProfile.Profile()
        profiler.enable()
        profiler.runcall(f, *args, **kwargs)
        profiler.disable()
        output = StringIO()
        stats = pstats.Stats(
            profiler,
            stream=output
        ).sort_stats('cumulative')
        stats.print_stats(10)
        print(output.getvalue())

    return estimate_time


# Example of usage

@timeit_deep
def look_for_df(df: pd.DataFrame):
    for i in range(num_iter):
        df.loc[10][10]


@timeit_deep
def look_for_list(data):
    for i in range(num_iter):
        data[10][10]


print(f'dataframe access timetable')
look_for_df(df)

print(f'list access timetable')
look_for_list(data)