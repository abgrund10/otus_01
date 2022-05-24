import os, fnmatch
import argparse
import glob
import os.path

import Parsing_file


def find(pattern, path1):
    result = []
    for root, dirs, files in os.walk(path1):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(name))
    return result


def main():
    files_list = set()
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('path', default=os.path.curdir)
    args = parser.parse_args()
    path0 = '/home/tank34/PycharmProjects/pythonProject1/otus_01/src/files'
    new_file = find('*.log', path0)
    os.chdir(path0)
    for f in new_file:
        Parsing_file.parsing_file(f)


if __name__ == "__main__":
    main()
