from indeed import get_all_jobs as get_indeed_jobs
from stackoverflow import get_all_jobs as get_so_jobs
from save import save_as_csv
from bs4 import BeautifulSoup
import requests


try:
    indeed_jobs = get_indeed_jobs()
    so_jobs = get_so_jobs()
    jobs = indeed_jobs + so_jobs

    file_stream = save_as_csv( jobs )
    file_stream.close()
    
    # jobs = indeed_jobs
    # print(jobs)
    # print('Hello')
except Exception as e:
    print(e)
finally:
    print('Done...')