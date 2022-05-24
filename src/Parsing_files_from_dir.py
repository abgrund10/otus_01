import argparse
import os

import Parsing_file

parser = argparse.ArgumentParser(description='Process access.log')

parser.add_argument('--target', action='store')
args = parser.parse_args()

target_files = []

if os.path.isfile(args.target):
    target_files.append(args.target)

for target_file in target_files:
    print(target_file)
    ff = Parsing_file(target_file)
