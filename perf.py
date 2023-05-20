import argparse
import logging
import time
from functools import wraps
import threading
import os
import requests  # pip install requests, # https://requests.readthedocs.io/en/latest/
import datetime
import multiprocessing
logging.basicConfig(format='%(asctime)s %(levelname)-5.5s %(message)s  (%(filename)s:%(lineno)s) [%(name)-15.15s] [%(threadName)s]', level=logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)

def timeit_and_thread(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'{datetime.datetime.now()} {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds.  Process_id:({os.getppid()}-{multiprocessing.current_process()._identity}) Thread({threading.current_thread().native_id})')
        return result
    return timeit_wrapper

@timeit_and_thread
def recover_temperature(coord):
    latitude, longitude = coord
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude:0.2f}&longitude={longitude:0.2f}&current_weather=true"
    response = requests.get(url)
    result = response.json()
    temperature = result["current_weather"]["temperature"]
    return temperature

@timeit_and_thread
def do_hard_calculation(n):
    for _ in range(20000000):
        pass
    return f"really hard calculation over {n}"

# https://towardsdatascience.com/multithreading-multiprocessing-python-180d0975ab29
if __name__ == "__main__":
    logging.info(f'Program start')
    # sequential download
    coords = [(latitude/100, 1.9) for latitude in range(4100,4110)]

    if True:
        logging.info(f'>>>>>>>>>>>>>>>>> Sequential: recover_temperature')
        for coord in coords:
            recover_temperature(coord)
        logging.info(f'<<<<<<<<<<<<<<<<< Sequential: recover_temperature (end)')

    # sequential calculation
    numbers_to_calculate = [n for n in range(0, 10)]

    if True:
        logging.info(f'>>>>>>>>>>>>>>>>> Sequential: do_hard_calculation')
        for n in numbers_to_calculate:
            do_hard_calculation(n)
        logging.info(f'<<<<<<<<<<<<<<<<< Sequential: do_hard_calculation (end)')

    # https://realpython.com/intro-to-python-threading/#join-a-thread

    import concurrent.futures
    NUM_THREADS=4
    if True:
        logging.info(f'>>>>>>>>>>>>>>>>> Thread({NUM_THREADS}): recover_temperature')
        with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            executor.map(recover_temperature, coords)
        logging.info(f'<<<<<<<<<<<<<<<<< Thread({NUM_THREADS}): recover_temperature (end)')

    if True:
        logging.info(f'>>>>>>>>>>>>>>>>> Thread({NUM_THREADS}): do_hard_calculation')
        with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            executor.map(do_hard_calculation, numbers_to_calculate)
        logging.info(f'<<<<<<<<<<<<<<<<< Thread({NUM_THREADS}): do_hard_calculation (end)')

    if True:
        logging.info(f'>>>>>>>>>>>>>>>>> Processes({NUM_THREADS}): recover_temperature')
        with concurrent.futures.ProcessPoolExecutor(max_workers=NUM_THREADS) as executor:
            executor.map(recover_temperature, coords)
        logging.info(f'<<<<<<<<<<<<<<<<< Processes({NUM_THREADS}): recover_temperature (end)')

    if True:
        logging.info(f'>>>>>>>>>>>>>>>>> Processes({NUM_THREADS}): do_hard_calculation')
        with concurrent.futures.ProcessPoolExecutor(max_workers=NUM_THREADS) as executor:
            executor.map(do_hard_calculation, numbers_to_calculate)
        logging.info(f'<<<<<<<<<<<<<<<<< Processes({NUM_THREADS}): do_hard_calculation (end)')

    logging.info(f'Program end')
