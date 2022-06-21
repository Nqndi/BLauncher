from getpass import getuser
from hashlib import md5
from shutil import copyfile
from threading import Thread
from time import sleep

import io
import os
import requests
import urllib.request
import urllib3
from colorama import init, Fore
from pyunpack import Archive


class vars:
    exit = False
    red = Fore.RED
    reset = Fore.RESET
    cyan = Fore.LIGHTBLUE_EX
    informative = f'[{cyan}~{reset}]'
    error = f'[{red}!{reset}]'
    blauncher_dir = f'{os.getenv("APPDATA")}\\.blauncher'


def check_md5sum(file):
    md5_hash = md5()
    a_file = open(file, "rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest


class main:
    def __init__(self):
        Thread(target=self.blauncher, ).start()
        while not vars.exit:
            sleep(0.1)

    def update_status(self, update_status, url, saveas):
        while 1:
            try:
                resp = urllib.request.urlopen(url)
                break
            except:
                print('Unknown error occured while downloading BLauncher, retrying...')
                sleep(0.1)
        length = resp.getheader('content-length')
        if length:
            length = int(length)
            blocksize = max(4096, length // 100)
        else:
            blocksize = 1000000
        buf = io.BytesIO()
        size = 0
        while True:
            buf1 = resp.read(blocksize)
            if not buf1:
                break
            buf.write(buf1)
            size += len(buf1)
            try:
                if length:
                    print(update_status.replace('REPLACE', str(int(size / 1048576))).replace('TOTALSIZE', str(int(
                        length / 1048576))), end='\r')
            except:
                print(update_status.replace('REPLACE', 'null').replace('TOTALSIZE', 'null', end='\r'))
        try:
            print(update_status.replace('REPLACE', str(int(length / 1048576))).replace('TOTALSIZE',
                                                                                       str(int(length / 1048576))))
        except:
            print(update_status.replace('REPLACE', 'null').replace('TOTALSIZE', 'null'))
        with open(saveas, 'wb') as f:
            f.write(buf.getbuffer())

    def blauncher(self):
        try:
            print(f'{vars.informative} Creating directory...')
            os.mkdir(f'{vars.blauncher_dir}')
        except FileExistsError:
            print(f'{vars.error} Directory already exists!')
        print('')
        try:
            print(f'{vars.informative} Creating sub-directory...')
            os.mkdir(f'{vars.blauncher_dir}\\launcher')
        except FileExistsError:
            print(f'{vars.error} Directory already exists!')
        print('')

        try:
            os.remove(f'{vars.blauncher_dir}\\launcher\\client.jar')
        except:
            pass

        if not os.path.exists(f'{vars.blauncher_dir}\\launcher\\lc.jar'):
            self.update_status(f'{vars.informative} Downloading Lunar client... (REPLACE/TOTALSIZE MB)',
                               'https://www.dropbox.com/s/11xrh03k9f1wj02/LC.jar?dl=1',
                               f'{vars.blauncher_dir}\\launcher\\lc.jar')
        else:
            if check_md5sum(f'{vars.blauncher_dir}\\launcher\\lc.jar') == '65627d3205d9d25f9c73bb16bc35b054':
                print(f'{vars.error} Lunar client already installed!')
            else:
                print(f'{vars.error} Bad Lunar client installation! Reinstalling...')
                self.update_status(f'{vars.informative} Downloading Lunar client... (REPLACE/TOTALSIZE MB)',
                                   'https://www.dropbox.com/s/11xrh03k9f1wj02/LC.jar?dl=1',
                                   f'{vars.blauncher_dir}\\launcher\\lc.jar')
        print('')

        if not os.path.exists(f'{vars.blauncher_dir}\\launcher\\dc.jar'):
            self.update_status(f'{vars.informative} Downloading Doge client... (REPLACE/TOTALSIZE MB)',
                               'https://www.dropbox.com/s/660uegvhlqnylg8/dc.jar?dl=1',
                               f'{vars.blauncher_dir}\\launcher\\dc.jar')
        else:
            check_md5sum(f'{vars.blauncher_dir}\\launcher\\dc.jar')
            print(f'{vars.error} Doge client already installed!')
        print('')

        if not os.path.exists(f'{vars.blauncher_dir}\\libraries'):
            self.update_status(f'{vars.informative} Downloading libraries... (REPLACE/TOTALSIZE MB)',
                               'https://www.dropbox.com/s/2fy50egnytp2fwu/libraries.zip?dl=1',
                               f'{vars.blauncher_dir}\\libraries.zip')
            print(f'{vars.informative} Extracting libraries...')
            Archive(f'{vars.blauncher_dir}\\libraries.zip').extractall(f'{vars.blauncher_dir}')
            os.remove(f'{vars.blauncher_dir}\\libraries.zip')
        else:
            print(f'{vars.error} Libraries already installed!')
        print('')

        if not os.path.exists(f'{vars.blauncher_dir}\\lib'):
            self.update_status(f'{vars.informative} Downloading client libraries... (REPLACE/TOTALSIZE MB)',
                               'https://www.dropbox.com/s/lfatlncck33h1pf/lib.zip?dl=1',
                               f'{vars.blauncher_dir}\\lib.zip')
            print(f'{vars.informative} Extracting Client libraries...')
            Archive(f'{vars.blauncher_dir}\\lib.zip').extractall(f'{vars.blauncher_dir}')
            os.remove(f'{vars.blauncher_dir}\\lib.zip')
        else:
            print(f'{vars.error} Client libraries already installed!')
        print('')

        try:
            os.remove(f'{vars.blauncher_dir}\\launcher.exe')
        except:
            pass
        if not os.path.exists(f'{vars.blauncher_dir}\\launcher.exe'):
            with requests.Session() as s:
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                launcher_url = s.get('http://blauncher.atwebpages.com/latest_launcher', headers={'Pragma': 'no-cache'},
                                     verify=False).text
                self.update_status(f'{vars.informative} Downloading Launcher... (REPLACE/TOTALSIZE MB)', launcher_url,
                                   f'{vars.blauncher_dir}\\launcher.exe')
                try:
                    copyfile(f'{vars.blauncher_dir}\\launcher.exe', f'C:\\Users\\{getuser()}\\Desktop\\BLauncher.exe')
                except:
                    try:
                        urllib.request.urlretrieve(launcher_url, f'C:\\Users\\{getuser()}\\Desktop\\BLauncher.exe')
                    except:
                        print(
                            r'\nError occured whilst copying BLauncher to Desktop! You can find the program in %appdata%\.blauncher\n')
        else:
            print(f'{vars.error} Launcher already installed!')
        print()

        try:
            os.remove(f'{vars.blauncher_dir}\\updater.exe')
        except:
            pass
        if not os.path.exists(f'{vars.blauncher_dir}\\updater.exe'):
            with requests.Session() as s:
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                updater_url = s.get('http://blauncher.atwebpages.com/latest_updater', headers={'Pragma': 'no-cache'},
                                    verify=False).text
                self.update_status(f'{vars.informative} Downloading Updater... (REPLACE/TOTALSIZE MB)', updater_url,
                                   f'{vars.blauncher_dir}\\updater.exe')

        write_v = open(f'{vars.blauncher_dir}\\version.txt', 'w')
        with requests.Session() as s:
            latest_version = s.get('http://blauncher.atwebpages.com/latest_version', headers={'Pragma': 'no-cache'},
                                   verify=False).text
        write_v.writelines(latest_version)
        write_v.close()

        print(f'\nBLauncher has been installed!')
        asd = input('\nPress enter to exit.')
        vars.exit = True
        try:
            os.startfile(f'{os.getenv("APPDATA")}\\.blauncher\\launcher.exe')
        except:
            pass


if __name__ == '__main__':
    init()
    main()
