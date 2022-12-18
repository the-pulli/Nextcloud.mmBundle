#!/usr/bin/env python3

from helpers import clean_up, upload_files as uploader
import sys
import os

if len(sys.argv) == 1:
    try:
        uploader.create_share_url()
    finally:
        path = os.path.dirname(os.path.abspath(__file__))
        tmp_files = [f"{path}/tmp/attachments.json", f"{path}/tmp/config.json"]
        for tmp_file in tmp_files:
            clean_up.delete_file(tmp_file)
