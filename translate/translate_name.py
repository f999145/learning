from yandex_free_translate import run_translate
import pandas as pd
from os.path import join as os_path_join

if __name__ == '__main__':
    df = pd.read_csv(os_path_join('data','webnovel.zip'))
    test = (list(df['name'].values))
    name_rus = run_translate(test)