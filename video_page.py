import os, requests, json

# ---- Your Page ID & Access Token 
page_id = 'xxxx'
access_token = 'xxxx'
# ---- Fill Title & Description Of Video
title = 'xxxx'
description = 'xxxx'
# ---- Your Path Video File
path = '/sdcard/video.mp4'
# ---- Get Video Size To Bytes

upload = f'https://graph-video.facebook.com/v20.0/{page_id}/videos?access_token={access_token}'
files = { 'file': open(path, 'rb'), }
payload = { "title": title, "description": description, }
result = requests.post(upload, files=files, data=payload)

# If Result Get "200 OK & Video ID" Your Videos Success Uploaded
print(result.text)

