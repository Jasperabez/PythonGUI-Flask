import os
import ftplib
import tempfile
import shutil
import datetime
import uuid
import json
import requests

import config

def UploadFileWithMetadata(rec_title, rec_location, rec_date, rec_audio_data):
    try:
        # save audio in temp location with unique name
        dirpath = tempfile.mkdtemp()
        audio_filename = str(uuid.uuid4())+".mp3"
        audio_path = os.path.join(
            dirpath, audio_filename
        )
        rec_audio_data.save(audio_path)

        # post data to web server (with audio file unique name)
        metadata = {
            "title" : rec_title,
            "location" : rec_location,
            "date" : rec_date.strftime('%m/%d/%Y'),
            "audio_filename" : audio_filename
        }
        json_body_payload = json.dumps(metadata)
        requests.post(config.POST_ENDPOINT, json=json_body_payload)

        # Upload audio file to FTP server
        ftp = ftplib.FTP()
        ftp.connect(config.FTP_HOST, config.FTP_PORT)
        ftp.login(config.FTP_USER, config.FTP_PASS)
        ftp.encoding = "utf-8"
        filename = "some_file.txt"
        with open(audio_path, "rb") as file:
            # use FTP's STOR command to upload the file
            ftp.storbinary(f"STOR {audio_filename}", file)

        #delete temp files/dire
        shutil.rmtree(dirpath)

        return True
    except:
        return False

def DummyUploadFileWithMetadata(rec_title, rec_location, rec_date, rec_audio_data):
    return True