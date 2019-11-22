from bs4 import BeautifulSoup
import requests

RESULT_PER_PAGE = 50
URL = f'https://www.indeed.com/jobs?q=python&limit={RESULT_PER_PAGE}'

def get_last_page():
    python_job = requests.get( URL )
    soup = BeautifulSoup(python_job.text, 'html.parser')
    page_data = soup.find_all( 'span', { 'class': 'pn' } )
    last_page = int(page_data[-2].text)
    return last_page

def get_job_info( html ):
    title_div = html.find( 'div', { 'class': 'title' } ).find('a')
    title = str(title_div['title'])
    link = 'www.indeed.com/' + str(title_div['href'])

    company_div = html.find( 'span', { 'class': 'company' } )
    location_div = html.find( 'span', { 'class': 'location' } ).text
    location_div = str(location_div).strip()
    if company_div.text is None:
        company = company_div.find('a', { 'class': 'turnstileLink'}).text
    else:
        company = company_div.text

    job_obj = { 
        'title': title, 
        'company': str(company).strip(),
        'location': location_div,
        'link': link
    }
    # print(job_obj)
    return job_obj

def get_job_data( last_page ):
    jobs = []
    for page in range(last_page):
        print( f'Now Scrapping Indeed page : {page+1}' )
        page_html = requests.get( URL + f'&start={page*50}' )
        soup = BeautifulSoup(page_html.text, 'html.parser')
        page_data = soup.find_all( 'div', { 'class': 'jobsearch-SerpJobCard' } )
        for data in page_data:
            job = get_job_info(data)
            jobs.append(job)
    return jobs

def get_all_jobs( ):
    last_page = get_last_page()
    all_jobs = get_job_data(last_page)
    return all_jobs