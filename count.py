'''
@author : yichao.li
@time : 2019-09-28
@description : Reguale investment DEMO
'''
import csv
import argparse
from strategy import run_fix, run_covering
from tools import plot
from pandas.core.frame import DataFrame
import os

def read_index(args):
    file_path = os.path.join(os.getcwd(),'data')
    if(args.index == 1):
        file = os.path.join(file_path,'000001.csv')
        title = "SSE Composite Index"
    elif(args.index == 2):
        file = os.path.join(file_path,'399001.csv')
        title = "SZSE Component Index"
    elif(args.index == 3):
        file = os.path.join(file_path,'000016.csv')
        title = "SSE 50 Index"
    elif(args.index == 4):
        file = os.path.join(file_path,'399300.csv')
        title = "CSI 300 Index"
    else:
        file = os.path.join(file_path,'000905.csv')
        title = "CSI Smallcap 500 index"
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
    # I only choose the last 5 years data to make demo
    timeseries = 244 * 5
    j = timeseries

    INDEX = []
    Time_Label = []
    while(j >= 0):
        INDEX.append(round(data[j], 2))
        temp = time[j].split("/")
        newtime = '-'.join(temp)
        Time_Label.append(newtime)
        j -= 1

    data = {"time":Time_Label,
            "index":INDEX}
    data = DataFrame(data)
    # Draw the picture of INDEX
    name = title.replace(' ', '-') + '.png'
    path = os.path.join(os.getcwd(),'pics')
    plot(data, path = os.path.join(path, name), title = title)
    print("Curve of {} has saved in {}\n".format(title, os.path.join(path, name)))
    return data, title

def run(args):
    data, title = read_index(args)
    if(args.strategy == 'fix'):
        run_fix.run_fix(args, data, title)
    else:
        run_covering.run_covering(args, data, title)


def main():
    parser =argparse.ArgumentParser()
    parser.add_argument('--strategy', default = 'fix', 
        help = "For now, I have achieve two startegies for investing, \"fix\" or \"covering\".")
    parser.add_argument('--start_time', default = '2016-1-1')
    parser.add_argument('--interval', type = int, default = 5, 
        help = "It depends on you, means that how ofter do you invest. For instance, 5 means 5 trading days i.e. one week.")
    parser.add_argument('--money', type = float, default = 1000.00, 
        help = "It means that how much do you invest every investment day.")
    parser.add_argument('--duration', type = int, default = 1, 
        help = "It means that how long do you want to invest.")
    parser.add_argument('--index', type = int, default = 1, 
        help = '''It means that what index do you want to test, optional index is in [1 2 3 4 5], 
        1 refer to SSE Composite Index,    000001;
        2 refer to SZSE Component Index,   399001;
        3 refer to SSE 50 Index,           000016;
        4 refer to CSI 300 Index,          399300;
        5 refer to CSI Smallcap 500 index, 000905.''') 


    args = parser.parse_args()
    accepted_strategy = ['fix', 'covering']
    accepted_index = [1, 2, 3, 4, 5]
    if(args.strategy not in accepted_strategy):
        raise Exception('Not accepted strategy, please choose one of them in \"fix\" or \"covering\"')
    elif(args.index not in accepted_index):
        raise Exception('Not accepted index, please choose one of them in [1 2 3 4 5]')
    else:        
        run(args)

if __name__ == '__main__':
    main()


