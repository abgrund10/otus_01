import argparse
import glob
import os.path

import Parsing_file

files = []


def main():
    parser = argparse.ArgumentParser(description='Process command line arguments.')
    parser.add_argument('indir')
    args = parser.parse_args()

    full_paths = [os.path.join(os.getcwd(), path) for path in args.indir]
    files = set()
    for indir in full_paths:
        if os.path.isfile(indir):
            files.add(indir)
        else:
            full_paths += glob.glob(indir + '/*')

    for file in files:
        Parsing_file.parsing_file(file)


if __name__ == "__main__":
    main()
