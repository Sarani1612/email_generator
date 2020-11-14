import os
# from datetime import datetime, timezone
import datetime
import random
import time
import copy

path = os.getcwd() + "/input_emails/"

header = {
    'start': 'Message-ID: ',
    'id': '.53774466.mnmnmn.danish@behavox\n',
    'from': 'From: jane.doe@gmail.com\n',
    'to': 'To: john.smith@gmail.com\n',
    'subject': 'Subject: Signatures_da\n',
    'date': 'Date: ',
    'version': 'Mime-Version: 1.0\n',
    'encoding': 'Content-Transfer-Encoding: 7bit\n',
    'type': 'Content-Type: text/plain; charset=utf-8\n',
    'space': '\n'
}

body = ''
email_txt = ''

# .eml file save path
email_path = os.getcwd() + "output_emails/"

dt = datetime.datetime.now(datetime.timezone.utc)
dt -= datetime.timedelta(days=365)

idn = 22950000

for file in os.listdir(path):
    nheader = copy.deepcopy(header)
    idn += 1
    nheader['id'] = str(idn) + header['id']

    dt += datetime.timedelta(seconds=10)
    dtime = dt.strftime("%a") + ', ' + dt.strftime("%d %b %Y %X %z %Z") + '\n'

    nheader['date'] = header['date'] + dtime

    header_info = nheader.values()
    header_txt = ''
    for each in header_info:
        header_txt += each

    fname = path + "/" + file
    f = open(fname, "r")
    body = f.read()

    email_txt = header_txt + body
    emlname = email_path + file + '.eml'
    eml_fp = open(emlname, "w")
    eml_fp.write(email_txt)
    eml_fp.close()
    # time.sleep(2)
