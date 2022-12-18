#!/usr/bin/env python3

import os


def delete_file(file):
    if os.path.isfile(file):
        os.unlink(file)


def delete_tmp_files():
    path = os.path.dirname(os.path.abspath(__file__))
    tmp_files = [f"{path}/tmp/attachments.json", f"{path}/tmp/config.json"]
    for tmp_file in tmp_files:
        delete_file(tmp_file)
