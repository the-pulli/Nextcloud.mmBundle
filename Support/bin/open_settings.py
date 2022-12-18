#!/usr/bin/env python3

import os
import shutil


def open_settings():
    bundle_path = os.path.dirname(os.path.abspath(__file__)) + "/"
    settings_file = "{}settings.py".format(bundle_path)
    if not os.path.exists(settings_file):
        shutil.copy("{}settings.stub".format(bundle_path), settings_file)
    os.system("open '{}settings.py'".format(bundle_path))
    exit(0)


if os.getenv("OPEN_SETTINGS", None) is not None:
    open_settings()
