import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import time
import random
from my_decorator import my_decorator
from io import BytesIO
from zipfile import ZipFile, ZIP_DEFLATED

"""
https://medium.com/dev-bits/ultimate-guide-for-working-with-i-o-streams-and-zip-archives-in-python-3-6f3cf96dca50

"""

def always_load():
    # изменение рабочего каталога
    file_name = os.path.basename(__file__)
    cwd = os.path.abspath(__file__).replace(file_name, '')
    os.chdir(cwd)

    global url, host, headers
    url = 'http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie'
    host = '/'.join(url.split(sep='/', maxsplit=3)[:3])
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
    }
    

@my_decorator
def save_index_html():
    
    req = requests.get(url=url, headers=headers)
    src = req.text

    # создаем буфер в оперативной памяти, где будем формировать зип файл
    buf = BytesIO()
    
    # создаем в этом буфере зип-файл на запись
    with ZipFile(buf, 'w', compression=ZIP_DEFLATED, compresslevel=1) as file:
        # создаем еще один буфер и открываем его на запись
        with BytesIO() as html_buf:
            # записываем в него данные в двоичном коде
            html_buf.write(src.encode())
            # переводим указатель буфера на начало
            # html_buf.seek(0)
            # Записываем буфер с файлом в буфер фип-файла
            file.writestr(zinfo_or_arcname='index.html', data=html_buf.getbuffer())
    
    # Записываем буфер зип-файла в файл в бинарном режиме
    with open('zipfile.zip', 'wb') as file:
        file.write(buf.getbuffer())            

def open_in_zip():
    with ZipFile('zipfile.zip') as zfile:
        with zfile.open('index.html') as file:
            src = file.read().decode('utf-8')
    print(src) 
 
if __name__ == '__main__':
    always_load()
    # save_index_html()
    # open_in_zip()