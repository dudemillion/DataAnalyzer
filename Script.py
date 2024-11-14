import pandas as pd
import statistics
import argparse
from scipy.stats import linregress

# presetting empty dictionaries for later.
tavgdict = dict()

# function to read the CSV file and process the data.
def load_data(file_path):
    temperatureCSV = pd.read_csv(file_path)
    temperatureCSV['TAVG'] = pd.to_numeric(temperatureCSV['TAVG'], errors='coerce')
    return temperatureCSV

# function to calculate sum
def calculate_sum(data):
    return data.sum()

# function to calculate average
def calculate_average(data):
    return round(data.sum() / len(data.dropna()), 2)

# function to calculate median
def calculate_median(data):
    return statistics.median(data.dropna())

# function to calculate standard deviation
def calculate_std_dev(data):
    return round(data.std(), 2)

# function to calculate variance
def calculate_variance(data):
    return round(data.var(), 2)

# function to calculate skewness
def calculate_skewness(data):
    return round(data.skew(), 2)

# function to calculate kurtosis
def calculate_kurtosis(data):
    return round(data.kurt(), 2)

# Function to calculate linear trend (slope)
def calculate_linear_trend(data):
    x = range(len(data.dropna()))
    y = data.dropna()
    slope = linregress(x, y)
    return round(slope, 2)

# tavgdict values
def update_tavgdict(data):
    tavgdict.update({
        'Sum': calculate_sum(data['TAVG']),
        'Average': calculate_average(data['TAVG']),
        'Median': calculate_median(data['TAVG']),
        'standev': calculate_std_dev(data['TAVG']),
        'variance': calculate_variance(data['TAVG']),
        'skewness': calculate_skewness(data['TAVG']),
        'kurtosis': calculate_kurtosis(data['TAVG']),
        'linear trend': calculate_linear_trend(data['TAVG'])
    })

# parser for CLI.
def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='Data Analyzer', description='Calculates statistics for temperature.'
    )
    parser.add_argument(
        '--calc',
        choices=[
            'sum', 'average', 'median', 'standev', 'variance',
            'skewness', 'kurtosis', 'linear_trend'
        ],
        required=True,
        help="Choose a statistic to calculate."
    )
    return parser.parse_args()

# script execution
def main(file_path):
    data = load_data(file_path)
    update_tavgdict(data)
    args = parse_arguments()

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
    elif args.calc == "linear_trend":
        print(tavgdict.get('linear trend'))
