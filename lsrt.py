#!/usr/bin/python3

'''
These lists will have to modified to take our scraped data from the excel file.
'''

import csv

'''
Our list with the years (X axis).
'''
years = [1,2,3,4,5,6,7,8,9,10]



with open('salaries.csv', 'r') as data:
  # Our list with salaries (Y axis)
  salaries = []  # adding dummy data for now
  for i in csv.reader(data):
      salaries.append(i[0])



# Summing up the Years (X)
def sumYears():
  #print(sum(years))
  return sum(years)


# Summing up the Salaries (Y)
def sumSalaries():
  #print (sum(salaries))
  return sum(salaries)

def sumSquareYears():
  squareYears = ([i**2 for i in years])
  #print (sum(squareYears))
  return sum(squareYears)

def sumYearsSalaries():
  yearsSalaries = [] #creating an empty list
  for i in range(0, len(years)):
    yearsSalaries.append(years[i]*salaries[i]) #doing the multiplication and adding it to our list
  #print(yearsSalaries)
  #print (sum(yearsSalaries))
  return sum(yearsSalaries)

def computeReg():
  '''
  SlopeEQ = (Summation of XY) - ((Summation of X)*(Summation of Y)/(Number of data points)) /
  (Summation of X^2) - ((Summation of X squared)/(Number of data points))
  '''
  partialNumerator = (sumYears() * sumSalaries()) / (float(len(years)))
  numerator = sumYearsSalaries() - partialNumerator
  partialDenominator = (pow(sumYears(),2))/(float(len(years)))
  denominator = sumSquareYears() - partialDenominator

  slope = (numerator)/(denominator)

  '''
  InterceptEQ = (Summation of Y - (Slope * Summation of X)) / (Number of data points)
  '''
  partialIntercept = slope - (sumYears())
  partialInterceptNumerator = sumSalaries() - partialIntercept
  intercept = partialInterceptNumerator / (float(len(years)))
  #print(numerator)

  #print(slope)
  #print(intercept)


  return 1


def main():
  #calling all the functions
  sumYears()
  sumSalaries()
  sumSquareYears()
  sumYearsSalaries()
  computeReg()

if __name__ == '__main__':
  main()
