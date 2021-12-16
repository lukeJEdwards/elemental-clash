import time

def get_dt(previous_time:float, target_fps:int) -> tuple[float, float]:
    """get delta time.
    
    calculates delta time by finding the difference between the previous time
    and current time, then multiplies the difference by the target fps.

    Args:
        previous_time (float): the last time dt was calculated.
        target_fps (int): the target fps for the game.

    Returns:
        tuple[float, float]: the delta time and last update time.
    """
    now: float = time.time()
    last_updated: float = now - previous_time
    dt:float == last_updated * target_fps
    return dt, last_updated