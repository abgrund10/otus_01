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
    if os.path.isdir(args.path):
        cwd = os.getcwd()
        new_way = cwd + "/" + args.path
        new_file = find('*.log', args.path)
        os.chdir(new_way)
        for f in new_file:
            Parsing_file.parsing_file(f)
    elif os.path.isfile(args.path):
        os.chdir(os.path.dirname(args.path))
        filename = os.path.basename(args.path)
        Parsing_file.parsing_file(filename)
    else:
        raise Exception("Please check path to your file")


if __name__ == "__main__":
    main()
