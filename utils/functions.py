import time

__all__ = ['get_dt']

def get_dt(previous_time:float) -> tuple[float, float]:
    if previous_time > 0:  return time.time() - previous_time, time.time()
    else: return 0, time.time()