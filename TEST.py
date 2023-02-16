import time

# Boucle de 5 secondes
start_time = time.time()
i = 0
while (time.time() - start_time) < 5:
    print(i)
    i += 1


