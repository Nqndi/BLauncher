# -*- coding: utf-8 -*-
import base64
import checksumdir
import json
import os
import shutil
import urllib.request
from hashlib import md5
from subprocess import Popen
from sys import exit as brexit
from threading import Thread
from time import sleep, time

import discord_rpc
import platform
import requests
import urllib3
from colorama import Fore
from console.utils import set_title
from pyunpack import Archive

import getpass_ak


class var:
    if 'Windows-10' in platform.platform() or 'Windows-11' in platform.platform():
        compatibility_mode = False
    else:
        compatibility_mode = True
    exit = False
    if compatibility_mode:
        cyan = ''
        b = ''
        r = ''
        red = ''
        g = ''
    else:
        cyan = Fore.LIGHTBLUE_EX
        b = '\u001b[31;1m'
        r = '\u001b[0m'
        red = '\u001b[31m'
        g = '\u001b[32m'
    back = f'{red}[{r}0{red}]{r}'
    first = f'{cyan}[{r}1{cyan}]{r}'
    second = f'{cyan}[{r}2{cyan}]{r}'
    third = f'{cyan}[{r}3{cyan}]{r}'
    fourth = f'{cyan}[{r}4{cyan}]{r}'
    fifth = f'{cyan}[{r}5{cyan}]{r}'
    sixth = f'{cyan}[{r}6{cyan}]{r}'
    seventh = f'{cyan}[{r}7{cyan}]{r}'
    eighth = f'{cyan}[{r}8{cyan}]{r}'
    pointer = f'{cyan}[{r}>{cyan}]{r}'
    winuser = 'None'
    twofa_value = ''

    username = 'None'
    password = ''
    twofa = 'False'
    ram = '1000'
    client = 'Lunar'
    rc = 'lc'
    heapdump = 'True'

    hex_c = 'False'
    hex_val = 'None'

    starting_time = time()
    rpc_status = 'Loading program...'
    is_rpc = 'True'

    is_vanity = 'True'
    server_url = 'play.vanityempire.hu:1999'


def spawn(program, exit_code=0):
    Popen(program)
    var.exit = True
    brexit(exit_code)


def middle(string):
    spaces = int((120 - len(string)) / 2) - 2
    sp = ""
    for i in range(spaces):
        sp += " "
    return sp + string


def start_rpc():
    if var.is_rpc == 'True' or var.is_rpc == True:
        discord_rpc.initialize('919956777506848778', log=False)
        while not var.exit and var.is_rpc == 'True':
            discord_rpc.update_presence(
                **{
                    'details': var.rpc_status,
                    'start_timestamp': var.starting_time,
                    'large_image_key': 'lunar'
                }
            )
            discord_rpc.update_connection()
            sleep(1)
        discord_rpc.shutdown()


