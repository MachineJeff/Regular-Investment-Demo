'''
@author : yichao.li
@time : 2019-09-28
@description : Reguale investment DEMO
'''
import csv
import argparse
import matplotlib.pyplot as plt
from run_fix import run_fix
from run_covering import run_covering

########################################################################################
# Read data

file = '000001.csv'
timeseries = 5 * 240

data = []
with open(file, 'r') as fp:
	i = 0
	reader = csv.reader(fp)
	for line in reader:
		line = float(line[0])
		if(i < timeseries):
			data.append(line)
			i += 1
j = len(data) - 1

# because the name is of index is SSE_Composite_Index
# I only choose the last 5 years data to make demo
SSE_Composite_Index = []
while(j >= 0):
	SSE_Composite_Index.append(data[j])
	j -= 1
########################################################################################

def run(args):
	if(args.strategy == 'fix'):
		run_fix(args, SSE_Composite_Index)
	else:
		run_covering(args, SSE_Composite_Index)

def main():
	parser =argparse.ArgumentParser()
	parser.add_argument('--strategy', default = 'fix')
	parser.add_argument('--start_time', type = int, default = 240 * 4)
	parser.add_argument('--interval', type = int, default = 5)
	parser.add_argument('--money', type = float, default = 1000.00)
	parser.add_argument('--duration', type = int, default = 240 * 1)

	args = parser.parse_args()
	accepted_strategy = ['fix', 'covering']
	if(args.strategy not in accepted_strategy):
		raise Exception('Not accepted strategy, please choose one of them in \"fix\" or \"covering\"')
	else:
		run(args)

if __name__ == '__main__':
	main()




