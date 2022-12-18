#!/usr/bin/env python3

from helpers import attachments, subdomains, password
import datetime
import json
import open_settings
import os
import re
import settings
import shutil


if not all(map(lambda s: True if s != "" else False, settings.SETTINGS.values())):
    apple_script = '''
        use AppleScript version "2.4" -- Yosemite (10.10) or later
        use scripting additions

        display dialog "Configure the settings first." with icon caution with title "Error" buttons { "OK" } default button { "OK" }
    '''
    os.system("osascript -e '{}'".format(apple_script))
    open_settings.open_settings()

attachments = attachments.prepare_attachments(json.loads(os.getenv("MM_FILES", [].__str__())))

if len(attachments) >= 1:
    sharing_password = password.prompt()
    url_string = subdomains.configure_sharing_url()
    path = os.path.dirname(os.path.abspath(__file__))
    i = 0
    for attachment in attachments:
        file_path = f"{path}/tmp/files/{attachment['fileName']}"
        shutil.copyfile(attachment['filePath'], file_path)
        attachments[i]["filePath"] = file_path
        i = i + 1
    with open(f"{path}/tmp/attachments.json", "w") as file:
        json.dump(attachments, file)
    date = datetime.date.today().strftime("%Y-%m-%d")
    base_folder = settings.SETTINGS["base_folder"]
    mail_id = os.getenv("MM_MESSAGE_ID")
    # Remove the @ Part
    mail_id = re.sub("@.*", "", mail_id)
    upload_config = {
        "base_folder": base_folder,
        "date": date,
        "mail_id": mail_id,
        "sharing_password": sharing_password,
        "url_string": url_string
    }
    with open(f"{path}/tmp/config.json", "w") as file:
        json.dump(upload_config, file)
    os.system("open '{}/Upload Attachments.app'".format(path))
else:
    apple_script = '''
        use AppleScript version "2.4" -- Yosemite (10.10) or later
        use scripting additions

        display dialog "No files attached to the email." with icon caution with title "Error" buttons { "OK" } default button { "OK" }
    '''
    os.system("osascript -e '{}'".format(apple_script))
