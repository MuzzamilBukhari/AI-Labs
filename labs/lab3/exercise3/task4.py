import time

curr_time = time.time()

print(curr_time)

actual_time = time.ctime(curr_time)
print(actual_time)

print(time.ctime())

time.sleep(3)

print('3 seconds complete')