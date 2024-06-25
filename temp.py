import numpy as np

data = np.random.randn(1000_000_000)

num_greater_than_4 = np.sum(data > 4)
num_greater_than_5 = np.sum(data > 5)
num_greater_than_6 = np.sum(data > 6)

print(f'4 이상인 값의 개수: {num_greater_than_4}')
print(f'5 이상인 값의 개수: {num_greater_than_5}')
print(f'6 이상인 값의 개수: {num_greater_than_6}')