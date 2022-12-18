#!/usr/bin/env python3

import os
import settings as s


def check_env():
    path = os.path.dirname(os.path.abspath(__file__)) + "/../venv"
    if not os.path.isdir(path):
        os.system("'{}' -m venv '{}'".format(s.SETTINGS["python"], path))
