# coding utf-8
# author: Zoraa Dev

import requests
import re
import json
import time
import os
dm=[]
class login:
    def __init__(self) -> None:
        pass        
        
    def login_cookies(self):
        try:
            cookies = input("[•] Cookies: ")
            if len(cookies) >0:
                with requests.Session() as r:
                    try:
                        response = r.get('https://www.facebook.com/adsmanager/manage/campaigns', cookies = {'cookie': cookies}).text
                        self.act = re.search(r'act=(.*?)&nav_source',str(response)).group(1)
                        response2 = r.get(f'https://www.facebook.com/adsmanager/manage/campaigns?act={self.act}&nav_source=no_referrer&breakdown_regrouping=1', cookies = {'cookie': cookies}).text
                        EAAB = re.search(r'accessToken="(.*?)"',str(response2)).group(1)
                        self.userid, self.username = self.graph_id_nama(cookies, EAAB)
                        print(f"[•] Token EAAB: {EAAB}")
                        with open('.cookies_token.json', mode='w') as wr:
                            wr.write(json.dumps({
                                'Cookie': cookies,
                                'Token': EAAB
                            }))
                            wr.close()
                        print(f'[!] Success Login Cookie {self.userid}/{self.username}')
                    except (Exception) as e:
                        exit(f'[!] Error: {str(e).title()}')
            else:
                exit('[!] Input Kosong')
        except (KeyboardInterrupt, Exception) as e:
            exit(f'[!] Error: {str(e).title()}')
            
    def graph_id_nama(self, cookies, EAAB):
        with requests.Session() as r:
            try:
                response = r.get(f"https://graph.facebook.com/me?fields=id,name&access_token={EAAB}", cookies = {'cookies':cookies}).json()
                return (response['id'],response['name'])
            except (Exception) as e:
                exit(f'[!] Error: {str(e).title()}')
                
class facebook:
    def __init__(self):
        print('[!] Contoh Nama File Dump: dumpid.txt')
        self.sv_dump = input('[?] Nama File Dump: ')
        self.cek_data_log()
        
    def cek_data_log(self):
        if os.path.isfile('.cookies_token.json') is True:
            self.data_log = json.loads(open('.cookies_token.json', mode='r').read())
            self.main(self.data_log)
        else:
            print('\n[!] File Data Login Not Found')
            time.sleep(3)
            login().login_cookies()
            
    def main(self, data_log):
        try:
            print('\n[!] Setiap ID, Gunakan Pemisah Koma, No Spasi')
            id = input('[?] ID facebook: ');print()
            if len(id) >0:
                for i in id.split(','):
                    try: self.dump_id(i, self.data_log['Cookie'],self.data_log['Token'],'')
                    except (KeyboardInterrupt, Exception) as e: pass
                    exit(f'\n\n[•] Success Dump: {len(dm)}\n[•] Semua Tersimpan Di Internal: /sdcard/dump/{self.sv_dump}')
            else:
                exit('[!] Input Kosong')
        except (Exception) as e:
            exit(f'[!] Error: {str(e).title()}')    
            
    def dump_id(self, i, cookies, EAAB, fields):
        with requests.Session() as r:
            try:
                if len(dm) ==0:
                    pars = {"access_token": EAAB,"fields": "name,friends.fields(id,name,birthday)"}
                else: pars = {"access_token": EAAB,"fields": f"name,friends.fields(id,name,birthday).after({fields})"}
                response = r.get(f"https://graph.facebook.com/{i}", params=pars,headers={"connection": "keep-alive","accept": "*/*","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-fetch-user": "?1","sec-ch-ua-mobile": "?1","upgrade-insecure-requests": "1","user-agent": "Mozilla/5.0 (Linux; Android 11; AC2003) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"},cookies={'cookie':cookies}).json()
                for im in response["friends"]["data"]:
                    self.id, self.nama = im["id"],im["name"]
                    dm.append(self.id+'|'+self.nama)
                    print(f'[!] Dump {str(im['id'])[:20]}/{len(dm)} ID    ', end='\r')
                    open('/sdcard/dump/'+self.sv_dump,'a').write(self.id+'|'+self.nama+'\n')
                if response:
                    fields = response["friends"]["paging"]["cursors"]["after"]
                    self.dump_id(i, cookies, EAAB, fields)
            except (AttributeError, KeyboardInterrupt) as e: pass        
            
            