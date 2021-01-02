#!/usr/bin/python3.9

try:
  import sys,requests
except:
  import os
  os.system('pip install requests')
  quit('Jalankan ulang skrip')

if len(sys.argv) == 2:
  url = "https://api.github.com/users/" + sys.argv[1]
  req = requests.get(url)
  try:
    if req.status_code == 200:
      req = req.json()
      print("\n\033[32;1mMelihat akun GitHub",req['login'])
      print("\n\nID:",req['id'])
      print("NodeID:",req['node_id'])
      print("GitURL:",req['html_url'])
      print("Avatar:",req['avatar_url'])
      print("Tipe",req['type'])
      print("SiteAdmin:",req['site_admin'])
      print("Nama:",req['name'])
      print("Company:",req['company'])
      print("Blog:",req['blog'])
      print("Lokasi:",req['location'])
      print("Email:",req['email'])
      print("Bio:",req['bio'])
      print("Hireable:",req['hireable'])
      print("Twitter:",req['twitter_username'])
      print("Public repository:",req['public_repos'])
      print("Gist:",req['public_gists'])
      print("Pengikut:",req['followers'])
      print("Mengikuti:",req['following'])
      print("Akun sejak:",req['created_at'])
      print("Terakhir diupdate",req['updated_at'])
      print()
      quit("\033[00;0mHadeh.. Capek juga ya ngeliat data orang. Istirahat dulu..")
    else:
      quit("\033[31;1mKesalahan input. Masukkan username dengan benar")
  except Exception as err:
    quit("Ada yg salah kayak nya.",err)
else:
  print("""
  []                           []
  []   GitHub Account Lookup   []
  []        by: EtcAug10       []
  []                           []
  
  USAGE:
    python3 githublookup.py {username}
  EXAMPLE:
    python3 githublookup.py EtcAug10
    
  Happy stalking ^_^
  """)
  exit()
