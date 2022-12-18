#!/usr/bin/env python3

import os
import settings


def generate_apple_script(subdomains, standard_choice):
    return '''
        use AppleScript version "2.4" -- Yosemite (10.10) or later
        use scripting additions
    
        set UrlList to %s
    
        set UrlAnswer to choose from list UrlList with title "Url Dialog" with prompt "Which URL should be used for sharing?" default items "%s"
    
        if UrlAnswer is false then
          set UrlAnswer to "Abort"
        else
          set UrlAnswer to UrlAnswer's item 1
        end if
    
        return UrlAnswer
    ''' % (subdomains, standard_choice)


def convert_subdomains_to_apple_script(subdomains):
    apple_script_string = subdomains.__str__()
    dictionary = {"[": "{", "]": "}", "'": '"'}
    for key in dictionary.keys():
        apple_script_string = apple_script_string.replace(key, dictionary[key])
    return apple_script_string


def generate_bash_script(apple_script):
    return '''#!/bin/bash
read -r -d '' APPLESCRIPT_SUBDOMAINS << EOM
    %s
EOM
osascript -e "$APPLESCRIPT_SUBDOMAINS"
    ''' % apple_script


def configure_sharing_url():
    base_url = settings.SETTINGS["url"]
    subdomains = settings.SETTINGS["subdomains"]
    if len(subdomains) >= 1:
        if base_url not in subdomains:
            subdomains.insert(0, base_url)  # Insert base URL as first in the list
        apple_script_subdomains = convert_subdomains_to_apple_script(subdomains)
        # Use subdomains last element as default value for the selection
        apple_script = generate_apple_script(apple_script_subdomains, subdomains[-1])
        url_string = os.popen(generate_bash_script(apple_script)).read().strip()
        if url_string == "Abort":
            exit(0)
    else:
        url_string = base_url
    return url_string
