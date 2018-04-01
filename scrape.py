#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib.request as urllib2
import re

import csv

data = 'salaries.csv'

term = ['200608', '200702', '200708', '200802', '200808', '200902', '200908', '201002', '201008',
        '201102', '201108', '201202', '201205', '201208', '201302', '201305', '201308', '201402',
        '201405', '201408', '201502', '201505', '201508', '201602', '201605', '201608', '201702',
        '201705', '201708']
year_term = {'2006': '200608', '2007': '200702,200708', '2008': '200802,200808', '2009': '200902,200908',
             '2010': '201002,201008', '2011': '201102,201108', '2012': '201202,201205,201208',
             '2013': '201302,201305,201308', '2014': '201402,201405,201408',
             '2015': '201502,201505,201508', '2016': '201602,201605,201608', '2017': '201702,201705,201708'}


def scrape():
    salaries = []

    for i in year_term:

        if i[:4] in i:

            page_src = urllib2.urlopen("https://webapps.gatech.edu/cfcampus/adors/commencement/salary_report_result.cfm?termcode=" + year_term[i] + "&college=2&level=1&surveyid=105&Submit=Submit").read()
            soup = BeautifulSoup(page_src, 'html.parser')
            salary = soup.findAll("td")[34]
            strip = re.sub(r"[^\w]", "", str(salary))
            print(strip)

            #if '' != strip:
                #salaries += [float(strip)]

    #avg = sum(salaries) / (len(salaries))
    #with open(data, 'a') as f:
    #   f.write(str(avg) + '\n')





def main():
    scrape()

if __name__ == '__main__':
  main()
