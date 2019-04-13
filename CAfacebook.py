import requests


p_t_e = raw_input('path mail: ')
email = open(p_t_e)

for emails in email:
      url = 'https://mbasic.facebook.com/login/identify/'
      data = {'email':emails.strip('\n'[0]),"did_submit":"Cari"}
      r = requests.post(url=url, data=data)
      if  "/recover/code/" in r.url or '/recover/initiate/?ldata=' in r.url:
          print('\033[32mfund this account: '+emails)
      else:
          print('\033[31mnot fund this account: '+emails)