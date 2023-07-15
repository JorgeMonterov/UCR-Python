from api import *
from ids import elem
import time

usuarios = elem

star_time=time.time()
for user_id in usuarios:
    
    result = getOneUser(user_id)
    print(result)

duration=time.time()-star_time
print(duration)
