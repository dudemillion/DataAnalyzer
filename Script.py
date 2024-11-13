# Getting a module to read CSV files, statistics to find median, linregress for linear trend, and argparse to make CLI.
import pandas
import statistics
from scipy.stats import linregress
import argparse
#Presetting empty dictionaries for later.
tavgdict = dict()
#Setting options to make sure every row and column displays.
pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)
#All data for each station, date, temp avg, temp max, and temp min are in this CSV. Storing it in the variable 'temperatureCSV'.
temperatureCSV = pandas.read_csv(r'C:\Users\Nick\Documents\Python Scripts\Competition Folder\3842963.csv')
# setting each value in TAVG to a seperate number.
temperatureCSV['TAVG'] = pandas.to_numeric(temperatureCSV['TAVG'], errors='coerce')
#Adding a value to the tavgdict dictionary which makes the key value "sum" and the value the sum of all the values of the tavg dictionary.
tavgsum = temperatureCSV['TAVG'].sum()
tavgdict.update({'Sum':tavgsum})
#Averaging it, and rounding to the nearest hundredth with the dropna at the end to make sure there are no NaN values. 
average = round(tavgsum / len(temperatureCSV['TAVG'].dropna()), 2)
#Adding it to the dictionary
tavgdict.update({'Average':average})
#Finding the median using statistic's median, and dropna to remove and NaN values.
median = statistics.median(temperatureCSV['TAVG'].dropna())
tavgdict.update({'Median':median})
# Finding standard deviation and rounding it to the nearest hundredth.
std_dev = round(temperatureCSV['TAVG'].std(), 2)
tavgdict.update({'standev':std_dev})
# Finding standard deviation and rounding it to the nearest hundredth.
variance = round(temperatureCSV['TAVG'].var(), 2)
tavgdict.update({'variance':variance})
#Finding skewness and rounding it to the nearest hundredth.
skewness = round(temperatureCSV['TAVG'].skew(), 2)
tavgdict.update({'skewness':skewness})
#Finding Kurtosis and rounding it to the nearest hundredth.
kurtosis = round(temperatureCSV['TAVG'].kurt(), 2)
tavgdict.update({'kurtosis':kurtosis})
#Finding Linear Trend
x = range(len(temperatureCSV['TAVG'].dropna()))  
y = temperatureCSV['TAVG'].dropna()
slope, intercept, r_value, p_value, std_err = linregress(x, y)
tavgdict.update({'linear trend': round(slope, 2)})
parser = argparse.ArgumentParser(prog='Data Analyzer', description='Calculates statistics for temperature.')
parser.add_argument('--calc', choices=['sum', 'average', 'median', 'standev', 'variance', 'skewness', 'kurtosis', 'linear trend'], required=True, help="Choose a statistic to calculate. You can use 'sum', 'average', 'median', 'standev', 'variance', 'skewness', 'kurtosis', or 'linear trend'.")
args = parser.parse_args()
if args.calc == 'sum':
    print(tavgdict.get('Sum'))
elif args.calc == 'average':
    print(tavgdict.get('Average'))
elif args.calc == 'median':
    print(tavgdict.get('Median'))
elif args.calc == "standev":
    print(tavgdict.get('standev'))
elif args.calc == "variance":
    print(tavgdict.get('variance'))
elif args.calc == "skewness":
    print(tavgdict.get('skewness'))
elif args.calc == "kurtosis":
    print(tavgdict.get('kurtosis'))
elif args.calc == "linear trend":
    print(tavgdict.get('linear trend'))