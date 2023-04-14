import time
import requests
from bs4 import BeautifulSoup


def find_jobs():
    html_text = requests.get(
        'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=C%2B%2B&txtLocation=').text
    val1, val2 = input("Enter your skill: ").split()
    soup = BeautifulSoup(html_text, 'lxml')
    headings = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    for index, comps in enumerate(headings):
        span = comps.find('span', class_='sim-posted').span.text
        skills = comps.find('span', class_='srp-skills').text
        more_info = comps.header.h2.a['href']
        if val1 in skills or val2 in skills:
            comp_name = comps.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            pay = comps.find_all('li')
            with open(f'Posts/{index}.txt', 'w') as f:
                if '₹' in pay[1].text.split()[0]:
                    f.write(f'{comp_name.strip()} is paying {pay[1].text.strip()}, find more at : {more_info}')
                else:
                    f.write(f'{comp_name.strip()} with no valid payout written, find more at : {more_info}')
            print(f'File saved as {index}.text')
        else:
            continue


if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 0.1
        print(f'waiting for {time_wait} minutes.....')
        time.sleep(time_wait * 60)
