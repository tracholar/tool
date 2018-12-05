#!/usr/bin/env python
import os
import re
import argparse
from os.path import join


def file_type(name):
    sep = name.split('.')
    if len(sep) <= 2:
        return 'page'
    else:
        return sep[-2]



def gen_html(root):
    fs = [for f in os.listdir(root) if f not in ('.', '..') and len(f) >= 4 and f[-4:] == '.html']
    for f in fs:
        if file_type(f) == 'page':
            ctx = open(join(root, f)).read()
            includes = re.findall(r'{include (.+)}')
            print includes
            
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Web Tool')
    
    gen_html('./src')