#!/usr/bin/env python3

import os
import re


def change_attachment_dict(file):
    return {
        "filePath": file["filePath"],
        "fileName": os.path.basename(file["filePath"]),
        "MIME": file["MIME"]
    }


def filter_attachments(file):
    filename_rejecting_regex = re.compile(
        r"signature|msg|encrypted|openpgp|attachment(.txt)?|smime\.p7s|.+\.eml",
        flags=re.IGNORECASE
    )
    if not filename_rejecting_regex.match(file["fileName"]):
        return file


def prepare_attachments(attachments):
    return list(filter(None, map(filter_attachments, map(change_attachment_dict, attachments))))
