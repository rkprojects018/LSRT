import re
from datetime import datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup as bs, Tag
import json

college_map = {
    'computing': 2,
    'design': 1,
    'engineering': 3,
    'sciences': 6,
    'ivan': 4,
    'multi': 7,
    'business': 5,
    'all': 'TOTAL'
}


def main():
    year = 2006
    cur_year = datetime.now().year
    college_code = college_map['computing']

    out_file = "data.json"
    avg_file = "avg.json"

    f = open(out_file,'w')

    salaries = {}

    while year < cur_year:
        year_sals = []
        for term in ['02','05','08']:
            url = f'''https://webapps.gatech.edu/cfcampus/adors/commencement/salary_report_result.cfm?termcode={year}{term}&college={college_code}&level=1&surveyid=105&Submit=Submit'''
            res: requests.Request = requests.get(url)
            soup: bs = bs(res.content, "lxml")
            salary = soup.find_all('td')[34].string
            if salary[0] == '$':
                stripped = re.sub("[^0-9\.]", "", str(salary))
                year_sals.append(float(stripped))
        avg = sum(year_sals)/(len(year_sals))
        salaries[year] = (year_sals, avg)
        year += 1
    f.write(json.dumps(salaries))
    f.close()


if __name__ == '__main__':
    main()
