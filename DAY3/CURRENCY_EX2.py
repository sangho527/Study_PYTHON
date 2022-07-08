n,k = map(int, input("금액을 입력해주세요: ").split())
result = 0

list = [1, 5, 50, 100, 500, 1000, 5000 ,10000, 50000]


for coin in list:
    result += n // coin
    n %= coin

list.sort(reverse = True)
print(('동전의 거스름돈 최소 개수는: '), result)