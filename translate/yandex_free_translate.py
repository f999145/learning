from yandexfreetranslate import YandexFreeTranslate
import multiprocessing as mp
import pandas as pd
from os.path import join as os_path_join

def _worker(queue: str) -> str:
    if not queue:
        return ''
    yt = YandexFreeTranslate()
    text = yt.translate("en", "ru", queue)
    return text


def run_translate(lst: list[str])-> list[str]:
    with mp.Pool(mp.cpu_count()) as process:
        workreturn = process.map(_worker, lst)
    return workreturn


if __name__ == '__main__':
    pass
