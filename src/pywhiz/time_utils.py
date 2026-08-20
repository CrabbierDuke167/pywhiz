import time


def start_timer():
    """Returns the current time in seconds."""
    return time.time()

def end_timer(start_time):
    """Calculates total time taken in seconds"""
    current = time.time()
    time_taken = current - start_time
    return round(time_taken, 2)

def t_delay(seconds):
    """Pauses the program for a few seconds."""
    time.sleep(seconds)

def t_countdown(n):
    """Prints a countdown from n to 1."""
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)