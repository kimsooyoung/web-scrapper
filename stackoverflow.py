from bs4 import BeautifulSoup
import requests

# https://stackoverflow.com/jobs?q=python&sort=i&pg=2

URL = 'https://stackoverflow.com/jobs?q=python&sort=i'

def get_last_page():
    python_job = requests.get( URL )
    soup = BeautifulSoup( python_job.text, 'html.parser' )
    pagination = soup.find('div', { 'class': 'pagination' }).find_all('a')
    last_page =int(pagination[-2].text.strip())
    return last_page

def get_job_info( html ):
    # title = html.find('div', { 'class': '-title' }).find('h2').find('a')['title']
    title = html.find('a', { 'class': 'job-link' }).text
    title = str(title).strip()

    company, location = html.find('div', { 'class': '-company' }).find_all('span', recursive=False)
    company = company.get_text(strip= True)
    location = location.get_text(strip=True).strip('-').strip()

    id = html['data-jobid']
    link = f'https://stackoverflow.com/jobs/{id}'

    job_obj = { 
        'title': title, 
        'company': company,
        'location': location,
        'link': link
    }
    return job_obj

def get_job_data( last_page ):
    jobs = []
    for page in range(last_page):
        print( f'Now Scrapping StackOverflow page : {page+1}' )
        page_html = requests.get( URL + f'&pg={page+1}' )
        soup = BeautifulSoup( page_html.text, 'html.parser' )
        page_data = soup.find_all( 'div', { 'class': '-job' } )
        for data in page_data:
            job = get_job_info(data)
            jobs.append(job)
    return jobs


def get_all_jobs( ):
    last_page = get_last_page()
    all_jobs = get_job_data(last_page)
    return all_jobs
