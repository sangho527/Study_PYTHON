import time
import os
import psutil

process = psutil.Process(os.getpid())
start_time = time.time()
n = int(input('거스름돈을 가격(정수)로 입력해 주세요: '))
count = 0

array = [500, 100, 50, 10]
for coin in array:
    count += n // coin
    n %= coin
    
print("동전의 거스름돈 최소 개수는 : " , count)

end_time = time.time()
print("time:", format(end_time - start_time, '.10f'))
print('MB bytes : ', process.memory_info().rss / (1024.0 * 1024.0))

"""n = int(input('거스름돈을 가격(정수)로 입력해 주세요: '))
count = 0

array = [500, 100, 50, 10]
for coin in array:
    count += n // coin
    n %= coin
    
print('동전의 거스름돈 최소 개수는 :', count)"""