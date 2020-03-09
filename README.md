# Python Profiling Decorator

This is a simple python profiling decorator. Whatever function you decorate - it will show you the full timing stats for all the sub-function calls.

Example:

```
   Ordered by: cumulative time
   List reduced from 157 to 10 due to restriction <10>

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.088    2.088 /usr/local/lib/python3.8/cProfile.py:106(runcall)
        1    0.036    0.036    2.088    2.088 /home/ivan/GIT/timing_decorator/timing_decorator.py:46(look_for_df)
    10000    0.014    0.000    1.751    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/indexing.py:1753(__getitem__)
    10000    0.034    0.000    1.733    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/indexing.py:1901(_getitem_axis)
    10000    0.011    0.000    1.458    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/indexing.py:614(_get_label)
    10000    0.070    0.000    1.446    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/generic.py:3415(xs)
    10000    0.070    0.000    1.213    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/series.py:183(__init__)
    10000    0.039    0.000    0.686    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/construction.py:388(sanitize_array)
    10000    0.028    0.000    0.533    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/construction.py:506(_try_cast)
    10000    0.024    0.000    0.305    0.000 /usr/local/lib/python3.8/site-packages/pandas/core/internals/managers.py:1467(__init__)



func result
list access timetable
Timings for function=look_for_list
         5 function calls in 0.000 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 /usr/local/lib/python3.8/cProfile.py:106(runcall)
        1    0.000    0.000    0.000    0.000 /home/ivan/GIT/timing_decorator/timing_decorator.py:54(look_for_list)
        1    0.000    0.000    0.000    0.000 {method 'enable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
```