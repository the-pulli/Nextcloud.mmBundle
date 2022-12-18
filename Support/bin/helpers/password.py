#!/usr/bin/env python3

import settings
import os


def prompt():
    if settings.SETTINGS["sharing_password"]:
        path = f"{os.path.dirname(os.path.abspath(__file__))}/../AppleScript/SetPassword.scpt"
        sharing_password = os.popen("osascript '{}'".format(path)).read().strip()
        if sharing_password != "false":
            return sharing_password
    return None
