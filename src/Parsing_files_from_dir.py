import os, fnmatch
import argparse
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
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('--path')
    args = parser.parse_args()
    cwd = os.getcwd()
    new_way = cwd + "/" + args.path
    new_file = find('*.log', args.path)
    os.chdir(new_way)
    for f in new_file:
        Parsing_file.parsing_file(f)


if __name__ == "__main__":
    main()
