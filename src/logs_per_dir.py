import argparse
import os

import parse_single_log

parser = argparse.ArgumentParser(description='Process access.log')

parser.add_argument('--target', dest='target', action='store')
args = parser.parse_args()

target_files = []

if os.path.isfile(args.target):
    target_files.append(args.target)
else:
    files = os.listdir(args.target)
    for item in files:
        if item.endswith(".log"):
            target_files.append(os.path.join(args.target, item))

for target_file in target_files:
    parse_single_log(target_file)