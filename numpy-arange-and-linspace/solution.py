import numpy as np

def make_range(start: float, stop: float, step: float) -> np.ndarray:
    """
    Return an array of values from `start` up to (but not
    including) `stop`, incrementing by `step`, using np.arange.
    """
    return np.arange(start, stop, step)

def make_evenly_spaced(start: float, stop: float, count: int) -> np.ndarray:
    """
    Return an array of exactly `count` evenly-spaced values from
    `start` to `stop`, inclusive of both endpoints, using
    np.linspace.
    """
    return np.linspace(start, stop, count)

def compare_arange_linspace(start: float, stop: float, step: float) -> dict:
    arange_result = np.arange(start, stop, step)
    linspace_result = np.linspace(start, stop, len(arange_result))
    return {
       "arange_result": arange_result,
       "linspace_result": linspace_result,
       "arange_includes_stop": stop in arange_result,
       "linspace_includes_stop": stop in linspace_result
     }
