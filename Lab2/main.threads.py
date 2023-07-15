from concurrent.futures import ThreadPoolExecutor
from api import *
from ids import elem
import time

usuarios = elem

start_time = time.time()

with ThreadPoolExecutor() as executor:
    results = executor.map(getOneUser, usuarios)
    for result in results:
        print(result)

duration = time.time() - start_time
print(duration)