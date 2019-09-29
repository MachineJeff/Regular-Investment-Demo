'''
@author : yichao.li
@time : 2019-09-28
@description : Reguale investment DEMO
'''
import csv
import argparse
from run_fix import run_fix
from run_covering import run_covering
from plot import plot
from pandas.core.frame import DataFrame

########################################################################################
# Read data

file = 'data/000001.csv'

data = []
time = []
with open(file, 'r') as fp:
    reader = csv.reader(fp)
    next(reader)
    for line in reader:
        times = line[0]
        index = line[3]
        data.append(float(index))
        time.append(times)

# One year include about 244 trading days
# Because the name of index is SSE_Composite_Index
# I only choose the last 5 years data to make demo
timeseries = 244 * 5
j = timeseries

SSE_Composite_Index = []
Time_Label = []
while(j >= 0):
    SSE_Composite_Index.append(round(data[j], 2))
    temp = time[j].split("/")
    newtime = '-'.join(temp)
    Time_Label.append(newtime)
    j -= 1

data = {"time":Time_Label,
        "index":SSE_Composite_Index}
data = DataFrame(data)
########################################################################################

########################################################################################
# Draw the picture of SSE_Composite_Index

# plot(data, path = 'pics/SSE.png')


########################################################################################


def run(args):
    if(args.strategy == 'fix'):
        run_fix(args, data)
    else:
        run_covering(args, data)


def main():
    parser =argparse.ArgumentParser()
    parser.add_argument('--strategy', default = 'fix')
    parser.add_argument('--start_time', default = '2016-1-1')
    parser.add_argument('--interval', type = int, default = 5)
    parser.add_argument('--money', type = float, default = 1000.00)
    parser.add_argument('--duration', type = int, default = 1)

    args = parser.parse_args()
    accepted_strategy = ['fix', 'covering']
    if(args.strategy not in accepted_strategy):
        raise Exception('Not accepted strategy, please choose one of them in \"fix\" or \"covering\"')
    else:
        run(args)

if __name__ == '__main__':
    main()


