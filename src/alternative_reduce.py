#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_paths',nargs='+',required=True)
parser.add_argument('--keys',nargs='+',required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

total = defaultdict(lambda: Counter())
for path in args.input_paths:
    with open(path) as f:
        tmp = json.load(f)
        for k in tmp:
            if k in args.keys:
                total[k][path[21:26]] += sum(tmp[k].values())
fig, ax = plt.subplots()
for k in total.keys():
    ax.plot(total[k].keys(),total[k].values(),label = f'{k}')

# counts = list(total.values())
plt.savefig('lineplot.png')