def install_batmod():
    if not os.path.exists(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\bm.jar'):
        installfrom = requests.get('http://blauncher.atwebpages.com/batmod').text
        print(var.red + middle(f'{var.client} letöltése...'))
        urllib.request.urlretrieve(installfrom,
                                   f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\bm.jar')


def check_md5sum(file):
    md5_hash = md5()
    try:
        a_file = open(file, "rb")
    except:
        return None
        a_file = open(file.replace(var.winuser, winuser), "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest


def install_melon():
    if not os.path.exists(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\mc.jar'):
        print(f'\u001b[33m                                                {var.client} letöltése...')
        urllib.request.urlretrieve('https://www.dropbox.com/s/9ve60rtwxg0cmu9/mc.jar?dl=1',
                                   f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\mc.jar')
        urllib.request.urlretrieve('https://www.dropbox.com/s/tx9r64evz1tkmp4/melon_libs.zip?dl=1',
                                   f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries\\mlibs.zip')
        Archive(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries\\mlibs.zip').extractall(
            f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries')
        try:
            os.remove(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries\\mlibs.zip')
        except:
            pass
    else:
        if check_md5sum(
                f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\mc.jar') != '396099e23e58309d21713ab5d7c1d1a8':
            print(var.red + middle(f'{var.client} letöltése...'))
            urllib.request.urlretrieve('https://www.dropbox.com/s/9ve60rtwxg0cmu9/mc.jar?dl=1',
                                       f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\mc.jar')
            urllib.request.urlretrieve('https://www.dropbox.com/s/tx9r64evz1tkmp4/melon_libs.zip?dl=1',
                                       f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries\\mlibs'
                                       f'.zip')
            Archive(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries\\mlibs.zip').extractall(
                f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries')
            try:
                os.remove(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\libraries\\mlibs.zip')
            except:
                pass


def install_cheatbreaker():
    if not os.path.exists(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\cb.jar'):
        latest = requests.get('http://blauncher.atwebpages.com/cheatbreaker-link').text
        print(var.red + middle(f'{var.client} letöltése...'))
        urllib.request.urlretrieve(latest,
                                   f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\cb.jar')
    else:
        if check_md5sum(
                f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\cb.jar') != '5881582f30057c2d642815f2d32753f3':
            print(f'\u001b[33m                                                {var.client} letöltése...')
            latest = requests.get('http://blauncher.atwebpages.com/cheatbreaker-link').text
            urllib.request.urlretrieve(latest,
                                       f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\cb.jar')


class Main:
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        Thread(target=start_rpc, ).start()
        self.check()

        if os.path.exists(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\config.json'):
            with open(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\config.json', 'r',
                      encoding="utf-8") as file:
                try:
                    var.username = self.decrypt(file.readline())
                    var.password = self.decrypt(file.readline())
                    var.ram = self.decrypt(file.readline())
                    var.client = self.decrypt(file.readline())
                    var.rc = self.decrypt(file.readline())
                    var.heapdump = self.decrypt(file.readline())
                    var.twofa = self.decrypt(file.readline())
                    var.is_rpc = self.decrypt(file.readline())
                    var.is_vanity = self.decrypt(file.readline()).rstrip('\n')
                except:
                    pass

        if os.path.exists(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\theme.json'):
            with open(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\theme.json', 'r',
                      encoding="utf-8") as file:
                try:
                    if var.compatibility_mode:
                        var.cyan = ''
                        var.g = ''
                        var.red = ''
                    else:
                        var.cyan = self.decrypt(file.readline())
                        var.g = self.decrypt(file.readline())
                        var.red = self.decrypt(file.readline())
                except:
                    pass

        var.back = f'{var.red}[{var.r}0{var.red}]{var.r}'
        var.first = f'{var.cyan}[{var.r}1{var.cyan}]{var.r}'
        var.second = f'{var.cyan}[{var.r}2{var.cyan}]{var.r}'
        var.third = f'{var.cyan}[{var.r}3{var.cyan}]{var.r}'
        var.fourth = f'{var.cyan}[{var.r}4{var.cyan}]{var.r}'
        var.fifth = f'{var.cyan}[{var.r}5{var.cyan}]{var.r}'
        var.sixth = f'{var.cyan}[{var.r}6{var.cyan}]{var.r}'
        var.seventh = f'{var.cyan}[{var.r}7{var.cyan}]{var.r}'
        var.eighth = f'{var.cyan}[{var.r}8{var.cyan}]{var.r}'
        var.pointer = f'{var.cyan}[{var.r}>{var.cyan}]{var.r}'

        self.main_screen()

    def clear(self):
        _ = os.system('cls')

    def split(self, word):
        return [char for char in word]

    def decrypt(self, string):
        try:
            decrypted3 = base64.b64decode(str(string).encode()).decode('utf-8')
            stringa = decrypted3.replace('ß', 'Y').replace('¤', 'A').replace('÷', 'b').replace('×', 'O').replace('đ',
                                                                                                                 'n').replace(
                'Ää', 'M').replace('°', 'w').replace('˛', 'k').replace('Ł', '=').replace('˙', 'E').replace('¨', 'F')
            decrypted1 = base64.b64decode(str(stringa).encode()).decode('utf-8')
            decrypted = decrypted1.replace('ß', 'Y').replace('¤', 'A').replace('÷', 'b').replace('×', 'O').replace('đ',
                                                                                                                   'n').replace(
                'Ää', 'M').replace('°', 'w').replace('˛', 'k').replace('Ł', '=').replace('˙', 'E').replace('¨', 'F')
            decrypted2 = base64.b64decode(str(decrypted).encode()).decode('utf-8')
            return decrypted2
        except:
            try:
                os.remove(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\config.json')
            except:
                var.exit = True
                brexit(0)

    def encrypt(self, string):
        try:
            enc1 = base64.b64encode(str(string).encode()).decode('utf-8')
            encrypted_string = str(self.split(str(enc1))).replace('Y', 'ß').replace('A', '¤').replace('b', '÷').replace(
                'O', '×').replace('n', 'đ').replace('M', 'Ää').replace('w', '°').replace('k', '˛').replace('=',
                                                                                                           'Ł').replace(
                'E', '˙').replace('F', '¨').replace("', '", '').replace("['", '').replace("']",
                                                                                          '')  # .replace(',',
            # '').replace(' ', '')#.replace('[', '').replace(']', '').replace("'", '')
            enc2 = base64.b64encode(str(encrypted_string).encode()).decode('utf-8')
            encrypted_stringa = str(self.split(str(enc2))).replace('Y', 'ß').replace('A', '¤').replace('b',
                                                                                                       '÷').replace('O',
                                                                                                                    '×').replace(
                'n', 'đ').replace('M', 'Ää').replace('w', '°').replace('k', '˛').replace('=', 'Ł').replace('E',
                                                                                                           '˙').replace(
                'F', '¨').replace("', '", '').replace("['", '').replace("']",
                                                                        '')  # .replace(',', '').replace(' ',
            # '')#.replace('[', '').replace(']', '').replace("'", '')
            enc3 = base64.b64encode(str(encrypted_stringa).encode()).decode('utf-8')
            return enc3
        except:
            try:
                os.remove(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\config.json')
            except:
                var.exit = True
                brexit(0)

    def name(self):
        if var.compatibility_mode:
            print(var.cyan + '''\n  ██████╗ ██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗
  ██╔══██╗██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗
  ██████╔╝██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝
  ██╔══██╗██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗
  ██████╔╝███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║
  ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''' + var.r)
        else:
            print(var.cyan + '''\n                    ██████╗ ██╗      █████╗ ██╗   ██╗███╗   ██╗ ██████╗██╗  ██╗███████╗██████╗
                    ██╔══██╗██║     ██╔══██╗██║   ██║████╗  ██║██╔════╝██║  ██║██╔════╝██╔══██╗
                    ██████╔╝██║     ███████║██║   ██║██╔██╗ ██║██║     ███████║█████╗  ██████╔╝
                    ██╔══██╗██║     ██╔══██║██║   ██║██║╚██╗██║██║     ██╔══██║██╔══╝  ██╔══██╗
                    ██████╔╝███████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╗██║  ██║███████╗██║  ██║
                    ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝\n\n''' + var.r)

    def check(self):
        try:
            var.winuser = os.getenv("APPDATA").replace('C:\\Users\\', '').replace('\\AppData\\Roaming', '')
        except:
            var.winuser = input('Rossz windows user, kérlek írd be: ')

        version = open(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\version.txt', 'r').readlines()[0]
        with requests.Session() as s:
            try:
                latest_version = s.get('http://blauncher.atwebpages.com/latest_version', verify=False).text
            except:
                sleep(5)
                try:
                    latest_version = s.get('http://blauncher.atwebpages.com/latest_version', verify=False).text
                except:
                    latest_version = version
        if latest_version not in version:  # UPDATE
            if os.path.exists(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\config.json'):
                try:
                    os.remove(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\config.json')
                except:
                    pass
            try:
                spawn([f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\updater.exe'])
            except FileNotFoundError:
                urllib.request.urlretrieve(
                    requests.get('http://blauncher.atwebpages.com/latest_updater', headers={'Pragma': 'no-cache'},
                                 verify=False).text,
                    f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\updater.exe')
                spawn([f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\updater.exe'])

    def set_twofa(self):
        self.clear()
        self.name()
        print(f'''                                                2FA:\n
                                                {var.first} Be
                                                {var.second} Ki\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input('')
        if option == '1':
            var.twofa = True
            self.account()
        elif option == '2':
            var.twofa = False
            self.account()
        else:
            self.set_twofa()

    def account(self):
        var.rpc_status = 'Configuring Account...'
        self.clear()
        self.name()
        censored_pass = None
        if var.password != 'None':
            censored_pass = ''
            for i in range(len(var.password)):
                censored_pass += '*'
        if var.is_vanity == 'False':
            print(f'''                                                Fiók:\n
                                                {var.back} Vissza
                                                {var.first} Felhasználónév ({var.username})
                                                {var.second} Vanity Auth ({var.is_vanity})\n\n''')
            print(f'                                                {var.pointer} ', end='')
            option = input('')
            if option == '0':
                self.main_screen()
            elif option == '1':
                self.set_var('Felhasználónév', 'var.username', False)
            elif option == '2':
                if var.is_vanity == 'True':
                    var.is_vanity = 'False'
                else:
                    var.is_vanity = 'True'
                self.account()
            else:
                self.account()
        else:
            print(f'''                                                Fiók:\n
                                                {var.back} Vissza
                                                {var.first} Felhasználónév ({var.username})
                                                {var.second} Jelszó ({censored_pass})
                                                {var.third} 2FA ({var.twofa})
                                                {var.fourth} Vanity Auth ({var.is_vanity})\n\n''')
            print(f'                                                {var.pointer} ', end='')
            option = input('')
            if option == '0':
                self.main_screen()
            elif option == '1':
                self.set_var('Felhasználónév', 'var.username', False)
            elif option == '2':
                self.set_var('Jelszó', 'var.password', True)
            elif option == '3':
                self.set_twofa()
            elif option == '4':
                if var.is_vanity == 'True':
                    var.is_vanity = 'False'
                else:
                    var.is_vanity = 'True'
                self.account()
            else:
                self.account()

    def custom_color(self, variable):
        self.clear()
        self.name()
        print(f'''                                                HEX:''')
        print(f'                                                {var.pointer} ', end='')
        input('').replace(' ', '')
        try:
            exec(f"{variable} = fg(hex_color)")
        except:
            self.custom_color(variable)
        var.back = f'{var.red}[{var.r}0{var.red}]{var.r}'
        var.first = f'{var.cyan}[{var.r}1{var.cyan}]{var.r}'
        var.second = f'{var.cyan}[{var.r}2{var.cyan}]{var.r}'
        var.third = f'{var.cyan}[{var.r}3{var.cyan}]{var.r}'
        var.fourth = f'{var.cyan}[{var.r}4{var.cyan}]{var.r}'
        var.fifth = f'{var.cyan}[{var.r}5{var.cyan}]{var.r}'
        var.sixth = f'{var.cyan}[{var.r}6{var.cyan}]{var.r}'
        var.seventh = f'{var.cyan}[{var.r}7{var.cyan}]{var.r}'
        var.eighth = f'{var.cyan}[{var.r}8{var.cyan}]{var.r}'
        var.pointer = f'{var.cyan}[{var.r}>{var.cyan}]{var.r}'
        self.customization()

    def select_color(self, variable):
        self.clear()
        self.name()
        print(f'''                                                Színek:\n
                                                {var.back} Vissza
                                                {var.first} \u001b[31mPiros{var.r}
                                                {var.second} \u001b[33mSárga{var.r}
                                                {var.third} \u001b[32mZöld{var.r}
                                                {var.fourth} {Fore.LIGHTBLUE_EX}Cián{var.r}
                                                {var.fifth} \u001b[34mKék{var.r}
                                                {var.sixth} \u001b[35mMagenta{var.r}
                                                {var.seventh} \u001b[37mFehér{var.r}\n
                                                {var.eighth} Egyedi\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input('')
        if option == '0':
            self.customization()
        elif option == '1':
            exec(f"{variable} = '\u001b[31m'")
        elif option == '2':
            exec(f"{variable} = '\u001b[33m'")
        elif option == '3':
            exec(f"{variable} = '\u001b[32m'")
        elif option == '4':
            exec(f"{variable} = Fore.LIGHTBLUE_EX")
        elif option == '5':
            exec(f"{variable} = '\u001b[34m'")
        elif option == '6':
            exec(f"{variable} = '\u001b[35m'")
        elif option == '7':
            exec(f"{variable} = '\u001b[37m'")
        elif option == '8':
            self.custom_color(variable)
        else:
            self.select_color()
        var.back = f'{var.red}[{var.r}0{var.red}]{var.r}'
        var.first = f'{var.cyan}[{var.r}1{var.cyan}]{var.r}'
        var.second = f'{var.cyan}[{var.r}2{var.cyan}]{var.r}'
        var.third = f'{var.cyan}[{var.r}3{var.cyan}]{var.r}'
        var.fourth = f'{var.cyan}[{var.r}4{var.cyan}]{var.r}'
        var.fifth = f'{var.cyan}[{var.r}5{var.cyan}]{var.r}'
        var.sixth = f'{var.cyan}[{var.r}6{var.cyan}]{var.r}'
        var.seventh = f'{var.cyan}[{var.r}7{var.cyan}]{var.r}'
        var.eighth = f'{var.cyan}[{var.r}8{var.cyan}]{var.r}'
        var.pointer = f'{var.cyan}[{var.r}>{var.cyan}]{var.r}'
        self.customization()

    def customization(self):
        self.clear()
        self.name()
        print(f'''                                                Színek:\n
                                                {var.back} Vissza
                                                {var.first} {var.cyan}Szín{var.r}
                                                {var.second} {var.g}Szín 2{var.r}
                                                {var.third} {var.red}Szín 3{var.r}\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input('')
        if option == '0':
            self.main_screen()
        elif option == '1':
            self.select_color('var.cyan')
        elif option == '2':
            self.select_color('var.g')
        elif option == '3':
            self.select_color('var.red')
        else:
            self.customization()

    def customization_menu(self):
        var.rpc_status = 'Customizing Client...'
        self.clear()
        self.name()
        print(f'''                                                Személyre szabás:\n
                                                {var.back} Vissza
                                                {var.first} Színek
                                                {var.second} Discord RPC\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input('')
        if option == '0':
            self.main_screen()
        elif option == '1':
            self.customization()
        elif option == '2':
            self.rpc()
        else:
            self.customization_menu()

    def rpc(self):
        self.clear()
        self.name()
        print(f'''                                                Discord Rich Presence:\n
                                                {var.back} Vissza
                                                {var.first} Ki/Be ({var.is_rpc})\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input()
        if option == '0':
            self.customization_menu()
        elif option == '1':
            if var.is_rpc == 'True' or var.is_rpc == True:
                var.is_rpc = 'False'
                self.rpc()
            elif var.is_rpc == 'False' or var.is_rpc == False:
                var.is_rpc = 'True'
                Thread(target=start_rpc, ).start()
                self.rpc()
        else:
            self.rpc()

    def main_screen(self):
        var.rpc_status = 'In Menu'
        self.clear()
        self.name()
        if var.compatibility_mode:
            print(f'''                                                Lehetőségek:\n
                                                {var.first} Indítás
                                                {var.second} Fiók
                                                {var.third} Beállítások\n\n''')
            print(f'                                                {var.pointer} ', end='')
            option = input('')

            if option == '1':
                self.launch()
            elif option == '2':
                self.account()
            elif option == '3':
                self.options()
            else:
                self.main_screen()
        else:
            print(f'''                                                Lehetőségek:\n
                                                {var.first} Indítás
                                                {var.second} Fiók
                                                {var.third} Beállítások
                                                {var.fourth} Személyre Szabás\n\n''')
            print(f'                                                {var.pointer} ', end='')
            option = input('')

            if option == '1':
                self.launch()
            elif option == '2':
                self.account()
            elif option == '3':
                self.options()
            elif option == '4':
                self.customization_menu()
            else:
                self.main_screen()

    def options(self):
        var.rpc_status = 'Configuring Client Options...'
        self.clear()
        self.name()
        print(f'''                                                Beállítások:\n
                                                {var.back} Vissza
                                                {var.first} Ram ({var.ram} MB)
                                                {var.second} Kliens ({var.client})
                                                {var.third} HeapDump ({var.heapdump})\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input('')
        if option == '0':
            self.main_screen()
        elif option == '1':
            self.set_ram()
        elif option == '2':
            self.set_client()
        elif option == '3':
            self.set_heapdump()
        else:
            self.options()

    def set_heapdump(self):
        self.clear()
        self.name()
        print(f'''                                                HeapDump:\n
                                                {var.first} Be
                                                {var.second} Ki\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input('')
        if option == '1':
            var.heapdump = True
            self.options()
        elif option == '2':
            var.heapdump = False
            self.options()
        else:
            self.set_heapdump()

    def set_ram(self):
        self.clear()
        self.name()
        print(f'                                                Ram:\n')
        print(f'                                                {var.pointer} ', end='')
        var_content = input('')
        var.ram = var_content
        self.options()

    def set_var(self, var_name, string_name, censor):
        self.clear()
        self.name()
        print(f'                                                {var_name}:\n')
        sleep(0.05)
        if not censor:
            var_content = input(f'                                                {var.pointer} ')
        else:
            var_content = (getpass_ak.getpass(f'                                                {var.pointer} '))
        exec(f"{string_name} = '{var_content}'")
        self.account()

    def set_twofa_val(self):
        self.clear()
        self.name()
        print(f'                                                {var_name}:\n')
        print(f'                                                {var.pointer} ', end='')
        var_content = input('')
        var.twofa_value = var_content.replace(' ', '')

    def set_client(self):
        var.rpc_status = 'Selecting Client...'
        self.clear()
        self.name()
        print(f'''                                                Kliens:\n
                                                {var.first} Lunar Client
                                                {var.second} Doge Client
                                                {var.third} CheatBreaker
                                                {var.fourth} Melon Client
                                                {var.fifth} BatMod
                                                {var.sixth} Modpack\n\n''')
        print(f'                                                {var.pointer} ', end='')
        option = input('')
        if option == '1':
            var.client = 'Lunar'
            var.rc = 'lc'
            self.options()
        elif option == '2':
            var.client = 'Doge'
            var.rc = 'dc'
            self.options()
        elif option == '3':
            var.client = 'Cheatbreaker'
            self.options()
        elif option == '4':
            var.client = 'Melon'
            self.options()
        elif option == '5':
            var.client = 'BatMod'
            self.options()
        elif option == '6':
            var.client = 'Forge'
            self.options()
        else:
            self.set_client()

    def check_mods(self):
        try:
            dirhash = checksumdir.dirhash(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods')
        except:
            os.mkdir(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods')
            dirhash = checksumdir.dirhash(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods')
        correct_hash = requests.get('http://blauncher.atwebpages.com/chash').text
        if str(dirhash) != str(correct_hash):
            try:
                shutil.rmtree(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods')
                os.mkdir(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods')
            except:
                try:
                    os.mkdir(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods')
                except:
                    pass
            latest = requests.get('http://blauncher.atwebpages.com/pack_url').text
            print(var.red + middle('Modpack letöltése...'))
            urllib.request.urlretrieve(str(latest), f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods.zip')
            Archive(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods.zip').extractall(
                f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods')
            os.remove(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\mods.zip')
            self.check_mods()

    def launch(self):
        global uuid, user
        var.rpc_status = 'Launching Client...'
        self.clear()
        self.name()

        if var.is_vanity != 'True' and var.is_vanity != 'False':
            var.is_vanity = 'True'

        if var.is_vanity == 'True':
            var.server_url = 'play.vanityempire.hu:1999'

        if var.is_vanity == 'False':
            sid = 'X'
            uuid = 'X'

        if var.client == 'Lunar' and var.is_vanity == 'False':
            user = var.username
            print(f'                                                Server IP:\n')
            print(f'                                                {var.pointer} ', end='')
            var.server_url = input()

        self.clear()
        self.name()
        with open(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\config.json', 'w') as file:
            file.write(
                f'{self.encrypt(var.username)}\n{self.encrypt(var.password)}\n{self.encrypt(var.ram)}\n{self.encrypt(var.client)}\n{self.encrypt(var.rc)}\n{self.encrypt(var.heapdump)}\n{self.encrypt(var.twofa)}\n{self.encrypt(var.is_rpc)}\n{self.encrypt(var.is_vanity)}')
        with open(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\theme.json', 'w') as theme:
            theme.write(f'{self.encrypt(var.cyan)}\n{self.encrypt(var.g)}\n{self.encrypt(var.red)}')
        if var.is_vanity == 'True':
            if var.twofa == True or var.twofa == 'True':
                print(f'                                                2FA:\n')
                print(f'                                                {var.pointer} ', end='')
                var_content = input('')
                var.twofa_value = var_content.replace(' ', '')
                self.clear()
                self.name()
        try:
            if var.ram == '' or var.ram == None or var.ram == 'None':
                print(var.red + middle('Ram nincs megadva!') + var.r)
                sleep(3)
                self.main_screen()
            elif int(var.ram) < 1000:
                print(var.red + middle('1000MB RAM alatt a játék nem fog elindulni!') + var.r)
                sleep(3)
                self.main_screen()
        except:
            print(var.red + middle('Ram rosszul lett megadva!') + var.r)
            sleep(3)
            self.main_screen()
        if var.is_vanity == 'True':
            print(middle('Bejelentkezés...'))
            with requests.Session() as s:
                if not var.exit:
                    fields = s.get('http://blauncher.atwebpages.com/fields', verify=False)
            field_print = str(fields.text).split(':')
            payload = {field_print[0]: var.username, field_print[1]: var.password, "twofact": var.twofa_value}
            try:
                if not var.exit:
                    response = requests.post('https://kliens.vanityempire.hu/login.php',
                                             headers={'Accept': 'text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2',
                                                      'Connection': 'keep-alive', 'Content-Type': 'application/json',
                                                      'Host': 'kliens.vanityempire.hu',
                                                      'User-Agent': 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.4; '
                                                                    'en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2'},
                                             json=payload)
            except Exception as e:
                print(var.red + middle('Hálózati hiba!') + var.r)
                print(var.red + middle(f'({e})'))
                input()
                self.main_screen()
            if '{"error":"adathiba"' in response.text:
                print(var.red + middle('Rossz felhasználónév/jelszó!') + var.r)
                sleep(2)
                self.main_screen()
            elif '"sessionId"' in response.text:
                print(var.g + middle('Sikeres belépés!') + var.r)
                sleep(1.4)
            self.clear()
            self.name()
            try:
                obj = json.loads(response.text)
            except:
                print(var.red + middle('Hálózati hiba!') + var.r)
                print(var.red + middle(f'({response.status_code})') + var.r)
                sleep(6)
                self.main_screen()

            if var.username == '' or var.username == 'None' or var.username == None:
                print(var.red + middle('Felhasználónév nincs megadva!') + var.r)
                sleep(3)
                self.main_screen()
            if var.password == '' or var.password == 'None' or var.password == None:
                print(var.red + middle('Jelszó nincs megadva!') + var.r)
                sleep(3)
                self.main_screen()

            try:
                sid = obj["sessionId"]
            except:
                print(var.red + middle('2FA szükséges!') + var.r)
                sleep(3)
                self.main_screen()
            uuid = obj["uuid"]
            user = obj["username"]

        print(middle(f'{var.client} indítása...'))
        if var.is_vanity == 'False':
            sid = 'X'
            uuid = 'X'
            user = var.username

        def started():
            var.rpc_status = f'Playing as {var.username}'
            print(var.g + middle(f'{var.client} elindítva! ') + var.r)

        if var.client == 'CheatBreaker':
            args = r'javaw.exe "-Dos.name=Windows 10" -Dos.version=10.0REPLACEMEHEAPDUMP ' \
                   r'-Djava.library.path="C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\lib" ' \
                   r'-Dminecraft.launcher.brand=minecraft-launcher -Dminecraft.launcher.version=2.2.3965 ' \
                   r'"-Dminecraft.client.jar=C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\launcher\\cb.jar' \
                   r'" -cp "C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\mojang\\netty\\1' \
                   r'.6\\netty-1.6.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\org\\ow2' \
                   r'\\asm\\asm-all\\5.0.3\\asm-all-5.0.3.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\net\\minecraft\\launchwrapper\\1.7\\launchwrapper-1.7.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.blauncher\\libraries\\oshi-project\\oshi-core\\1.1\\oshi-core-1.1.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\net\\java\\dev\\jna\\jna\\3.4' \
                   r'.0\\jna-3.4.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\net\\java' \
                   r'\\dev\\jna\\platform\\3.4.0\\platform-3.4.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\com\\ibm\\icu\\icu4j-core-mojang\\51.2\\icu4j-core-mojang-51.2.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\net\\sf\\jopt-simple\\jopt' \
                   r'-simple\\4.6\\jopt-simple-4.6.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\com\\paulscode\\codecjorbis\\20101023\\codecjorbis-20101023.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\paulscode\\codecwav\\20101023' \
                   r'\\codecwav-20101023.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com' \
                   r'\\paulscode\\libraryjavasound\\20101123\\libraryjavasound-20101123.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.blauncher\\libraries\\com\\paulscode\\librarylwjglopenal\\20100824' \
                   r'\\librarylwjglopenal-20100824.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\com\\paulscode\\soundsystem\\20120107\\soundsystem-20120107.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\io\\netty\\netty-all\\4.0.23.Final' \
                   r'\\netty-all-4.0.23.Final.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries' \
                   r'\\com\\google\\guava\\guava\\17.0\\guava-17.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\org\\apache\\commons\\commons-lang3\\3.3.2\\commons-lang3-3.3.2.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\commons-io\\commons-io\\2.4' \
                   r'\\commons-io-2.4.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\commons' \
                   r'-codec\\commons-codec\\1.9\\commons-codec-1.9.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\net\\java\\jinput\\jinput\\2.0.5\\jinput-2.0.5.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\net\\java\\jutils\\jutils\\1.0.0' \
                   r'\\jutils-1.0.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com' \
                   r'\\google\\code\\gson\\gson\\2.2.4\\gson-2.2.4.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\com\\mojang\\authlib\\1.5.21\\authlib-1.5.21.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\mojang\\realms\\1.7.59\\realms-1' \
                   r'.7.59.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache' \
                   r'\\commons\\commons-compress\\1.8.1\\commons-compress-1.8.1.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.blauncher\\libraries\\org\\apache\\httpcomponents\\httpclient\\4.3.3\\httpclient-4.3' \
                   r'.3.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\commons-logging' \
                   r'\\commons-logging\\1.1.3\\commons-logging-1.1.3.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\org\\apache\\httpcomponents\\httpcore\\4.3.2\\httpcore-4.3.2.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache\\logging\\log4j' \
                   r'\\log4j-api\\2.0-beta9\\log4j-api-2.0-beta9.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\org\\apache\\logging\\log4j\\log4j-core\\2.0-beta9\\log4j-core-2.0' \
                   r'-beta9.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\org\\lwjgl\\lwjgl' \
                   r'\\lwjgl\\2.9.4-nightly-20150209\\lwjgl-2.9.4-nightly-20150209.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.blauncher\\libraries\\org\\lwjgl\\lwjgl\\lwjgl_util\\2.9.4-nightly-20150209' \
                   r'\\lwjgl_util-2.9.4-nightly-20150209.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\tv\\twitch\\twitch\\6.5\\twitch-6.5.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\launcher\\cb.jar" -XmxREPLACEMERAMM -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC ' \
                   r'-XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M ' \
                   r'Start --username REPLACEMEMCUSER --version "Offline CheatBreaker 1.8.9" --gameDir ' \
                   r'"C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher" --assetsDir ' \
                   r'"C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\assets" --assetIndex 1.8 --uuid ' \
                   r'REPLACEMEUUID --accessToken REPLACEMEAT --userProperties {} --userType legacy'.replace(
                'REPLACEMEUUID', uuid).replace('REPLACEMEMCUSER', user).replace('REPLACEMEUSER', var.winuser).replace(
                'REPLACEMELIBPATH', f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\lib').replace(
                'REPLACEMERAM', var.ram).replace('REPLACEMEAT', sid)
            if var.heapdump == 'True' or var.heapdump == True:
                args = args.replace('REPLACEMEHEAPDUMP',
                                    '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe'
                                    '.heapdump')
            else:
                args = args.replace('REPLACEMEHEAPDUMP', '')
            if os.path.exists('C:\\Program Files\\Java\\jre1.8.0_301\\bin'):
                os.chdir('C:\\Program Files\\Java\\jre1.8.0_301\\bin')
            install_cheatbreaker()
            started()
            os.system(args)
            self.main_screen()

        elif var.client == 'BatMod':
            args = r'javaw.exe "-Dos.name=Windows 10" -Dos.version=10.0REPLACEMEHEAPDUMP ' \
                   r'-Djava.library.path="REPLACEMELIBPATH" -Dminecraft.launcher.brand=minecraft-launcher ' \
                   r'-Dminecraft.launcher.version=2.2.3965 ' \
                   r'-Dminecraft.client.jar="C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\launcher\bm.jar" -cp ' \
                   r'"C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\com\mojang\netty\1.6\netty-1.6.jar' \
                   r';C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\oshi-project\oshi-core\1.1\oshi' \
                   r'-core-1.1.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\net\java\dev\jna\jna\3' \
                   r'.4.0\jna-3.4.0.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\net\java\dev\jna' \
                   r'\platform\3.4.0\platform-3.4.0.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries' \
                   r'\com\ibm\icu\icu4j-core-mojang\51.2\icu4j-core-mojang-51.2.jar;C:\Users\REPLACEMEUSER\AppData' \
                   r'\Roaming\.blauncher\libraries\net\sf\jopt-simple\jopt-simple\4.6\jopt-simple-4.6.jar;C:\Users' \
                   r'\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\com\paulscode\codecjorbis\20101023' \
                   r'\codecjorbis-20101023.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\com' \
                   r'\paulscode\codecwav\20101023\codecwav-20101023.jar;C:\Users\REPLACEMEUSER\AppData\Roaming' \
                   r'\.blauncher\libraries\com\paulscode\libraryjavasound\20101123\libraryjavasound-20101123.jar;C' \
                   r':\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\com\paulscode\librarylwjglopenal' \
                   r'\20100824\librarylwjglopenal-20100824.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher' \
                   r'\libraries\com\paulscode\soundsystem\20120107\soundsystem-20120107.jar;C:\Users\REPLACEMEUSER' \
                   r'\AppData\Roaming\.blauncher\libraries\io\netty\netty-all\4.0.23.Final\netty-all-4.0.23.Final.jar' \
                   r';C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\com\google\guava\guava\17.0\guava' \
                   r'-17.0.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\org\apache\commons\commons' \
                   r'-lang3\3.3.2\commons-lang3-3.3.2.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries' \
                   r'\commons-io\commons-io\2.4\commons-io-2.4.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher' \
                   r'\libraries\commons-codec\commons-codec\1.9\commons-codec-1.9.jar;C:\Users\REPLACEMEUSER\AppData' \
                   r'\Roaming\.blauncher\libraries\net\java\jinput\jinput\2.0.5\jinput-2.0.5.jar;C:\Users' \
                   r'\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\net\java\jutils\jutils\1.0.0\jutils-1.0.0' \
                   r'.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\com\google\code\gson\gson\2.2.4' \
                   r'\gson-2.2.4.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.vanityempire.hu\libraries\com\mojang' \
                   r'\authlib\1.5.21\authlib-1.5.21.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries' \
                   r'\com\mojang\realms\1.7.39\realms-1.7.39.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher' \
                   r'\libraries\org\apache\commons\commons-compress\1.8.1\commons-compress-1.8.1.jar;C:\Users' \
                   r'\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\org\apache\httpcomponents\httpclient\4.3.3' \
                   r'\httpclient-4.3.3.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\commons' \
                   r'-logging\commons-logging\1.1.3\commons-logging-1.1.3.jar;C:\Users\REPLACEMEUSER\AppData\Roaming' \
                   r'\.blauncher\libraries\org\apache\httpcomponents\httpcore\4.3.2\httpcore-4.3.2.jar;C:\Users' \
                   r'\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\org\apache\logging\log4j\log4j-api\2.0-beta9' \
                   r'\log4j-api-2.0-beta9.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\org\apache' \
                   r'\logging\log4j\log4j-core\2.0-beta9\log4j-core-2.0-beta9.jar;C:\Users\REPLACEMEUSER\AppData' \
                   r'\Roaming\.blauncher\libraries\org\lwjgl\lwjgl\lwjgl\2.9.4-nightly-20150209\lwjgl-2.9.4-nightly' \
                   r'-20150209.jar;C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\libraries\org\lwjgl\lwjgl' \
                   r'\lwjgl_util\2.9.4-nightly-20150209\lwjgl_util-2.9.4-nightly-20150209.jar;C:\Users\REPLACEMEUSER' \
                   r'\AppData\Roaming\.blauncher\libraries\tv\twitch\twitch\6.5\twitch-6.5.jar;C:\Users\REPLACEMEUSER' \
                   r'\AppData\Roaming\.blauncher\launcher\\bm.jar" -XmxREPLACEMERAMM -XX:+UnlockExperimentalVMOptions ' \
                   r'-XX:+UseG1GC -XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 ' \
                   r'-XX:G1HeapRegionSize=32M ' \
                   r'-Dlog4j.configurationFile="C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher\assets\log_configs' \
                   r'\client-1.7.xml" net.minecraft.client.main.Main --username REPLACEMEMCUSER --version BatMod ' \
                   r'--gameDir "C:\Users\REPLACEMEUSER\AppData\Roaming\.blauncher" --assetsDir ' \
                   r'"C:\Users\REPLACEMEUSER\AppData\Roaming\.vanityempire.hu\assets" --assetIndex 1.8 --uuid ' \
                   r'REPLACEMEUUID --accessToken REPLACEMEAT --userProperties {} --userType legacy'.replace(
                'REPLACEMEACCESSTOKEN', sid).replace('REPLACEMEUUID', uuid).replace('REPLACEMEMCUSER', user).replace(
                'REPLACEMEUSER', var.winuser).replace('REPLACEMELIBPATH',
                                                      f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\lib').replace(
                'REPLACEMERAM', var.ram).replace('REPLACEMEAT', sid)
            if var.heapdump == 'True' or var.heapdump == True:
                args = args.replace('REPLACEMEHEAPDUMP',
                                    '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe'
                                    '.heapdump')
            else:
                args = args.replace('REPLACEMEHEAPDUMP', '')
            if os.path.exists('C:\\Program Files\\Java\\jre1.8.0_301\\bin'):
                os.chdir('C:\\Program Files\\Java\\jre1.8.0_301\\bin')
            install_batmod()
            started()
            os.system(args)
            self.main_screen()

        elif var.client == 'Melon':
            args = r'javaw.exe "-Dos.name=Windows 10" -Dos.version=10.0REPLACEMEHEAPDUMP ' \
                   r'-Djava.library.path="REPLACEMELIBPATH" -Dminecraft.launcher.brand=minecraft-launcher ' \
                   r'-Dminecraft.launcher.version=2.2.3965 ' \
                   r'"-Dminecraft.client.jar=C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\launcher\\mc.jar' \
                   r'" -cp "C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\melonclient' \
                   r'\\MelonClient\\0.1-BETA\\MelonClient-0.1-BETA.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\optifine\\launchwrapper-of\\2.2\\launchwrapper-of-2.2.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\optifine\\OptiFine\\1.8.9_HD_U_M5' \
                   r'\\OptiFine-1.8.9_HD_U_M5.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries' \
                   r'\\com\\mojang\\netty\\1.6\\netty-1.6.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\oshi-project\\oshi-core\\1.1\\oshi-core-1.1.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.blauncher\\libraries\\net\\java\\dev\\jna\\jna\\3.4.0\\jna-3.4.0.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\net\\java\\dev\\jna\\platform\\3.4.0' \
                   r'\\platform-3.4.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\ibm' \
                   r'\\icu\\icu4j-core-mojang\\51.2\\icu4j-core-mojang-51.2.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.blauncher\\libraries\\net\\sf\\jopt-simple\\jopt-simple\\4.6\\jopt-simple-4.6.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\paulscode\\codecjorbis' \
                   r'\\20101023\\codecjorbis-20101023.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\com\\paulscode\\codecwav\\20101023\\codecwav-20101023.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.blauncher\\libraries\\com\\paulscode\\libraryjavasound\\20101123' \
                   r'\\libraryjavasound-20101123.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\com\\paulscode\\librarylwjglopenal\\20100824\\librarylwjglopenal-20100824.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\paulscode\\soundsystem' \
                   r'\\20120107\\soundsystem-20120107.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\io\\netty\\netty-all\\4.0.23.Final\\netty-all-4.0.23.Final.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\google\\guava\\guava\\17.0\\guava' \
                   r'-17.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache' \
                   r'\\commons\\commons-lang3\\3.3.2\\commons-lang3-3.3.2.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.blauncher\\libraries\\commons-io\\commons-io\\2.4\\commons-io-2.4.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\commons-codec\\commons-codec\\1.9' \
                   r'\\commons-codec-1.9.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\net' \
                   r'\\java\\jinput\\jinput\\2.0.5\\jinput-2.0.5.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\net\\java\\jutils\\jutils\\1.0.0\\jutils-1.0.0.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\com\\google\\code\\gson\\gson\\2.2.4' \
                   r'\\gson-2.2.4.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com' \
                   r'\\mojang\\authlib\\1.5.21\\authlib-1.5.21.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.blauncher\\libraries\\com\\mojang\\realms\\1.7.59\\realms-1.7.59.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache\\commons\\commons-compress\\1.8.1' \
                   r'\\commons-compress-1.8.1.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries' \
                   r'\\org\\apache\\httpcomponents\\httpclient\\4.3.3\\httpclient-4.3.3.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.blauncher\\libraries\\commons-logging\\commons-logging\\1.1.3\\commons' \
                   r'-logging-1.1.3.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\org' \
                   r'\\apache\\httpcomponents\\httpcore\\4.3.2\\httpcore-4.3.2.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.blauncher\\libraries\\org\\apache\\logging\\log4j\\log4j-api\\2.0-beta9\\log4j-api-2' \
                   r'.0-beta9.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache' \
                   r'\\logging\\log4j\\log4j-core\\2.0-beta9\\log4j-core-2.0-beta9.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.blauncher\\libraries\\org\\lwjgl\\lwjgl\\lwjgl\\2.9.4-nightly-20150209' \
                   r'\\lwjgl-2.9.4-nightly-20150209.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher' \
                   r'\\libraries\\org\\lwjgl\\lwjgl\\lwjgl_util\\2.9.4-nightly-20150209\\lwjgl_util-2.9.4-nightly' \
                   r'-20150209.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\libraries\\tv\\twitch' \
                   r'\\twitch\\6.5\\twitch-6.5.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\launcher' \
                   r'\\mc.jar" -XmxREPLACEMERAMM -XX:+UnlockExperimentalVMOptions -XX:+UseG1GC ' \
                   r'-XX:G1NewSizePercent=20 -XX:G1ReservePercent=20 -XX:MaxGCPauseMillis=50 -XX:G1HeapRegionSize=32M ' \
                   r'-Dlog4j.configurationFile="C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.minecraft\\assets' \
                   r'\\log_configs\\client-1.7.xml" net.minecraft.launchwrapper.Launch --username REPLACEMEMCUSER ' \
                   r'--version "Melon Client" --gameDir ' \
                   r'"C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu" --assetsDir ' \
                   r'"C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\assets" --assetIndex 1.8 --uuid ' \
                   r'REPLACEMEUUID --accessToken REPLACEMEAT --userProperties {} --userType legacy --tweakClass ' \
                   r'me.kaimson.melonclient.launch.MelonClientTweaker'.replace(
                'REPLACEMEUUID', uuid).replace('REPLACEMEMCUSER', user).replace('REPLACEMEUSER', var.winuser).replace(
                'REPLACEMELIBPATH', f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\lib').replace(
                'REPLACEMERAM', var.ram).replace('REPLACEMEAT', sid)
            if var.heapdump == 'True' or var.heapdump == True:
                args = args.replace('REPLACEMEHEAPDUMP',
                                    '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe'
                                    '.heapdump')
            else:
                args = args.replace('REPLACEMEHEAPDUMP', '')
            if os.path.exists('C:\\Program Files\\Java\\jre1.8.0_301\\bin'):
                os.chdir('C:\\Program Files\\Java\\jre1.8.0_301\\bin')
            install_melon()
            started()
            os.system(args)
            self.main_screen()

        elif var.client == 'Forge':
            args = r'javaw.exe -XmxREPLACEMERAMM -XX:+UseConcMarkSweepGC -XX:-UseAdaptiveSizePolicy ' \
                   r'-XX:+CMSParallelRemarkEnabled -XX:+ParallelRefProcEnabled -XX:+CMSClassUnloadingEnabled ' \
                   r'-noverify -XX:+UseCMSInitiatingOccupancyOnly -Dfml.ignoreInvalidMinecraftCertificates=true ' \
                   r'-Dfml.ignorePatchDiscrepancies=true -Djava.net.useSystemProxies=trueREPLACEMEHEAPDUMP ' \
                   r'"-Dos.name=Windows 10" -Dos.version=10.0 ' \
                   r'-Djava.library.path="C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher\\lib" -cp ' \
                   r'"C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\net\\minecraftforge' \
                   r'\\forge\\1.8.9-11.15.1.1722\\forge-1.8.9-11.15.1.1722.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.vanityempire.hu\\libraries\\net\\minecraft\\launchwrapper\\1.12\\launchwrapper-1.12' \
                   r'.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\ow2\\asm\\asm' \
                   r'-all\\5.0.3\\asm-all-5.0.3.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\com\\typesafe\\akka\\akka-actor_2.11\\2.3.3\\akka-actor_2.11-2.3.3.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com\\typesafe\\config\\1.2.1' \
                   r'\\config-1.2.1.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org' \
                   r'\\scala-lang\\scala-actors-migration_2.11\\1.1.0\\scala-actors-migration_2.11-1.1.0.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\scala-lang\\scala' \
                   r'-compiler\\2.11.1\\scala-compiler-2.11.1.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\org\\scala-lang\\plugins\\scala-continuations-library_2.11\\1.0.2' \
                   r'\\scala-continuations-library_2.11-1.0.2.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\org\\scala-lang\\plugins\\scala-continuations-plugin_2.11.1\\1.0' \
                   r'.2\\scala-continuations-plugin_2.11.1-1.0.2.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\org\\scala-lang\\scala-library\\2.11.1\\scala-library-2.11.1.jar' \
                   r';C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\scala-lang\\scala' \
                   r'-parser-combinators_2.11\\1.0.1\\scala-parser-combinators_2.11-1.0.1.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\scala-lang\\scala-reflect' \
                   r'\\2.11.1\\scala-reflect-2.11.1.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\org\\scala-lang\\scala-swing_2.11\\1.0.1\\scala-swing_2.11-1.0.1.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\scala-lang\\scala-xml_2.11' \
                   r'\\1.0.2\\scala-xml_2.11-1.0.2.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\lzma\\lzma\\0.0.1\\lzma-0.0.1.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\net\\sf\\jopt-simple\\jopt-simple\\4.6\\jopt-simple-4.6.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\java3d\\vecmath\\1.5.2' \
                   r'\\vecmath-1.5.2.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\net' \
                   r'\\sf\\trove4j\\trove4j\\3.0.3\\trove4j-3.0.3.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\com\\mojang\\netty\\1.6\\netty-1.6.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.vanityempire.hu\\libraries\\oshi-project\\oshi-core\\1.1\\oshi-core-1.1.jar' \
                   r';C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\net\\java\\dev\\jna' \
                   r'\\jna\\3.4.0\\jna-3.4.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\net\\java\\dev\\jna\\platform\\3.4.0\\platform-3.4.0.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com\\ibm\\icu\\icu4j-core-mojang\\51.2\\icu4j' \
                   r'-core-mojang-51.2.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries' \
                   r'\\net\\sf\\jopt-simple\\jopt-simple\\4.6\\jopt-simple-4.6.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.vanityempire.hu\\libraries\\com\\paulscode\\codecjorbis\\20101023\\codecjorbis' \
                   r'-20101023.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com' \
                   r'\\paulscode\\codecwav\\20101023\\codecwav-20101023.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.vanityempire.hu\\libraries\\com\\paulscode\\libraryjavasound\\20101123' \
                   r'\\libraryjavasound-20101123.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\com\\paulscode\\librarylwjglopenal\\20100824\\librarylwjglopenal-20100824.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com\\paulscode' \
                   r'\\soundsystem\\20120107\\soundsystem-20120107.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\io\\netty\\netty-all\\4.0.23.Final\\netty-all-4.0.23.Final.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com\\google\\guava' \
                   r'\\guava\\17.0\\guava-17.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\org\\apache\\commons\\commons-lang3\\3.3.2\\commons-lang3-3.3.2.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\commons-io\\commons-io\\2.4' \
                   r'\\commons-io-2.4.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries' \
                   r'\\commons-codec\\commons-codec\\1.9\\commons-codec-1.9.jar;C:\\Users\\REPLACEMEUSER\\AppData' \
                   r'\\Roaming\\.vanityempire.hu\\libraries\\net\\java\\jinput\\jinput\\2.0.5\\jinput-2.0.5.jar;C' \
                   r':\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\net\\java\\jutils' \
                   r'\\jutils\\1.0.0\\jutils-1.0.0.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\com\\google\\code\\gson\\gson\\2.2.4\\gson-2.2.4.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com\\mojang\\authlib\\1.5.21\\authlib-1.5.21' \
                   r'.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\com\\mojang' \
                   r'\\realms\\1.7.59\\realms-1.7.59.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\org\\apache\\commons\\commons-compress\\1.8.1\\commons-compress-1.8.1.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\apache\\httpcomponents' \
                   r'\\httpclient\\4.3.3\\httpclient-4.3.3.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\commons-logging\\commons-logging\\1.1.3\\commons-logging-1.1.3' \
                   r'.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\apache' \
                   r'\\httpcomponents\\httpcore\\4.3.2\\httpcore-4.3.2.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\org\\apache\\logging\\log4j\\log4j-api\\2.0-beta9\\log4j-api-2.0' \
                   r'-beta9.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\apache' \
                   r'\\logging\\log4j\\log4j-core\\2.0-beta9\\log4j-core-2.0-beta9.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.vanityempire.hu\\libraries\\org\\lwjgl\\lwjgl\\lwjgl\\2.9.4-nightly' \
                   r'-20150209\\lwjgl-2.9.4-nightly-20150209.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming' \
                   r'\\.vanityempire.hu\\libraries\\org\\lwjgl\\lwjgl\\lwjgl_util\\2.9.4-nightly-20150209\\lwjgl_util' \
                   r'-2.9.4-nightly-20150209.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu' \
                   r'\\libraries\\org\\lwjgl\\lwjgl\\lwjgl-platform\\2.9.4-nightly-20150209\\lwjgl-platform-2.9.4' \
                   r'-nightly-20150209-natives-windows.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire' \
                   r'.hu\\libraries\\net\\java\\jinput\\jinput-platform\\2.0.5\\jinput-platform-2.0.5-natives-windows' \
                   r'.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\tv\\twitch\\twitch' \
                   r'\\6.5\\twitch-6.5.jar;C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries' \
                   r'\\tv\\twitch\\twitch-platform\\6.5\\twitch-platform-6.5-natives-windows-64.jar;C:\\Users' \
                   r'\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\libraries\\tv\\twitch\\twitch-external' \
                   r'-platform\\4.5\\twitch-external-platform-4.5-natives-windows-64.jar;C:\\Users\\REPLACEMEUSER' \
                   r'\\AppData\\Roaming\\.vanityempire.hu\\bin\\minecraft_1.8.jar" net.minecraft.launchwrapper.Launch ' \
                   r'--username REPLACEMEMCUSER --version "Forge 1.8.9" --gameDir ' \
                   r'"C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.blauncher" --assetsDir ' \
                   r'"C:\\Users\\REPLACEMEUSER\\AppData\\Roaming\\.vanityempire.hu\\assets" --assetIndex 1.8 --uuid ' \
                   r'REPLACEMEUUID --accessToken REPLACEMEAT --userProperties {} --userType legacy --tweakClass ' \
                   r'net.minecraftforge.fml.common.launcher.FMLTweaker'.replace(
                'REPLACEMEAT', sid).replace('REPLACEMEUUID', uuid).replace('REPLACEMEMCUSER', user).replace(
                'REPLACEMEUSER', var.winuser).replace('REPLACEMERAM', var.ram)
            if var.heapdump == 'True' or var.heapdump == True:
                args = args.replace('REPLACEMEHEAPDUMP',
                                    '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft.exe'
                                    '.heapdump')
            else:
                args = args.replace('REPLACEMEHEAPDUMP', '')
            if os.path.exists('C:\\Program Files\\Java\\jre1.8.0_301\\bin'):
                os.chdir('C:\\Program Files\\Java\\jre1.8.0_301\\bin')
            if os.path.exists(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.vanityempire.hu\\bin\\minecraft_1.8.jar'):
                self.check_mods()
                started()
                os.system(args)
                self.main_screen()
            else:
                print(var.red + middle('Vanity 1.8-as klienst futtasd le egyszer!') + var.r)
                sleep(3)
                self.main_screen()

        else:
            if var.rc == 'lc':
                md5sum = check_md5sum(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\lc.jar')
            elif var.rc == 'dc':
                md5sum = check_md5sum(f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\dc.jar')

            auth = 'javaw.exe -XX:+UseConcMarkSweepGC -XX:-UseAdaptiveSizePolicy -XX:+CMSParallelRemarkEnabled ' \
                   '-XX:+ParallelRefProcEnabled -XX:+CMSClassUnloadingEnabled -noverify ' \
                   '-XX:+UseCMSInitiatingOccupancyOnly -XmxREPLACEMERAMM ' \
                   '-Dfml.ignoreInvalidMinecraftCertificates=true -Dfml.ignorePatchDiscrepancies=true ' \
                   '-Djava.net.useSystemProxies=trueREPLACEMEHEAPDUMP "-Dos.name=Windows 10" -Dos.version=10.0 ' \
                   '-Djava.library.path="REPLACEMELIBPATH" -Dminecraft.launcher.brand=java-minecraft-launcher ' \
                   '-Dminecraft.launcher.version=1.6.84-j ' \
                   '-Dminecraft.client.jar="C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\launcher' \
                   '\\CLIENTNAME.jar" -cp "C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\com' \
                   '\\mojang\\netty\\1.6\\netty-1.6.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher' \
                   '\\libraries\\oshi-project\\oshi-core\\1.1\\oshi-core-1.1.jar;C:\\Users\\REPLACEMEUSERNAME' \
                   '\\AppData\\Roaming\\.blauncher\\libraries\\net\\java\\dev\\jna\\jna\\3.4.0\\jna-3.4.0.jar;C' \
                   ':\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\net\\java\\dev\\jna' \
                   '\\platform\\3.4.0\\platform-3.4.0.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher' \
                   '\\libraries\\com\\ibm\\icu\\icu4j-core-mojang\\51.2\\icu4j-core-mojang-51.2.jar;C:\\Users' \
                   '\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\net\\sf\\jopt-simple\\jopt-simple' \
                   '\\4.6\\jopt-simple-4.6.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries' \
                   '\\com\\paulscode\\codecjorbis\\20101023\\codecjorbis-20101023.jar;C:\\Users\\REPLACEMEUSERNAME' \
                   '\\AppData\\Roaming\\.blauncher\\libraries\\com\\paulscode\\codecwav\\20101023\\codecwav-20101023' \
                   '.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\com\\paulscode' \
                   '\\libraryjavasound\\20101123\\libraryjavasound-20101123.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData' \
                   '\\Roaming\\.blauncher\\libraries\\com\\paulscode\\librarylwjglopenal\\20100824' \
                   '\\librarylwjglopenal-20100824.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher' \
                   '\\libraries\\com\\paulscode\\soundsystem\\20120107\\soundsystem-20120107.jar;C:\\Users' \
                   '\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\io\\netty\\netty-all\\4.0.23.Final' \
                   '\\netty-all-4.0.23.Final.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher' \
                   '\\libraries\\com\\google\\guava\\guava\\17.0\\guava-17.0.jar;C:\\Users\\REPLACEMEUSERNAME' \
                   '\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache\\commons\\commons-lang3\\3.3.2\\commons' \
                   '-lang3-3.3.2.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\commons' \
                   '-io\\commons-io\\2.4\\commons-io-2.4.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming' \
                   '\\.blauncher\\libraries\\commons-codec\\commons-codec\\1.9\\commons-codec-1.9.jar;C:\\Users' \
                   '\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\net\\java\\jinput\\jinput\\2.0.5' \
                   '\\jinput-2.0.5.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\net' \
                   '\\java\\jutils\\jutils\\1.0.0\\jutils-1.0.0.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming' \
                   '\\.blauncher\\libraries\\com\\google\\code\\gson\\gson\\2.2.4\\gson-2.2.4.jar;C:\\Users' \
                   '\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\com\\mojang\\authlib\\1.5.21' \
                   '\\authlib-1.5.21.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\com' \
                   '\\mojang\\realms\\1.7.59\\realms-1.7.59.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming' \
                   '\\.blauncher\\libraries\\org\\apache\\commons\\commons-compress\\1.8.1\\commons-compress-1.8.1' \
                   '.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache' \
                   '\\httpcomponents\\httpclient\\4.3.3\\httpclient-4.3.3.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData' \
                   '\\Roaming\\.blauncher\\libraries\\commons-logging\\commons-logging\\1.1.3\\commons-logging-1.1.3' \
                   '.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache' \
                   '\\httpcomponents\\httpcore\\4.3.2\\httpcore-4.3.2.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData' \
                   '\\Roaming\\.blauncher\\libraries\\org\\apache\\logging\\log4j\\log4j-api\\2.0-beta9\\log4j-api-2' \
                   '.0-beta9.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\org\\apache' \
                   '\\logging\\log4j\\log4j-core\\2.0-beta9\\log4j-core-2.0-beta9.jar;C:\\Users\\REPLACEMEUSERNAME' \
                   '\\AppData\\Roaming\\.blauncher\\libraries\\org\\lwjgl\\lwjgl\\lwjgl\\2.9.4-nightly-20150209' \
                   '\\lwjgl-2.9.4-nightly-20150209.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher' \
                   '\\libraries\\org\\lwjgl\\lwjgl\\lwjgl_util\\2.9.4-nightly-20150209\\lwjgl_util-2.9.4-nightly' \
                   '-20150209.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\libraries\\tv\\twitch' \
                   '\\twitch\\6.5\\twitch-6.5.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.minecraft' \
                   '\\libraries\\misc\\tweaker\\1.2\\tweaker-1.2.jar;C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming' \
                   '\\.minecraft\\libraries\\misc\\tweaker\\net.minecraft.client.main.Main\\tweakesxyssr-net' \
                   '.minecraft.client.main.Main.jar;C:\\Users\\REPLACEMEUSERNAME\\Appdata\\Roaming\\.blauncher' \
                   '\\launcher\\CLIENTNAME.jar" net.minecraft.client.main.Main --username REPLACEMEMCUSER --version ' \
                   'client --resourcePackDir ' \
                   '"C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher\\v1.8\\resourcepacks" --gameDir ' \
                   '"C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.blauncher" --assetsDir ' \
                   '"C:\\Users\\REPLACEMEUSERNAME\\AppData\\Roaming\\.vanityempire.hu\\assets" --assetIndex 1.8 ' \
                   '--uuid REPLACEMEUUID --accessToken REPLACEMEACCESSTOKEN --userProperties {} --userType legacy ' \
                   '--width 925 --height 530 --server "REPLACEMESERVER"'.replace(
                'REPLACEMESERVER', var.server_url).replace('REPLACEMEACCESSTOKEN', sid).replace('REPLACEMEUUID',
                                                                                                uuid).replace(
                'REPLACEMEMCUSER', user).replace('REPLACEMEUSERNAME', var.winuser).replace('REPLACEMELIBPATH',
                                                                                           f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\lib').replace(
                'REPLACEMERAM', var.ram).replace('CLIENTNAME', var.rc)
            if md5sum == '65627d3205d9d25f9c73bb16bc35b054' or md5sum == '8e8cae418c6f85c1368792c022c20b63':
                if var.heapdump == 'True' or var.heapdump == True:
                    auth = auth.replace('REPLACEMEHEAPDUMP',
                                        '-XX:HeapDumpPath=MojangTricksIntelDriversForPerformance_javaw.exe_minecraft'
                                        '.exe.heapdump')
                else:
                    auth = auth.replace('REPLACEMEHEAPDUMP', '')
                if os.path.exists('C:\\Program Files\\Java\\jre1.8.0_301\\bin'):
                    os.chdir('C:\\Program Files\\Java\\jre1.8.0_301\\bin')
                started()
                os.system(auth)
            else:
                print(var.red + middle('Kliens helytelenül letöltve!') + var.r)
                sleep(0.5)
                print(var.red + middle('Kliens újratelepítése...') + var.r)
                if var.rc == 'lc':
                    urllib.request.urlretrieve('https://www.dropbox.com/s/11xrh03k9f1wj02/LC.jar?dl=1',
                                               f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\lc '
                                               f'.jar')
                elif var.rc == 'dc':
                    urllib.request.urlretrieve('https://www.dropbox.com/s/660uegvhlqnylg8/dc.jar?dl=1',
                                               f'C:\\Users\\{var.winuser}\\AppData\\Roaming\\.blauncher\\launcher\\dc'
                                               f'.jar')
                print(var.g + middle('Kliens újratelepítve!') + var.r)
                sleep(3)
                self.launch()
            self.main_screen()


if __name__ == '__main__':
    set_title('BLauncher | Nandi#0001')

    Thread(target=Main, ).start()
    while not var.exit:
        try:
            sleep(0.5)
        except:
            os._exit(0)
