#!/bin/env python3

import os
import argparse
from api.api import *

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--username", required=True,
                help="username of account to scan")
ap.add_argument("-p", "--postscrap", action='store_true',
                help="scrape all uploaded images info ")
ap.add_argument("-s", "--savedata", action='store_true',
                help="save data to file")
ap.add_argument("-t", "--tagscrap", action="store_true",
                help="list often used tags")
args = vars(ap.parse_args())

os.system('clear') if os.name == 'posix' else os.system('cls')
ig = main(user=args["username"])
if args['tagscrap']:
    ig.print_data()
else:
    ig.print_data_()

if args['postscrap']:
    ig.scrap_uploads()

if args['savedata']:
    ig.save_data()
