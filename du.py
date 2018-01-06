#!/usr/bin/env python

import argparse
import os
from os.path import join, getsize, exists, isdir
import sys

DEFAULT_BLOCK_SIZE = 512.0

KB = 1024.0
MB = 1024.0 * KB
GB = 1024.0 * MB

class BadPathException(Exception):
    pass


# you can count file size in 2 diff ways: number of blocks allocated on disk or the size of data stored in the file
def get_size(path, args):
  # obtain the number of blocks allocated in the disk for a file
  if args.e:
    size_in_b = getsize(path)
  else:
    size_in_b = os.stat(path).st_blocks * DEFAULT_BLOCK_SIZE
  # convert to appropriate units depends on user input
  if args.g:
    return size_in_b / GB
  if args.m:
    return size_in_b / MB
  if args.k:
    return size_in_b / KB
  return size_in_b / DEFAULT_BLOCK_SIZE

def compute_size(args, root):

    if not exists(root):
        raise BadPathException("Path {} does not exist".format(root))


    cur_dir_size = 0
    for name in os.listdir(root):
        path = join(root, name)
        # if current path is a directory, recurse
        if isdir(path):
            path_size = compute_size(args, path)
            # -a flag
            if args.all:
                print("{0:0.1f} \t {1}".format(path_size, path))
            cur_dir_size += path_size
            continue
        try:
            path_size = get_size(path, args)
            if args.all:
                print("{0:0.1f} \t {1}".format(path_size, path))
            cur_dir_size += path_size
        except OSError as e:
            print("Warning: Ignoring {} because of {}".format(path, e))
            # Ignore temp files that got removed or if we don't have proper permissions
            pass

    print("{0:0.1f} \t {1}".format(cur_dir_size, root))
    return cur_dir_size

def parse_args(args):
    parser = argparse.ArgumentParser(description='''The du utility displays the file system usage for each file argument and for each directory in the file hierarchy rooted in each directory argument.  If no file is speci-
     fied, the block usage of the hierarchy rooted in the current directory is displayed.''')
    parser.add_argument('-a', '--all', action='store_true',
                        help='Display an entry for each file in a file hierarchy')
    parser.add_argument('-k', action='store_true', help='Display the results in kb')
    parser.add_argument('-m', action='store_true', help='Display the results in mb')
    parser.add_argument('-g', action='store_true', help='Display the results in gb')
    parser.add_argument('-e', action='store_true', help='Use actual file size instead of block count')

    parser.add_argument('path', help='Path to a valid directory')
    
    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    compute_size(args, args.path)