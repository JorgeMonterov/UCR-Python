from api import *
from ids import elem
import time

usuarios = elem

star_time=time.time()
for user_id in usuarios:
    #llama la funcion y utilizando el diccionario de idds.
    result = getOneUser(user_id)
    print(result)
#Formula para saber el tiempo que dura
duration=time.time()-star_time
print(duration)
