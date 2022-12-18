#!/usr/bin/env python3

from helpers import clean_up, upload_files
import sys
import os
import glob

if len(sys.argv) > 1:
    try:
        upload_files.upload_file(sys.argv[1])
    finally:
        path = os.path.dirname(os.path.abspath(__file__))
        for file in glob.glob(f"{path}/tmp/files"):
            clean_up.delete_file(file)
        clean_up.delete_tmp_files()
