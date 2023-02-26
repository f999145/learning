from yandex_free_translate import run_translate
import pandas as pd
from os.path import join as os_path_join
from os import mkdir as os_mkdir

if __name__ == '__main__':
    df = pd.read_csv(os_path_join('data','webnovel.zip'))
    desc = (list(df['description'].values))
    description_rus = run_translate(desc)
    
    nms = (list(df['name'].values))
    name_rus = run_translate(nms)
    
    test = df.copy()
    test.insert(1, 'name_rus', name_rus)
    test.insert(len(test.columns), 'description_rus', description_rus)
    print(test.info())
    
    name = 'webnovel_rus_name'
    try:
        os_mkdir(os_path_join('data'))
    except FileExistsError as ex:
        pass
    test.to_csv(
        os_path_join('data', f'{name}.zip'), 
        index=False,
        compression={'method':'zip', 'archive_name':f'{name}.csv'}
        )