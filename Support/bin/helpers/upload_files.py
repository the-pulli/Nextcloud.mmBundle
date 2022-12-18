#!/usr/bin/env python3

from .clean_up import delete_tmp_files
import os
import json
import settings
try:
    from nextcloud import NextCloud
except ModuleNotFoundError:
    path = os.path.dirname(os.path.abspath(__file__))
    output = os.popen("pip3 install -r '{}/../requirements.txt'".format(path)).read()
    from nextcloud import NextCloud


def read_config():
    file_path = os.path.dirname(os.path.abspath(__file__))
    with open("{}/../tmp/config.json".format(file_path), "r") as file:
        return json.load(file)


def upload_file(attachment):
    parsed_attachment = json.loads(attachment)
    config = read_config()
    with NextCloud(
            config["url_string"],
            user=settings.SETTINGS["username"],
            password=settings.SETTINGS["password"],
            session_kwargs={
                "verify": True
            }) as nxc:
        mail_folder = "{}/{}/{}".format(config["base_folder"], config["date"], config["mail_id"])
        file_name = "{}/{}".format(mail_folder, parsed_attachment["fileName"])
        nxc.create_folder("{}".format(config["base_folder"]))
        nxc.create_folder("{}/{}".format(config["base_folder"], config["date"]))
        nxc.create_folder("{}".format(mail_folder))
        nxc.upload_file(parsed_attachment["filePath"], file_name)
        os.unlink(parsed_attachment["filePath"])


def create_share_url():
    config = read_config()
    mail_folder = "{}/{}/{}".format(config["base_folder"], config["date"], config["mail_id"])
    with NextCloud(
            config["url_string"],
            user=settings.SETTINGS["username"],
            password=settings.SETTINGS["password"],
            session_kwargs={
                "verify": True
            }) as nxc:
        share_url = nxc.create_share(path=mail_folder, share_type=3, password=config["sharing_password"]).data["url"]
        os.system("printf %s '{}' | pbcopy".format(share_url))  # Don't copy new line into clipboard
        delete_tmp_files()
