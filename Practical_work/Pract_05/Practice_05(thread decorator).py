from threading import Thread
import time
import os
from datetime import datetime
import urllib.request
from urllib.parse import urlparse


def dec_thread(func, **t_kwargs):

    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func_started = Thread(target=func, args=args, kwargs=kwargs, **t_kwargs)
        print(f'[{datetime.strftime(datetime.now(), "%H:%M:%S")}] Start {func_started.name} exec function {str(func.__name__).upper()}, {args[0]}')
        func_started.start()
        print(f'[{datetime.strftime(datetime.now(), "%H:%M:%S")}] Completed {func_started.name}, time taken: [{round((time.perf_counter()  - start_time) * 1000, 3)} milliseconds]'
              f' thread deamon? = {func_started.isDaemon()}')
        return func_started
    return wrapper


def download(urls):
    paces_imag = urlparse(urls)
    name_pic = os.path.basename(paces_imag.path)
    urllib.request.urlretrieve(urls, name_pic)


url_list = ['http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/batchnorm.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/dany.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/new2_dropout.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/new_gatis.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/bias.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/pattern-recognition.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/minimum.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/batches.jpeg',
            'https://alexanderdyakonov.files.wordpress.com/2018/08/hackaton2.jpeg',
            ]
for ind, dir_url in enumerate(url_list):
    name_ = f'Thread: {ind+1}'
    if ind in (5, 7):
        deamon_ = True
    else:
        deamon_=False
    dec_thread(download, name=name_, daemon=deamon_)(dir_url)