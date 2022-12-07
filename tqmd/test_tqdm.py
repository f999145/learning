from tqdm import tqdm, trange
from time import sleep

data = list(range(10))
# print(data)
for item in tqdm(data,  desc='privet'):
    for i in trange(0,10,1, ascii=True):
        sleep(0.1)