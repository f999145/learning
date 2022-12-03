import requests
from bs4 import BeautifulSoup
import json
import pandas as pd
import os
import time
import random
from my_decorator import my_decorator
import io
from zipfile import ZipFile, ZIP_DEFLATED

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

    with ZipFile(file='zipfile.zip', mode='w', compression=ZIP_DEFLATED, compresslevel=1) as file:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(src)
        with open('index2.html', 'w', encoding='utf-8') as f:
            f.write(src)
        file.write('index.html')
        file.write('index2.html')

@my_decorator    
def open_in_zip():
    with ZipFile('zipfile.zip') as zfile:
        with zfile.open('index.html') as file:
            src = file.read().decode('utf-8')
    print(src) 


@my_decorator 
def unzip_file():
    with ZipFile('zipfile.zip') as myzip:
        myzip.extractall('data')
    
    with open('data/index.html', encoding='utf-8') as file:
        print(file.read())
    
@my_decorator   
def main():
    with open ('index.html', encoding='utf-8') as file:
        print(file.read())

if __name__ == '__main__':
    always_load()
    # save_index_html()
    open_in_zip()
    # unzip_file()
    # main()