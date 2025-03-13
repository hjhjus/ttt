# -*- coding: utf-8 -*-
import concurrent.futures
import sys, os, random, string
# from os import listdir
# from os.path import isfile, join
#
# import hmac, base64, struct, hashlib, time

from datetime import datetime
import psutil
import re

import time
import random
import pyperclip
import shutil
# from operator import itemgetter
#
# from subprocess import Popen
# import multiprocessing
# from multiprocessing.pool import Pool
from concurrent.futures import *
from concurrent.futures import ThreadPoolExecutor

import threading
# import concurrent.futures

from PyQt5 import QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import configparser
from functools import lru_cache
@lru_cache(maxsize=1)
def load_config():
    config = configparser.ConfigParser()
    config.read('./app.ini')
    return config
config_app = load_config()

import secrets

import json
import requests
import pyotp

# Library
import logging
import subprocess
from subprocess import Popen, PIPE
# from imap_tools import MailBox, AND
from imbox import Imbox

try:
    from gui.gui_main import Ui_Main
    from gui.gui_facebook import Ui_Facebook
    from gui.gui_market import Ui_Marketplace
    from gui.gui_google import Ui_Google

    from library.mail._mail import Mail, EmailChecker
    from library.logger import Handler, Formatter
    from library._database import MyData
    # from library.facebook import ChromeFingerprint
    from library._browsers import BrowserAuto, Marketplace, Google
    # from library.emulator import Emulator
    # from library._ldplayer import Emulator, FakeInfos
    # from library._memu import Emulator, FakeInfos
    from library._noxplayer import Emulator, FakeInfos
    # from library.qconcurrent import ThreadPoolExecutor
    from library._spoof.spoof_timezone import TimezoneSys, Score
    from library._spoof.spoof_geo import Geo
    from library._proxy.proxy_server import ProxyServer, LocalIpAddress, ForwardProxy, ProxySevices
    # from library._proxy.forward_proxy_auth import ProxyServer, LocalIpAddress
    from library._graph import GraphFacebook
except:
    from gui.gui_main import Ui_Main
    from gui.gui_facebook import Ui_Facebook
    from gui.gui_market import Ui_Marketplace
    from gui.gui_google import Ui_Google

    from library.logger import Handler, Formatter
    from library.mail._mail import Mail, EmailChecker
    from library._database import MyData
    # from .library.facebook import ChromeFingerprint, FirefoxFingerprint
    from library._browsers import BrowserAuto, Marketplace, Google
    # from .library.emulator import Emulator'
    from library._noxplayer import Emulator, FakeInfos
    # from .library._ldplayer import Emulator, FakeInfos
    # from .library._memu import MemuEmulator
    # from .library.qconcurrent import ThreadPoolExecutor
    from library._spoof.spoof_timezone import TimezoneSys, Score
    from library._spoof.spoof_geo import Geo
    from library._proxy.proxy_server import ProxyServer, LocalIpAddress, ForwardProxy
    # from .library._proxy.forward_proxy_auth import ProxyServer, LocalIpAddress
    from library._graph import GraphFacebook
#
CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))

# chrome
CHROME_PROFILES = CURRENT_FOLDER + config_app['CHROMES']['PROFILES_FACEBOOK']
CHROME_EXTENSIONS = CURRENT_FOLDER + config_app['CHROMES']['CHROME_EXTENSIONS']
# CHROME_EXTENSIONS = str(CHROME_EXTENSIONS).replace('/', '\\')

PROFILES_MARKETPLACE = rf"{CURRENT_FOLDER}{config_app['CHROMES']['PROFILES_MARKETPLACE']}"
PROFILES_GOOGLE = rf"{CURRENT_FOLDER}{config_app['CHROMES']['PROFILES_GOOGLE']}"

# app
DATA = CURRENT_FOLDER + config_app['APP']['DATA']
UID_TXT = CURRENT_FOLDER + config_app['APP']['UID_TXT']
SQLITE = CURRENT_FOLDER + config_app['APP']['SQLITE']
BACKUP = CURRENT_FOLDER + config_app['APP']['BACKUP_DATA']
BACKUP_VIA_COMMENTS = CURRENT_FOLDER + config_app['APP']['BACKUP_VIA_COMMENTS']
BACKUP_VIA_MESSAGE = CURRENT_FOLDER + config_app['APP']['BACKUP_VIA_MESSAGE']
BACKUP_VIA_PHOTOS = CURRENT_FOLDER + config_app['APP']['BACKUP_VIA_PHOTOS']
PROXIES = CURRENT_FOLDER + config_app['PROXIES']['PATH']

# apps
APPS_DATA = CURRENT_FOLDER + config_app['APPS']['DATA']
APPS_INSTALL = CURRENT_FOLDER + config_app['APPS']['APPS_INSTALL']
# APPS_DATA = str(APPS_DATA).replace('/', '\\')

#
PROXYSERVICES = CURRENT_FOLDER + config_app['PROXYSERVICES']['DATA']

# user-agent
USERAGENT_COMPUTER = CURRENT_FOLDER + config_app['USERAGENT']['USERAGENT_COMPUTER']
USERAGENT_MOBILE = CURRENT_FOLDER + config_app['USERAGENT']['USERAGENT_MOBILE']

# PAGE
PAGE_PATH = CURRENT_FOLDER + config_app['PAGE']['PATH']

# MAIL
MAIL_DATA = CURRENT_FOLDER + config_app['MAIL']['MAIL_DATA']
MAIL_IMAP = CURRENT_FOLDER + config_app['MAIL']['MAIL_IMAP']
MAIL_YCHECKER = CURRENT_FOLDER + config_app['MAIL']['MAIL_YCHECKER']

# ADS
ADS_CARD_GOOGLE = CURRENT_FOLDER + config_app['ADS']['ADS_CARD_GOOGLE']
ADS_ADDRESS = CURRENT_FOLDER + config_app['ADS']['ADS_ADDRESS']
ADS_CARD = CURRENT_FOLDER + config_app['ADS']['ADS_CARD']
ADS_GOOGLE_STATUS = CURRENT_FOLDER + config_app['ADS']['ADS_GOOGLE_STATUS']
ADS_GOOGLE_WEB = CURRENT_FOLDER + config_app['ADS']['ADS_GOOGLE_WEB']

# MENU_RIGHT
MENU_RIGHT_GADSENSE_P = CURRENT_FOLDER + config_app['MENU_RIGHT']['GADSENSE']
MENU_RIGHT_GLEVEL_P = CURRENT_FOLDER + config_app['MENU_RIGHT']['GLEVEL']
MENU_RIGHT_KHANG_P = CURRENT_FOLDER + config_app['MENU_RIGHT']['KHANG']
MENU_RIGHT_DEPOSIT_P = CURRENT_FOLDER + config_app['MENU_RIGHT']['DEPOSIT']

# GOOGLE
GOOGLE_STATUS = CURRENT_FOLDER + config_app['GOOGLE']['GOOGLE_FOLDER'] + "google_status.txt"
GOOGLE_LAST = CURRENT_FOLDER + config_app['GOOGLE']['GOOGLE_FOLDER'] + "google_last.txt"
GOOGLE_CAMPS = CURRENT_FOLDER + config_app['GOOGLE']['GOOGLE_FOLDER'] + "google_camps.txt"
GOOGLE_PLAN = CURRENT_FOLDER + config_app['GOOGLE']['GOOGLE_FOLDER'] + "google_plan.txt"

# FACEBOOK
FACEBOOK_STATUS = CURRENT_FOLDER + config_app['FACEBOOK']['FACEBOOK_FOLDER'] + "status.txt"
FACEBOOK_SOURCES = CURRENT_FOLDER + config_app['FACEBOOK']['FACEBOOK_FOLDER'] + "via_sources.txt"
FACEBOOK_TUTS = CURRENT_FOLDER + config_app['FACEBOOK']['FACEBOOK_FOLDER'] + "via_tuts.txt"

FACEBOOK_PLANS = CURRENT_FOLDER + config_app['FACEBOOK']['FACEBOOK_FOLDER'] + "camps_plans.txt"
FACEBOOK_PIXELS = CURRENT_FOLDER + config_app['FACEBOOK']['FACEBOOK_FOLDER'] + "camps_pixels.txt"
FACEBOOK_GROUPS = CURRENT_FOLDER + config_app['FACEBOOK']['FACEBOOK_FOLDER'] + "camps_groups.txt"

# BROWSERS
BROWSERS_USERAGENT_WINDOW = CURRENT_FOLDER + config_app['BROWSERS']['USERAGENT_WINDOW']
BROWSERS_USERAGENT_MACOS = CURRENT_FOLDER + config_app['BROWSERS']['USERAGENT_MACOS']
BROWSERS_GPU_MACOS = CURRENT_FOLDER + config_app['BROWSERS']['GPU_MACOS']
BROWSERS_GPU_WINDOW = CURRENT_FOLDER + config_app['BROWSERS']['GPU_WINDOW']
BROWSERS_LANGUAGE = CURRENT_FOLDER + config_app['BROWSERS']['LANGUAGE']
BROWSERS_WINDOW_SIZE = CURRENT_FOLDER + config_app['BROWSERS']['WINDOW_SIZE']
BROWSERS_MAC = CURRENT_FOLDER + config_app['BROWSERS']['MAC']
BROWSERS_LAN_IP = CURRENT_FOLDER + config_app['BROWSERS']['LAN_IP']

# Global variables
MYDATA = MyData(f'sqlite:///{SQLITE}')

running_count: int = 0
uid_current: int = 0

# Emulator Index
v_index = '0'


class Library(QObject):
    def __init__(self):
        pass

    def pages_config(self, path):
        d = dict()
        with open(path, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            return data
            # for item in data:
            #     d['Id'] = item['Id']
            #     # General
            #     d['G_Name'] = item['General']['Name']
            #     d['G_Desciption'] = item['General']['Desciption']
            #     d['G_Categories'] = []
            #     for g_item in item['General']['Categories']:
            #         d['G_Categories'].append(g_item)
            #     # Contact
            #     d['C_Web'] = item['Contact']['Web']
            #     d['C_Email'] = item['Contact']['Email']
            #     d['C_Phone'] = item['Contact']['Phone']
            #     # Location
            #     d['L_Address'] = item['Location']['Address']
            #     d['L_City'] = item['Location']['City']
            #     d['L_Zipcode'] = item['Location']['Zipcode']
            #     # More
            #     d['M_Policy'] = item['More']['Policy']
            #     d['M_Impressum'] = item['More']['Impressum']
            #     d['M_Products'] = item['More']['Products']
            #     d['M_AddInfomations'] = item['More']['AddInfomations']
        # return d


from multiprocessing import Process
# Tạo ThreadPoolExecutor để xử lý đa luồng
task_executor = ThreadPoolExecutor(max_workers=5)
class MyThread:
    def __init__(self, chromeId, proxyId):
        self.chromeId = chromeId
        self.proxyId = proxyId

    def monitor_process(self):
        while True:
            if self.chromeId == 1:
                break
            if psutil.pid_exists(self.chromeId):
                time.sleep(5)
            else:
                if psutil.pid_exists(self.proxyId):
                    p = psutil.Process(self.proxyId)
                    p.kill()
                    break

    def run(self):
        task_executor.submit(self.monitor_process)

# class myThread(Process):
#     def __init__(self, chromeId, proxyId):
#         Process.__init__(self)
#         self.chromeId = chromeId
#         self.proxyId = proxyId
#
#     def run(self):
#         while True:
#             if self.chromeId == 1:
#                 break
#             import psutil
#             if psutil.pid_exists(self.chromeId):
#                 time.sleep(5)
#             else:
#                 if psutil.pid_exists(self.proxyId):
#                     p = psutil.Process(self.proxyId)
#                     p.kill()
#                     break


class GoogleBrowser(QObject):
    sig = pyqtSignal(tuple)

    def __init__(self, method, infos, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.method = method
        self.infos = infos
        self.br = Google()

    def run(self):
        if self.method == 'google_browsers_spoof':
            # chromeId, proxyId = self.br.google_browsers_spoof(self.infos)
            # i = chromeId, proxyId
            google_browsers_spoof = self.br.google_browsers_spoof(self.infos)
            i = ('google_browsers_spoof', 1)
            self.sig.emit(i)


class MarketplaceBrowser(QObject):
    sig = pyqtSignal(tuple)

    def __init__(self, method, infos, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.method = method
        self.infos = infos
        self.br = Marketplace()

    def run(self):
        if self.method == 'marketplace_browsers_spoof':
            marketplace_browsers_spoof = self.br.marketplace_browsers_spoof(self.infos)
            i = ('marketplace_browsers_spoof', marketplace_browsers_spoof)
            self.sig.emit(i)


class FacebookBrowser(QObject):
    sig = pyqtSignal(tuple)

    def __init__(self, method, infos, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.method = method
        self.infos = infos
        self.br = BrowserAuto()

    def run(self):
        if self.method == 'robot_computer_facebook_reactions':
            robot_computer_facebook_reactions = self.br.robot_computer_facebook_reactions(self.infos)
            i = ('robot_computer_facebook_reactions', robot_computer_facebook_reactions)
            self.sig.emit(i)
        if self.method == 'robot_mobile_facebook_reactions':
            robot_mobile_facebook_reactions = self.br.robot_mobile_facebook_reactions(self.infos)
            i = ('robot_mobile_facebook_reactions', robot_mobile_facebook_reactions)
            self.sig.emit(i)
        if self.method == 'robot_facebook_page':
            robot_facebook_page = self.br.robot_facebook_pages(self.infos)
            i = ('robot_facebook_page', robot_facebook_page)
            self.sig.emit(i)
        if self.method == 'robot_facebook_infos':
            robot_facebook_infos = self.br.robot_facebook_infos(self.infos)
            i = ('robot_facebook_infos', robot_facebook_infos)
            self.sig.emit(i)
        if self.method == 'robot_facebook_cmd':
            robot_facebook_cmd = self.br.robot_facebook_cmd(self.infos)
            i = ('robot_facebook_cmd', robot_facebook_cmd)
            self.sig.emit(i)
        if self.method == 'robot_facebook_cmd_cookies':
            robot_facebook_cmd_cookies = self.br.robot_facebook_cmd_cookies(self.infos)
            i = ('robot_facebook_cmd_cookies', robot_facebook_cmd_cookies)
            self.sig.emit(i)
        if self.method == 'robot_facebook_cmd_extensions':
            robot_facebook_cmd_extensions = self.br.robot_facebook_cmd_extensions(self.infos)
            i = ('robot_facebook_cmd_extensions', robot_facebook_cmd_extensions)
            self.sig.emit(i)
        if self.method == 'robot_facebook_login':
            robot_facebook_login = self.br.robot_facebook_login(self.infos)
            i = ('robot_facebook_login', robot_facebook_login)
            self.sig.emit(i)
        if self.method == 'robot_facebook_setups':
            robot_facebook_setups = self.br.robot_facebook_setups(self.infos)
            i = ('robot_facebook_setups', robot_facebook_setups)
            self.sig.emit(i)
        if self.method == 'robot_facebook_business_add_infos':
            robot_facebook_business_add_infos = self.br.robot_facebook_business_add_infos(self.infos)
            i = ('robot_facebook_business_add_infos', robot_facebook_business_add_infos)
            self.sig.emit(i)
        if self.method == 'robot_mail_changepass':
            robot_mail_changepass = self.br.robot_mail_changepass(self.infos)
            i = ('robot_mail_changepass', robot_mail_changepass)
            self.sig.emit(i)
        if self.method == 'robot_mail_login':
            robot_mail_login = self.br.robot_mail_login(self.infos)
            i = ('robot_mail_login', robot_mail_login)
            self.sig.emit(i)


class EmulatorLoops(QObject):
    sig = pyqtSignal(tuple)

    def __init__(self, method, infos, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.infos = infos
        self.method = method

    @pyqtSlot()
    def run(self):
        emulator = Emulator()

        # fb_reactions
        if self.method == 'fb_reactions':
            fb_reactions = emulator.fb_reactions(self.infos)
            i = ('fb_reactions', fb_reactions)

        # fb_pass_multi
        if self.method == 'fb_pass_multi':
            fb_pass_multi = emulator.fb_pass_multi(self.infos)
            i = ('fb_pass_multi', fb_pass_multi)

        # fb_login_multi
        if self.method == 'fb_login_multi':
            fb_login_multi = emulator.fb_login_multi(self.infos)
            i = ('fb_login_multi', fb_login_multi)

        self.sig.emit(i)


class EmulatorPlayer(QObject):
    sig = pyqtSignal(tuple)
    result = None

    def __init__(self, method, infos, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self.infos = infos
        self.method = method

    @pyqtSlot()
    def run(self):
        emulator = Emulator()
        # fb_login
        if self.method == 'fb_login':
            fb_login = emulator.fb_login(self.infos)
            result = ('fb_login', fb_login)
        # fb_restore
        if self.method == 'fb_restore':
            fb_restore = emulator.fb_restore(self.infos)
            result = ('fb_restore', fb_restore)
        # fb_backup
        if self.method == 'fb_backup':
            fb_backup = emulator.fb_backup(self.infos)
            result = ('fb_backup', (self.infos['fb_user'], fb_backup))
        # fb_reactions_notifications
        if self.method == 'fb_reactions_notifications':
            fb_reactions_notifications = emulator.fb_reactions_notifications(self.infos)
            result = ('fb_reactions_notifications', fb_reactions_notifications)
        # fb_reactions_photos
        if self.method == 'fb_reactions_photos':
            fb_reactions_photos = emulator.fb_reactions_photos(self.infos)
            result = ('fb_reactions_photos', fb_reactions_photos)
        # apps_uninstall
        if self.method == 'apps_uninstall':
            index = self.infos['index']
            apps = self.infos['apps_info']
            apps_uninstall = emulator.apps_config(index, apps)
            result = ('apps_uninstall', apps_uninstall)
        # fb - create pages
        if self.method == 'fb_pages_create':
            library = Library()
            pages_config = library.pages_config(PAGE_PATH)
            # print(pages_config['General']['Categories'])
            fb_pages_create = emulator.fb_pages_create(pages_config)
            result = ('fb_pages_create', fb_pages_create)
        # get info
        if self.method == 'fb_info':
            fb_info = emulator.fb_get_info()
            result = ('fb_info', fb_info)
        # set mail
        if self.method == 'fb_mail':
            fb_mail = emulator.fb_set_mail()
            result = ('fb_mail', fb_mail)
        # set 2fa
        if self.method == 'fb_2fa':
            fb_2fa = emulator.fb_set_2fa()
            result = ('fb_2fa', fb_2fa)
        # set pass
        if self.method == 'fb_pass':
            fb_pass = emulator.fb_set_password()
            result = ('fb_pass', fb_pass)

        self.sig.emit(result)


class CheckMail(QObject):
    sig = pyqtSignal(tuple)

    def __init__(self, mailpass, parent=None):
        # QObject.__init__(self, parent)
        super().__init__(parent)
        self.mailpass = mailpass
        self.status = False

    @pyqtSlot()
    def worker(self):
        # Load _proxy
        with open(PROXIES, 'r') as f:
            proxies = f.readlines()
        # set mail
        m = Mail(self.mailpass, proxies[0].strip())
        infos = m.imap_proxy()
        if type(infos) == tuple:
            i = infos
        self.sig.emit(i)


class FacebookForm(QMainWindow, Ui_Facebook):
    def __init__(self, _uid):
        super(FacebookForm, self).__init__()
        self.setupUi(self)

        self.setWindowIcon(QIcon("icon/facebook.png"))
        self.setWindowTitle("Add or Edit")
        # self.show()

        #
        self.lineEdit_fake_agent_mobile.setReadOnly(True)

        # load
        # self.widget = widget
        # row = widget.tableWidget.currentIndex()
        # self.uid = widget.tableWidget.item(int(row.row()), 0).text()
        self.uid = _uid
        self.edit_facebook()
        #
        # logging.info(f'Row - {int(row.row()) + 1} - {self.uid}')
        logging.info(f'Current - {_uid}')
        # Geo random
        # self.pushButton_geo_random.clicked.connect(self.geo_random)
        # Proxies random
        self.pushButton_proxies_random.clicked.connect(self.proxies_random)
        #
        self.pushButton_saved.clicked.connect(self.facebook_saved)
        # self.pushButton_reset.clicked.connect(self.reset_input)
        # self.pushButton_mail_check.clicked.connect(self.fb_get_code)
        # agent
        # self.pushButton_fake_useragen_c_rand.clicked.connect(self.random_useragent)
        # self.pushButton_fake_useragen_c_update.clicked.connect(self.update_useragent)
        self.pushButton_fake_useragen_mobile.clicked.connect(self.useragent_mobile)
        self.pushButton_info_getotp.clicked.connect(self.get_otp)
        # get location
        # self.pushButton_info_getlocation.clicked.connect(self.get_location)
        # self.pushButton_info_2fa_get.clicked.connect(self.emulator_2fa_get)
        # Set Mail, 2FA, Password
        # self.pushButton_info_2fa_set.clicked.connect(self.emulator_fb_2fa_set)
        # self.pushButton_info_mail_set.clicked.connect(self.emulator_fb_mail_set)
        # self.pushButton_info_pass_set.clicked.connect(self.emulator_fb_pass_set)
        # Login, Get Infos
        # self.pushButton_info_home.clicked.connect(self.emulator_fb_home)
        # self.pushButton_event_login.clicked.connect(self.emulator_fb_login)
        # self.pushButton_info_get.clicked.connect(self.emulator_fb_get_infos)
        # Backup, Restore
        # self.pushButton_event_restore.clicked.connect(self.emulator_fb_restore)
        # self.pushButton_event_backup.clicked.connect(self.emulator_fb_backup)
        # Login & Info, Full Changed
        # self.pushButton_event_full_changed.clicked.connect(self.emulator_fb_full_changed)
        # Create Pages
        # self.pushButton_pages_run.clicked.connect(self.emulator_fb_pages_create)
        
        # MAIL
        self.pushButton_mailer.clicked.connect(self.mail_imap)
        self.pushButton_mailer_fb.clicked.connect(self.mail_fb_code)
        self.pushButton_mailer.clicked.connect(self.mail_imap)
        # self.pushButton_mail_browser_open.clicked.connect(self.mail_browser_open)
        # stop thread
        # self.pushButton_thread_stop.clicked.connect(self.stopThread)
        
        
        #
        self.pushButton_pages_config.clicked.connect(self.page_config_edit)
        # Info
        self.pushButton_action.clicked.connect(self.emulator_fb_action)
        # thread
        self.pushButton_action_stop.clicked.connect(self.stop_thread)

        # self.thread = QThread()
        # self.worker = None

        # install apps
        # self.pushButton_action_installapps.clicked.connect(self.emulator_apps_install)
        self.pushButton_action_apps_uninstall.clicked.connect(self.emulator_apps_uninstall)

        # right menu widget
        # page
        self.tableWidget_page.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_page.customContextMenuRequested.connect(self.menu_right_page)
        self.tableWidget_page.cellClicked.connect(self.menu_right_page_itemchanged)

        # bm
        self.tableWidget_bm.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_bm.customContextMenuRequested.connect(self.menu_right_bm)
        self.tableWidget_bm.cellClicked.connect(self.menu_right_bm_itemchanged)

        # camps
        self.tableWidget_camps.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_camps.customContextMenuRequested.connect(self.menu_right_camps)
        self.tableWidget_camps.cellClicked.connect(self.menu_right_camps_itemchanged)

        # proxy
        self.pushButton_4.clicked.connect(self.getProxy)
        self.pushButton_5.clicked.connect(self.saveProxy)

        # load data from ads, pages, camps
        self.load_pages()
        self.load_ads()
        self.load_camps()
        # self.load_logs()
        self.load_tab_phoneInfo()

        #
        self.pushButton_plans.clicked.connect(self.camps_plans_edit)
        self.pushButton_groups.clicked.connect(self.camps_groups_edit)
        self.pushButton_pixels.clicked.connect(self.camps_pixels_edit)

        # Events: Change
        self.lineEdit_proxy_private.textChanged.connect(self.commit)
        # self.lineEdit_16.textChanged.connect(self.commit)
        self.comboBox.currentTextChanged.connect(self.commit)
        self.lineEdit_info_name.textChanged.connect(self.commit)
        self.lineEdit_info_password.textChanged.connect(self.commit)
        self.lineEdit_info_f2a.textChanged.connect(self.commit)
        self.lineEdit_info_token.textChanged.connect(self.commit)
        self.lineEdit_info_cookie.textChanged.connect(self.commit)
        self.lineEdit_info_birthday.textChanged.connect(self.commit)
        self.lineEdit_info_register_date.textChanged.connect(self.commit)
        self.lineEdit_info_totalfriend.textChanged.connect(self.commit)
        self.comboBox_info_country.currentTextChanged.connect(self.commit)
        self.comboBox_info_gender.currentTextChanged.connect(self.commit)
        self.comboBox_ads_group.currentTextChanged.connect(self.commit)
        self.comboBox_ads_tuts.currentTextChanged.connect(self.commit)
        self.comboBox_camps_plans.currentTextChanged.connect(self.commit)
        self.comboBox_general_status.currentTextChanged.connect(self.commit)
        self.comboBox_camps_groups.currentTextChanged.connect(self.commit)
        self.comboBox_camps_pixels.currentTextChanged.connect(self.commit)
        self.comboBox_camps_camp.currentTextChanged.connect(self.commit)
        self.lineEdit_mail_username.textChanged.connect(self.commit)
        self.lineEdit_mail_password.textChanged.connect(self.commit)
        self.lineEdit_mail_2fa.textChanged.connect(self.commit)
        self.lineEdit_mail_recovery.textChanged.connect(self.commit)
        # histories
        self.textEdit_logs.textChanged.connect(self.commit)
        
    def mail_fb_code(self):
        mail =self.lineEdit_mail_username.text().strip() + '|' + self.lineEdit_mail_password.text().strip()
        emailChecker = EmailChecker()
        t1 = threading.Thread(target=emailChecker.checker, args=[mail])
        t1.start()

    def camps_plans_edit(self):
        subprocess.Popen(["cmd", "/k", "start", "", FACEBOOK_PLANS], stderr=subprocess.STDOUT)

    def camps_groups_edit(self):
        subprocess.Popen(["cmd", "/k", "start", "", FACEBOOK_GROUPS], stderr=subprocess.STDOUT)

    def camps_pixels_edit(self):
        subprocess.Popen(["cmd", "/k", "start", "", FACEBOOK_PIXELS], stderr=subprocess.STDOUT)

    def saveProxy(self):
        proxy = self.comboBox_2.currentText() + '|' + self.lineEdit_16.text().strip()
        with open(PROXYSERVICES, 'w') as f:
            f.write(proxy)

    def getProxy(self):
        proxyServices = ProxySevices()
        results = proxyServices.proxy_new(
            {"service": self.comboBox_2.currentText(), "api": self.lineEdit_16.text().strip()})
        if results is None:
            QMessageBox.about(self, "Alert", "Get Proxy: ERRORS")
            return
        self.comboBox.setCurrentText('socks5')
        self.lineEdit_proxy_private.setText(results['socks']['ipv4'])
        QMessageBox.about(self, "Alert", "Get Proxy: SUCCESS")

    def load_tab_phoneInfo(self):
        info = MYDATA.select_data(int(self.uid))
        fake = MYDATA.select_fakephone(info.fakephone_id)
        _fake = {
            'manufacturer': fake.manufacturer,
            'model': fake.model,
            'imei': fake.imei,
            'imsi': fake.imsi,
            'simserial': fake.simserial,
            'androidid': fake.androidid,
            'pnumber': fake.pnumber,
            'macaddress': fake.macaddress,
            'ssid': fake.ssid
        }
        self.plainTextEdit_phoneInfo.setPlainText(str(_fake))

    def page_config_edit(self):
        Popen(["notepad", PAGE_PATH])

    """ Table Ads """
    def headerColumns_Ads(self, name):
        for index in range(self.tableWidget_bm.columnCount()):
            headItemText = self.tableWidget_bm.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    def load_ads(self):
        self.tableWidget_bm.setRowCount(0)
        info_ads = MYDATA.search_ads(self.uid)
        for row, info in enumerate(info_ads):
            self.tableWidget_bm.insertRow(row)
            for column, data in enumerate(info):
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('id'),
                                            self.createItem(str(info['id']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('uid'),
                                            self.createItem(str(info['uid']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('id_bm'),
                                            self.createItem(str(info['id_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('status_bm'),
                                            self.createItem(str(info['status_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('type_bm'),
                                            self.createItem(str(info['type_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('limit_bm'),
                                            self.createItem(str(info['limit_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('spend_bm'),
                                            self.createItem(str(info['spend_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('recover_bm'),
                                            self.createItem(str(info['recover_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('card_bm'),
                                            self.createItem(str(info['card_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('card_bank_bm'),
                                            self.createItem(str(info['card_bank_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('currency_bm'),
                                            self.createItem(str(info['currency_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('note_bm'),
                                            self.createItem(str(info['note_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('mail_bm'),
                                            self.createItem(str(info['mail_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_bm.setItem(int(row), self.headerColumns_Ads('date_create_bm'),
                                            self.createItem(str(info['date_create_bm']),
                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))

        self.tableWidget_bm.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_bm.resizeColumnsToContents()
        self.tableWidget_bm.setColumnWidth(0, 10)
        self.tableWidget_bm.setColumnWidth(1, 10)
        self.tableWidget_bm.setColumnWidth(8, 30)

    def menu_right_bm(self, pos):
        rowPosition = self.tableWidget_bm.rowCount()
        menu = QMenu()
        item_cn_us = menu.addAction(u'CN - USD,-7,US')
        item_cn_vn = menu.addAction(u'CN - VND,+7,US')
        item_cn_nolimit = menu.addAction(u'CN - Nolimit')
        item_bm = menu.addAction(u'BM')
        item_bm_ss = menu.addAction(u'BM - SS')
        item_delete = menu.addAction(u'Delete')
        # item_update = menu.addAction(u'Update')
        action = menu.exec_(self.tableWidget_bm.mapToGlobal(pos))
        if action == item_cn_us:
            self.commit_ads()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.ads_insert(
                {'uid': self.uid, 'id_bm': '', 'type_bm': 'CN', 'limit_bm': '50', 'spend_bm': '',
                 'recover_bm': '',
                 'card_bm': '', 'card_bank_bm': '', 'currency_bm': 'USD, US, -7',
                 'note_bm': '', 'date_create_bm': action_last, 'mail_bm': '', 'status_bm': 'Live'})
            self.load_ads()
        if action == item_cn_vn:
            self.commit_ads()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.ads_insert(
                {'uid': self.uid, 'id_bm': '', 'type_bm': 'CN', 'limit_bm': '50', 'spend_bm': '',
                 'recover_bm': '',
                 'card_bm': '', 'card_bank_bm': '', 'currency_bm': 'VND, US, +7',
                 'note_bm': '', 'date_create_bm': action_last, 'mail_bm': '', 'status_bm': 'Live'})
            self.load_ads()
        if action == item_cn_nolimit:
            self.commit_ads()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.ads_insert(
                {'uid': self.uid, 'id_bm': '', 'type_bm': 'CN', 'limit_bm': '-0', 'spend_bm': '',
                 'recover_bm': '',
                 'card_bm': '', 'card_bank_bm': '', 'currency_bm': 'USD',
                 'note_bm': '', 'date_create_bm': action_last, 'mail_bm': '', 'status_bm': 'Live'})
            self.load_ads()
        if action == item_bm_ss:
            self.commit_ads()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.ads_insert(
                {'uid': self.uid, 'id_bm': '', 'type_bm': 'BM-SS', 'limit_bm': '50', 'spend_bm': '',
                 'recover_bm': '',
                 'card_bm': '', 'card_bank_bm': '', 'currency_bm': 'USD',
                 'note_bm': '', 'date_create_bm': action_last, 'mail_bm': '', 'status_bm': 'Live'})
            self.load_ads()
        if action == item_bm:
            self.commit_ads()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.ads_insert(
                {'uid': self.uid, 'id_bm': '', 'type_bm': 'BM', 'limit_bm': '50', 'spend_bm': '',
                 'recover_bm': '',
                 'card_bm': '', 'card_bank_bm': '', 'currency_bm': 'USD',
                 'note_bm': '', 'date_create_bm': action_last, 'mail_bm': '', 'status_bm': 'Live'})
            self.load_ads()
            # self.tableWidget_bm.insertRow(rowPosition)
            # self.tableWidget_bm.setItem(rowPosition, 0, QtableWidgetItem(""))
            # self.tableWidget_bm.setItem(rowPosition, 1, QtableWidgetItem(""))
            # self.tableWidget_bm.setItem(rowPosition, 2, QtableWidgetItem(""))
            # self.tableWidget_bm.setItem(rowPosition, 3, QtableWidgetItem(""))
        # if action == item_update:
        #     self.commit_ads()
        if action == item_delete:
            self.delete_ads()

    def commit_ads(self):
        action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        column_total = self.tableWidget_bm.columnCount()
        row_total = self.tableWidget_bm.rowCount()
        for row in range(int(row_total)):
            id_column = self.headerColumns_Ads('id')
            id = self.tableWidget_bm.item(row, id_column).text()

            id_bm_column = self.headerColumns_Ads('id_bm')
            id_bm = self.tableWidget_bm.item(row, id_bm_column).text()

            status_bm_column = self.headerColumns_Ads('status_bm')
            status_bm = self.tableWidget_bm.item(row, status_bm_column).text()

            type_bm_column = self.headerColumns_Ads('type_bm')
            type_bm = self.tableWidget_bm.item(row, type_bm_column).text()

            limit_bm_column = self.headerColumns_Ads('limit_bm')
            limit_bm = self.tableWidget_bm.item(row, limit_bm_column).text()

            spend_bm_column = self.headerColumns_Ads('spend_bm')
            spend_bm = self.tableWidget_bm.item(row, spend_bm_column).text()

            currency_bm_column = self.headerColumns_Ads('currency_bm')
            currency_bm = self.tableWidget_bm.item(row, currency_bm_column).text()

            recover_bm_column = self.headerColumns_Ads('recover_bm')
            recover_bm = self.tableWidget_bm.item(row, recover_bm_column).text()

            card_bm_column = self.headerColumns_Ads('card_bm')
            card_bm = self.tableWidget_bm.item(row, card_bm_column).text()

            card_bank_bm_column = self.headerColumns_Ads('card_bank_bm')
            card_bank_bm = self.tableWidget_bm.item(row, card_bank_bm_column).text()

            mail_bm_column = self.headerColumns_Ads('mail_bm')
            mail_bm = self.tableWidget_bm.item(row, mail_bm_column).text()

            note_bm_column = self.headerColumns_Ads('note_bm')
            note_bm = self.tableWidget_bm.item(row, note_bm_column).text()

            date_create_bm_column = self.headerColumns_Ads('date_create_bm')
            date_create_bm = self.tableWidget_bm.item(row, date_create_bm_column).text()

            MYDATA.update_ads(int(id),
                              {'id_bm': id_bm, 'status_bm': status_bm,
                               'type_bm': type_bm, 'limit_bm': limit_bm,
                               'spend_bm': spend_bm, 'currency_bm': currency_bm,
                               'recover_bm': recover_bm, 'card_bm': card_bm,
                               'card_bank_bm': card_bank_bm, 'mail_bm': mail_bm,
                               'note_bm': note_bm, 'date_create_bm': date_create_bm
                               })

    def menu_right_bm_itemchanged(self):
        self.commit_ads()

    def delete_ads(self):
        # rows = self.tableWidget_bm.selectedIndexes()
        rows = self.tableWidget_bm.selectionModel().selectedRows()
        for row in rows:
            id = self.tableWidget_bm.item(row.row(), 0).text()
            MYDATA.delete_ads(id)
        self.load_ads()

    def getIndexTableAds(self, name):
        for index in range(self.tableWidget_bm.columnCount()):
            headItemText = self.tableWidget_bm.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    """ Table Pages """
    def headerColumns_Pages(self, name):
        for index in range(self.tableWidget_page.columnCount()):
            headItemText = self.tableWidget_page.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def load_pages(self):
        self.tableWidget_page.setRowCount(0)
        info_pages = MYDATA.search_pages(self.uid)
        for row, info in enumerate(info_pages):
            self.tableWidget_page.insertRow(row)
            for column, data in enumerate(info):
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('id'),
                                              self.createItem(str(info['id']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('uid'),
                                              self.createItem(str(info['uid']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('id_page'),
                                              self.createItem(str(info['id_page']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('status_page'),
                                              self.createItem(str(info['status_page']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('name_page'),
                                              self.createItem(str(info['name_page']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('categories_page'),
                                              self.createItem(str(info['categories_page']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('date_create_page'),
                                              self.createItem(str(info['date_create_page']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('liked_page'),
                                              self.createItem(str(info['liked_page']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_page.setItem(int(row), self.headerColumns_Pages('note_page'),
                                              self.createItem(str(info['note_page']),
                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))

        self.tableWidget_page.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_page.resizeColumnsToContents()
        self.tableWidget_page.setColumnWidth(0, 10)
        self.tableWidget_page.setColumnWidth(1, 10)

    def delete_pages(self):
        # rows = self.tableWidget_page.selectedIndexes()
        rows = self.tableWidget_page.selectionModel().selectedRows()
        for row in rows:
            id = self.tableWidget_page.item(row.row(), 0).text()
            MYDATA.delete_pages(id)
        self.load_pages()

    def menu_right_page(self, pos):
        rowPosition = self.tableWidget_page.rowCount()
        menu = QMenu()
        item_add = menu.addAction(u'Add')
        item_pro5 = menu.addAction(u'Pro5')
        item_delete = menu.addAction(u'Delete')
        # item_update = menu.addAction(u'Update')
        action = menu.exec_(self.tableWidget_page.mapToGlobal(pos))
        if action == item_add:
            self.commit_pages()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.insert_pages(
                {'uid': self.uid, 'id_page': '', 'status_page': 'Live', 'name_page': '', 'categories_page': '',
                 'date_create_page': action_last, 'liked_page': '', 'note_page': ''})
            self.load_pages()
        if action == item_pro5:
            self.commit_pages()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.insert_pages(
                {'uid': self.uid, 'id_page': '', 'status_page': 'Live', 'name_page': '', 'categories_page': '',
                 'date_create_page': action_last, 'liked_page': '', 'note_page': 'pro5'})
            self.load_pages()
        # if action == item_update:
        #     self.commit_pages()
        if action == item_delete:
            self.delete_pages()

    def menu_right_page_itemchanged(self):
        self.commit_pages()

    def commit_pages(self):
        action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        column_total = self.tableWidget_page.columnCount()
        row_total = self.tableWidget_page.rowCount()
        for row in range(int(row_total)):
            id_column = self.headerColumns_Pages('id')
            id = self.tableWidget_page.item(row, id_column).text()

            id_page_column = self.headerColumns_Pages('id_page')
            id_page = self.tableWidget_page.item(row, id_page_column).text()

            status_page_column = self.headerColumns_Pages('status_page')
            status_page = self.tableWidget_page.item(row, status_page_column).text()

            name_page_column = self.headerColumns_Pages('name_page')
            name_page = self.tableWidget_page.item(row, name_page_column).text()

            categories_page_column = self.headerColumns_Pages('categories_page')
            categories_page = self.tableWidget_page.item(row, categories_page_column).text()

            date_create_page_column = self.headerColumns_Pages('date_create_page')
            date_create_page = self.tableWidget_page.item(row, date_create_page_column).text()

            liked_page_column = self.headerColumns_Pages('liked_page')
            liked_page = self.tableWidget_page.item(row, liked_page_column).text()

            note_page_column = self.headerColumns_Pages('note_page')
            note_page = self.tableWidget_page.item(row, note_page_column).text()
            MYDATA.pages_update(id,
                                {'id_page': id_page, 'status_page': status_page, 'name_page': name_page,
                                 'categories_page': categories_page, 'date_create_page': date_create_page,
                                 'liked_page': liked_page, 'note_page': note_page
                                 })

    ######## Table Camps ########

    def headerColumns_Camps(self, name):
        for index in range(self.tableWidget_camps.columnCount()):
            headItemText = self.tableWidget_camps.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def load_camps(self):
        self.tableWidget_camps.setRowCount(0)
        info_camps = MYDATA.search_camps(self.uid)
        for row, info in enumerate(info_camps):
            self.tableWidget_camps.insertRow(row)
            for column, data in enumerate(info):
                self.tableWidget_camps.setItem(int(row), self.headerColumns_Camps('id'),
                                               self.createItem(str(info['id']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_camps.setItem(int(row), self.headerColumns_Camps('uid'),
                                               self.createItem(str(info['uid']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_camps.setItem(int(row), self.headerColumns_Camps('id_camps'),
                                               self.createItem(str(info['id_camps']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_camps.setItem(int(row), self.headerColumns_Camps('name_camps'),
                                               self.createItem(str(info['name_camps']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_camps.setItem(int(row), self.headerColumns_Camps('date_create_camps'),
                                               self.createItem(str(info['date_create_camps']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_camps.setItem(int(row), self.headerColumns_Camps('status_camps'),
                                               self.createItem(str(info['status_camps']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_camps.setItem(int(row), self.headerColumns_Camps('note_camps'),
                                               self.createItem(str(info['note_camps']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))

        self.tableWidget_camps.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_camps.resizeColumnsToContents()
        self.tableWidget_camps.setColumnWidth(0, 10)
        self.tableWidget_camps.setColumnWidth(1, 10)

    def delete_camps(self):
        # rows = self.tableWidget_camps.selectedIndexes()
        rows = self.tableWidget_camps.selectionModel().selectedRows()
        for row in rows:
            id = self.tableWidget_camps.item(row.row(), 0).text()
            MYDATA.delete_camps(id)
        self.load_camps()

    def menu_right_camps(self, pos):
        rowPosition = self.tableWidget_camps.rowCount()
        menu = QMenu()
        item_likepage = menu.addAction(u'Like Page')
        item_ppe = menu.addAction(u'PPE')
        item_conversion = menu.addAction(u'Conversion')
        item_delete = menu.addAction(u'Delete')
        # item_update = menu.addAction(u'Update')
        action = menu.exec_(self.tableWidget_camps.mapToGlobal(pos))
        if action == item_likepage:
            self.commit_camps()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.insert_camps(
                {'uid': self.uid, 'id_camps': '', 'name_camps': 'Like Page', 'date_create_camps': action_last,
                 'note_camps': '',
                 'status_camps': 'Publish'})
            self.load_camps()
        if action == item_ppe:
            self.commit_camps()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.insert_camps(
                {'uid': self.uid, 'id_camps': '', 'name_camps': 'PPE', 'date_create_camps': action_last,
                 'note_camps': '',
                 'status_camps': 'Publish'})
            self.load_camps()
        if action == item_conversion:
            self.commit_camps()
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.insert_camps(
                {'uid': self.uid, 'id_camps': '', 'name_camps': 'Conversion', 'date_create_camps': action_last,
                 'note_camps': '',
                 'status_camps': 'Publish'})
            self.load_camps()
        # if action == item_update:
        #     self.commit_camps()
        if action == item_delete:
            self.delete_camps()

    def menu_right_camps_itemchanged(self):
        self.commit_camps()

    def commit_camps(self):
        action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        column_total = self.tableWidget_camps.columnCount()
        row_total = self.tableWidget_camps.rowCount()
        for row in range(int(row_total)):
            id_column = self.headerColumns_Camps('id')
            id = self.tableWidget_camps.item(row, id_column).text()

            id_camps_column = self.headerColumns_Camps('id_camps')
            id_camps = self.tableWidget_camps.item(row, id_camps_column).text()

            name_camps_column = self.headerColumns_Camps('name_camps')
            name_camps = self.tableWidget_camps.item(row, name_camps_column).text()

            date_create_camps_column = self.headerColumns_Camps('date_create_camps')
            date_create_camps = self.tableWidget_camps.item(row, date_create_camps_column).text()

            status_camps_column = self.headerColumns_Camps('status_camps')
            status_camps = self.tableWidget_camps.item(row, status_camps_column).text()

            note_camps_column = self.headerColumns_Camps('note_camps')
            note_camps = self.tableWidget_camps.item(row, note_camps_column).text()

            MYDATA.update_camps(id,
                                {'id_camps': id_camps, 'name_camps': name_camps,
                                 'date_create_camps': date_create_camps, 'status_camps': status_camps,
                                 'note_camps': note_camps
                                 })

    def stop_thread(self):
        try:
            self.thread.terminate()
        except:
            pass

    def closeEvent(self, event):
        try:
            self.stopThreads(self.thread_fb_login)
            self.stopThreads(self.thread_fb_backup)
            self.stopThreads(self.thread_fb_restore)
        except:
            pass
        event.accept()

    def adb_killer(self):
        PROCNAME = "adb.exe"
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc.kill()

    def stopThreads(self, thread):
        try:
            if thread.isRunning():
                thread.quit()
                # thread.terminate()
                thread.wait()
        except:
            logging.info('Thread - Error')

    #####################################################################################
    def emulator_update_page(self, infos):
        self.stopThreads(self.thread_fb_pages_create)
        self.pushButton_pages_run.setDisabled(False)
        self.pushButton_pages_run.setText('Run')
        self.pushButton_pages_run.setStyleSheet('background-color: rgb(50, 205, 50)')
        method, info = infos
        # Page
        if method == 'fb_pages_create':
            self.checkBox_pages_create.setDisabled(False)
            self.checkBox_pages_create.setStyleSheet("background-color : rgb(50, 205, 50)")

    def emulator_update_data(self, infos):
        global _thread_edit
        _thread_edit = False
        self.pushButton_action.setDisabled(False)
        self.pushButton_action.setText('Run')
        self.pushButton_action.setStyleSheet('background-color: rgb(50, 205, 50)')
        #
        method, info = infos
        # login
        if method == 'fb_login':
            self.stopThreads(self.thread_fb_login)
            self.radioButton_fb_login.setDisabled(False)
            a, login_status = info
            if login_status is None or 'Checkpoint' in login_status or 'WrongPassword' in login_status:
                self.radioButton_fb_login.setStyleSheet("background-color : rgb(255, 69, 0)")
                logging.info(f'[{a}][LOGIN - ERROR]')
            else:
                self.radioButton_fb_login.setStyleSheet("background-color : rgb(50, 205, 50)")
                logging.info(f'[{a}][LOGIN - {login_status}]')
        if method == 'fb_backup':
            self.stopThreads(self.thread_fb_backup)
            uid, fakeInfos = info
            self.radioButton_fb_backup.setDisabled(False)
            if fakeInfos is None:
                self.radioButton_fb_backup.setStyleSheet("background-color : rgb(255, 69, 0)")
                logging.info(f'[{uid}][BACKUP - ERROR]')
            else:
                info_uid = MYDATA.select_data(uid)
                self.radioButton_fb_backup.setStyleSheet("background-color : rgb(50, 205, 50)")
                # update table fakephone
                MYDATA.fakephone_update_data(info_uid.fakephone_id, fakeInfos)
                # logging.info(f'[{a}][BACKUP - SUCCESS][{phone_info}]')
        if method == 'fb_restore':
            self.stopThreads(self.thread_fb_restore)
            self.radioButton_fb_restore.setDisabled(False)
            self.radioButton_fb_restore.setStyleSheet("background-color : rgb(50, 205, 50)")
            #
            info_uid = MYDATA.select_data(info)
            MYDATA.fakephone_update_data(info_uid.fakephone_id, {'last_backup': datetime.now().strftime("%m/%d/%Y-%H.%M.%S")})
            # uid, results = info
            # status, _infos = results
            # if status:
            #     # logging.info(f'[{uid}][RESTORE - SUCCESS]')
            #     # update last action
            #     info_uid = MYDATA.select_data(uid)
            #     MYDATA.fakephone_update_data(info_uid.fakephone_id,
            #                                  {'last_backup': datetime.now().strftime("%m/%d/%Y-%H.%M.%S")})
            # else:
            #     # logging.info(f'[{uid}][RESTORE - ERROR][{_infos}]')
            #     self.checkBox_action_set_restore.setStyleSheet("background-color: rgb(255, 69, 0)")
        # fb_info
        if method == 'fb_info':
            self.stopThreads(self.thread_fb_info)
            self.checkBox_action_get_info.setDisabled(False)
            uid, _info = info
            if info is None:
                self.checkBox_action_get_info.setStyleSheet('background-color: rgb(255, 69, 0)')
                logging.info(f'[{uid}][GET INFO - ERROR]')
            else:
                name, friend, birthday, country, gender = _info
                self.checkBox_action_get_info.setStyleSheet('background-color: rgb(50, 205, 50)')
                self.lineEdit_info_name.setText(name)
                self.lineEdit_info_totalfriend.setText(friend)
                self.lineEdit_info_birthday.setText(birthday)
                self.comboBox_info_gender.setCurrentText(gender)
                # country
                if country == 'Other':
                    self.comboBox_info_country.setCurrentText('Other')
                else:
                    with open('library/emulator/country.json') as json_file:
                        countries = json.load(json_file)
                        for c in countries:
                            try:
                                if str(country) in c["dial_code"]:
                                    self.comboBox_info_country.setCurrentText(
                                        f'{c["name"]} [{c["code"]}][{c["dial_code"]}]')
                                    break
                            except:
                                self.comboBox_info_country.setCurrentText('Other')
                logging.info(f'[{uid}][{name}, {friend}, {birthday}, {country}, {gender}]')
        # fb_reactions_photos
        if method == 'fb_reactions_photos':
            self.stopThreads(self.thread_fb_reactions_photos)
            self.checkBox_action_reactions.setDisabled(False)
            a, login_status = info
            if login_status is None or 'Checkpoint' in login_status or 'WrongPassword' in login_status:
                self.checkBox_action_reactions.setStyleSheet("background-color : rgb(255, 69, 0)")
                logging.info(f'[{a}][Reactions - ERROR]')
            else:
                self.checkBox_action_reactions.setStyleSheet("background-color : rgb(50, 205, 50)")
                logging.info(f'[{a}][Reactions - {login_status}]')
        # fb_reactions_notifications
        if method == 'fb_reactions_notifications':
            self.stopThreads(self.thread_fb_reactions_notifications)
            self.checkBox_action_reactions_notifications.setDisabled(False)
            a, login_status = info
            if login_status is None or 'Checkpoint' in login_status or 'WrongPassword' in login_status:
                self.checkBox_action_reactions_notifications.setStyleSheet("background-color : rgb(255, 69, 0)")
                logging.info(f'[{a}][Reactions - ERROR]')
            else:
                self.checkBox_action_reactions_notifications.setStyleSheet("background-color : rgb(50, 205, 50)")
                logging.info(f'[{a}][Reactions - {login_status}]')
        # if method == 'apps_install':
        #     self.stopThreads(self.thread_install_apps)
        #     self.pushButton_action_installapps.setDisabled(False)
        #     self.pushButton_action_installapps.setStyleSheet("background-color : rgb(50, 205, 50)")
        #     self.pushButton_action_installapps.setText('Install Apps')
        if method == 'apps_uninstall':
            self.stopThreads(self.thread_apps_uninstall)
            self.pushButton_action_apps_uninstall.setDisabled(False)
            self.pushButton_action_apps_uninstall.setStyleSheet("background-color : rgb(50, 205, 50)")
            self.pushButton_action_apps_uninstall.setText('Uninstall')
        # if method == 'fb_pass':
        #     self.stopThreads(self.thread_fb_pass)
        #     self.checkBox_action_set_pass.setDisabled(False)
        #     uid, _pass = info
        #     if _pass is None:
        #         self.checkBox_action_set_pass.setStyleSheet("background-color: rgb(255, 69, 0)")
        #         logging.info(f'[{uid}][SET PASSWORD - ERROR]')
        #     else:
        #         self.checkBox_action_set_pass.setStyleSheet("background-color: rgb(50, 205, 50)")
        #         self.lineEdit_info_password.setText(_pass)
        #         logging.info(f'[{uid}][SET PASSWORD - SUCCESS][{_pass}]')
        # if method == 'fb_2fa':
        #     self.stopThreads(self.thread_fb_2fa)
        #     self.checkBox_action_set_2fa.setDisabled(False)
        #     uid, _2fa = info
        #     if _2fa is None:
        #         self.checkBox_action_set_2fa.setStyleSheet("background-color: rgb(255, 69, 0)")
        #         logging.info(f'[{uid}][SET 2FA - ERROR]')
        #     else:
        #         self.checkBox_action_set_2fa.setStyleSheet("background-color: rgb(50, 205, 50)")
        #         self.lineEdit_info_f2a.setText(_2fa)
        #         logging.info(f'[{uid}][SET 2FA - SUCCESS][{_2fa}]')
        # if method == 'fb_mail':
        #     self.stopThreads(self.thread_fb_mail)
        #     self.checkBox_action_set_mail.setDisabled(False)
        #     uid, status = info
        #     if status is None:
        #         self.checkBox_action_set_mail.setStyleSheet("background-color: rgb(255, 69, 0)")
        #         logging.info(f'[{uid}][SET MAIL - ERROR]')
        #     else:
        #         self.checkBox_action_set_mail.setStyleSheet("background-color: rgb(50, 205, 50)")
        #         phone_delete_error, mail_delete_error = status
        #         logging.info(f'[{uid}][SET MAIL - SUCCESS][Phone - {phone_delete_error}, Mail - {mail_delete_error}]')
        # if method == 'fb_restore_retry':
        #     self.stopThreads(self.thread_fb_acc_restore_retry)
        #     self.checkBox_action_set_restore_retry.setDisabled(False)
        #     self.checkBox_action_set_restore_retry.setStyleSheet("background-color : rgb(50, 205, 50)")
        #     uid, results = info
        #     status, _infos = results
        #     if status:
        #         logging.info(f'[{uid}][RESTORE - SUCCESS]')
        #         # update last action
        #         info_uid = MYDATA.select_data(uid)
        #         MYDATA.fakephone_update_data(info_uid.fakephone_id,
        #                                      {'last_backup': datetime.now().strftime("%m/%d/%Y-%H.%M.%S")})
        #     else:
        #         logging.info(f'[{uid}][RESTORE - ERROR][{_infos}]')
        #         self.checkBox_action_set_restore_retry.setStyleSheet("background-color: rgb(255, 69, 0)")
        # if method == 'fb_full_changed':
        #     self.stopThreads(self.thread_fb_full_changed)
        #     uid, infos_changed = info
        #     # info
        #     self.checkBox_action_full_change.setDisabled(False)
        #     if infos_changed is None:
        #         self.checkBox_action_full_change.setStyleSheet('background-color: rgb(255, 69, 0)')
        #         logging.info(f'[{uid}][GET INFO - ERROR]')
        #     else:
        #         _infos, _newpassword, _2fa, _phoneinfo = infos_changed
        #         name, friend, birthday, country, gender = _infos
        #         self.lineEdit_info_name.setText(name)
        #         self.lineEdit_info_totalfriend.setText(friend)
        #         self.lineEdit_info_birthday.setText(birthday)
        #         self.comboBox_info_gender.setCurrentText(gender)
        #         # country
        #         if country == 'Other':
        #             self.comboBox_info_country.setCurrentText('Other')
        #         else:
        #             with open('library/emulator/country.json') as json_file:
        #                 countries = json.load(json_file)
        #                 for c in countries:
        #                     try:
        #                         if str(country) in c["dial_code"]:
        #                             self.comboBox_info_country.setCurrentText(
        #                                 f'{c["name"]} [{c["code"]}][{c["dial_code"]}]')
        #                             break
        #                     except:
        #                         self.comboBox_info_country.setCurrentText('Other')
        #         #
        #         self.checkBox_action_full_change.setStyleSheet("background-color : rgb(50, 205, 50)")
        #         # Password
        #         self.lineEdit_info_password.setText(_newpassword)
        #         # 2FA
        #         self.lineEdit_info_f2a.setText(_2fa)
        #         # Backup
        #         info_uid = MYDATA.select_data(uid)
        #         MYDATA.fakephone_update_data(info_uid.fakephone_id, _phoneinfo)

    # fb home
    def emulator_fb_home_status(self, infos):
        # self.stopThread()
        a, b, c = infos
        self.pushButton_info_home.setDisabled(False)

    def loopfunction(self, x):
        self.counter.setValue(x)

    def emulator_apps_uninstall(self):
        self.pushButton_action_apps_uninstall.setDisabled(True)
        self.pushButton_action_apps_uninstall.setText('Running')
        info = MYDATA.select_data(self.uid)
        # apps
        with open(APPS_INSTALL, 'r') as f:
            apps_install = f.readlines()
        apps_info = []
        for app in apps_install:
            if len(app.strip()) == 0:
                continue
            apps_info.append({
                'name': app.strip(),
                'uninstallapp': 1,
                'installapp': 0,
                'runapp': 0,
                'killapp': 0,
                'remove_cache': 0
            })
        #
        infos = {
            'index': v_index,
            'fb_user': str(info.uid),
            'fb_pass': str(info.info_password),
            'mail_user': str(info.mail_user),
            'mail_pass': str(info.mail_pass),
            'fb_2fa': str(info.info_f2a),
            'fb_agent_mobile': str(info.fake_agent_mobile),
            'ip_services': info.fake_service_proxy,
            'apps_info': apps_info,
        }
        self.thread_apps_uninstall = QThread()
        self.worker = EmulatorPlayer('apps_uninstall', infos)
        self.thread_apps_uninstall.started.connect(self.worker.run)
        self.worker.sig.connect(self.emulator_update_data)
        self.worker.moveToThread(self.thread_apps_uninstall)
        self.thread_apps_uninstall.start()


    def emulator_fb_action(self):
        global _thread_edit
        _thread_edit = True
        #
        self.pushButton_action.setDisabled(True)
        self.pushButton_action.setText('Running')
        self.pushButton_action.setStyleSheet('background-color: rgb(255, 69, 0)')

        info = MYDATA.select_data(self.uid)
        #
        config = dict()
        if self.checkBox_action_reactions.isChecked():
            config['fb_reactions_photos'] = True
        if self.checkBox_action_reactions_notifications.isChecked():
            config['fb_reactions_notifications'] = True
        # if self.checkBox_action_home.isChecked():
        #     config['home'] = True
        if self.radioButton_fb_login.isChecked():
            config['fb_login'] = True
        if self.radioButton_fb_backup.isChecked():
            config['fb_backup'] = True
        if self.radioButton_fb_restore.isChecked():
            config['fb_restore'] = True
        # if self.checkBox_action_get_info.isChecked():
        #     config['fb_info'] = True
        # if self.checkBox_action_set_mail.isChecked():
        #     config['fb_mail'] = True
        # if self.checkBox_action_set_pass.isChecked():
        #     config['fb_pass'] = True
        # if self.checkBox_action_set_2fa.isChecked():
        #     config['fb_2fa'] = True
        # if self.checkBox_action_set_restore_retry.isChecked():
        #     config['fb_restore_retry'] = True
        # if self.checkBox_action_full_change.isChecked():
        #     config['fb_full_change'] = True

        if len(list(config.values())) > 1:
            self.pushButton_action.setDisabled(False)
            self.pushButton_action.setText('Run')
            self.pushButton_action.setStyleSheet('background-color: rgb(255, 69, 0)')
            return
        # fb_reactions_photos
        if config.get('fb_reactions_photos'):
            # self.checkBox_action_reactions.setStyleSheet('background-color: rgb(50, 205, 50)')
            self.checkBox_action_reactions.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                # 'fb_type': info.type,
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_cookie': info.info_cookie,
                'fb_agent_mobile': str(info.fake_agent_mobile),
                # 'fb_browsers': info.fake_agent_computer,
                # 'ip_services': self.widget.comboBox_proxy_services.currentText(),
                # 'ip_location': self.widget.comboBox_ip_location.currentText(),
                'proxy_private': str(info.proxy_private),
                'fb_reactions_notifications_loops': 5,
                'fb_reactions_photos_loops': 7,
                'infoPath': CURRENT_FOLDER + '/data/emulator'
            }
            self.thread_fb_reactions_photos = QThread()
            self.worker = EmulatorPlayer('fb_reactions_photos', infos)
            self.thread_fb_reactions_photos.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_reactions_photos)
            self.thread_fb_reactions_photos.setTerminationEnabled(True)
            self.thread_fb_reactions_photos.start()
        # fb_reactions_notifications
        if config.get('fb_reactions_notifications'):
            # self.checkBox_action_reactions.setStyleSheet('background-color: rgb(50, 205, 50)')
            self.checkBox_action_reactions_notifications.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                # 'fb_type': info.type,
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_cookie': info.info_cookie,
                'fb_agent_mobile': str(info.fake_agent_mobile),
                # 'fb_browsers': info.fake_agent_computer,
                # 'ip_services': self.widget.comboBox_proxy_services.currentText(),
                # 'ip_location': self.widget.comboBox_ip_location.currentText(),
                'proxy_private': str(info.proxy_private),
                'fb_reactions_notifications_loops': 5,
                'fb_reactions_photos_loops': 7,
                'infoPath': CURRENT_FOLDER + '/data/emulator'
            }
            self.thread_fb_reactions_notifications = QThread()
            self.worker = EmulatorPlayer('fb_reactions_notifications', infos)
            self.thread_fb_reactions_notifications.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_reactions_notifications)
            self.thread_fb_reactions_notifications.setTerminationEnabled(True)
            self.thread_fb_reactions_notifications.start()
        # login
        if config.get('fb_login'):
            self.radioButton_fb_login.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                # 'fb_type': info.type,
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_cookie': info.info_cookie,
                'fb_agent_mobile': str(info.fake_agent_mobile),
                # 'fb_browsers': info.fake_agent_computer,
                # 'ip_services': self.widget.comboBox_proxy_services.currentText(),
                # 'ip_location': self.widget.comboBox_ip_location.currentText(),
                'proxy_private': str(info.proxy_private),
                'infoPath': CURRENT_FOLDER + '/data/emulator'
            }
            self.thread_fb_login = QThread()
            self.worker = EmulatorPlayer('fb_login', infos)
            self.thread_fb_login.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_login)
            # self.thread_fb_login.setTerminationEnabled(True)
            self.thread_fb_login.start()
        # backup
        if config.get('fb_backup'):
            self.radioButton_fb_backup.setDisabled(True)
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.update_data(self.uid, {'action_last': action_last})
            # phone info
            account = MYDATA.select_data(str(info.uid))
            fakephone = MYDATA.select_fakephone(account.fakephone_id)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'phone_info': fakephone,
                'proxy_private': str(info.proxy_private),
                'infoPath': CURRENT_FOLDER + '/data/emulator'
            }
            self.thread_fb_backup = QThread()
            self.worker = EmulatorPlayer('fb_backup', infos)
            self.thread_fb_backup.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_backup)
            # self.thread_fb_backup.setTerminationEnabled(True)
            self.thread_fb_backup.start()
        # restore
        if config.get('fb_restore'):
            # # check
            # uid_path = f'{CURRENT_FOLDER}/data/emulator/data/{info.uid}.tar.gz'
            # if os.path.exists(uid_path) is False:
            #     self.pushButton_action.setDisabled(False)
            #     self.pushButton_action.setText('Run')
            #     self.pushButton_action.setStyleSheet('background-color: rgb(50, 205, 50)')
            #     QMessageBox.about(self, "Errors", f"Not find {uid_path}")
            #     return
            #
            self.radioButton_fb_restore.setDisabled(True)
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.update_data(self.uid, {'action_last': action_last})
            # phone info
            account = MYDATA.select_data(str(info.uid))
            fakephone = MYDATA.select_fakephone(account.fakephone_id)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'phone_info': fakephone,
                'proxy_private': str(info.proxy_private),
                'infoPath': CURRENT_FOLDER + '/data/emulator'
            }

            # self.thread_fb_restore = f'thread_fb_restore_{random.randint(1, 99999)}'
            self.thread_fb_restore = QThread()
            self.worker = EmulatorPlayer('fb_restore', infos)
            self.thread_fb_restore.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_restore)
            # self.thread_fb_restore.setTerminationEnabled(True)
            self.thread_fb_restore.start()
        # info
        if config.get('fb_info'):
            self.checkBox_action_get_info.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'proxy_private': str(info.proxy_private),

            }
            self.thread_fb_info = QThread()
            self.worker = EmulatorPlayer('fb_info', infos)
            self.thread_fb_info.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_info)
            self.thread_fb_info.setTerminationEnabled(True)
            self.thread_fb_info.start()
        # mail
        if config.get('fb_mail'):
            self.checkBox_action_set_mail.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'ip_location': '',
                # 'ip_list': str(self.widget.plainTextEdit_tethering_proxy.toPlainText()).split('\n'),
                'proxy_private': str(info.proxy_private),

            }
            self.thread_fb_mail = QThread()
            self.worker = EmulatorPlayer('fb_mail', infos)
            self.thread_fb_mail.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_mail)
            self.thread_fb_mail.setTerminationEnabled(True)
            self.thread_fb_mail.start()
        # pass
        if config.get('fb_pass'):
            self.checkBox_action_set_pass.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'ip_location': '',
                # 'ip_list': str(self.widget.plainTextEdit_tethering_proxy.toPlainText()).split('\n'),
                'proxy_private': str(info.proxy_private),

            }
            self.thread_fb_pass = QThread()
            self.worker = EmulatorPlayer('fb_pass', infos)
            self.thread_fb_pass.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_pass)
            self.thread_fb_pass.setTerminationEnabled(True)
            self.thread_fb_pass.start()
        # 2fa
        if config.get('fb_2fa'):
            self.checkBox_action_set_2fa.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'ip_location': '',
                # 'ip_list': str(self.widget.plainTextEdit_tethering_proxy.toPlainText()).split('\n'),
                'proxy_private': str(info.proxy_private),

            }
            self.thread_fb_2fa = QThread()
            self.worker = EmulatorPlayer('fb_2fa', infos)
            self.thread_fb_2fa.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_2fa)
            self.thread_fb_2fa.setTerminationEnabled(True)
            self.thread_fb_2fa.start()
        if config.get('fb_restore_retry'):
            self.checkBox_action_set_restore_retry.setDisabled(True)
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            MYDATA.update_data(self.uid, {'action_last': action_last})
            # phone info
            account = MYDATA.select_data(str(info.uid))
            fakephone = MYDATA.select_fakephone(account.fakephone_id)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'ip_location': '',
                # 'ip_list': str(self.widget.plainTextEdit_tethering_proxy.toPlainText()).split('\n'),
                'phone_info': fakephone,
                'quit_emulator': False,
                # 'add_proxy': self.checkBox_action_proxy.isChecked(),
                'proxy_private': str(info.proxy_private),

            }
            self.thread_fb_acc_restore_retry = QThread()
            self.worker = EmulatorPlayer('fb_acc_restore_retry', infos)
            self.thread_fb_acc_restore_retry.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_acc_restore_retry)
            self.thread_fb_acc_restore_retry.setTerminationEnabled(True)
            self.thread_fb_acc_restore_retry.start()

        # complete changed
        if config.get('fb_full_change'):
            self.checkBox_action_full_change.setDisabled(True)
            infos = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'ip_location': '',
                # 'ip_list': str(self.widget.plainTextEdit_tethering_proxy.toPlainText()).split('\n'),
                'proxy_private': str(info.proxy_private),

            }
            #
            self.thread_fb_full_changed = QThread()
            self.worker = EmulatorPlayer('fb_full_changed', infos)
            self.thread_fb_full_changed.started.connect(self.worker.run)
            self.worker.sig.connect(self.emulator_update_data)
            self.worker.moveToThread(self.thread_fb_full_changed)
            self.thread_fb_full_changed.setTerminationEnabled(True)
            self.thread_fb_full_changed.start()

    @pyqtSlot()
    # def emulator_fb_pages_create(self):
    #     self.pushButton_pages_run.setDisabled(True)
    #     self.pushButton_pages_run.setText('Running')
    #     self.pushButton_pages_run.setStyleSheet('background-color: rgb(255, 69, 0)')
    #     info = MYDATA.select_data(self.uid)
    #     infos = {
    #         'fb_user': str(info.uid),
    #         'fb_pass': str(info.info_password),
    #         'mail_user': str(info.mail_user),
    #         'mail_pass': str(info.mail_pass),
    #         'fb_2fa': str(info.info_f2a),
    #         'fb_agent_mobile': str(info.fake_agent_mobile),
    #         'ip_services': info.fake_service_proxy,
    #         'ip_location': '',
    #         # 'ip_list': str(self.widget.plainTextEdit_tethering_proxy.toPlainText()).split('\n'),
    #         # 'page_info': {
    #         #     'page_names': [
    #         #         self.lineEdit_name_page.text(),
    #         #     ],
    #         #     'page_categories':
    #         #         ['Shopping & Retail']
    #         # }
    #         'proxy_private': str(info.proxy_private),
    #         'location_spoof': str(info.location_spoof)
    #     }
    #     self.thread_fb_pages_create = QThread()
    #     self.worker = EmulatorPlayer('fb_pages_create', infos)
    #     self.thread_fb_pages_create.started.connect(self.worker.get)
    #     self.worker.sig.connect(self.emulator_update_page)
    #     self.worker.moveToThread(self.thread_fb_pages_create)
    #     self.thread_fb_pages_create.setTerminationEnabled(True)
    #     self.thread_fb_pages_create.start()

    #############################################################################################################
    def mail_status(self, infos):
        self.stopThreads(self.thread_mail)
        self.pushButton_mail_check.setDisabled(False)
        _mail, info = infos
        if type(info) == dict:
            self.pushButton_mail_check.setStyleSheet('background-color: rgb(255, 69, 0)')
            self.label_mail_getcode_status.setText(info['status'])
            return
        else:
            self.pushButton_mail_check.setStyleSheet('background-color: rgb(50, 205, 50)')
            self.label_mail_getcode_status.setText(f'Success')
            self.lineEdit_mail_codefb.setText(str(info))

    @pyqtSlot()
    def fb_get_code(self):
        self.label_mail_getcode_status.setText('Waiting...')
        self.pushButton_mail_check.setDisabled(True)
        mailpass = f'{self.lineEdit_mail_username.text().strip()}:{self.lineEdit_mail_password.text().strip()}'
        #
        self.thread_mail = QThread()
        self.worker = CheckMail(mailpass)
        self.thread_mail.started.connect(self.worker.worker)
        self.worker.sig.connect(self.mail_status)
        self.worker.moveToThread(self.thread_mail)
        self.thread_mail.setTerminationEnabled(True)
        self.thread_mail.start()

    @pyqtSlot()
    def mail_imap(self):
        try:
            path_mail = 'library/mail/live.txt'
            # get mail
            with open(path_mail, 'r') as f:
                mails = f.readlines()
            mail = random.choice(mails)
            self.lineEdit_mail_username.setText(mail.split(':')[0].strip())
            self.lineEdit_mail_password.setText(mail.split(':')[1].strip())
            logging.info(f'Get new mail : {mail}')
            # save mail
            mails.remove(mail)
            with open(path_mail, 'w') as f:
                f.writelines(mails)
        except:
            pass

    def get_otp(self):
        # Case 1
        tfa = str(self.lineEdit_info_f2a.text()).strip().translate(str.maketrans('', '', ' \n\t\r'))
        # totp = pyotp.TOTP(re.sub(r'\s+', '', str(self.lineEdit_info_f2a.text()).strip())).now()
        totp = pyotp.TOTP(str(tfa)).now()

        # import onetimepass as otp
        # totp = str(otp.get_totp(tfa))
        # totp = str(otp.get_hotp(tfa, intervals_no=i))

        # method set text to clipboard
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(totp, mode=cb.Clipboard)

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    # def update_useragent(self):
    #     _random_infos_computer = self._random_infos_computer()
    #     self.lineEdit_fake_agent_computer.clear()
    #     self.lineEdit_fake_agent_computer.setText(str(_random_infos_computer))

    # def random_useragent(self):
    #     _random_infos_computer = self._random_infos_computer()
    #     self.lineEdit_fake_agent_computer.clear()
    #     self.lineEdit_fake_agent_computer.setText(str(_random_infos_computer))

    def _random_infos_computer(self):
        with open(BROWSERS_USERAGENT_WINDOW, 'r', encoding='utf-8') as f:
            agent_c = f.readlines()
        _browsersInfos = random.choice(agent_c)
        return _browsersInfos
        # with open(USERAGENT_COMPUTER, 'r', encoding='utf-8') as f:
        #     agent_c = f.readlines()
        # useragent = random.choice(agent_c)
        # self.lineEdit_fake_agent_computer.setText(useragent.strip())
        # with open(BROWSERS_USERAGENT_WINDOW, 'r', encoding='utf-8') as f:
        #     agent_c = f.readlines()
        # with open(BROWSERS_WINDOW_SIZE, 'r', encoding='utf-8') as f:
        #     _window_size = f.readlines()
        # with open(BROWSERS_MAC, 'r', encoding='utf-8') as f:
        #     _mac = f.readlines()
        # with open(BROWSERS_LAN_IP, 'r', encoding='utf-8') as f:
        #     _lanip = f.readlines()
        #
        # while True:
        #     useragent = random.choice(agent_c).strip()
        #     mac = str(random.choice(_mac)).upper().strip()
        #     lanip = random.choice(_lanip).strip()
        #     name_computer = str(f'DESKTOP-{id_generator()}').upper().strip()
        #
        #     cpu = random.randint(2, 16)
        #     ram = random.randint(5, 32)
        #     while True:
        #         windowsize = random.choice(_window_size).split('|')
        #         if windowsize[0].strip() == 'Mobile':
        #             continue
        #         break
        #     browsersInfos = [
        #         "gologin|97|Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        #         "gologin|100|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        #         "dolphin|99|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        #         "dolphin|100|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        #     ]
        #     _browsersInfos = random.choice(browsersInfos).split('|')
        #     computer = str({
        #         "browsers": _browsersInfos[0],
        #         "version": _browsersInfos[1],
        #         "user_agent": _browsersInfos[2],
        #         "name_computer": name_computer,
        #         "cpu": cpu,
        #         "ram": ram,
        #         "swidth": windowsize[1].strip(),
        #         "sheight": windowsize[2].strip(),
        #         "pixelratio": windowsize[3].strip(),
        #         "mac_address": mac,
        #         "lan_ip": lanip,
        #     })
        #     return computer

    def useragent_mobile(self):
        self.lineEdit_fake_agent_mobile.clear()
        with open(USERAGENT_MOBILE, 'r', encoding='utf-8') as f:
            agent_c = f.readlines()
        useragent = random.choice(agent_c)
        self.lineEdit_fake_agent_mobile.setText(useragent.strip())

        # Update Database
        MYDATA.update_data(self.uid, {'fake_agent_mobile': useragent})
        # #
        # general = FakeInfos(CURRENT_FOLDER + '/data/emulator')
        # fake = general.fake_infos(useragent)
        # _fake = {
        #     'imei': fake['imei'],
        #     'imsi': fake['imsi'],
        #     'simserial': fake['simserial'],
        #     'androidid': fake['androidid'],
        #     'manufacturer': fake['manufacturer'],
        #     'model': fake['model'],
        #     'pnumber': fake['linenum'],
        #     'macaddress': fake['macaddress'],
        #     # 'last_backup': datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        # }
        # infos = MYDATA.select_data(self.uid)
        # MYDATA.fakephone_update_data(infos.fakephone_id, _fake)
        # logging.info(f'[{self.uid}][{infos.fakephone_id}][{_fake}]')

    def edit_facebook(self):
        with open(PROXYSERVICES, 'r', encoding='utf8') as f:
            proxyServicesList = f.readlines()[0].split('|')
        self.comboBox_2.setCurrentText(proxyServicesList[0])
        self.lineEdit_16.setText(proxyServicesList[1])

        info = MYDATA.select_data(self.uid)
        # Status
        with open(FACEBOOK_STATUS, 'r', encoding='utf8') as f:
            combo_status = f.readlines()
        for c in combo_status:
            self.comboBox_general_status.addItem(c.split('|')[0])
        self.comboBox_general_status.setCurrentText(str(info.status))

        # VIA
        ## Source
        with open(FACEBOOK_SOURCES, 'r', encoding='utf8') as f:
            ads_group = f.readlines()
        for c in ads_group:
            self.comboBox_ads_group.addItem(c.strip())
        self.comboBox_ads_group.setCurrentText(info.ads_groups)
        ## Tuts
        with open(FACEBOOK_TUTS, 'r', encoding='utf8') as f:
            ads_tuts = f.readlines()
        for c in ads_tuts:
            self.comboBox_ads_tuts.addItem(c.strip())
        self.comboBox_ads_tuts.setCurrentText(info.ads_tuts)
        ## Tuts 1
        for c in ads_tuts:
            self.comboBox_ads_tuts_1.addItem(c.strip())
        # self.comboBox_Ads_Tuts_1.setCurrentText(info.ads_tuts)

        # CAMPS
        ## Plans
        with open(FACEBOOK_PLANS, 'r', encoding='utf8') as f:
            camps_plans = f.readlines()
        for c in camps_plans:
            self.comboBox_camps_plans.addItem(c.strip())
        self.comboBox_camps_plans.setCurrentText(info.camps_plans)

        ## Groups
        with open(FACEBOOK_GROUPS, 'r', encoding='utf8') as f:
            camps_groups = f.readlines()
        for c in camps_groups:
            self.comboBox_camps_groups.addItem(c.strip())
        self.comboBox_camps_groups.setCurrentText(info.camps_groups)

        ## Pixels
        with open(FACEBOOK_PIXELS, 'r', encoding='utf8') as f:
            camps_pixels = f.readlines()
        for c in camps_pixels:
            self.comboBox_camps_pixels.addItem(c.strip())
        self.comboBox_camps_pixels.setCurrentText(info.camps_pixels)

        # # Load _spoof _proxy
        # with open('./data/spoof_proxy.txt', 'r', encoding='utf8') as f:
        #     spoof_proxies = f.readlines()
        # for c in spoof_proxies:
        #     self.comboBox_proxy_select.addItem(c.strip())

        # # Load _spoof geo
        # with open('./data/spoof_geo.txt', 'r', encoding='utf8') as f:
        #     spoof_geo = f.readlines()
        # for c in spoof_geo:
        #     self.comboBox_geo_select.addItem(c.strip().split('|')[0])

        self.lineEdit_general_uid.setText(str(info.uid))
        # self.widget.comboBox_ip_location.setCurrentText(info.fake_ip)
        # self.widget.comboBox_proxy_services.setCurrentText(info.fake_service_proxy)
        self.lineEdit_fake_agent_mobile.setText(info.fake_agent_mobile)
        # self.lineEdit_fake_agent_computer.setText(info.fake_agent_computer)

        self.lineEdit_info_name.setText(info.info_name)
        self.lineEdit_info_password.setText(info.info_password)
        self.lineEdit_info_f2a.setText(info.info_f2a)
        self.lineEdit_info_cookie.setText(info.info_cookie)
        self.lineEdit_info_token.setText(info.info_token)
        self.lineEdit_info_birthday.setText(info.info_birthday)
        self.comboBox_info_gender.setCurrentText(info.info_gender)
        self.lineEdit_info_totalfriend.setText(str(info.info_friend))
        # self.lineEdit_info_createdate.setText(info.info_createdate)
        self.lineEdit_info_register_date.setText(str(info.info_register_date))
        # self.lineEdit_info_last_location.setText(str(info.ip_last_location))
        self.textEdit_logs.setPlainText(info.histories)
        # self.lineEdit_proxy_private.setText(str(info.proxy_private))
        # self.lineEdit_location_spoof.setText(str(info.location_spoof))
        self.comboBox_general_change_mail.setCurrentText(str(info.info_change_mail))
        self.comboBox_general_change_pass.setCurrentText(str(info.info_change_pass))
        # proxy
        if ':' in info.proxy_private:
            proxy = str(info.proxy_private).split(":", 1)
            self.comboBox.setCurrentText(proxy[0])
            self.lineEdit_proxy_private.setText(proxy[1])

        # Load Country
        with open('./data/_countries.txt', 'r', encoding='utf8') as f:
            combo_country = f.readlines()
        for c in combo_country:
            self.comboBox_info_country.addItem(c.strip())
        self.comboBox_info_country.setCurrentText(info.ads_groups)
        # country_list = []
        # with open('library/emulator/country.json') as json_file:
        #     countries = json.load(json_file)
        #     for c in countries:
        #         country_list.append(f'{c["name"]} [{c["code"]}][{c["dial_code"]}]')
        # self.comboBox_info_country.addItems(country_list)
        self.comboBox_info_country.setCurrentText(str(info.info_country))

        self.lineEdit_mail_username.setText(info.mail_user)
        self.lineEdit_mail_password.setText(info.mail_pass)
        self.lineEdit_mail_recovery.setText(info.mail_recovery)

    def commit(self):
        logging.info(f'[{self.uid}][Events: Commited]')
        info = MYDATA.select_data(self.uid)
        #
        try:
            action_begin = info.action_begin
            action_last = info.action_last

            if action_begin == '':
                action_begin = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            if action_last == '':
                action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")

            # update
            MYDATA.update_data(int(info.uid), {'status': self.comboBox_general_status.currentText(),
                                               'camps_plans': self.comboBox_camps_plans.currentText(),
                                               'camps_groups': self.comboBox_camps_groups.currentText(),
                                               'camps_pixels': self.comboBox_camps_pixels.currentText(),
                                               'ads_groups': self.comboBox_ads_group.currentText(),
                                               'ads_tuts': self.comboBox_ads_tuts.currentText(),
                                               'info_change_mail': self.comboBox_general_change_mail.currentText(),
                                               'info_change_pass': self.comboBox_general_change_pass.currentText(),
                                               # 'fake_ip': self.widget.comboBox_ip_location.currentText(),
                                               # 'fake_service_proxy': self.widget.comboBox_proxy_services.currentText(),
                                               'fake_agent_mobile': self.lineEdit_fake_agent_mobile.text(),
                                               # 'fake_agent_computer': self.lineEdit_fake_agent_computer.text(),
                                               # 'fake_agent_computer': '',

                                               'info_name': self.lineEdit_info_name.text(),
                                               'info_password': self.lineEdit_info_password.text(),
                                               'info_f2a': self.lineEdit_info_f2a.text(),
                                               'info_cookie': self.lineEdit_info_cookie.text(),
                                               'info_token': self.lineEdit_info_token.text(),
                                               'info_birthday': self.lineEdit_info_birthday.text(),
                                               'info_gender': self.comboBox_info_gender.currentText(),
                                               'info_friend': self.lineEdit_info_totalfriend.text(),
                                               'info_country': self.comboBox_info_country.currentText(),
                                               'info_register_date': self.lineEdit_info_register_date.text(),
                                               # 'ip_last_location': self.lineEdit_info_last_location.text(),
                                               'histories': self.textEdit_logs.toPlainText(),

                                               'proxy_private': self.comboBox.currentText() + ':' + self.lineEdit_proxy_private.text().strip(),
                                               # 'location_spoof': str(
                                               #     re.sub(r"\s+", "", self.lineEdit_location_spoof.text(),
                                               #            flags=re.UNICODE)),
                                               'mail_user': self.lineEdit_mail_username.text(),
                                               'mail_pass': self.lineEdit_mail_password.text(),
                                               'mail_recovery': self.lineEdit_mail_recovery.text(),
                                               'action_begin': action_begin,
                                               'action_last': action_last,
                                               # 'last_profile_mobile': bool(info.last_profile_mobile),
                                               # 'last_profile_computer': bool(info.last_profile_computer)
                                               })
            return True
        except:
            pass

    @pyqtSlot()
    def facebook_saved(self):
        result = self.commit()
        if result:
            QMessageBox.about(self, "Saved Form", "Success")
            # self.widget.load_data()

    def ip_geo(self):
        info = MYDATA.select_data(self.uid)
        timezone_sys = TimezoneSys(info.proxy_private)
        _timezone = timezone_sys.proxy_data()
        ip = _timezone['ip']
        timezone = _timezone['timezone']
        utc = _timezone['utc']
        _latitude = _timezone['g_latitude']
        _longitude = _timezone['g_longitude']
        if _latitude is None:
            return
        geo = Geo()
        latitude, longitude = geo.kilometers(_latitude, _longitude, 30, random.uniform(0.5, 5.0))
        return latitude, longitude

    def ip_geo_thread(self):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(self.ip_geo)
            return_value = future.result()
            return return_value

    # def geo_random(self):
    #     with open('./data/spoof_geo.txt', 'r', encoding='utf8') as f:
    #         spoof_geo = f.readlines()
    #     for c in spoof_geo:
    #         if self.comboBox_geo_select.currentText() in c:
    #             _latitude = (c.split('|')[1]).split(',')[0]
    #             _longitude = (c.split('|')[1]).split(',')[1]
    #             geo = Geo()
    #             latitude, longitude = geo.kilometers(_latitude, _longitude, 30, random.uniform(0.5, 5.0))
    #             self.lineEdit_location_spoof.setText(f'{latitude},{longitude}')
    #     self.lineEdit_location_spoof.setText(f'{latitude},{longitude}')

    def proxies_random(self):
        utilities = Utilities()
        _proxy = utilities.proxies_get('US', './data/spoof_proxy.txt')
        scheme = _proxy.split(':')[0]
        self.comboBox.setCurrentText(scheme)
        self.lineEdit_proxy_private.setText(_proxy.replace(scheme + ':', ''))


class Utilities(object):
    def __init__(self):
        pass

    def proxies_get(self, location, path):
        with open(path, 'r', encoding='utf8') as f:
            spoof_proxies = f.readlines()
        while True:
            rand = random.choice(spoof_proxies)
            if location in rand:
                return rand.split('|')[1].strip()


# Global
_flag_thread = False
_thread_edit = False


class GoogleForm(QMainWindow, Ui_Google):
    def __init__(self, username):
        super(GoogleForm, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon/facebook.png"))
        self.setWindowTitle("EDIT")

        self.username = username
        logging.info(f'Current - {username}')
        self.edit()

        self.pushButton.clicked.connect(self.save)
        self.pushButton_2.clicked.connect(self.currenttime_tkcn)
        # self.pushButton_3.clicked.connect(self.currenttime_mcc)

        # proxy
        style_button = "QPushButton{background-color : lightblue;}QPushButton::pressed{background-color : red;}"
        self.pushButton_4.setStyleSheet(style_button)
        self.pushButton_5.setStyleSheet(style_button)
        # self.pushButton_6.setStyleSheet(style_button)
        self.pushButton_7.setStyleSheet(style_button)
        self.pushButton_mail_r.setStyleSheet(style_button)

        self.pushButton_4.clicked.connect(self.getProxy_t)
        self.pushButton_5.clicked.connect(self.editProxy)
        # self.pushButton_6.clicked.connect(self.editAdsWeb)
        self.pushButton_7.clicked.connect(self.editCard)
        self.pushButton_8.clicked.connect(self.editPlan)

        #
        self.pushButton_pass_r.clicked.connect(self.passwordrandom)
        self.pushButton_2fa.clicked.connect(self.google_otp2fa)
        self.pushButton_mail_r.clicked.connect(self.mail_get_t)


        # Delegate: Event
        self.comboBox_5.currentTextChanged.connect(self.save)
        self.comboBox_10.currentTextChanged.connect(self.save)
        self.comboBox_12.currentTextChanged.connect(self.save)
        self.comboBox_6.currentTextChanged.connect(self.save)
        self.comboBox_7.currentTextChanged.connect(self.save)
        self.comboBox_google_ads.currentTextChanged.connect(self.save)
        self.comboBox_11.currentTextChanged.connect(self.save)
        self.comboBox_8.currentTextChanged.connect(self.save)

        # self.comboBox_ads_web.currentTextChanged.connect(self.save)
        self.lineEdit_4.textChanged.connect(self.save)
        self.lineEdit_2fa.textChanged.connect(self.save)
        self.lineEdit.textChanged.connect(self.save)
        self.lineEdit_10.textChanged.connect(self.save)
        self.lineEdit_11.textChanged.connect(self.save)
        self.lineEdit_2.textChanged.connect(self.save)
        self.lineEdit_3.textChanged.connect(self.save)
        self.lineEdit_12.textChanged.connect(self.save)
        self.plainTextEdit.textChanged.connect(self.save)
        self.plainTextEdit_marketplace.textChanged.connect(self.save)

        # Google: Level
        self.load_glevel()
        self.tableWidget_level.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_level.customContextMenuRequested.connect(self.menu_right_glevel)
        self.tableWidget_level.cellChanged.connect(self.menu_right_glevel_itemchanged)

        # Google: Adsense
        self.load_gadsense()
        self.tableWidget_adsense.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_adsense.customContextMenuRequested.connect(self.menu_right_gadsense)
        self.tableWidget_adsense.cellChanged.connect(self.menu_right_gadsense_itemchanged)

        # Google: tableWidget_ads
        self.load_gads()
        self.tableWidget_ads.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_ads.customContextMenuRequested.connect(self.menu_right_gads)
        self.tableWidget_ads.cellChanged.connect(self.menu_right_gads_itemchanged)

        # # Google: tableWidget_ads_deposit
        # self.load_ads_deposit()
        # self.tableWidget_ads_deposit.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tableWidget_ads_deposit.customContextMenuRequested.connect(self.menu_right_ads_deposit)
        # self.tableWidget_ads_deposit.cellChanged.connect(self.menu_right_ads_deposit_itemchanged)

        # Google: tableWidget_ads_affiliate
        self.load_ads_affiliate()
        self.tableWidget_ads_affliate.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_ads_affliate.customContextMenuRequested.connect(self.menu_right_ads_affiliate)
        self.tableWidget_ads_affliate.cellChanged.connect(self.menu_right_ads_affiliate_itemchanged)


    def getIndexHeaderTableWidget(self, tableWidget, name):
        for index in range(tableWidget.columnCount()):
            headItemText = tableWidget.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    # """tableWidget_ads_deposit"""
    # def load_ads_deposit(self):
    #     self.tableWidget_ads_deposit.setRowCount(0)
    #     search_logs = MYDATA.search_ads_deposit(self.username)
    #     for row, info in enumerate(search_logs):
    #         self.tableWidget_ads_deposit.insertRow(row)
    #         for column, data in enumerate(info):
    #             self.tableWidget_ads_deposit.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_ads_deposit, 'id'),
    #                                            self.createItem(str(info['id']),
    #                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #             self.tableWidget_ads_deposit.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_ads_deposit, 'logs'),
    #                                            self.createItem(str(info['logs']),
    #                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #             self.tableWidget_ads_deposit.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_ads_deposit, 'date'),
    #                                            self.createItem(str(info['date']),
    #                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #     self.tableWidget_ads_deposit.setSizeAdjustPolicy(
    #         QtWidgets.QAbstractScrollArea.AdjustToContents)
    #     self.tableWidget_ads_deposit.resizeColumnsToContents()
    #
    # def delete_ads_deposit(self):
    #     rows = self.tableWidget_ads_deposit.selectedIndexes()
    #     # rows = self.tableWidget_ads_deposit.selectionModel().selectedRows()
    #     for row in rows:
    #         id = self.tableWidget_ads_deposit.item(row.row(), 0).text()
    #         MYDATA.delete_ads_deposit(id)
    #     self.load_ads_deposit()

    # def commit_ads_deposit(self):
    #     # action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
    #     # column_total = self.tableWidget_ads_deposit.columnCount()
    #     row_total = self.tableWidget_ads_deposit.rowCount()
    #     for row in range(int(row_total)):
    #         id_column = self.getIndexHeaderTableWidget(self.tableWidget_ads_deposit, 'id')
    #         id = self.tableWidget_ads_deposit.item(row, id_column).text()
    #
    #         logs_column = self.getIndexHeaderTableWidget(self.tableWidget_ads_deposit, 'logs')
    #         logs = self.tableWidget_ads_deposit.item(row, logs_column).text()
    #
    #         date_column = self.getIndexHeaderTableWidget(self.tableWidget_ads_deposit, 'date')
    #         date = self.tableWidget_ads_deposit.item(row, date_column).text()
    #
    #         MYDATA.update_ads_deposit(id,
    #                            {
    #                                'logs': logs,
    #                                'date': date
    #                            })
    #
    # def menu_right_ads_deposit(self, pos):
    #     action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
    #
    #     menu = QMenu()
    #     item_add = menu.addAction(QIcon("icon/add.png"), u'Add')
    #     item_delete = menu.addAction(QIcon("icon/delete_folder.png"), u'Delete')
    #
    #     action = menu.exec_(self.tableWidget_ads_deposit.mapToGlobal(pos))
    #     if action == item_delete:
    #         self.delete_ads_deposit()
    #         return
    #
    #     if action == item_add:
    #         data = {'uid': self.username, 'logs': '', 'date': action_last}
    #     try:
    #         MYDATA.insert_ads_deposit(data)
    #     except:
    #         pass
    #     self.commit_ads_deposit()
    #     self.load_ads_deposit()
    #
    # def menu_right_ads_deposit_itemchanged(self):
    #     try:
    #         self.commit_ads_deposit()
    #     except:
    #         pass

    """tableWidget_ads_affiliate"""
    def load_ads_affiliate(self):
        self.tableWidget_ads_affliate.setRowCount(0)
        search_logs = MYDATA.search_ads_affiliate(self.username)
        for row, info in enumerate(search_logs):
            self.tableWidget_ads_affliate.insertRow(row)
            for column, data in enumerate(info):
                self.tableWidget_ads_affliate.setItem(int(row),
                                                     self.getIndexHeaderTableWidget(self.tableWidget_ads_affliate, 'id'),
                                                     self.createItem(str(info['id']),
                                                                     Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_ads_affliate.setItem(int(row),
                                                     self.getIndexHeaderTableWidget(self.tableWidget_ads_affliate,
                                                                                    'logs'),
                                                     self.createItem(str(info['logs']),
                                                                     Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_ads_affliate.setItem(int(row),
                                                     self.getIndexHeaderTableWidget(self.tableWidget_ads_affliate,
                                                                                    'date'),
                                                     self.createItem(str(info['date']),
                                                                     Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
        self.tableWidget_ads_affliate.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_ads_affliate.resizeColumnsToContents()

    def delete_ads_affiliate(self):
        rows = self.tableWidget_ads_affliate.selectedIndexes()
        # rows = self.tableWidget_ads_deposit.selectionModel().selectedRows()
        for row in rows:
            id = self.tableWidget_ads_affliate.item(row.row(), 0).text()
            MYDATA.delete_ads_affiliate(id)
        self.load_ads_affiliate()

    def commit_ads_affiliate(self):
        # column_total = self.tableWidget_ads_deposit.columnCount()
        row_total = self.tableWidget_ads_affliate.rowCount()
        for row in range(int(row_total)):
            id_column = self.getIndexHeaderTableWidget(self.tableWidget_ads_affliate, 'id')
            id = self.tableWidget_ads_affliate.item(row, id_column).text()

            logs_column = self.getIndexHeaderTableWidget(self.tableWidget_ads_affliate, 'logs')
            logs = self.tableWidget_ads_affliate.item(row, logs_column).text()

            date_column = self.getIndexHeaderTableWidget(self.tableWidget_ads_affliate, 'date')
            date = self.tableWidget_ads_affliate.item(row, date_column).text()
            MYDATA.update_ads_affiliate(id,
                                      {
                                          'logs': logs,
                                          'date': date
                                      })

    def menu_right_ads_affiliate(self, pos):
        action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")

        menu = QMenu()
        item_add = menu.addAction(QIcon("icon/add.png"), u'Add')
        item_delete = menu.addAction(QIcon("icon/delete_folder.png"), u'Delete')
        item_tracking = menu.addAction(QIcon("icon/add.png"), u'Tracking')
        item_camps = menu.addAction(QIcon("icon/add.png"), u'Camps: 20K')

        action = menu.exec_(self.tableWidget_ads_affliate.mapToGlobal(pos))
        if action == item_delete:
            self.delete_ads_affiliate()
            return

        if action == item_add:
            data = {'uid': self.username, 'logs': '', 'date': action_last}
        if action == item_tracking:
            data = {'uid': self.username, 'logs': 'Tracking', 'date': action_last}
        if action == item_camps:
            data = {'uid': self.username, 'logs': 'Camps: 20K', 'date': action_last}
        try:
            MYDATA.insert_ads_affiliate(data)
        except:
            pass
        self.commit_ads_affiliate()
        self.load_ads_affiliate()

    def menu_right_ads_affiliate_itemchanged(self):
        try:
            self.commit_ads_affiliate()
        except:
            pass

    """tableWidget_ads"""

    def load_gads(self):
        self.tableWidget_ads.setRowCount(0)
        search_logs = MYDATA.search_gads(self.username)
        for row, info in enumerate(search_logs):
            self.tableWidget_ads.insertRow(row)
            for column, data in enumerate(info):
                self.tableWidget_ads.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_ads, 'id'),
                                               self.createItem(str(info['id']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_ads.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_ads, 'logs'),
                                               self.createItem(str(info['logs']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_ads.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_ads, 'date'),
                                               self.createItem(str(info['date']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
        self.tableWidget_ads.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_ads.resizeColumnsToContents()

    def delete_gads(self):
        rows = self.tableWidget_ads.selectedIndexes()
        for row in rows:
            id = self.tableWidget_ads.item(row.row(), 0).text()
            MYDATA.delete_gads(id)
        self.load_gads()

    def commit_gads(self):
        row_total = self.tableWidget_ads.rowCount()
        for row in range(int(row_total)):
            id_column = self.getIndexHeaderTableWidget(self.tableWidget_ads, 'id')
            id = self.tableWidget_ads.item(row, id_column).text()

            logs_column = self.getIndexHeaderTableWidget(self.tableWidget_ads, 'logs')
            logs = self.tableWidget_ads.item(row, logs_column).text()

            date_column = self.getIndexHeaderTableWidget(self.tableWidget_ads, 'date')
            date = self.tableWidget_ads.item(row, date_column).text()

            MYDATA.update_gads(id,
                               {
                                   'logs': logs,
                                   'date': date
                               })

    def menu_right_gads(self, pos):
        action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        menu = QMenu()
        item_add = menu.addAction(QIcon("icon/add.png"), u'Add')
        item_delete = menu.addAction(QIcon("icon/delete_folder.png"), u'Delete')

        # xmdt: Xac minh danh tinh
        menu.addSeparator()
        _xmtc_wait = 'XM.TC/CN: WAIT'
        item_xmtc_wait= menu.addAction(QIcon("icon/add.png"), _xmtc_wait)
        _xmtc_submited = 'XM.TC/CN: SUBMITED'
        item_xmtc_submited= menu.addAction(QIcon("icon/add.png"), _xmtc_submited)
        _xmtc_success = 'XM.TC/CN: SUCCESS'
        item_xmtc_success = menu.addAction(QIcon("icon/add.png"), _xmtc_success)
        _xmtc_fail = 'XM.TC/CN: FAIL'
        item_xmtc_fail = menu.addAction(QIcon("icon/add.png"), _xmtc_fail)

        # TTDN: Thanh toan dang ngo
        menu.addSeparator()
        _ttdn_wait = 'TTDN: WAIT'
        item_ttdn_wait= menu.addAction(QIcon("icon/add.png"), _ttdn_wait)
        _ttdn_submited = 'TTDN: SUBMITED'
        item_ttdn_submited= menu.addAction(QIcon("icon/add.png"), _ttdn_submited)
        _ttdn_success = 'TTDN: SUCCESS'
        item_ttdn_success = menu.addAction(QIcon("icon/add.png"), _ttdn_success)
        _ttdn_fail = 'TTDN: FAIL'
        item_ttdn_fail = menu.addAction(QIcon("icon/add.png"), _ttdn_fail)

        # TNHT: Tranh ne he thong
        menu.addSeparator()
        _tnht_wait = 'TNHT: WAIT'
        item_tnht_wait= menu.addAction(QIcon("icon/add.png"), _tnht_wait)
        _tnht_submited = 'TNHT: SUBMITED'
        item_tnht_submited= menu.addAction(QIcon("icon/add.png"), _tnht_submited)
        _tnht_success = 'TNHT: SUCCESS'
        item_tnht_success = menu.addAction(QIcon("icon/add.png"), _tnht_success)
        _tnht_fail = 'TNHT: FAIL'
        item_tnht_fail = menu.addAction(QIcon("icon/add.png"), _tnht_fail)

        action = menu.exec_(self.tableWidget_ads.mapToGlobal(pos))
        if action == item_delete:
            self.delete_gads()
            return
        self.commit_gads()
        _logs = ''
        if action == item_add:
            _logs = ''
        # xmdt: Xac minh danh tinh
        if action == item_xmtc_wait:
            _logs = _xmtc_wait
        if action == item_xmtc_submited:
            _logs = item_xmtc_submited
        if action == item_xmtc_success:
            _logs = _xmtc_success
        if action == item_xmtc_fail:
            _logs = _xmtc_fail

        # TTDN: Thanh toan dang ngo
        if action == item_ttdn_wait:
            _logs = _ttdn_wait
        if action == item_ttdn_submited:
            _logs = _ttdn_submited
        if action == item_ttdn_success:
            _logs = _ttdn_success
        if action == item_ttdn_fail:
            _logs = _ttdn_fail

        # TNHT: Tranh ne he thong
        if action == item_tnht_wait:
            _logs = _tnht_wait
        if action == item_tnht_submited:
            _logs = _tnht_submited
        if action == item_tnht_success:
            _logs = _tnht_success
        if action == item_tnht_fail:
            _logs = _tnht_fail

        # add to database
        data = {'uid': self.username, 'logs': str(_logs), 'date': action_last}
        try:
            MYDATA.insert_gads(data)
            self.load_gads()
        except:
            pass

    def menu_right_gads_itemchanged(self):
        try:
            self.commit_gads()
        except:
            pass

    """Table: Adsense"""

    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    def load_gadsense(self):
        self.tableWidget_adsense.setRowCount(0)
        search_logs = MYDATA.search_gadsense(self.username)
        for row, info in enumerate(search_logs):
            self.tableWidget_adsense.insertRow(row)
            for column, data in enumerate(info):
                self.tableWidget_adsense.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_adsense, 'id'),
                                               self.createItem(str(info['id']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_adsense.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_adsense, 'logs'),
                                               self.createItem(str(info['logs']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_adsense.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_adsense, 'date'),
                                               self.createItem(str(info['date']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
        self.tableWidget_adsense.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_adsense.resizeColumnsToContents()

    def delete_gadsense(self):
        rows = self.tableWidget_adsense.selectedIndexes()
        # rows = self.tableWidget_level.selectionModel().selectedRows()
        for row in rows:
            id = self.tableWidget_adsense.item(row.row(), 0).text()
            MYDATA.delete_gadsense(id)
        self.load_gadsense()

    def commit_gadsense(self):
        row_total = self.tableWidget_adsense.rowCount()
        for row in range(int(row_total)):
            id_column = self.getIndexHeaderTableWidget(self.tableWidget_adsense, 'id')
            id = self.tableWidget_adsense.item(row, id_column).text()

            logs_column = self.getIndexHeaderTableWidget(self.tableWidget_adsense, 'logs')
            logs = self.tableWidget_adsense.item(row, logs_column).text()

            date_column = self.getIndexHeaderTableWidget(self.tableWidget_adsense, 'date')
            date = self.tableWidget_adsense.item(row, date_column).text()

            MYDATA.update_gadsense(id,
                                 {
                                     'logs': logs,
                                     'date': date
                                 })

    def menu_right_gadsense(self, pos):
        rowPosition = self.tableWidget_adsense.rowCount()
        menu = QMenu()
        item_add = menu.addAction(QIcon("icon/line.png"), u'Add')
        item_delete = menu.addAction(QIcon("icon/line.png"), u'Delete')

        items = []
        with open(MENU_RIGHT_GADSENSE_P, 'r', encoding='utf8') as f:
            ads_gadsense = f.readlines()
            for c in ads_gadsense:
                _line = str(c).split(':')
                _item = _line[0]
                if _item == 'item_1:':
                    menu.addSeparator()
                    continue
                _item = menu.addAction(QIcon("icon/line.png"), _line[1])
                items.append((_item, str(_line[1]).strip()))

        # Action: Delete
        action = menu.exec_(self.tableWidget_adsense.mapToGlobal(pos))
        if action == item_delete:
            self.delete_gadsense()
            self.commit_gadsense()
            return
        # Action: Add
        action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        if action == item_add:
            data = {'uid': self.username, 'logs': '', 'date': action_last}
        # Action: Other
        for i in items:
            if action == i[0]:
                data = {'uid': self.username, 'logs': i[1], 'date': action_last}
                break
        try:
            MYDATA.insert_gadsense(data)
            self.load_gadsense()
        except:
            pass

    def menu_right_gadsense_itemchanged(self):
        try:
            self.commit_gadsense()
        except:
            pass

    """"""

    """Table: Level"""
    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    def load_glevel(self):
        self.tableWidget_level.setRowCount(0)
        search_logs = MYDATA.search_glevel(self.username)
        for row, info in enumerate(search_logs):
            self.tableWidget_level.insertRow(row)
            for column, data in enumerate(info):
                self.tableWidget_level.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_level, 'id'),
                                               self.createItem(str(info['id']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_level.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_level, 'logs'),
                                               self.createItem(str(info['logs']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
                self.tableWidget_level.setItem(int(row), self.getIndexHeaderTableWidget(self.tableWidget_level, 'date'),
                                               self.createItem(str(info['date']),
                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
        self.tableWidget_level.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_level.resizeColumnsToContents()

    def delete_glevel(self):
        rows = self.tableWidget_level.selectedIndexes()
        # rows = self.tableWidget_level.selectionModel().selectedRows()
        for row in rows:
            id = self.tableWidget_level.item(row.row(), 0).text()
            MYDATA.delete_glevel(id)
        self.load_glevel()

    def commit_glevel(self):
        # action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        # column_total = self.tableWidget_level.columnCount()
        row_total = self.tableWidget_level.rowCount()
        for row in range(int(row_total)):
            id_column = self.getIndexHeaderTableWidget(self.tableWidget_level, 'id')
            id = self.tableWidget_level.item(row, id_column).text()

            logs_column = self.getIndexHeaderTableWidget(self.tableWidget_level, 'logs')
            logs = self.tableWidget_level.item(row, logs_column).text()

            date_column = self.getIndexHeaderTableWidget(self.tableWidget_level, 'date')
            date = self.tableWidget_level.item(row, date_column).text()

            MYDATA.update_glevel(id,
                               {
                                   'logs': logs,
                                   'date': date
                               })

    def menu_right_glevel(self, pos):
        rowPosition = self.tableWidget_level.rowCount()
        menu = QMenu()
        item_add = menu.addAction(QIcon("icon/line.png"), u'Add')
        item_delete = menu.addAction(QIcon("icon/line.png"), u'Delete')

        items = []
        with open(MENU_RIGHT_GLEVEL_P, 'r', encoding='utf8') as f:
            ads_glevel = f.readlines()
            for c in ads_glevel:
                _line = str(c).split(':')
                _item = _line[0]
                if _item == 'item_1:':
                    menu.addSeparator()
                    continue
                _item = menu.addAction(QIcon("icon/line.png"), _line[1])
                items.append((_item, str(_line[1]).strip()))

        # Action: Delete
        action = menu.exec_(self.tableWidget_level.mapToGlobal(pos))
        if action == item_delete:
            self.delete_glevel()
            self.commit_glevel()
            return
        # Action: Add
        action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
        if action == item_add:
            data = {'uid': self.username, 'logs': '', 'date': action_last}
        # Action: Other
        for i in items:
            if action == i[0]:
                data = {'uid': self.username, 'logs': i[1], 'date': action_last}
                break
        try:
            MYDATA.insert_glevel(data)
            self.load_glevel()
        except:
            pass

    def menu_right_glevel_itemchanged(self):
        try:
            self.commit_glevel()
        except:
            pass

    """"""

    def passwordrandom(self):
        password = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(5)))
        self.lineEdit_2.setText('YeuLa.{}'.format(password))

    def mail_get_t(self):
        t1 = threading.Thread(target=self.mail_get)
        t1.start()

    def mail_get(self):
        mail_line = str(self.lineEdit_3.text()).strip().split('|')
        e_user = mail_line[0]
        e_pass = mail_line[1]
        logging.info('Reading : {}|{}'.format(e_user, e_pass))
        if ('hotmail' in e_user) or ('outlook' in e_user):
            try:
                with Imbox('outlook.office365.com',
                           username=e_user,
                           password=e_pass,
                           ssl=True,
                           ssl_context=None,
                           starttls=False) as imbox:
                    # Gets all messages from the inbox
                    all_inbox_messages = imbox.messages(unread=True)
                    count = 0
                    for uid, message in all_inbox_messages:
                        imbox.mark_seen(uid)
                        if count >= 10:
                            break
                        mail_info = "{} - Date: {} Title: {} {}".format(e_user, message.date, message.subject, str(message.body['plain']).replace('\r','').replace('\n',''))
                        logging.info(mail_info)
                        count += 1

                # with MailBox('outlook.office365.com').login(e_user, e_pass) as mailbox:
                #     count = 0
                #     for msg in mailbox.fetch():
                #         if count >= 3:
                #             break
                #         mail_info = "{} - Date: {} Title: {} {}".format(e_user, msg.date, msg.subject, str(msg.text).replace('\r','').replace('\n',''))
                #         logging.info(mail_info)
                #         count += 1
            except Exception as ex:
                print(ex)

    def google_otp2fa(self):
        try:
            totp = pyotp.TOTP(re.sub(r'\s+', '', str(self.lineEdit_2fa.text())))
            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(totp.now(), mode=cb.Clipboard)
        except Exception as ex:
            print(ex)

    def editProxy(self):
        subprocess.Popen(["cmd", "/k", "start", "", PROXYSERVICES], stderr=subprocess.STDOUT)
    def editAdsWeb(self):
        subprocess.Popen(["cmd", "/k", "start", "", ADS_GOOGLE_WEB], stderr=subprocess.STDOUT)
    def editCard(self):
        subprocess.Popen(["cmd", "/k", "start", "", ADS_CARD_GOOGLE], stderr=subprocess.STDOUT)
    def editPlan(self):
        subprocess.Popen(["cmd", "/k", "start", "", GOOGLE_PLAN], stderr=subprocess.STDOUT)
    def getProxy_t(self):
        t1 = threading.Thread(target=self.getProxy)
        t1.start()

    def getProxy(self):
        proxyServices = ProxySevices()
        results = proxyServices.proxy_new(
            {"service": self.comboBox_2.currentText().split('|')[0],
             "api": self.comboBox_2.currentText().split('|')[1]})
        if results is None:
            self.lineEdit_11.setText('')
            return
        self.comboBox.setCurrentText('socks5')
        self.lineEdit_11.setText(results['socks']['ipv4'])
        logging.info(results['message'])

    def currenttime_tkcn(self):
        current = str(datetime.now().strftime("%m/%d/%Y-%H.%M.%S"))
        self.lineEdit_12.setText(current)

    def currenttime_mcc(self):
        current = str(datetime.now().strftime("%m/%d/%Y-%H.%M.%S"))
        self.lineEdit_13.setText(current)

    def edit(self):
        with open(GOOGLE_PLAN, 'r', encoding='utf8') as f:
            cardList = f.readlines()
        for c in cardList:
            self.comboBox_7.addItem(c.strip())

        with open(ADS_CARD_GOOGLE, 'r', encoding='utf8') as f:
            cardList = f.readlines()
        for c in cardList:
            self.comboBox_6.addItem(c.strip())

        with open(PROXYSERVICES, 'r', encoding='utf8') as f:
            proxyServicesList = f.readlines()
        for c in proxyServicesList:
            self.comboBox_2.addItem(c)
        # self.lineEdit_16.setText(c.split('|')[1])

        with open(ADS_GOOGLE_STATUS, 'r', encoding='utf8') as f:
            _lines = f.readlines()
        for c in _lines:
            self.comboBox_8.addItem(str(c).strip())

        with open(GOOGLE_STATUS, 'r', encoding='utf8') as f:
            _lines = f.readlines()
        for c in _lines:
            self.comboBox_11.addItem(str(c).strip())

        with open(GOOGLE_CAMPS, 'r', encoding='utf8') as f:
            _lines = f.readlines()
        for c in _lines:
            self.comboBox_google_ads.addItem(str(c).strip())

        info = MYDATA.select_data_google(self.username)
        #
        self.lineEdit.setText(str(info.username))
        self.lineEdit_2.setText(str(info.password))
        self.lineEdit_3.setText(str(info.recovery_mail))
        # self.comboBox_9.setCurrentText(str(info.admod))
        self.comboBox_11.setCurrentText(str(info.status))
        self.comboBox_7.setCurrentText(str(info.plan))

        # Ads
        self.comboBox_12.setCurrentText(str(info.ads_type))
        self.lineEdit_4.setText(str(info.ads_id))
        self.comboBox_8.setCurrentText(str(info.ads_status))
        self.comboBox_google_ads.setCurrentText(str(info.ads_camps))
        self.lineEdit_12.setText(str(info.ads_date))
        self.comboBox_5.setCurrentText(str(info.ads_currency))
        self.comboBox_6.setCurrentText(str(info.ads_payment))

        # self.lineEdit_6.setText(str(info.useragent))
        # self.lineEdit_7.setText(str(info.name))
        # self.lineEdit_8.setText(str(info.birthday))
        self.comboBox_10.setCurrentText(str(info.country))
        self.lineEdit_2fa.setText(str(info.twofa))
        self.lineEdit_10.setText(str(info.date_create))
        self.plainTextEdit.setPlainText(info.logs_google)
        self.plainTextEdit_marketplace.setPlainText(info.logs_marketplace)

        # proxy
        if ':' in info.proxy:
            proxy = str(info.proxy).split(":", 1)
            self.comboBox.setCurrentText(proxy[0])
            self.lineEdit_11.setText(proxy[1])


    def save(self):
        MYDATA.update_data_google(self.username, {
            'status': self.comboBox_11.currentText(),
            'username': self.lineEdit.text().strip(),
            'password': self.lineEdit_2.text().strip(),
            'recovery_mail': self.lineEdit_3.text().strip(),
            'plan': self.comboBox_7.currentText(),
            'ads_type': self.comboBox_12.currentText(),
            'ads_id': self.lineEdit_4.text().strip(),
            'ads_status': self.comboBox_8.currentText(),
            # 'ads_web': self.comboBox_ads_web.currentText(),
            'ads_date': self.lineEdit_12.text().strip(),
            'ads_currency': self.comboBox_5.currentText(),
            'ads_payment': self.comboBox_6.currentText(),
            'ads_camps': self.comboBox_google_ads.currentText(),

            # 'useragent': self.lineEdit_6.text().strip(),
            # 'name': self.lineEdit_7.text().strip(),
            # 'birthday': self.lineEdit_8.text().strip(),
            'country': self.comboBox_10.currentText(),
            'twofa': self.lineEdit_2fa.text().strip(),
            'date_create': self.lineEdit_10.text().strip(),
            'proxy': self.comboBox.currentText() + ':' + self.lineEdit_11.text().strip(),
            'logs_google': self.plainTextEdit.toPlainText(),
            'logs_marketplace': self.plainTextEdit_marketplace.toPlainText()
        })
        # QMessageBox.about(self, "Alert", "Save : Success")


class MarketplaceForm(QMainWindow, Ui_Marketplace):
    def __init__(self, ssn):
        super(MarketplaceForm, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon/facebook.png"))
        self.setWindowTitle("EDIT")

        self.ssn = ssn
        logging.info(f'Current - {ssn}')

        # Load Infos
        # self.handle_tabbar_clicked()
        # self.tabWidget.tabBarClicked.connect(self.handle_tabbar_clicked)

        # proxy-services
        self.pushButton_proxy_get.clicked.connect(self.proxyservices_current)
        self.pushButton_proxy_new.clicked.connect(self.proxyservices_new)

        # button Save
        self.pushButton_save.clicked.connect(self.tabinfos_save)
        self.pushButton_3.clicked.connect(self.tabinfos_save)
        self.pushButton_7.clicked.connect(self.tabinfos_save)
        self.pushButton_10.clicked.connect(self.tabinfos_save)
        self.pushButton_13.clicked.connect(self.tabinfos_save)

        # timer
        self.pushButton_4.clicked.connect(self.get_time_buyer)
        self.pushButton_5.clicked.connect(self.get_time_seller)
        self.pushButton_8.clicked.connect(self.get_time_buyer)
        self.pushButton_6.clicked.connect(self.get_time_seller)
        self.pushButton_11.clicked.connect(self.get_time_buyer)
        self.pushButton_9.clicked.connect(self.get_time_seller)
        self.pushButton_14.clicked.connect(self.get_time_buyer)
        self.pushButton_12.clicked.connect(self.get_time_seller)

        self.pushButton_19.clicked.connect(self.get_time_seller_draft)
        self.pushButton_20.clicked.connect(self.get_time_seller_draft)
        # opt
        self.pushButton_15.clicked.connect(self.amazon_get_otp)
        self.pushButton_16.clicked.connect(self.etsy_get_otp)

        # proxy
        with open(PROXYSERVICES, 'r', encoding='utf8') as f:
            self.proxyServicesList = f.readlines()
        for c in self.proxyServicesList:
            self.comboBox_proxyserver.addItem(c.split('|')[0])

    def etsy_get_otp(self):
        try:
            totp = pyotp.TOTP(re.sub(r'\s+', '', str(self.lineEdit_16.text())))
            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(totp.now(), mode=cb.Clipboard)
        except Exception as ex:
            print(ex)

    def amazon_get_otp(self):
        try:
            # re.sub(r'\s+', '', str(self.lineEdit_4.text()).strip())
            totp = pyotp.TOTP(re.sub(r'\s+', '', str(self.lineEdit_4.text())))
            cb = QApplication.clipboard()
            cb.clear(mode=cb.Clipboard)
            cb.setText(totp.now(), mode=cb.Clipboard)
        except Exception as ex:
            print(ex)

    def get_time_seller_draft(self):
        index = self.tabWidget.currentIndex()
        current = str(datetime.now().strftime("%m/%d/%Y-%H.%M.%S"))
        if self.tabWidget.tabText(index) == "Ebay":
            self.lineEdit_25.setText(current)
        if self.tabWidget.tabText(index) == "Etsy":
            self.lineEdit_26.setText(current)

    def get_time_buyer(self):
        index = self.tabWidget.currentIndex()
        current = str(datetime.now().strftime("%m/%d/%Y-%H.%M.%S"))
        if self.tabWidget.tabText(index) == "Amazon":
            self.lineEdit_8.setText(current)
        if self.tabWidget.tabText(index) == "Ebay":
            self.lineEdit_10.setText(current)
        if self.tabWidget.tabText(index) == "Etsy":
            self.lineEdit_13.setText(current)
        if self.tabWidget.tabText(index) == "Zazzle":
            self.lineEdit_19.setText(current)

    def get_time_seller(self):
        index = self.tabWidget.currentIndex()
        current = str(datetime.now().strftime("%m/%d/%Y-%H.%M.%S"))
        if self.tabWidget.tabText(index) == "Amazon":
            self.lineEdit_9.setText(current)
        if self.tabWidget.tabText(index) == "Ebay":
            self.lineEdit_11.setText(current)
        if self.tabWidget.tabText(index) == "Etsy":
            self.lineEdit_15.setText(current)
        if self.tabWidget.tabText(index) == "Zazzle":
            self.lineEdit_21.setText(current)

    def handle_tabbar_clicked(self):
        infos = MYDATA.select_data_marketplace(self.ssn)
        for i in range(self.tabWidget.count()):
            if self.tabWidget.tabText(i) == "Infos":
                self.load_infos("Infos", infos)
            if self.tabWidget.tabText(i) == "Amazon":
                amazon = MYDATA.select_data_marketplace_sites("Amazon", infos)
                self.load_infos("Amazon", amazon)
            if self.tabWidget.tabText(i) == "Ebay":
                ebay = MYDATA.select_data_marketplace_sites("Ebay", infos)
                self.load_infos("Ebay", ebay)
            if self.tabWidget.tabText(i) == "Etsy":
                etsy = MYDATA.select_data_marketplace_sites("Etsy", infos)
                self.load_infos("Etsy", etsy)
            if self.tabWidget.tabText(i) == "Zazzle":
                zazzle = MYDATA.select_data_marketplace_sites("Zazzle", infos)
                self.load_infos("Zazzle", zazzle)

    def load_infos(self, tabs, infos):
        if tabs == 'Infos':
            self.lineEdit_source.setText(infos.source)
            self.lineEdit_name.setText(string.capwords(infos.name))
            self.comboBox_gender.setCurrentText(str(infos.gender))
            self.lineEdit_dob.setText(infos.dob)
            self.lineEdit_address.setText(string.capwords(infos.address))
            self.lineEdit_city.setText(string.capwords(infos.city))
            self.lineEdit_state.setText(string.capwords(infos.state))
            self.lineEdit_statecode.setText(infos.statecode)
            self.lineEdit_zipcode.setText(infos.zipcode)
            self.lineEdit_country.setText(infos.country)
            self.lineEdit_phone.setText(infos.phone)
            self.lineEdit_ssn.setText(infos.ssn)
            self.comboBox_ssa_gov.setCurrentText(str(infos.ssa_gov))
            self.lineEdit_ein.setText(infos.ein)
            self.comboBox_irs.setCurrentText(str(infos.irs))
            self.comboBox_people.setCurrentText(str(infos.people))
            self.lineEdit_driverlicense.setText(infos.driver_license)
            self.textEdit_notes.setPlainText(infos.note)

            self.lineEdit_useragent.setText(infos.useragent)
            self.lineEdit_proxy.setText(infos.proxy)

            self.lineEdit_email.setText(infos.email)
            self.lineEdit_emailpass.setText(infos.email_pass)
            self.lineEdit_emailrecovery.setText(infos.email_recovery)
            self.textEdit_lastip.setPlainText(infos.ip_logs)

        if tabs == 'Amazon':
            self.lineEdit.setText(infos.username)
            self.lineEdit_2.setText(infos.password)
            self.comboBox.setCurrentText(str(infos.status))
            self.lineEdit_4.setText(infos.twofa)
            self.lineEdit_7.setText(infos.phone)
            self.lineEdit_8.setText(infos.buyer_date)
            self.lineEdit_9.setText(infos.seller_date)
            self.textEdit_2.setPlainText(infos.note)
        if tabs == 'Ebay':
            self.lineEdit_6.setText(infos.username)
            self.lineEdit_3.setText(infos.password)
            self.comboBox_2.setCurrentText(str(infos.status))
            self.lineEdit_5.setText(infos.twofa)
            self.lineEdit_12.setText(infos.phone)
            self.lineEdit_10.setText(infos.buyer_date)
            self.lineEdit_25.setText(infos.seller_draft_date)
            self.lineEdit_11.setText(infos.seller_date)
            self.lineEdit_27.setText(infos.seller_limited)
            self.textEdit_3.setPlainText(infos.note)
        if tabs == 'Etsy':
            self.lineEdit_17.setText(infos.username)
            self.lineEdit_14.setText(infos.password)
            self.comboBox_3.setCurrentText(str(infos.status))
            self.lineEdit_16.setText(infos.twofa)
            self.lineEdit_18.setText(infos.phone)
            self.lineEdit_13.setText(infos.buyer_date)
            self.lineEdit_26.setText(infos.seller_draft_date)
            self.lineEdit_15.setText(infos.seller_date)
            self.textEdit_4.setPlainText(infos.note)
        if tabs == 'Zazzle':
            self.lineEdit_23.setText(infos.username)
            self.lineEdit_20.setText(infos.password)
            self.comboBox_4.setCurrentText(str(infos.status))
            self.lineEdit_22.setText(infos.twofa)
            self.lineEdit_24.setText(infos.phone)
            self.lineEdit_19.setText(infos.buyer_date)
            self.lineEdit_21.setText(infos.seller_date)
            self.textEdit_5.setPlainText(infos.note)

    @pyqtSlot()
    def proxyservices_current(self):
        service = self.comboBox_proxyserver.currentText()
        proxyServices = ProxySevices()
        for c in self.proxyServicesList:
            site = c.split('|')[0]
            api = c.split('|')[1]
            expire = c.split('|')[2]
            if site == service:
                results = proxyServices.proxy_current({"service": site, "api": api})
                if results is None:
                    QMessageBox.about(self, "Alert", "Get Proxy: ERRORS")
                    return
                proxy = 'socks5:' + results['socks']['ipv4']
                self.lineEdit_proxy.setText(proxy)
                QMessageBox.about(self, "Alert", "Get Proxy: SUCCESS")

    @pyqtSlot()
    def proxyservices_new(self):
        service = self.comboBox_proxyserver.currentText()
        proxyServices = ProxySevices()
        for c in self.proxyServicesList:
            site = c.split('|')[0]
            api = c.split('|')[1]
            expire = c.split('|')[2]
            if site == service:
                results = proxyServices.proxy_new({"service": site, "api": api})
                if results is None:
                    QMessageBox.about(self, "Alert", "New Proxy: ERRORS")
                    return
                proxy = 'socks5:' + results['socks']['ipv4']
                self.lineEdit_proxy.setText(proxy)
                QMessageBox.about(self, "Alert", "New Proxy: SUCCESS")

    def tabinfos_save(self):
        info = MYDATA.select_data_marketplace(self.ssn)
        i = self.tabWidget.currentIndex()
        if self.tabWidget.tabText(i) == "Infos":
            MYDATA.update_data_marketplace(self.ssn, {
                'driver_license': self.lineEdit_driverlicense.text(),
                'ein': self.lineEdit_ein.text(),
                'irs': self.comboBox_irs.currentText(),
                'ssa_gov': self.comboBox_ssa_gov.currentText(),
                'people': self.comboBox_people.currentText(),
                'name': self.lineEdit_name.text(),
                'gender': self.comboBox_gender.currentText(),
                'dob': self.lineEdit_dob.text().strip(),
                'address': self.lineEdit_address.text(),
                'city': self.lineEdit_city.text(),
                'state': self.lineEdit_state.text(),
                'statecode': self.lineEdit_statecode.text(),
                'zipcode': self.lineEdit_zipcode.text(),
                'country': self.lineEdit_country.text(),
                'phone': self.lineEdit_phone.text(),

                'source': self.lineEdit_source.text(),
                'useragent': self.lineEdit_useragent.text(),
                'proxy': self.lineEdit_proxy.text(),

                'email': self.lineEdit_email.text().strip(),
                'email_pass': self.lineEdit_emailpass.text().strip(),
                'email_recovery': self.lineEdit_emailrecovery.text().strip(),
                'note': self.textEdit_notes.toPlainText()
            })
        if self.tabWidget.tabText(i) == "Amazon":
            MYDATA.update_data_marketplace_sites("Amazon", info, {
                'username': self.lineEdit.text().strip(),
                'password': self.lineEdit_2.text().strip(),
                'status': self.comboBox.currentText(),
                'twofa': self.lineEdit_4.text().strip(),
                'phone': self.lineEdit_7.text().strip(),
                'buyer_date': self.lineEdit_8.text().strip(),
                'seller_date': self.lineEdit_9.text().strip(),
                'note': self.textEdit_2.toPlainText()
            })
        if self.tabWidget.tabText(i) == "Ebay":
            MYDATA.update_data_marketplace_sites("Ebay", info, {
                'username': self.lineEdit_6.text().strip(),
                'password': self.lineEdit_3.text().strip(),
                'status': self.comboBox_2.currentText(),
                'twofa': self.lineEdit_5.text().strip(),
                'phone': self.lineEdit_12.text().strip(),
                'buyer_date': self.lineEdit_10.text().strip(),
                'seller_draft_date': self.lineEdit_25.text().strip(),
                'seller_date': self.lineEdit_11.text().strip(),
                'seller_limited': self.lineEdit_27.text().strip(),
                'note': self.textEdit_3.toPlainText()
            })
        if self.tabWidget.tabText(i) == "Etsy":
            MYDATA.update_data_marketplace_sites("Etsy", info, {
                'username': self.lineEdit_17.text().strip(),
                'password': self.lineEdit_14.text().strip(),
                'status': self.comboBox_3.currentText(),
                'twofa': self.lineEdit_16.text().strip(),
                'phone': self.lineEdit_18.text().strip(),
                'buyer_date': self.lineEdit_13.text().strip(),
                'seller_draft_date': self.lineEdit_26.text().strip(),
                'seller_date': self.lineEdit_15.text().strip(),
                'note': self.textEdit_4.toPlainText()
            })
        if self.tabWidget.tabText(i) == "Zazzle":
            MYDATA.update_data_marketplace_sites("Zazzle", info, {
                'username': self.lineEdit_23.text().strip(),
                'password': self.lineEdit_20.text().strip(),
                'status': self.comboBox_4.currentText(),
                'twofa': self.lineEdit_22.text().strip(),
                'phone': self.lineEdit_24.text().strip(),
                'buyer_date': self.lineEdit_19.text().strip(),
                'seller_date': self.lineEdit_21.text().strip(),
                'note': self.textEdit_5.toPlainText()
            })
        QMessageBox.about(self, "Alert", "Save : Success")


class AppWindow(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon("icon/facebook.png"))
        self.setWindowTitle("POD Tools v1.0.1")
        self.showMaximized()
        self.initUI()

    def initUI(self):
        log_path = './logs.txt'
        with open(log_path, 'r', encoding = 'windows-1252', errors='ignore') as f:
            self.plainTextEdit_logs.setPlainText(f.read())
        handler = Handler(self.plainTextEdit_logs)
        handler.setFormatter(
            logging.Formatter(
                '%(asctime)s %(message)s'))
        logging.getLogger().addHandler(handler)
        logging.getLogger().setLevel(logging.INFO)
        handler.new_record.connect(self.plainTextEdit_logs.appendPlainText)

        # Logs to plainTextEdit_logs
        fh = logging.FileHandler(log_path, encoding='windows-1252')
        fh.setLevel(logging.INFO)
        fh.setFormatter(
            logging.Formatter(
                '%(asctime)s %(message)s'))
        logging.getLogger().addHandler(fh)
        # self.plainTextEdit_logs.moveCursor(QtGui.QTextCursor.End)

        # backupdata
        self.backup_daily()

        # # line edit for filtering
        # self.lineEdit_search.returnPressed.connect(self.search)

        self.pushButton_search.clicked.connect(self.search)

        # # Proxy Service
        # self.proxy_change_service()
        # self.comboBox_proxy_services.currentTextChanged.connect(self.proxy_change_service)

        # # Run Tethering Proxy
        # self.phone_app_running()
        # self.pushButton_tethering_resetip.clicked.connect(self.phone_reset_ip)
        # self.pushButton_tethering_proxy.clicked.connect(self.phone_proxy_server)

        # Spoof: MAC, TimeZone
        # self.pushButton_spoof_timezone.clicked.connect(self.spoof_timezone)
        # self.pushButton_spoof_mac.clicked.connect(self.spoof_mac)

        # Get global Proxy
        # self.global_Proxies('read')
        # self.plainTextEdit_tethering_proxy.textChanged.connect(self.global_Proxies)

        # Tabs:
        self.tabWidget.setStyleSheet(self.stylesheetTableView())
        ## Tabs : Facebook
        # self.tableWidget.scrollToBottom()
        # self.tableWidget.setSizeAdjustPolicy
        #     QtWidgets.QAbstractScrollArea.AdjustToContents)
        # self.tableWidget.resizeColumnsToContents()
        # self.tabWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.tableWidget.itemDoubleClicked.connect(self.form_facebook_edit)
        self.tableView_Facebook.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_Facebook.customContextMenuRequested.connect(self.tablewidget_fb_menu)
        self.tableView_Facebook.setSortingEnabled(True)
        self.tableView_Facebook.setSelectionBehavior(QAbstractItemView.SelectRows)


        # self._sort_ads_cards()

        # Tab Tools
        # self.pushButton_regex.clicked.connect(self.tab_tools_regex)
        # self.pushButton_spotify.clicked.connect(self.tab_tools_spotify)

        # Tabs : Marketplace
        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_2.customContextMenuRequested.connect(self.tableWidget_marketplace_contextmenu)

        self.tableWidget_2.setSelectionBehavior(QAbstractItemView.SelectRows)

        # # Tabs : GoogleAds
        # self.tableWidget_3.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.tableWidget_3.customContextMenuRequested.connect(self.tableWidget_googleads_contextmenu)
        # self.tableWidget_3.setSortingEnabled(True)
        # self.tableWidget_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableWidget_3.cellClicked.connect(self.save_lastmouse)

        # Tabs: Google
        self.tableView_Google.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableView_Google.customContextMenuRequested.connect(self.tableView_Google_contextmenu)
        self.tableView_Google.setSortingEnabled(True)
        self.tableView_Google.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView_Google.clicked.connect(self.save_lastmouse)

        # Tabs
        self.tabWidget.setCurrentIndex(2)
        current_index = self.tabWidget.currentIndex()
        self.handle_tabbar_clicked(current_index)
        self.tabWidget.tabBarClicked.connect(self.handle_tabbar_clicked)

    def save_lastmouse(self, e):
        with open(GOOGLE_LAST, 'w') as f:
            f.write(str(e.row()))

    def edit_form_marketplace(self):
        row = self.tableWidget_2.currentIndex()
        ssn = self.tableWidget_2.item(int(row.row()), 1).text()
        # global _flag_thread
        # global _thread_edit
        # if _flag_thread or _thread_edit:
        #     QMessageBox.about(self, "WARNING", f'Other Thread Running !')
        #     return
        self.MarketplaceForm = MarketplaceForm(ssn)
        self.MarketplaceForm.show()

    def edit_form_google(self):
        global _flag_thread
        global _thread_edit
        if _flag_thread or _thread_edit:
            QMessageBox.about(self, "WARNING", f'Other Thread Running !')
            return
        row = self.tableView_Google.currentIndex()
        username = self.tableView_Google.model().index(row.row(), 2).data()
        self.GoogleForm = GoogleForm(username)
        self.GoogleForm.show()
        # try:
        #     self.GoogleForm = GoogleForm(username)
        #     self.GoogleForm.show()
        # except:
        #     logging.info('Errors - Loading EDIT form')


    def tableWidget_marketplace_contextmenu(self, pos):
        # Calculate how many pieces of data, default -1,
        row_num = -1
        for i in self.tableWidget_2.selectionModel().selection().indexes():
            row_num = i.row()

        menu = QMenu()
        browser_open = QAction(QIcon("icon/chrome.svg"), "CHROME", self)
        menu.addAction(browser_open)
        browser_open.triggered.connect(self.marketplace_open)

        menu.addSeparator()
        add_data_action = QAction(QIcon("icon/add.png"), "ADD", self)
        menu.addAction(add_data_action)
        add_data_action.triggered.connect(self.add_data_marketplace)
        folder_data_action = QAction(QIcon("icon/folder.png"), "FOLDER", self)
        menu.addAction(folder_data_action)
        folder_data_action.triggered.connect(self.folder_marketplace)
        edit_data_action = QAction(QIcon("icon/edit.png"), "EDIT", self)
        menu.addAction(edit_data_action)
        edit_data_action.triggered.connect(self.edit_form_marketplace)
        delete_action = QAction(QIcon("icon/trash.png"), "DELETE", self)
        menu.addAction(delete_action)
        delete_action.triggered.connect(self.delete_marketplace)

        menu.addSeparator()
        ip_action = QAction(QIcon("icon/ip.png"), "IP", self)
        menu.addAction(ip_action)
        ip_action.triggered.connect(self.ipScore)

        action = menu.exec_(self.tableWidget_2.mapToGlobal(pos))

    def tableView_Google_contextmenu(self, pos):
        # row_num = -1
        # for i in self.tableView_Google.selectionModel().selection().indexes():
        #     row_num = i.row()
        menu = QMenu()
        # table_reset = QAction(QIcon("icon/chrome.svg"), "RESET", self)
        # menu.addAction(table_reset)
        # table_reset.triggered.connect(self.table_reset)
        # menu.addSeparator()
        browser_open = QAction(QIcon("icon/chrome.svg"), "CHROME", self)
        menu.addAction(browser_open)
        browser_open.triggered.connect(self.google_open)

        menu.addSeparator()
        add_data_action = QAction(QIcon("icon/add.png"), "ADD", self)
        menu.addAction(add_data_action)
        add_data_action.triggered.connect(self.add_data_google)
        folder_data_action = QAction(QIcon("icon/folder.png"), "FOLDER", self)
        menu.addAction(folder_data_action)
        folder_data_action.triggered.connect(self.folder_google)
        edit_data_action = QAction(QIcon("icon/edit.png"), "EDIT", self)
        menu.addAction(edit_data_action)
        edit_data_action.triggered.connect(self.edit_form_google)
        delete_action = QAction(QIcon("icon/trash.png"), "DELETE", self)
        menu.addAction(delete_action)
        delete_action.triggered.connect(self.delete_google)

        menu.addSeparator()
        ip_action = QAction(QIcon("icon/ip.png"), "IP", self)
        menu.addAction(ip_action)
        ip_action.triggered.connect(self.ipScore)

        # CHeck email
        menu.addSeparator()
        c_email_action = QAction(QIcon("icon/ip.png"), "CHECKER GMAIL", self)
        menu.addAction(c_email_action)
        c_email_action.triggered.connect(self.check_email_t)

        # Copy email
        menu.addSeparator()
        subCopy = menu.addMenu(QIcon("icon/smartphone.png"), 'COPY')
        copy_email_action = QAction(QIcon("icon/copy.png"), "EMAIL", self)
        subCopy.addAction(copy_email_action)
        copy_email_action.triggered.connect(self.copy_email)

        action = menu.exec_(self.tableView_Google.mapToGlobal(pos))

    def tableWidget_googleads_contextmenu(self, pos):
        # Calculate how many pieces of data, default -1,
        row_num = -1
        for i in self.tableWidget_3.selectionModel().selection().indexes():
            row_num = i.row()

        menu = QMenu()
        # table_reset = QAction(QIcon("icon/chrome.svg"), "RESET", self)
        # menu.addAction(table_reset)
        # table_reset.triggered.connect(self.table_reset)
        # menu.addSeparator()
        browser_open = QAction(QIcon("icon/chrome.svg"), "CHROME", self)
        menu.addAction(browser_open)
        browser_open.triggered.connect(self.google_open)

        menu.addSeparator()
        add_data_action = QAction(QIcon("icon/add.png"), "ADD", self)
        menu.addAction(add_data_action)
        add_data_action.triggered.connect(self.add_data_google)
        folder_data_action = QAction(QIcon("icon/folder.png"), "FOLDER", self)
        menu.addAction(folder_data_action)
        folder_data_action.triggered.connect(self.folder_google)
        edit_data_action = QAction(QIcon("icon/edit.png"), "EDIT", self)
        menu.addAction(edit_data_action)
        edit_data_action.triggered.connect(self.edit_form_google)
        delete_action = QAction(QIcon("icon/trash.png"), "DELETE", self)
        menu.addAction(delete_action)
        delete_action.triggered.connect(self.delete_google)

        menu.addSeparator()
        ip_action = QAction(QIcon("icon/ip.png"), "IP", self)
        menu.addAction(ip_action)
        ip_action.triggered.connect(self.ipScore)

        # CHeck email
        menu.addSeparator()
        c_email_action = QAction(QIcon("icon/ip.png"), "CHECK EMAIL", self)
        menu.addAction(c_email_action)
        c_email_action.triggered.connect(self.check_email_t)

        # Copy email
        menu.addSeparator()
        subCopy = menu.addMenu(QIcon("icon/smartphone.png"), 'COPY')
        copy_email_action = QAction(QIcon("icon/copy.png"), "EMAIL", self)
        subCopy.addAction(copy_email_action)
        copy_email_action.triggered.connect(self.copy_email)

        action = menu.exec_(self.tableWidget_3.mapToGlobal(pos))

    def ipInfos(self):
        _flag_thread = True
        # rows = self.tableWidget_2.selectedIndexes()
        rows = self.tableWidget_2.selectionModel().selectedRows()
        for row in rows:
            ssn = self.tableWidget_2.item(row.row(), 1).text()
            infos = MYDATA.select_data_marketplace(ssn)
            score = Score(ssn, infos.proxy)
            score.proxy_data(logs=True)
            _flag_thread = False

    def check_email_t(self):
        t = threading.Thread(target=self.check_email)
        t.start()

    def check_email(self):
        with open(MAIL_YCHECKER, 'r', encoding='utf-8') as f:
            ycheckers = f.readlines()
        rows = self.tableView_Google.selectionModel().selectedRows()
        emails = []
        for index, row in enumerate(rows):
            index += 1
            e_username = self.tableView_Google.model().index(row.row(), 2).data()
            # # https://rapidapi.com/mrsonj/api/email-checker7/
            # # Limit 50 daily
            # url = "https://email-checker7.p.rapidapi.com/email-checker"
            # if "@" not in e :
            #     e = '{}@gmail.com'.format(e)
            # querystring = {"email": e}
            # headers = {
            #     "X-RapidAPI-Key": "dd414a12fbmsh9230cc3bf767711p1ccf53jsn9a1ea763ef8e",
            #     "X-RapidAPI-Host": "email-checker7.p.rapidapi.com"
            # }
            # response = requests.get(url, headers=headers, params=querystring)
            # data = response.json()
            # logging.info("[{}/{}][{}] - {}".format(index, len(rows), e, data))
            # if int(data['code']) == 200:
            #     MYDATA.update_data_google(e, {'status': data['items']['status']})
            e = e_username
            if "@" not in e_username:
                e = '{}@gmail.com'.format(e_username)
            # Get
            for ychecker in ycheckers:
                proxy = ychecker.split('|')[0]
                keyTemp = ychecker.split('|')[1]
                url = "https://ychecker.com/app/payload?email={}".format(e)
                proxy_ip = proxy.split(':')[0]
                proxy_port = proxy.split(':')[1]
                proxy_user = proxy.split(':')[2]
                proxy_pass = proxy.split(':')[3]
                proxies = {
                    'http': f"socks5h://{proxy_user}:{proxy_pass}@{proxy_ip}:{proxy_port}",
                    'https': f"socks5h://{proxy_user}:{proxy_pass}@{proxy_ip}:{proxy_port}"
                }
                try:
                    response = requests.get(url, proxies=dict(proxies), timeout=10, verify=False)
                    if response.status_code == 429:
                        logging.info("[ERRORS] - Limited 20 mail/ 60m")
                        return
                    data = response.json()
                except:
                    continue
                try:
                    if int(data['code']) == 200:
                        key = data['items']
                        url = "https://app.sonjj.com/v1/check_email/?payload={}".format(key)
                        response = requests.get(url, proxies=dict(proxies), timeout=10, verify=False)
                        data = response.json()
                        logging.info("[{}/{}][{}] - {}".format(index, len(rows), e, data))
                        if response.status_code == 200:
                            time_current = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
                            MYDATA.update_data_google(e_username, {'status': '{}:{}'.format(data['status'], time_current)})
                except:
                    logging.info("[ERRORS] - {}".format(url))
                    pass


    def copy_email(self):
        rows = self.tableView_Google.selectionModel().selectedRows()
        emails = []
        for row in rows:
            e = self.tableView_Google.model().index(row.row(), 2).data()
            emails.append(e)
        pyperclip.copy('\n'.join(emails))

    def ipScore(self):
        global _flag_thread
        if _flag_thread:
            return
        t_ip = threading.Thread(target=self.ipInfos)
        t_ip.start()
    def handle_tabbar_clicked(self, index):
        global _flag_thread
        if _flag_thread:
            return
        if self.tabWidget.tabText(index) == "Marketplace":
            try:
                t = threading.Thread(target=self.sort_data_marketplace)
                t.start()
            except:
                return
        if self.tabWidget.tabText(index) == "Google":
            try:
                t = threading.Thread(target=self.sortData_Google)
                t.start()
            except:
                return
        if self.tabWidget.tabText(index) == "Facebook":
            try:
                # infos = MYDATA.query_all_accounts('id')
                # self._sort_ads_cards()
                self._sort_camps_plans()
            except:
                return
    def headerColumns(self, name):
        for index in range(self.tableWidget_2.columnCount()):
            headItemText = self.tableWidget_2.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def sort_data_marketplace(self):
        global _flag_thread
        _flag_thread = True
        self.tableWidget_2.setDisabled(True)
        self.tableWidget_2.reset()
        self.tableWidget_2.setRowCount(0)
        # self.tableWidget_2.setSortingEnabled(False)

        infos = MYDATA.query_all_accounts_marketplace('id')
        for row, info in enumerate(infos):
            self.tableWidget_2.insertRow(row)
            self.tableWidget_2.setItem(int(row), self.headerColumns('ssa_gov'), self.createItem(str(info['ssa_gov']),
                                                                                                Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('source'), self.createItem(str(info['source']),
                                                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('ssn'), self.createItem(str(info['ssn']),
                                                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('irs'), self.createItem(str(info['irs']),
                                                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('people'), self.createItem(str(info['people']),
                                                                                               Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('name'), self.createItem(str(info['name']),
                                                                                             Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('email'), self.createItem(str(info['email']),
                                                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('state'), self.createItem(str(info['state']),
                                                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.tableWidget_2.setItem(int(row), self.headerColumns('country'), self.createItem(str(info['country']),
                                                                                                Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            # actions last
            if str(info['actions_last']) != 'None' and str(info['actions_last']) != '':
                actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info['actions_last'])
                actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                              int(actions_last[0][1]))  # provide UTC time
                actions_last_day = datetime.utcnow() - actions_last_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('actions_last'),
                                           self.createItem(f'{actions_last_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            # amazon
            info_amazon = MYDATA.search_marketplace('Amazon', info['amazon_id'])[0]
            if str(info_amazon['buyer_date']) != 'None' and str(info_amazon['buyer_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['buyer_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('amazon_buyer'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            if str(info_amazon['seller_date']) != 'None' and str(info_amazon['seller_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['seller_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('amazon_merch'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            # ebay
            info_amazon = MYDATA.search_marketplace('Ebay', info['ebay_id'])[0]
            if str(info_amazon['buyer_date']) != 'None' and str(info_amazon['buyer_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['buyer_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('ebay_buyer'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            if str(info_amazon['seller_date']) != 'None' and str(info_amazon['seller_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['seller_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('ebay_seller'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            if str(info_amazon['seller_draft_date']) != 'None' and str(info_amazon['seller_draft_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['seller_draft_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('ebay_draft'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            if str(info_amazon['seller_limited']) != 'None' and str(info_amazon['seller_limited']) != '':
                self.tableWidget_2.setItem(int(row), self.headerColumns('ebay_limited'),
                                           self.createItem(info_amazon['seller_limited'],
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            # etsy
            info_amazon = MYDATA.search_marketplace('Etsy', info['etsy_id'])[0]
            if str(info_amazon['buyer_date']) != 'None' and str(info_amazon['buyer_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['buyer_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('etsy_buyer'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            if str(info_amazon['seller_date']) != 'None' and str(info_amazon['seller_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['seller_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('etsy_seller'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            if str(info_amazon['seller_draft_date']) != 'None' and str(info_amazon['seller_draft_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['seller_draft_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('etsy_draft'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))

            # zazzle
            info_amazon = MYDATA.search_marketplace('Zazzle', info['zazzle_id'])[0]
            if str(info_amazon['buyer_date']) != 'None' and str(info_amazon['buyer_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['buyer_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('zazzle_buyer'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            if str(info_amazon['seller_date']) != 'None' and str(info_amazon['seller_date']) != '':
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info_amazon['seller_date'])
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                self.tableWidget_2.setItem(int(row), self.headerColumns('zazzle_seller'),
                                           self.createItem(f'{page_day.days}',
                                                           Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))

            # proxy
            self.tableWidget_2.setItem(int(row), self.headerColumns('proxy'), self.createItem(str(info['proxy']),
                                                                                              Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))

        self.tableWidget_2.resizeColumnsToContents()
        self.tableWidget_2.setDisabled(False)
        _flag_thread = False

    def headerColumnsGoogle(self, name):
        for index in range(self.tableWidget_3.columnCount()):
            headItemText = self.tableWidget_3.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def getHeaderColumnsIndex(self, _model, name):
        for index in range(_model.columnCount()):
            headItemText = _model.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def google_column_ads_color(self, index, police, modelGoogle):
        police = str(police).lower()
        if 'wait' in police:
            modelGoogle.setData(index, QColor(167, 230, 255), Qt.BackgroundRole)
            return
        if ('dash' in police):
            modelGoogle.setData(index, QColor(101, 183, 65), Qt.BackgroundRole)
            return
        if ('paid' in police):
            modelGoogle.setData(index, QColor(131, 96, 150), Qt.BackgroundRole)
            return
        if ('pin' in police):
            modelGoogle.setData(index, QColor(237, 123, 123), Qt.BackgroundRole)
            return
        if ('xmdt' in police):
            modelGoogle.setData(index, QColor(235, 231, 108), Qt.BackgroundRole)
            return


        if 'review' in police:
            modelGoogle.setData(index, QColor(160, 222, 255), Qt.BackgroundRole)
            return
        if 'pending' in police:
            modelGoogle.setData(index, QColor(53, 89, 224), Qt.BackgroundRole)
        if ('submited' in police) or ('pause' in police):
            modelGoogle.setData(index, QColor(194, 18, 146), Qt.BackgroundRole)
            return
        if ('success' in police) or ('run' in police) or ('camps' in police) or ('optimize' in police):
            modelGoogle.setData(index, QColor(101, 183, 65), Qt.BackgroundRole)
            return
        if ('hstt' in police) or ('learning' in police) or ('approve' in police):
            modelGoogle.setData(index, QColor(193, 242, 176), Qt.BackgroundRole)
            return
        if ('fail' in police) or ('suspend' in police):
            modelGoogle.setData(index, QColor(255, 47, 47), Qt.BackgroundRole)
            return
        if ('deactive' in police):
            modelGoogle.setData(index, QColor(255, 85, 128), Qt.BackgroundRole)
            return


    def sortData_Google(self):
        global _flag_thread
        _flag_thread = True

        self.tableView_Google.setDisabled(True)
        self.tableView_Google.reset()

        infos = MYDATA.query_all_accounts_google('id')
        modelGoogle = QtGui.QStandardItemModel(5, 3)
        modelGoogle.setHorizontalHeaderLabels([
            'id', 'source', 'username', 'status', 'password', 'country', 'age', 'r', '2fa', 'PLANS', 'last', 'add',
            'G_Adsense', 'AFF', 'ads_type', 'ads_id', 'G_Ads','PROJECT',  'k_XMDT', 'k_TNHT', 'k_OTHER', 'ads_payment',
            'ads_currency', 'ads_date', 'name', 'birthday', 'proxy', 'useragent'
             ])
        self.tableView_Google.setModel(modelGoogle)
        for row, info in enumerate(infos):
            _id = QtGui.QStandardItem(info['id'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'id'), _id)
            _source = QtGui.QStandardItem(info['source'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'source'), _source)
            _username = QtGui.QStandardItem(info['username'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'username'), _username)

            # status
            if '/' in str(info['status']):
                istatus = str(info['status']).split(':')
                actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', istatus[1])
                actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                              int(actions_last[0][1]))  # provide UTC time
                time_ads_id = datetime.utcnow() - actions_last_begin
                _status = QtGui.QStandardItem('{} ({})'.format(istatus[0], str(time_ads_id.days)))
            else:
                _status = QtGui.QStandardItem(info['status'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'status'), _status)
            _statusIndex = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'status'))
            ss_status = str(info['status']).lower()
            if 'disable' in ss_status:
                modelGoogle.setData(_statusIndex, QColor(255, 47, 47), Qt.BackgroundRole)
            if 'ok' in ss_status:
                modelGoogle.setData(_statusIndex, QColor(101, 183, 65), Qt.BackgroundRole)
            if 'verify' in ss_status:
                modelGoogle.setData(_statusIndex, QColor(116, 71, 197), Qt.BackgroundRole)

            _password = QtGui.QStandardItem(info['password'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'password'), _password)

            _recovery_mail = QtGui.QStandardItem('')
            if (':' in str(info['recovery_mail'])) or ('|' in str(info['recovery_mail'])):
                _recovery_mail = QtGui.QStandardItem('Y')
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'r'), _recovery_mail)

            # infos
            _name = QtGui.QStandardItem(info['name'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'name'), _name)
            _birthday = QtGui.QStandardItem(info['birthday'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'birthday'), _birthday)
            _country = QtGui.QStandardItem(info['country'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'country'), _country)
            # _note = QtGui.QStandardItem(info['note'])
            # modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'note'), _note)

            _twofa = QtGui.QStandardItem('Y')
            if (str(info['twofa']) == '') or (str(info['twofa']) is None):
                _twofa = QtGui.QStandardItem('')
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, '2fa'), _twofa)

            # PLANS
            _plan = QtGui.QStandardItem(info['plan'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'PLANS'), _plan)

            _date_create = QtGui.QStandardItem(info['date_create'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'age'), _date_create)
            _proxy = QtGui.QStandardItem(info['proxy'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'proxy'), _proxy)
            # _useragent = QtGui.QStandardItem(info['useragent'])
            # modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'useragent'), _useragent)

            # actions_last
            if str(info['actions_last']) != 'None' and str(info['actions_last']) != '':
                actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info['actions_last'])
                actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                  int(actions_last[0][1]))  # provide UTC time
                actions_last_day = datetime.utcnow() - actions_last_begin
                _actions_last = QtGui.QStandardItem(str(actions_last_day.days))
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'last'), _actions_last)

            # time_add
            if str(info['time_add']) != 'None' and str(info['time_add']) != '':
                time_add = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info['time_add'])
                time_add_begin = datetime(int(time_add[0][2]), int(time_add[0][0]),
                                                      int(time_add[0][1]))  # provide UTC time
                time_add_day = datetime.utcnow() - time_add_begin
                _time_add = QtGui.QStandardItem(str(time_add_day.days))
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'add'), _time_add)

            # ads
            _ads_type = QtGui.QStandardItem(info['ads_type'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'ads_type'), _ads_type)

            # ads_id
            if '/' in str(info['ads_date']):
                actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(info['ads_date']))
                actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                              int(actions_last[0][1]))  # provide UTC time
                time_ads_id = datetime.utcnow() - actions_last_begin
                _ads_id = QtGui.QStandardItem(str(time_ads_id.days))
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'ads_id'), _ads_id)

            # camps: run, pause, suspend
            _ads_camps = QtGui.QStandardItem(info['ads_camps'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'G_Ads'), _ads_camps)
            _index_ads_camps = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'G_Ads'))
            self.google_column_ads_color(_index_ads_camps, info['ads_camps'], modelGoogle)

            # ads_XMDT
            search_gads = MYDATA.search_gads(info['username'])
            if len(search_gads) > 0:
                affs = []
                for i in search_gads:
                    if 'xm.' in str(i['logs']).lower():
                        actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', i['date'])
                        actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                      int(actions_last[0][1]))  # provide UTC time
                        ago = datetime.utcnow() - actions_last_begin
                        affs.append(i['logs'] + " ("+ str(ago.days) + 'd)')

                ads_police = ', '.join(affs)
                _ads_police = QtGui.QStandardItem(ads_police)
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'k_XMDT'), _ads_police)
                _index = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'k_XMDT'))
                self.google_column_ads_color(_index, ads_police, modelGoogle)

            # k_OTHER
            search_gads = MYDATA.search_gads(info['username'])
            if len(search_gads) > 0:
                affs = []
                for i in search_gads:
                    if ('xm.' not in str(i['logs']).lower()) and ('tnht' not in str(i['logs']).lower()):
                        actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', i['date'])
                        actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                      int(actions_last[0][1]))  # provide UTC time
                        ago = datetime.utcnow() - actions_last_begin
                        affs.append(i['logs'] + " (" + str(ago.days) + 'd)')

                ads_police = ', '.join(affs)
                _ads_police = QtGui.QStandardItem(ads_police)
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'k_OTHER'), _ads_police)
                _index = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'k_OTHER'))
                self.google_column_ads_color(_index, ads_police, modelGoogle)

            # G_Adsense
            search_g_adsense = MYDATA.search_gadsense(info['username'])
            if len(search_g_adsense) > 0:
                affs = []
                for i in search_g_adsense:
                    actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', i['date'])
                    actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                  int(actions_last[0][1]))  # provide UTC time
                    ago = datetime.utcnow() - actions_last_begin
                    affs.append(i['logs'] + " (" + str(ago.days) + 'd)')

                ads_police = ', '.join(affs)
                _ads_police = QtGui.QStandardItem(ads_police)
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'G_Adsense'), _ads_police)
                _index = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'G_Adsense'))
                self.google_column_ads_color(_index, ads_police, modelGoogle)

            # AFF
            search_aff = MYDATA.search_glevel(info['username'])
            if len(search_aff) > 0:
                affs = []
                for i in search_aff:
                    if '#aff:' in str(i['logs']).lower():
                        actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', i['date'])
                        actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                      int(actions_last[0][1]))  # provide UTC time
                        ago = datetime.utcnow() - actions_last_begin
                        affs.append(i['logs'] + " (" + str(ago.days) + 'd)')

                ads_police = ', '.join(affs)
                _ads_police = QtGui.QStandardItem(ads_police)
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'AFF'), _ads_police)
                _index = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'AFF'))
                self.google_column_ads_color(_index, ads_police, modelGoogle)

            # ads_TNHT
            search_gads = MYDATA.search_gads(info['username'])
            if len(search_gads) >0:
                affs = []
                for i in search_gads:
                    if 'tnht' in str(i['logs']).lower():
                        actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', i['date'])
                        actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                      int(actions_last[0][1]))  # provide UTC time
                        ago = datetime.utcnow() - actions_last_begin
                        affs.append(i['logs'] + " ("+ str(ago.days) + 'd)')

                ads_police = ', '.join(affs)
                _ads_police= QtGui.QStandardItem(ads_police)
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'k_TNHT'), _ads_police)
                _index = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'k_TNHT'))
                self.google_column_ads_color(_index, ads_police, modelGoogle)

            # _ads_status = QtGui.QStandardItem(info['ads_status'])
            # _adsStatusIndex = modelGoogle.index(row, self.getHeaderColumnsIndex(modelGoogle, 'ads_STATUS'))
            # modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'ads_STATUS'), _ads_status)


            # PROJECT
            search_ads_affiliate = MYDATA.search_ads_affiliate(info['username'])
            if len(search_ads_affiliate) >0:
                affs = []
                for i in search_ads_affiliate:
                    actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', i['date'])
                    actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                  int(actions_last[0][1]))  # provide UTC time
                    ago = datetime.utcnow() - actions_last_begin
                    affs.append(i['logs'] + " (" + str(ago.days) + 'd)')

                _ads_web = QtGui.QStandardItem(', '.join(affs))
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'PROJECT'), _ads_web)

            if str(info['ads_date']) != 'None' and str(info['ads_date']) != '':
                actions_last = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', info['ads_date'])
                actions_last_begin = datetime(int(actions_last[0][2]), int(actions_last[0][0]),
                                                  int(actions_last[0][1]))  # provide UTC time
                actions_last_day = datetime.utcnow() - actions_last_begin
                _ads_date = QtGui.QStandardItem(str(actions_last_day.days))
                modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'ads_date'), _ads_date)

            _ads_currency = QtGui.QStandardItem(info['ads_currency'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'ads_currency'), _ads_currency)
            _ads_payment = QtGui.QStandardItem(info['ads_payment'])
            modelGoogle.setItem(row, self.getHeaderColumnsIndex(modelGoogle, 'ads_payment'), _ads_payment)

        # Resize column
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'id'), 35)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'password'), 80)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'age'), 50)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'status'), 45)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'r'), 35)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, '2fa'), 35)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'PLANS'), 75)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'last'), 35)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'add'), 35)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'ads_id'), 45)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'ads_type'), 90)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'PROJECT'), 300)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'country'), 90)
        self.tableView_Google.setColumnWidth(self.getHeaderColumnsIndex(modelGoogle, 'G_Ads'), 85)

        self.tableView_Google.setDisabled(False)
        _flag_thread = False
        with open(GOOGLE_LAST, 'r', encoding='utf8') as f:
            row = int(f.readlines()[0])
            index = self.tableView_Google.model().index(row, 0)
            time.sleep(3)
            self.tableView_Google.selectRow(row)
            self.tableView_Google.scrollTo(index)


    def folder_marketplace(self):
        rows = self.tableWidget_2.selectionModel().selectedRows()
        for row in rows:
            ssn = self.tableWidget_2.item(row.row(), 1).text()
            Popen(
                f'explorer.exe "search-ms:query={ssn}&crumb=location:{PROFILES_MARKETPLACE}&"')

    def folder_google(self):
        rows = self.tableView_Google.selectionModel().selectedRows()
        for row in rows:
            username = self.tableView_Google.model().index(row.row(), 2).data()
            Popen(
                f'explorer.exe "search-ms:query={username}&crumb=location:{PROFILES_GOOGLE}&"')

    def delete_marketplace(self):
        # rows = self.tableWidget_2.selectedIndexes()
        rows = self.tableWidget_2.selectionModel().selectedRows()
        for row in rows:
            ssn = self.tableWidget_2.item(row.row(), 1).text()
            folder = f'{PROFILES_MARKETPLACE}/{ssn}-dolphin'
            reply = QMessageBox.question(
                self,
                "Warning !!",
                f"Status: Live. Are you delete it : {ssn} ?",
                QMessageBox.Yes,
                QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                if os.path.isdir(folder):
                    try:
                        MYDATA.delete_marketplace(ssn)
                        self.remove_dir(folder)
                        logging.info(f'Success - Deleted: {folder}')
                    except:
                        logging.info(f'Fail - Deleted: {folder}')

    def delete_google(self):
        rows = self.tableView_Google.selectionModel().selectedRows()
        for row in rows:
            username = self.tableView_Google.model().index(row.row(), 2).data()
            folder = f'{PROFILES_GOOGLE}/{username}-dolphin'
            reply = QMessageBox.question(
                self,
                "Warning !!",
                f"Status: Live. Are you delete it : {username} ?",
                QMessageBox.Yes,
                QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                MYDATA.delete_google(username)
                if os.path.isdir(folder):
                    self.remove_dir(folder)
                    logging.info(f'Success - Deleted: {username}')

    def add_data_marketplace(self):
        data_clipboard = QApplication.clipboard().text()
        datas = data_clipboard.split('\n')
        for line in datas:
            if line.strip() == "":
                continue
            _info = line.strip().split('|')
            if len(_info) < 5:
                QMessageBox.about(self, "Alert", "ERRORS")
                return
            infos = dict()
            infos['source'] = _info[0]
            infos['ssn'] = _info[1].strip()
            infos['ein'] = ''
            infos['irs'] = ''
            infos['people'] = ''
            infos['driver_license'] = ''
            infos['ssa_gov'] = ''
            infos['name'] = string.capwords(_info[2])
            infos['gender'] = ''
            infos['dob'] = _info[3]
            infos['address'] = string.capwords(_info[4])
            infos['city'] = string.capwords(_info[5])
            infos['state'] = string.capwords(_info[6])
            infos['statecode'] = _info[7]
            infos['zipcode'] = _info[8]
            infos['country'] = _info[9]
            infos['phone'] = _info[10]
            infos['email'] = _info[11]
            infos['email_pass'] = _info[12]
            infos['email_recovery'] = _info[13]
            infos['proxy'] = _info[14]
            infos['note'] = ''

            # browsersInfos = [
            #     # "gologin|97|Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
            #     # "gologin|100|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
            #     # "gologin|103|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            #     # "dolphin|99|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
            #     # "dolphin|100|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
            #     # "dolphin|101|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            #     "dolphin|103|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
            # ]
            # _browsersInfos = random.choice(browsersInfos).split('|')
            # infos['useragent'] = str({
            #     'browser': _browsersInfos[0],
            #     'version': _browsersInfos[1],
            #     'useragent': _browsersInfos[2]
            # })

            MYDATA.insert_data_marketpalce(infos)
        QMessageBox.about(self, "Alert", "SUCCESS")

    def add_data_google(self):
        data_clipboard = QApplication.clipboard().text()
        datas = data_clipboard.split('\n')
        for line in datas:
            if line.strip() == "":
                continue
            info = line.strip().split('|')
            if len(info) < 5:
                QMessageBox.about(self, "Alert", "ERRORS")
                return
            infos = dict()
            infos['source'] = info[0]
            infos['status'] = ''
            infos['username'] = info[1].strip()
            infos['password'] = info[2].strip()
            infos['recovery_mail'] = info[3].strip()
            infos['twofa'] = ''

            infos['plan'] = ''
            infos['ads_type'] = ''
            infos['ads_id'] = ''
            infos['ads_status'] = ''
            infos['ads_date'] = ''
            infos['ads_payment'] = ''
            infos['ads_currency'] = ''
            infos['ads_web'] = ''
            infos['ads_camps'] = ''

            infos['name'] = ''
            infos['birthday'] = ''
            infos['country'] = info[5].strip()
            infos['logs_google'] = ''
            infos['logs_marketplace'] = ''


            infos['date_create'] = info[4].strip()
            infos['proxy'] = 'socks5:103.124.94.246:37848:YrSg:6V61'
            infos['actions_last'] = ''
            infos['time_add'] = str(datetime.now().strftime("%m/%d/%Y-%H.%M.%S"))

            browsersInfos = ["dolphin|107|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"]
            _browsersInfos = random.choice(browsersInfos).split('|')
            infos['useragent'] = str({
                'browser': _browsersInfos[0],
                'version': _browsersInfos[1],
                'useragent': _browsersInfos[2]
            })
            MYDATA.insert_data_google(infos)
        QMessageBox.about(self, "Alert", "SUCCESS")

    def marketplace_open(self):
        # rows = self.tableWidget_2.selectedIndexes()
        rows = self.tableWidget_2.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            ssn = self.tableWidget_2.item(row.row(), 1).text()
            info = MYDATA.select_data_marketplace(ssn)
            _infos = {
                'fb_browsers': info.useragent,
                'fb_infos': info,
                'fb_user': ssn,
                'proxy_private': str(info.proxy),
                'debug_port': debug_port,

            }
            infos.append(_infos)
        self._thread = QThread(self)
        self._worker = MarketplaceBrowser('marketplace_browsers_spoof', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        # self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def google_open_status(self, pids):
        chromeId, proxyId = pids
        p = myThread(chromeId, proxyId)
        p.start()

    def stylesheet(self):
        # background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #babdb6, stop: 0.5 #d3d7cf, stop: 1 #babdb6);
            return """
        QTableWidget
        {
        background: #FFD89C;
        selection-color: white;
        border: 1px solid lightgrey;
        selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #219C90, stop: 1  #219C90);
        color: #202020;
        outline: 0;
        } 
        QTableWidget::item::hover{
        background-color: rgba(222,100,123,100);
        }
        QTableWidget::item::focus
        {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #219C90, stop: 1  #219C90);
        border: 0px;
        }
        """

    def stylesheetTableView(self):
            return """
        QTableView
        {
        background: #FFD89C;
        selection-color: white;
        border: 1px solid lightgrey;
        selection-background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #219C90, stop: 1  #219C90);
        color: #202020;
        outline: 0;
        } 
        QTableView::item::hover{
        background-color: rgba(222,100,123,100);
        }
        QTableView::item::focus
        {
        background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #219C90, stop: 1  #219C90);
        border: 0px;
        }
        """

    def google_open(self):
        index = self.tableView_Google.selectionModel().selectedRows()
        infos = []
        for row in index:
            debug_port = random.randint(1000, 9999)
            username = str(self.tableView_Google.model().index(row.row(), 2).data()).strip()
            info = MYDATA.select_data_google(username)
            _infos = {
                'fb_browsers': info.useragent,
                'fb_infos': info,
                'fb_user': username,
                'proxy_private': str(info.proxy),
                'debug_port': debug_port,
            }
            infos.append(_infos)
        self._thread = QThread(self)
        self._worker = GoogleBrowser('google_browsers_spoof', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        # self._worker.sig.connect(self.google_open_status)
        self._thread.start()

    def tablewidget_fb_menu(self, pos):
        # # Calculate how many pieces of data, default -1,
        # row_num = -1
        # for i in self.tableView_Facebook.selectionModel().selection().indexes():
        #     row_num = i.row()
        menu = QMenu()
        # # Via
        # subMenu_via = menu.addMenu(QIcon("icon/danger.png"), '')
        # menu.addSeparator()
        # mobile_get_all_friend_action = QAction(QIcon("icon/teamwork.png"), "Get all friend", self)
        # subMenu_via.addAction(mobile_get_all_friend_action)
        # mobile_get_all_friend_action.triggered.connect(self.mobile_get_all_friend)

        # Emulator -Folder
        subMenu = menu.addMenu(QIcon("icon/computer.png"), 'SORT')
        sort_begin = QAction(QIcon("icon/line.png"), "Begin days", self)
        subMenu.addAction(sort_begin)
        sort_begin.triggered.connect(self._sort_begin)
        sort_last = QAction(QIcon("icon/line.png"), "Last days", self)
        subMenu.addAction(sort_last)
        sort_last.triggered.connect(self._sort_last)

        ## Camps
        sort_camps = QAction(QIcon("icon/line.png"), "Camps - Plans", self)
        subMenu.addAction(sort_camps)
        sort_camps.triggered.connect(self._sort_camps_plans)
        sort_camps_pixels = QAction(QIcon("icon/line.png"), "Camps - Pixels", self)
        subMenu.addAction(sort_camps_pixels)
        sort_camps_pixels.triggered.connect(self._sort_camps_pixels)
        sort_camps_groups = QAction(QIcon("icon/line.png"), "Camps - Groups", self)
        subMenu.addAction(sort_camps_groups)
        sort_camps_groups.triggered.connect(self._sort_camps_groups)

        # subMenu.addSeparator()
        sort_ads_tuts = QAction(QIcon("icon/line.png"), "Ads - Tuts", self)
        subMenu.addAction(sort_ads_tuts)
        sort_ads_tuts.triggered.connect(self._sort_ads_tuts)
        # subMenu.addSeparator()
        sort_country = QAction(QIcon("icon/line.png"), "Country", self)
        subMenu.addAction(sort_country)
        sort_country.triggered.connect(self._sort_country)
        # subMenu.addSeparator()
        sort_groups = QAction(QIcon("icon/line.png"), "Groups", self)
        subMenu.addAction(sort_groups)
        sort_groups.triggered.connect(self._sort_groups)
        #
        sort_ads_cards = QAction(QIcon("icon/line.png"), "Ads - Cards", self)
        subMenu.addAction(sort_ads_cards)
        sort_ads_cards.triggered.connect(self._sort_ads_cards)
        #
        sort_ads_bm = QAction(QIcon("icon/line.png"), "Ads - BM", self)
        subMenu.addAction(sort_ads_bm)
        sort_ads_bm.triggered.connect(self._sort_ads_bm)

        #
        menu.addSeparator()
        edit_action = QAction(QIcon("icon/edit.png"), "EDIT", self)
        menu.addAction(edit_action)
        edit_action.triggered.connect(self.form_facebook_edit)

        # ################ Emulator Mobile ################
        menu.addSeparator()
        subMenu_emulator = menu.addMenu(QIcon("icon/emulator.png"), 'EMULATOR')
        # subMenu_cloneviet = subMenu_mobile_emulator.addMenu(QIcon("icon/emulator.png"), 'Clone Viet')
        # # clone viet
        # mobile_emulator_cloneviet_login_action = QAction(QIcon("icon/password.png"), "LOGIN", self)
        # subMenu_cloneviet.addAction(mobile_emulator_cloneviet_login_action)
        # mobile_emulator_cloneviet_login_action.triggered.connect(self.mobile_emulator_cloneviet_login)
        # #
        # mobile_emulator_cloneviet_backup_action = QAction(QIcon("icon/backup.png"), "BACKUP", self)
        # subMenu_cloneviet.addAction(mobile_emulator_cloneviet_backup_action)
        # mobile_emulator_cloneviet_backup_action.triggered.connect(self.mobile_emulator_cloneviet_backup)
        # #
        # mobile_emulator_cloneviet_restore_action = QAction(QIcon("icon/restore.png"), "RESTORE", self)
        # subMenu_cloneviet.addAction(mobile_emulator_cloneviet_restore_action)
        # mobile_emulator_cloneviet_restore_action.triggered.connect(self.mobile_emulator_cloneviet_restore)
        # #
        # mobile_emulator_cloneviet_restore_c_action = QAction(QIcon("icon/restore.png"), "RESTORE NOT CLOSE", self)
        # subMenu_cloneviet.addAction(mobile_emulator_cloneviet_restore_c_action)
        # mobile_emulator_cloneviet_restore_c_action.triggered.connect(self.mobile_emulator_cloneviet_restore_no_quit)

        # # firt login
        # subMenu_mobile_emulator.addSeparator()
        # mobile_emulator_firtlogin_action = QAction(QIcon("icon/password.png"), "LOGIN", self)
        # subMenu_mobile_emulator.addAction(mobile_emulator_firtlogin_action)
        # mobile_emulator_firtlogin_action.triggered.connect(self.emulator_login)
        #
        # # login - no addproxy
        # subMenu_mobile_emulator.addSeparator()
        # emulator_login_no_addproxy_action = QAction(QIcon("icon/password.png"), "LOGIN-NoAddProxy", self)
        # subMenu_mobile_emulator.addAction(emulator_login_no_addproxy_action)
        # emulator_login_no_addproxy_action.triggered.connect(self.emulator_login_no_addproxy)

        # # backup
        # subMenu_mobile_emulator.addSeparator()
        # emulator_backup_action = QAction(QIcon("icon/backup.png"), "BACKUP", self)
        # subMenu_mobile_emulator.addAction(emulator_backup_action)
        # emulator_backup_action.triggered.connect(self.emulator_backup)
        # # restore
        # subMenu_mobile_emulator.addSeparator()
        # emulator_restore_action = QAction(QIcon("icon/restore.png"), "RESTORE", self)
        # subMenu_mobile_emulator.addAction(emulator_restore_action)
        # emulator_restore_action.triggered.connect(self.emulator_restore)
        #
        # # subMenu_mobile_emulator.addSeparator()
        # emulator_restore_no_quit_action = QAction(QIcon("icon/restore.png"), "RESTORE NOT CLOSE", self)
        # subMenu_mobile_emulator.addAction(emulator_restore_no_quit_action)
        # emulator_restore_no_quit_action.triggered.connect(self.emulator_restore_no_quit)

        # Emulator -Folder
        subMenu_emulator.addSeparator()
        emulator_folder_q = QAction(QIcon("icon/folder.png"), "FOLDER", self)
        subMenu_emulator.addAction(emulator_folder_q)
        emulator_folder_q.triggered.connect(self.emulator_folder)

        # Emulator - Reactions
        subMenu_emulator.addSeparator()
        emulator_reactions_q = QAction(QIcon("icon/robot.png"), "REACTIONS", self)
        subMenu_emulator.addAction(emulator_reactions_q)
        emulator_reactions_q.triggered.connect(self.emulator_reactions)
        # self.emulator_reactions_stop = QAction(QIcon("icon/reactions.png"), "ROBOT - STOP", self)
        # subMenu_emulator.addAction(self.emulator_reactions_stop)
        # Login
        # subMenu_emulator.addSeparator()
        emulator_fb_login_multi_q = QAction(QIcon("icon/robot.png"), "CLOGIN", self)
        subMenu_emulator.addAction(emulator_fb_login_multi_q)
        emulator_fb_login_multi_q.triggered.connect(self.emulator_fb_login_multi)
        # Change pass
        # subMenu_emulator.addSeparator()
        emulator_fb_pass_multi_q = QAction(QIcon("icon/robot.png"), "CPASS", self)
        subMenu_emulator.addAction(emulator_fb_pass_multi_q)
        emulator_fb_pass_multi_q.triggered.connect(self.emulator_fb_pass_multi)

        ################## Computer ##################
        menu.addSeparator()
        computer_profile_action_cmd = QAction(QIcon("icon/chrome.png"), "CHROME", self)
        menu.addAction(computer_profile_action_cmd)
        computer_profile_action_cmd.triggered.connect(self.robot_facebook_cmd)

        menu.addSeparator()
        subMenu = menu.addMenu(QIcon("icon/computer.png"), "COMPUTER")

        # computer_profile_action_cmd_ex = QAction(QIcon("icon/profile.png"), "OPEN with Extensions", self)
        # subMenu.addAction(computer_profile_action_cmd_ex)
        # computer_profile_action_cmd_ex.triggered.connect(self.robot_facebook_cmd_extensions)

        # computer_profile_action_cmd_cookies = QAction(QIcon("icon/chrome.png"), "CHROME COOKIES", self)
        # subMenu.addAction(computer_profile_action_cmd_cookies)
        # computer_profile_action_cmd_cookies.triggered.connect(self.robot_facebook_cmd_cookies)

        computer_open_profile_action = QAction(QIcon("icon/folder.png"), "FOLDER", self)
        subMenu.addAction(computer_open_profile_action)
        computer_open_profile_action.triggered.connect(self.computer_open_profile)

        computer_delete_profile_action = QAction(QIcon("icon/trash.png"), "DELETE", self)
        subMenu.addAction(computer_delete_profile_action)
        computer_delete_profile_action.triggered.connect(self.computer_delete_profile)
        # Ads
        subMenu.addSeparator()
        computer_browser_reactions_action = QAction(QIcon("icon/robot.png"), "Reactions", self)
        subMenu.addAction(computer_browser_reactions_action)
        computer_browser_reactions_action.triggered.connect(self.robot_computer_facebook_reactions)
        computer_business_add_infos = QAction(QIcon("icon/robot.png"), "Ads - Add Infos", self)
        subMenu.addAction(computer_business_add_infos)
        computer_business_add_infos.triggered.connect(self.robot_facebook_business_add_infos)
        # computer_bussiness_add_card = QAction(QIcon("icon/trash.png"), "Ads - Add Card", self)
        # subMenu.addAction(computer_bussiness_add_card)
        # computer_bussiness_add_card.triggered.connect(self.robot_bussiness_add_card)

        subMenu.addSeparator()

        computer_browser_initial_action = QAction(QIcon("icon/robot.png"), "Initial", self)
        subMenu.addAction(computer_browser_initial_action)
        computer_browser_initial_action.triggered.connect(self.robot_facebook_setups)

        ################## MOBILE ##################
        subMenuMobile = menu.addMenu(QIcon("icon/smartphone.png"), 'MOBILE')
        # mobile_browser_a_cmd = QAction(QIcon("icon/profile.png"), "CMD", self)
        # subMenuMobile.addAction(mobile_browser_a_cmd)
        # mobile_browser_a_cmd.triggered.connect(self.robot_mobile_facebook_cmd)

        mobile_browser_reactions_action = QAction(QIcon("icon/robot.png"), "Reactions", self)
        subMenuMobile.addAction(mobile_browser_reactions_action)
        mobile_browser_reactions_action.triggered.connect(self.robot_mobile_facebook_reactions)

        mobile_browser_login_action = QAction(QIcon("icon/robot.png"), "Login", self)
        subMenuMobile.addAction(mobile_browser_login_action)
        mobile_browser_login_action.triggered.connect(self.robot_facebook_login)

        mobile_browser_c_page_action = QAction(QIcon("icon/robot.png"), "Create Pages", self)
        subMenuMobile.addAction(mobile_browser_c_page_action)
        mobile_browser_c_page_action.triggered.connect(self.robot_facebook_page)

        mobile_browser_fb_infos_action = QAction(QIcon("icon/robot.png"), "Get Infos", self)
        subMenuMobile.addAction(mobile_browser_fb_infos_action)
        mobile_browser_fb_infos_action.triggered.connect(self.robot_facebook_infos)

        ################## MAIL ##################
        subMenuMail = menu.addMenu(QIcon("icon/mail.png"), 'MAIL')
        # Mail
        # subMenu.addSeparator()
        mail_login_action = QAction(QIcon("icon/robot.png"), "Login", self)
        subMenuMail.addAction(mail_login_action)
        mail_login_action.triggered.connect(self.robot_mail_login)
        #
        mail_changepass_action = QAction(QIcon("icon/robot.png"), "Outlook - Change password", self)
        subMenuMail.addAction(mail_changepass_action)
        mail_changepass_action.triggered.connect(self.robot_mail_changepass)

        # #
        # computer_test_action = QAction(QIcon("icon/password.png"), "Test", self)
        # subMenu.addAction(computer_test_action)
        # computer_test_action.triggered.connect(self.computer_test)
        # # mail
        # subMenu.addSeparator()
        # computer_mail_action = QAction(QIcon("icon/password.png"), "library/mail", self)
        # subMenu.addAction(computer_mail_action)
        # computer_mail_action.triggered.connect(self.computer_mail)
        # # login user-pass - chrome profile
        # subMenu.addSeparator()
        # computer_login_userpass_action = QAction(QIcon("icon/password.png"), "Login - User|Pass|F2a", self)
        # subMenu.addAction(computer_login_userpass_action)
        # computer_login_userpass_action.triggered.connect(self.computer_login_userpass)
        # # login cookie - chrome profile
        # computer_login_cookie_action = QAction(QIcon("icon/cookie.png"), "Login - Cookies", self)
        # subMenu.addAction(computer_login_cookie_action)
        # computer_login_cookie_action.triggered.connect(self.computer_login_cookie)
        # profile
        # subMenu.addSeparator()

        # subMenu.addSeparator()
        # computer_profile_action = QAction(QIcon("icon/profile.png"), "COOKIES - Login", self)
        # subMenu.addAction(computer_profile_action)
        # computer_profile_action.triggered.connect(self.computer_profile)
        # computer_profile_update_cookies_action = QAction(QIcon("icon/profile.png"), "COOKIES - Get", self)
        # subMenu.addAction(computer_profile_update_cookies_action)
        # computer_profile_update_cookies_action.triggered.connect(self.computer_profile_update_cookies)

        # # rename folder chrome
        # subMenu_mobile.addSeparator()
        # mobile_rename_profile_action = QAction(QIcon("icon/folder.png"), "Rename - Profile", self)
        # subMenu_mobile.addAction(mobile_rename_profile_action)
        # mobile_rename_profile_action.triggered.connect(self.mobile_rename_profile)
        # # subMenu_mobile.addSeparator()
        # mobile_first_login_action = QAction(QIcon("icon/change.png"), "Mobile - First Login", self)
        # subMenu_mobile.addAction(mobile_first_login_action)
        # mobile_first_login_action.triggered.connect(self.mobile_first_login)
        # # subMenu_mobile.addSeparator()
        # mobile_change_info_action = QAction(QIcon("icon/change.png"), "Mobile - Change info", self)
        # subMenu_mobile.addAction(mobile_change_info_action)
        # mobile_change_info_action.triggered.connect(self.mobile_change_info)

        # # Add row
        # menu.addSeparator()
        # add_action = QAction(QIcon("icon/add.png"), "Add", self)
        # menu.addAction(add_action)
        # add_action.triggered.connect(self.add_data)

        # ################ Mobile - Browser ################
        # # menu.addSeparator()
        # subMenu_mobile = menu.addMenu(QIcon("icon/phone.png"), 'Mobile - Browser')
        # #
        # mobile_test_action = QAction(QIcon("icon/password.png"), "Test", self)
        # subMenu_mobile.addAction(mobile_test_action)
        # mobile_test_action.triggered.connect(self.mobile_test)
        # # # submenu Mobile - Backup
        # # subMenu_mobile.addSeparator()
        # # subMenu_backup_mobile = subMenu_mobile.addMenu(QIcon("icon/backup.png"), 'Backup')
        # # # submenu Mobile - Login
        # # subMenu_mobile.addSeparator()
        # # subMenu_login_mobile = subMenu_mobile.addMenu(QIcon("icon/password.png"), 'Login')
        # #
        # subMenu_mobile.addSeparator()
        # mobile_login_userpass_action = QAction(QIcon("icon/password.png"), "Login - User|Pass|F2a", self)
        # subMenu_mobile.addAction(mobile_login_userpass_action)
        # mobile_login_userpass_action.triggered.connect(self.mobile_login_userpass)
        # #
        # mobile_login_cookie_action = QAction(QIcon("icon/cookie.png"), "Login - User|Cookie", self)
        # subMenu_mobile.addAction(mobile_login_cookie_action)
        # mobile_login_cookie_action.triggered.connect(self.mobile_login_cookie)
        #
        # # submenu Mobile - Profile
        # # subMenu_profile_mobile = subMenu_mobile.addMenu(QIcon("icon/profile.png"), 'Profiles')
        # subMenu_mobile.addSeparator()
        # mobile_mobile_profile_action = QAction(QIcon("icon/profile.png"), "Profile", self)
        # subMenu_mobile.addAction(mobile_mobile_profile_action)
        # mobile_mobile_profile_action.triggered.connect(self.mobile_profile)
        # #
        # mobile_open_profile_action = QAction(QIcon("icon/folder.png"), "Profile - Open", self)
        # subMenu_mobile.addAction(mobile_open_profile_action)
        # mobile_open_profile_action.triggered.connect(self.mobile_open_profile)
        # #
        # mobile_delete_profile_action = QAction(QIcon("icon/trash.png"), "Profile - Delete", self)
        # subMenu_mobile.addAction(mobile_delete_profile_action)
        # mobile_delete_profile_action.triggered.connect(self.mobile_delete_profile)
        # #
        # menu.addSeparator()
        # mobile_getinfo_action = QAction(QIcon("icon/info.png"), "Get info", self)
        # subMenu_mobile.addAction(mobile_getinfo_action)
        # mobile_getinfo_action.triggered.connect(self.mobile_getinfo)

        ################## Other ##################

        # # Check Ip
        menu.addSeparator()
        checkip_action = QAction(QIcon("icon/ip.png"), "Check IP", self)
        menu.addAction(checkip_action)
        checkip_action.triggered.connect(self.checkip)
        # # # Reload
        # menu.addSeparator()
        # refesh_action = QAction(QIcon("icon/reload.png"), "Reload", self)
        # menu.addAction(refesh_action)
        # refesh_action.triggered.connect(self.load_data)
        # load text
        menu.addSeparator()
        add_data_action = QAction(QIcon("icon/add_data.png"), "Add", self)
        menu.addAction(add_data_action)
        add_data_action.triggered.connect(self.add_data)

        # # Killer ChromeDriver
        # menu.addSeparator()
        # killer_service_action = QAction(QIcon("icon/killer_chrome.png"), "STOP SERVICES", self)
        # menu.addAction(killer_service_action)
        # killer_service_action.triggered.connect(self.killer_services)

        # Delete row
        # menu.addSeparator()
        delete_action = QAction(QIcon("icon/trash.png"), "Delete Row", self)
        menu.addAction(delete_action)
        delete_action.triggered.connect(self.delete_row)

        # Copy UID
        menu.addSeparator()
        copy_uid_action = QAction(QIcon("icon/copy.png"), "Copy UID", self)
        menu.addAction(copy_uid_action)
        copy_uid_action.triggered.connect(self.copy_uid)

        # Copy UID
        menu.addSeparator()
        check_uid_action = QAction(QIcon("icon/checked.png"), "Check UID", self)
        menu.addAction(check_uid_action)
        check_uid_action.triggered.connect(self.checkuid)

        # menu.addSeparator()
        # groups_action = QAction(QIcon("icon/edit.png"), "GROUP", self)
        # menu.addAction(groups_action)
        # groups_action.triggered.connect(self.groups)

        # # Rename All
        # menu.addSeparator()
        # rename_all_action = QAction(QIcon("icon/killer_chrome.png"), "Rename All", self)
        # menu.addAction(rename_all_action)
        # rename_all_action.triggered.connect(self.search_rename_folder_all)

        # # load text
        # menu.addSeparator()
        # find_profile_action = QAction(QIcon("icon/reload.png"), "Find", self)
        # menu.addAction(find_profile_action)
        # find_profile_action.triggered.connect(self.find_profile)

        action = menu.exec_(self.tableView_Facebook.mapToGlobal(pos))

    #
    # def mousePressEvent(self, event):
    #     if event.type() == QEvent.MouseButtonPress:
    #         if event.button() == Qt.LeftButton:
    #             row = self.tableWidget.tableWidget.currentIndex()
    #             print(row.row())
    #             column_total = self.tableWidget.columnCount()
    #             for c in range(0, column_total):
    #                 self.tableWidget.item(row.row(), c).setBackground(QColor(236, 239, 164))

    def closeEvent(self, event):
        event.accept()
        # reset timezone
        self.spoof_timezone()
        # Kill
        services = ["chromedriver.exe", "adb.exe", "nox_adb.exe", "naive.exe", "gost3.exe"]
        self.killer_services(services)

    def global_Proxies(self, method=None):
        if method == 'read':
            proxies = []
            with open(PROXIES, 'r') as f:
                proxies = f.readlines()
            proxies = map(lambda s: s.strip(), proxies)
            self.plainTextEdit_tethering_proxy.setPlainText('\n'.join(proxies))
        else:
            proxies = self.plainTextEdit_tethering_proxy.toPlainText().split('\n')
            proxies = map(lambda s: s.strip(), proxies)
            with open(PROXIES, 'w') as f:
                f.write("\n".join(proxies))
            # print("Text changed...>>> " + self.plainTextEdit_tethering_proxy.toPlainText())

    def ip_geo(self, proxy_private):
        timezone_sys = TimezoneSys(proxy_private)
        _timezone = timezone_sys.proxy_data()
        ip = _timezone['ip']
        timezone = _timezone['timezone']
        utc = _timezone['utc']
        _latitude = _timezone['g_latitude']
        _longitude = _timezone['g_longitude']

        if _latitude is None:
            return
        geo = Geo()
        latitude, longitude = geo.kilometers(_latitude, _longitude, 30, random.uniform(0.5, 5.0))
        return latitude, longitude

    def ip_geo_thread(self, proxy_private):
        with ThreadPoolExecutor() as executor:
            future = executor.submit(self.ip_geo, proxy_private)
            return_value = future.result()
            return return_value

    # Tab Tools
    def tab_tools_spotify(self):
        s = requests.Session()
        url = f'https://open.spotify.com/search/{self.lineEdit_spotify_kw.text()}/artists'
        headers = {
            '': ''
        }
        r = s.get(url, timeout=30, verify=False, headers=headers)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(r.text, 'html.parser')
        print(soup)
        artists = soup.find_all("a", href=re.compile("artist"))
        print(artists)

    def tab_tools_regex(self):
        filter = [('&amp;', '&')]
        from lxml import etree, html
        document_root = html.fromstring(self.textEdit_input.toPlainText())
        _input = etree.tostring(document_root, encoding='unicode', pretty_print=True)
        # print(_input)
        _regex = self.lineEdit_regex.text()
        artist = re.findall(_regex, _input)
        artists = []
        for a in artist:
            for f in filter:
                if f[0] in a[1]:
                    _a = str(a[1]).replace(f[0], f[1])
                else:
                    _a = a[1]
            artists.append(_a)
        self.textEdit_input.clear()
        self.textEdit_input.setText('\n'.join(artists))

    def spoof_timezone(self):
        timezone_sys = TimezoneSys()
        timezone_sys.reset_timezone()

    def spoof_mac(self):
        os.system(f'python ./library/_spoof/spoof_mac.py list')
        os.system(f'python ./library/_spoof/spoof_mac.py randomize wi-fi')

    def form_facebook_edit(self):
        index = self.tableView_Facebook.selectionModel().selectedRows()
        uid = self.tableView_Facebook.model().index(index[0].row(), 0).data()
        global _flag_thread
        global _thread_edit
        if _flag_thread or _thread_edit:
            QMessageBox.about(self, "WARNING", f'Other Thread Running !')
            return
        self.FacebookForm = FacebookForm(uid)
        self.FacebookForm.show()

    def change_color_row(self, item, _status, _group):
        with open('./data/_status.txt', 'r', encoding='utf8') as f:
            uid_status = f.readlines()
        for status in uid_status:
            status_name = status.split('|')[0]
            status_color = status.split('|')[1]
            try:
                if _status == status_name:
                    a = int(status_color.split(',')[0])
                    b = int(status_color.split(',')[1])
                    c = int(status_color.split(',')[2])
                    item.setBackground(QColor(a, b, c))
            except:
                pass
        # try:
        #     if _status == 'Live' and _group == 'VIP-C':
        #         item.setBackground(QColor(50, 205, 50))
        #     if _status == 'Live' and _group == 'VIP-NC':
        #         item.setBackground(QColor(127, 255, 0))
        #     if _status == 'Live' and _group == 'Random-C':
        #         item.setBackground(QColor(198, 255, 26))
        #     if _status == 'Live' and _group == 'Random-NC':
        #         item.setBackground(QColor(230, 255, 153))
        #     if _status == 'Die':
        #         item.setBackground(QColor(255, 69, 0))
        #     if _group == 'Spam':
        #         item.setBackground(QColor(255, 69, 0))
        #     if _status == 'CheckPoint':
        #         item.setBackground(QColor(192, 192, 192))
        #     if 'Full-' in _group:
        #         item.setBackground(QColor(198, 255, 26))
        #     if _type == 'Clone':
        #         item.setBackground(QColor(94, 134, 255))
        # except:
        #     pass

    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    @pyqtSlot()
    def search(self):
        if self.lineEdit_search.text() == str.isspace:
            return
        # Find
        infos = None
        _search = str(self.lineEdit_search.text())
        if self.comboBox_search.currentText() == 'UID':
            infos = MYDATA.search_uid(_search)
        if self.comboBox_search.currentText() == 'TKQC':
            infos = MYDATA.search_uid_ads(_search)
        if self.comboBox_search.currentText() == 'BM':
            infos = MYDATA.search_uid_ads(_search)
        if self.comboBox_search.currentText() == 'PAGE':
            infos = MYDATA.search_uid_pages(_search)
        if self.comboBox_search.currentText() == 'Email':
            infos = MYDATA.search_uid_email(_search)
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()

    def ip_infos(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        for row in rows:
            try:
                _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
                info = MYDATA.select_data(_uid)
                score = Score(_uid, info.proxy_private)
                ip_infos = score.proxy_data(logs=True)
            except:
                pass

    @pyqtSlot()
    def checkip(self):
        t2 = threading.Thread(target=self.ip_infos)
        t2.start()
        # with ThreadPoolExecutor(max_workers=1) as executor:
        #     executor.submit(self.ip_infos,)


    def _sort_ads_bm(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('ads_bm')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()


    def _sort_ads_cards(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('ads_cards')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        t.start()

    def _sort_groups(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('ads_groups')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()

    def _sort_begin(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('action_begin_days')
        # sort: https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
        _infos = sorted(infos, key=lambda k: k['action_begin_days'])
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()

    def _sort_last(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('action_last_days')
        # sort: https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
        _infos = sorted(infos, key=lambda k: k['action_last_days'])
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()


    def _sort_country(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('info_country')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()


    def _sort_camps_plans(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('camps_plans')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()


    def _sort_camps_pixels(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('camps_pixels')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()


    def _sort_camps_groups(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('camps_groups')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        # t.setDaemon(True)
        t.start()


    def _sort_ads_tuts(self):
        global _flag_thread
        if _flag_thread:
            return
        infos = MYDATA.query_all_accounts('ads_tuts')
        t = threading.Thread(target=self.sortData_Facebook, args=(infos,))
        t.start()

    def headerColumns_facebook(self, nameColumn):
        for index in range(self.tableWidget.columnCount()):
            headItemText = self.tableWidget.horizontalHeaderItem(index).text()
            if headItemText == nameColumn:
                return int(index)

    def headerColumns_facebook_worker(self, index):
        headItemText = self.tableWidget.horizontalHeaderItem(index).text()
        return headItemText, index

    def headerColumns_facebook_pool(self, nameColumn):
        with ThreadPoolExecutor(max_workers=20) as e:
            fut = [e.submit(self.headerColumns_facebook_worker, i) for i in range(self.tableWidget.columnCount())]
            for r in as_completed(fut):
                column_name, index = r.result()
                if column_name == nameColumn:
                    return int(index)

        # with ThreadPoolExecutor(max_workers=5) as executor:
        #     future = executor.submit(self.headerColumns_facebook, nameColumn)
        #     return future.result()

    # def resizeColumns_facebook(self, nameColumn, newSize):
    #     _column = 0
    #     for index in range(self.tableWidget.columnCount()):
    #         headItemText = self.tableWidget.horizontalHeaderItem(index).text()
    #         if headItemText == nameColumn:
    #             _column = int(index)
    #     self.tableWidget.setColumnWidth(_column, newSize)

    #
    #
    # def sort_data(self, infos):
    #     global _flag_thread
    #     _flag_thread = True
    #     self.tableWidget.setDisabled(True)
    #     # self.tableWidget.reset()
    #     self.tableWidget.setSortingEnabled(False)
    #     self.tableWidget.setRowCount(0)
    #
    #     self.fb_live = 0
    #     self.fb_die = 0
    #     self.fb_checkpoint = 0
    #     column_total = self.tableWidget.columnCount()
    #
    #     for row, info in enumerate(infos):
    #         self.statusBar_main.showMessage(f'Loading.....{int(row)}/{len(infos)}')
    #
    #         self.tableWidget.insertRow(row)
    #         # uid
    #         c_uid = self.headerColumns_facebook_pool('uid')
    #         self.tableWidget.setItem(int(row), c_uid, self.createItem(str(info['uid']),
    #                                                                   Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # status
    #         c_status = self.headerColumns_facebook_pool('status')
    #         self.tableWidget.setItem(int(row), c_status, self.createItem(str(info['status']),
    #                                                                      Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # camps_plans
    #         self.tableWidget.setItem(int(row), self.headerColumns_facebook_pool('camps_plans'),
    #                                  self.createItem(str(info['camps_plans']),
    #                                                  Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # camps_groups
    #         self.tableWidget.setItem(int(row), self.headerColumns_facebook_pool('camps_groups'),
    #                                  self.createItem(str(info['camps_groups']),
    #                                                  Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # camps_pixels
    #         self.tableWidget.setItem(int(row), self.headerColumns_facebook_pool('camps_pixels'),
    #                                  self.createItem(str(info['camps_pixels']),
    #                                                  Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # ads_tuts
    #         c_ads_tuts = self.headerColumns_facebook_pool('ads_tuts')
    #         self.tableWidget.setItem(int(row), c_ads_tuts, self.createItem(str(info['ads_tuts']),
    #                                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # ads_groups
    #         c_ads_groups = self.headerColumns_facebook_pool('ads_groups')
    #         self.tableWidget.setItem(int(row), c_ads_groups, self.createItem(str(info['ads_groups']),
    #                                                                          Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # Change - Pass,Mail : Yes/No
    #         c_pm = self.headerColumns_facebook_pool('p/m')
    #         if 'None' in str(info['info_change_pass']):
    #             change_pass = 'n'
    #         else:
    #             change_pass = str(info['info_change_pass'])
    #         if 'None' in str(info['info_change_mail']):
    #             change_mail = 'n'
    #         else:
    #             change_mail = str(info['info_change_mail'])
    #         self.tableWidget.setItem(int(row), c_pm, self.createItem(f'{change_pass}/{change_mail}',
    #                                                                  Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # #
    #         # self.tableWidget.setItem(int(row), 4, self.createItem(str(info['last_profile_mobile']),
    #         #                                                       Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # last action computer
    #         c_computer = self.headerColumns_facebook_pool('c')
    #         try:
    #             last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(info['last_profile_computer']))
    #             born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
    #                             int(last_reaction[0][1]))  # provide UTC time
    #             age = datetime.utcnow() - born
    #             self.tableWidget.setItem(int(row), c_computer, self.createItem(f'{age.days}',
    #                                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         except:
    #             self.tableWidget.setItem(int(row), c_computer, self.createItem('',
    #                                                                            Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # # last action mobile
    #         # c_phone = self.headerColumns_facebook_pool('p')
    #         # try:
    #         #     fakephone = MYDATA.select_fakephone(str(info['fakephone_id']))
    #         #     last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(fakephone.last_backup))
    #         #     born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
    #         #                     int(last_reaction[0][1]))  # provide UTC time
    #         #     age = datetime.utcnow() - born
    #         #     self.tableWidget.setItem(int(row), c_phone, self.createItem(f'{age.days}',
    #         #                                                                 Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # except:
    #         #     self.tableWidget.setItem(int(row), c_phone, self.createItem('',
    #         #                                                                 Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # info_name
    #         c_name = self.headerColumns_facebook_pool('name')
    #         self.tableWidget.setItem(int(row), c_name, self.createItem(str(info['info_name']),
    #                                                                    Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # self.resizeColumns_facebook(self.headerColumns_facebook_pool('name'),100)
    #
    #         # info_birthday()
    #         c_birthday = self.headerColumns_facebook_pool('birthday')
    #         self.tableWidget.setItem(int(row), c_birthday, self.createItem(str(info['info_birthday']),
    #                                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # info_friend
    #         c_friends = self.headerColumns_facebook_pool('friends')
    #         self.tableWidget.setItem(int(row), c_friends, self.createItem(str(info['info_friend']),
    #                                                                       Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # info_register_date
    #         c_registed = self.headerColumns_facebook_pool('registed')
    #         self.tableWidget.setItem(int(row), c_registed, self.createItem(str(info['info_register_date']),
    #                                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # self.tableWidget.setItem(int(row), 10, self.createItem(str(info['ip_last_location']),
    #         #                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # info_country
    #         c_country = self.headerColumns_facebook_pool('country')
    #         self.tableWidget.setItem(int(row), c_country, self.createItem(str(info['info_country']),
    #                                                                       Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # info_2fa
    #         info_2fa = str(info['info_f2a'])
    #         c_2fa = self.headerColumns_facebook_pool('2fa')
    #         if (info_2fa == '') or (info_2fa is None):
    #             self.tableWidget.setItem(int(row), c_2fa, self.createItem('n',
    #                                                                       Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         else:
    #             self.tableWidget.setItem(int(row), c_2fa, self.createItem('Y',
    #                                                                       Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # action_begin
    #         c_begin = self.headerColumns_facebook_pool('begin')
    #         try:
    #             last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(info['action_begin']))
    #             born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
    #                             int(last_reaction[0][1]))  # provide UTC time
    #             age = datetime.utcnow() - born
    #             self.tableWidget.setItem(int(row), c_begin, self.createItem(f'{age.days}',
    #                                                                         Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         except:
    #             self.tableWidget.setItem(int(row), c_begin, self.createItem('NA',
    #                                                                         Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # last_reaction
    #         time_current = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
    #         c_last = self.headerColumns_facebook_pool('l')
    #         try:
    #             last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(info['action_last']))
    #             born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
    #                             int(last_reaction[0][1]))  # provide UTC time
    #             age = datetime.utcnow() - born
    #             self.tableWidget.setItem(int(row), c_last, self.createItem(f'{age.days}d',
    #                                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         except:
    #             self.tableWidget.setItem(int(row), c_last, self.createItem('NA',
    #                                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # pages
    #         info_pages = MYDATA.search_pages(info['uid'])
    #         niche_page = []
    #         c_pages = self.headerColumns_facebook_pool('pages')
    #         for i in info_pages:
    #             page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_page']))
    #             page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
    #                                   int(page_date_create[0][1]))  # provide UTC time
    #             page_day = datetime.utcnow() - page_begin
    #             # niche_page.append(
    #             #     f"{i['name_page']}({i['categories_page']})({page_day.days}d)({i['liked_page']}L)({i['note_page']})")
    #             niche_page.append(
    #                 f"{page_day.days}d")
    #         self.tableWidget.setItem(int(row), c_pages,
    #                                  self.createItem(f'[{len(info_pages)}] ' + str(','.join(niche_page)),
    #                                                  Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # Ads - TK
    #         ads_infos = MYDATA.search_ads(info['uid'])
    #         type_ads = []
    #         c_ads_tk = self.headerColumns_facebook_pool('ads-tk')
    #         for i in ads_infos:
    #             try:
    #                 ads_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_bm']))
    #                 ads_begin = datetime(int(ads_date_create[0][2]), int(ads_date_create[0][0]),
    #                                      int(ads_date_create[0][1]))  # provide UTC time
    #                 ads_day = datetime.utcnow() - ads_begin
    #                 ads_age = ads_day.days
    #             except:
    #                 ads_age = 'NA'
    #             if 'TK' in i['type_bm']:
    #                 type_ads.append(
    #                     f"{i['status_bm']}/{ads_age}d")
    #                 break
    #         self.tableWidget.setItem(int(row), c_ads_tk, self.createItem(str(', '.join(type_ads)),
    #                                                                      Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         # Ads - CN
    #         ads_cn = []
    #         c_ads_cn = self.headerColumns_facebook_pool('ads-cn')
    #         for i in ads_infos:
    #             try:
    #                 ads_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_bm']))
    #                 ads_begin = datetime(int(ads_date_create[0][2]), int(ads_date_create[0][0]),
    #                                      int(ads_date_create[0][1]))  # provide UTC time
    #                 ads_day = datetime.utcnow() - ads_begin
    #                 ads_age = ads_day.days
    #             except:
    #                 ads_age = 'NA'
    #             if 'CN' in i['type_bm']:
    #                 ads_cn.append(
    #                     f"{i['status_bm']}-{i['type_bm']}/{i['limit_bm']}/{i['spend_bm']}/{ads_age}d")
    #         self.tableWidget.setItem(int(row), c_ads_cn, self.createItem(f'[{len(ads_cn)}] ' + str(', '.join(ads_cn)),
    #                                                                      Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # Ads - BM
    #         ads_bm = []
    #         c_ads_bm = self.headerColumns_facebook_pool('ads-bm')
    #         for i in ads_infos:
    #             try:
    #                 ads_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_bm']))
    #                 ads_begin = datetime(int(ads_date_create[0][2]), int(ads_date_create[0][0]),
    #                                      int(ads_date_create[0][1]))  # provide UTC time
    #                 ads_day = datetime.utcnow() - ads_begin
    #                 ads_age = ads_day.days
    #             except:
    #                 ads_age = 'NA'
    #             if 'BM' in i['type_bm']:
    #                 ads_bm.append(
    #                     f"{i['status_bm']}-{i['type_bm']}/{i['limit_bm']}/{i['spend_bm']}/{ads_age}d")
    #             # type_ads.append(
    #             #     f"({i['type_bm']}-{i['limit_bm']}[{i['status_bm']}]/{i['spend_bm']}/{ads_day.days}d/{i['status_bm']})")
    #         self.tableWidget.setItem(int(row), c_ads_bm, self.createItem(f'[{len(ads_bm)}] ' + str(', '.join(ads_bm)),
    #                                                                      Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #         self.tableWidget.resizeColumnToContents(c_ads_bm)
    #
    #         # card
    #         info_card = MYDATA.search_ads(info['uid'])
    #         type_ads = []
    #         c_ads_card = self.headerColumns_facebook_pool('ads-card')
    #         for i in info_card:
    #             type_ads.append(i['card_bm'])
    #
    #         self.tableWidget.setItem(int(row), c_ads_card, self.createItem(str(','.join(type_ads)),
    #                                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # camps
    #         info_camps = MYDATA.search_camps(info['uid'])
    #         type_camps = []
    #         c_ads_camps = self.headerColumns_facebook_pool('ads-camps')
    #         for i in info_camps:
    #             try:
    #                 last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_camps']))
    #                 born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
    #                                 int(last_reaction[0][1]))  # provide UTC time
    #                 age = datetime.utcnow() - born
    #                 type_camps.append(f"{i['name_camps']}({i['status_camps']})({age.days}d)")
    #             except:
    #                 type_camps.append(f"{i['name_camps']}({i['status_camps']})(NA)")
    #         self.tableWidget.setItem(int(row), c_ads_camps, self.createItem(str(','.join(type_camps)),
    #                                                                         Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # # _proxy
    #         # self.tableWidget.setItem(int(row), 18, self.createItem(str(info['proxy_private']),
    #         #                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # Hitories
    #         search_logs = MYDATA.search_logs(info['uid'])
    #         type_logs = []
    #         c_logs = self.headerColumns_facebook_pool('logs')
    #         for i in search_logs:
    #             try:
    #                 last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date']))
    #                 born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
    #                                 int(last_reaction[0][1]))  # provide UTC time
    #                 age = datetime.utcnow() - born
    #                 type_logs.append(i['logs'] + f'({age.days}d)')
    #             except:
    #                 type_logs.append(i["logs"] + '(NA)')
    #         self.tableWidget.setItem(int(row), c_logs, self.createItem(str(','.join(type_logs)),
    #                                                                    Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
    #
    #         # Total
    #         if info['status'] == 'Live':
    #             self.fb_live += 1
    #         if info['status'] == 'Die':
    #             self.fb_die += 1
    #         if info['status'] == 'CheckPoint':
    #             self.fb_checkpoint += 1
    #
    #         # # Color
    #         # for column in range(int(column_total)):
    #         #     t = threading.Thread(target=self.change_color_row, args=(
    #         #         self.tableWidget.item(row, column), str(info['status']), str(info['ads_groups'])))
    #         #     t.start()
    #         #     self.change_color_row(self.tableWidget.item(row, column), str(info['status']), str(info['ads_groups']))
    #
    #     #
    #     # column_total = self.tableWidget.columnCount()
    #     # row_total = self.tableWidget.rowCount()
    #     # for column in range(int(column_total)):
    #     #     for row in range(int(row_total)):
    #     #         try:
    #     #             _status = self.tableWidget.item(row, 1).text()
    #     #             _type = self.tableWidget.item(row, 2).text()
    #     #             _group = self.tableWidget.item(row, 3).text()
    #     #             item = self.tableWidget.item(row, column)
    #     #             self.change_color_row(item, _status, _type, _group)
    #     #         except:
    #     #             pass
    #     #
    #
    #     self.tableWidget.resizeColumnToContents(c_uid)
    #     self.tableWidget.resizeColumnToContents(c_status)
    #     self.tableWidget.resizeColumnToContents(c_ads_tuts)
    #     self.tableWidget.resizeColumnToContents(c_ads_groups)
    #     self.tableWidget.resizeColumnToContents(c_computer)
    #     self.tableWidget.resizeColumnToContents(c_phone)
    #     self.tableWidget.resizeColumnToContents(c_last)
    #     self.tableWidget.resizeColumnToContents(c_pm)
    #     self.tableWidget.resizeColumnToContents(c_begin)
    #     self.tableWidget.resizeColumnToContents(c_birthday)
    #     self.tableWidget.resizeColumnToContents(c_friends)
    #     self.tableWidget.resizeColumnToContents(c_registed)
    #     self.tableWidget.resizeColumnToContents(c_country)
    #     self.tableWidget.resizeColumnToContents(c_2fa)
    #     self.tableWidget.resizeColumnToContents(c_ads_card)
    #
    #     # Sort table
    #     # self.resizeColumns_facebook('name', 50)
    #     # self.tableWidget.setSortingEnabled(True)
    #     # self.tableWidget.columnResized(5, 0, 5)
    #
    #     # Set color : https://www.w3schools.com/colors/colors_picker.asp
    #     # self.tableWidget.setSortingEnabled(True)
    #     # self.tableWidget.sortItems(11, Qt.DescendingOrder)
    #
    #     # scroll last section
    #     # self.tableWidget.scrollToItem('100053490493824')
    #
    #     self.statusBar_main.showMessage(
    #         f'COMPLETE - LIVE: {str(self.fb_live)} DISABLE: {str(self.fb_die)} CHECKPOINT: {str(self.fb_checkpoint)}')
    #     #
    #     _flag_thread = False
    #     self.tableWidget.setDisabled(False)

    def getHeaderColumnsIndex(self, _model, name):
        for index in range(_model.columnCount()):
            headItemText = _model.horizontalHeaderItem(index).text()
            if headItemText == name:
                return int(index)

    def sortData_Facebook(self, infos):
        global _flag_thread
        _flag_thread = True

        self.fb_live = 0
        self.fb_die = 0
        self.fb_checkpoint = 0

        self.tableView_Facebook.setDisabled(True)
        self.tableView_Facebook.reset()

        model = QtGui.QStandardItemModel(5, 3)
        model.setHorizontalHeaderLabels([
            'uid', 'via_groups', 'status', 'camps_PLANS', 'camps_GROUPS', 'camps_ADS', 'TUTS', 'p/m',  'c', 'p', 'l', 'age',
            'name', 'birthday', 'friends', 'registed', 'country', '2fa',
            'pages', 'ads-tk', 'ads-cn', 'ads-bm', 'ads-card', 'ads-camps', 'logs'
        ])
        self.tableView_Facebook.setModel(model)
        for row, info in enumerate(infos):
            self.statusBar_main.showMessage(f'Loading.....{int(row)}/{len(infos)}')
            # uid
            _uid = QtGui.QStandardItem(str(info['uid']))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'uid'), _uid)

            # status
            _status = QtGui.QStandardItem(info['status'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'status'), _status)
            _statusIndex = model.index(row, self.getHeaderColumnsIndex(model, 'status'))
            # if 'Live' in info['status']:
            #     model.setData(_statusIndex, QColor(101, 183, 65), Qt.BackgroundRole)
            if 'Die' in info['status']:
                model.setData(_statusIndex, QColor(255, 47, 47), Qt.BackgroundRole)

            # camps_PLANS
            _camps_plans = QtGui.QStandardItem(info['camps_plans'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'camps_PLANS'), _camps_plans)
            _camps_plansIndex = model.index(row, self.getHeaderColumnsIndex(model, 'camps_PLANS'))
            s_camps_plans = str(info['camps_plans']).lower()
            if 'ads' in s_camps_plans:
                model.setData(_camps_plansIndex, QColor(101, 183, 65), Qt.BackgroundRole)
            if 'pages' in s_camps_plans:
                model.setData(_camps_plansIndex, QColor(255, 218, 120), Qt.BackgroundRole)
            if 'pixels' in s_camps_plans:
                model.setData(_camps_plansIndex, QColor(161, 221, 112), Qt.BackgroundRole)


            # camps_GROUPS
            _camps_groups = QtGui.QStandardItem(info['camps_groups'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'camps_GROUPS'), _camps_groups)

            # camps_ADS
            _camps_pixels = QtGui.QStandardItem(info['camps_pixels'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'camps_ADS'), _camps_pixels)

            # TUTS
            _ads_tuts = QtGui.QStandardItem(info['ads_tuts'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'TUTS'), _ads_tuts)

            # via_groups
            _ads_groups = QtGui.QStandardItem(info['ads_groups'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'via_groups'), _ads_groups)

            # Change - Pass,Mail : Yes/No
            if 'None' in str(info['info_change_pass']):
                change_pass = 'n'
            else:
                change_pass = str(info['info_change_pass'])
            if 'None' in str(info['info_change_mail']):
                change_mail = 'n'
            else:
                change_mail = str(info['info_change_mail'])
            _pm = QtGui.QStandardItem(f'{change_pass}/{change_mail}')
            model.setItem(row, self.getHeaderColumnsIndex(model, 'p/m'), _pm)

            # last action computer
            l_computer = ''
            try:
                last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(info['last_profile_computer']))
                born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
                                int(last_reaction[0][1]))  # provide UTC time
                age = datetime.utcnow() - born
                l_computer = f'{age.days}'
            except:
                l_computer=''
            _l_computer = QtGui.QStandardItem(l_computer)
            model.setItem(row, self.getHeaderColumnsIndex(model, 'c'), _l_computer)

            # last action mobile
            l_phone = ''
            try:
                fakephone = MYDATA.select_fakephone(str(info['fakephone_id']))
                last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(fakephone.last_backup))
                born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
                                int(last_reaction[0][1]))  # provide UTC time
                age = datetime.utcnow() - born
                l_phone = f'{age.days}'
            except:
                l_phone = ''
            _l_phone = QtGui.QStandardItem(l_phone)
            model.setItem(row, self.getHeaderColumnsIndex(model, 'p'), _l_phone)

            # info_name
            _name = QtGui.QStandardItem(info['info_name'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'name'), _name)

            # info_birthday
            _birthday = QtGui.QStandardItem(info['info_birthday'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'birthday'), _birthday)

            # info_friend
            _friends = QtGui.QStandardItem(info['info_friend'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'friends'), _friends)

            # info_register_date
            _info_register_date = QtGui.QStandardItem(info['info_register_date'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'registed'), _info_register_date)

            # info_country
            _country = QtGui.QStandardItem(info['info_country'])
            model.setItem(row, self.getHeaderColumnsIndex(model, 'country'), _country)

            # info_2fa
            _2fa = ''
            info_2fa = str(info['info_f2a'])
            if (info_2fa == '') or (info_2fa is None):
                _2fa = ''
            else:
                _2fa = 'Y'
            _f_2fa = QtGui.QStandardItem(_2fa)
            model.setItem(row, self.getHeaderColumnsIndex(model, '2fa'), _f_2fa)

            # action_begin
            c_begin = ''
            try:
                last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(info['action_begin']))
                born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
                                int(last_reaction[0][1]))  # provide UTC time
                age = datetime.utcnow() - born
                c_begin = f'{age.days}'
            except:
                c_begin = ''
            _action_begin = QtGui.QStandardItem(c_begin)
            model.setItem(row, self.getHeaderColumnsIndex(model, 'age'), _action_begin)

            # last_reaction
            c_last = ''
            try:
                last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(info['action_last']))
                born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
                                int(last_reaction[0][1]))  # provide UTC time
                age = datetime.utcnow() - born
                c_last = f'{age.days}'
            except:
                c_last = ''
            _action_begin = QtGui.QStandardItem(c_last)
            model.setItem(row, self.getHeaderColumnsIndex(model, 'l'), _action_begin)

            # Pages
            info_pages = MYDATA.search_pages(info['uid'])
            niche_page = []
            for i in info_pages:
                page_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_page']))
                page_begin = datetime(int(page_date_create[0][2]), int(page_date_create[0][0]),
                                      int(page_date_create[0][1]))  # provide UTC time
                page_day = datetime.utcnow() - page_begin
                niche_page.append(
                    f"{page_day.days}d")
            _pages = QtGui.QStandardItem(f'[{len(info_pages)}] ' + str(','.join(niche_page)))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'pages'), _pages)

            # Ads - TK
            ads_infos = MYDATA.search_ads(info['uid'])
            type_ads = []
            for i in ads_infos:
                try:
                    ads_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_bm']))
                    ads_begin = datetime(int(ads_date_create[0][2]), int(ads_date_create[0][0]),
                                         int(ads_date_create[0][1]))  # provide UTC time
                    ads_day = datetime.utcnow() - ads_begin
                    ads_age = ads_day.days
                except:
                    ads_age = 'NA'
                if 'TK' in i['type_bm']:
                    type_ads.append(
                        f"{i['status_bm']}/{ads_age}d")
                    break
            _ads_tk = QtGui.QStandardItem(str(', '.join(type_ads)))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'ads-tk'), _ads_tk)

            # Ads - CN
            ads_cn = []
            for i in ads_infos:
                try:
                    ads_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_bm']))
                    ads_begin = datetime(int(ads_date_create[0][2]), int(ads_date_create[0][0]),
                                         int(ads_date_create[0][1]))  # provide UTC time
                    ads_day = datetime.utcnow() - ads_begin
                    ads_age = ads_day.days
                except:
                    ads_age = 'NA'
                if 'CN' in i['type_bm']:
                    ads_cn.append(
                        f"{i['status_bm']}-{i['type_bm']}/{i['limit_bm']}/{i['spend_bm']}/{ads_age}d")
            _ads_cn = QtGui.QStandardItem(f'[{len(ads_cn)}] ' + str(', '.join(ads_cn)))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'ads-cn'), _ads_cn)

            # Ads - BM
            ads_bm = []
            for i in ads_infos:
                try:
                    ads_date_create = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_bm']))
                    ads_begin = datetime(int(ads_date_create[0][2]), int(ads_date_create[0][0]),
                                         int(ads_date_create[0][1]))  # provide UTC time
                    ads_day = datetime.utcnow() - ads_begin
                    ads_age = ads_day.days
                except:
                    ads_age = 'NA'
                if 'BM' in i['type_bm']:
                    ads_bm.append(
                        f"{i['status_bm']}-{i['type_bm']}/{i['limit_bm']}/{i['spend_bm']}/{ads_age}d")
                # type_ads.append(
                #     f"({i['type_bm']}-{i['limit_bm']}[{i['status_bm']}]/{i['spend_bm']}/{ads_day.days}d/{i['status_bm']})")

            _ads_bm = QtGui.QStandardItem(f'[{len(ads_bm)}] ' + str(', '.join(ads_bm)))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'ads-bm'), _ads_bm)

            # card
            info_card = MYDATA.search_ads(info['uid'])
            type_ads = []
            for i in info_card:
                type_ads.append(i['card_bm'])
            _ads_card = QtGui.QStandardItem(str(','.join(type_ads)))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'ads-card'), _ads_card)

            # camps
            info_camps = MYDATA.search_camps(info['uid'])
            type_camps = []
            for i in info_camps:
                try:
                    last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date_create_camps']))
                    born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
                                    int(last_reaction[0][1]))  # provide UTC time
                    age = datetime.utcnow() - born
                    type_camps.append(f"{i['name_camps']}({i['status_camps']})({age.days})")
                except:
                    type_camps.append(f"{i['name_camps']}({i['status_camps']})(NA)")
            _ads_camps = QtGui.QStandardItem(str(','.join(type_camps)))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'ads-camps'), _ads_camps)

            # # _proxy
            # self.tableWidget.setItem(int(row), 18, self.createItem(str(info['proxy_private']),
            #                                                        Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))

            # Hitories
            search_logs = MYDATA.search_logs(info['uid'])
            type_logs = []
            for i in search_logs:
                try:
                    last_reaction = re.findall('([0-9]*)/([0-9]*)/([0-9]*)', str(i['date']))
                    born = datetime(int(last_reaction[0][2]), int(last_reaction[0][0]),
                                    int(last_reaction[0][1]))  # provide UTC time
                    age = datetime.utcnow() - born
                    type_logs.append(i['logs'] + f'({age.days})')
                except:
                    type_logs.append(i["logs"] + '(NA)')

            _ads_logs = QtGui.QStandardItem(str(','.join(type_logs)))
            model.setItem(row, self.getHeaderColumnsIndex(model, 'logs'), _ads_logs)

            # Total
            if info['status'] == 'Live':
                self.fb_live += 1
            if info['status'] == 'Die':
                self.fb_die += 1
            if info['status'] == 'CheckPoint':
                self.fb_checkpoint += 1

        self.statusBar_main.showMessage(
            f'COMPLETE - LIVE: {str(self.fb_live)} DISABLE: {str(self.fb_die)} CHECKPOINT: {str(self.fb_checkpoint)}')

        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'status'), 35)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'l'), 35)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'c'), 35)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'p'), 35)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'p/m'), 35)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'friends'), 40)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, '2fa'), 35)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'age'), 35)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'birthday'), 60)
        self.tableView_Facebook.setColumnWidth(self.getHeaderColumnsIndex(model, 'registed'), 60)

        _flag_thread = False
        self.tableView_Facebook.setDisabled(False)

    def copy_uid(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        uids = []
        for row in rows:
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            uids.append(_uid)
        pyperclip.copy('\n'.join(uids))

    def _checkuid(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        uids = []
        for row in rows:
            uids.append(self.tableView_Facebook.model().index(row.row(), 0).data())
        # check
        graph_fb = GraphFacebook()
        status = graph_fb.check_uid(uids)
        _live = 0
        _die = 0
        for s in status:
            _uid = s['uid']
            if s['status'] == 'Die':
                _die += 1
                MYDATA.update_data(_uid, {'status': 'CheckPoint'})
                logging.info(f'{_uid} - DIE')
            else:
                MYDATA.update_data(_uid, {'status': 'Live'})
                _live += 1
        logging.info(f'Check UID - LIVE: {_live}, DIE: {_die}')

    def checkuid(self):
        global _flag_thread
        if _flag_thread:
            QMessageBox.about(self, "WARNING", 'Current thread running !')
            return
        t11 = threading.Thread(target=self._checkuid)
        t11.start()

    def delete_row(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        for row in rows:
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            reply = QMessageBox.question(
                self,
                "Warning !!",
                f"Status: Live. Are you delete it : {_uid} ?",
                QMessageBox.Yes,
                QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                try:
                    # Delete in data
                    MYDATA.delete_data(int(_uid))
                    list_profiles = [name for name in os.listdir(CHROME_PROFILES) if
                                     os.path.isdir(os.path.join(CHROME_PROFILES, name))]
                    for profile in list_profiles:
                        if str.lower(_uid) in str.lower(profile):
                            _path = f'{CHROME_PROFILES}/{profile}'
                            shutil.rmtree(_path)
                            logging.info(f'Deleted: {_path}')
                except:
                    QMessageBox.about(self, "WARNING", f'Error delete')
        #
        # # Refesh
        # self.load_data()

    # def find_profile(self):
    #     infos = self.sqlhelper.select(
    #         "SELECT [uid] FROM info ORDER BY [action-begin] ASC")
    #
    #     for row, info in enumerate(infos):
    #         uid = infos[row][0]
    #
    #         # rename
    #         folder = CHROME_PROFILES
    #         src_name = str(uid)
    #         list_profiles = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    #         for profile in list_profiles:
    #             if src_name in profile:
    #                 self.sqlhelper.edit(
    #                     f"UPDATE info SET [profile-mobile]=FALSE , [profile-computer]=FALSE WHERE uid={uid};")
    #                 if '-mobile' in str.lower(profile):
    #                     self.sqlhelper.edit(
    #                         f"UPDATE info SET [profile-mobile]=TRUE WHERE uid={uid};")
    #                 elif '-computer' in str.lower(profile):
    #                     self.sqlhelper.edit(
    #                         f"UPDATE info SET [profile-computer]=TRUE WHERE uid={uid};")

    # def search_rename_folder_all(self):
    #     infos = self.sqlhelper.select(
    #         "SELECT [uid], [status], [type], [group], [fake-agent-mobile],[fake-agent-computer],[info-name], [info-birthday],[info-friend],[info-country],[action-begin],[action-last] FROM info ORDER BY [action-begin] ASC")
    #
    #     for row, info in enumerate(infos):
    #         uid = infos[row][0]
    #         _mobile = infos[row][4]
    #         _computer = infos[row][5]
    #
    #         mobile = True
    #         computer = True
    #         if (_mobile is None) or (_mobile == ''):
    #             mobile = False
    #         if (_computer is None) or (_computer == ''):
    #             computer = False
    #
    #         # rename
    #         folder = CHROME_PROFILES
    #         src_name = str(uid)
    #         if mobile:
    #             dst_name = f'{uid}-mobile'
    #         if computer:
    #             dst_name = f'{uid}-computer'
    #         if (mobile == True) and (computer == True):
    #             continue
    #         # self.search_rename_folder(CHROME_PROFILES, uid, f'{uid}-mobile')
    #         list_profiles = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    #         for profile in list_profiles:
    #             if str.lower(dst_name) == str.lower(profile):
    #                 logging.info(f'[{src_name}][Rename - File Exits]')
    #                 break
    #             if src_name in profile:
    #                 if ('-mobile' in str.lower(profile)) or ('-computer' in str.lower(profile)):
    #                     logging.info(f'[{src_name}][Rename - Error - ({profile})]')
    #                     break
    #                 os.rename(f'{folder}/{profile}', f'{folder}/{dst_name}')
    #                 logging.info(f'[{src_name}][Rename - Complete]({folder}/{profile})({folder}/{dst_name})')
    #                 break
    #
    # def search_rename_folder(self, method):
    #     infos = self.select_rows()
    #     for info in infos:
    #         uid = str(info[0])
    #         path = f"{CHROME_PROFILES}/{uid}-{method}"
    #         folder = CHROME_PROFILES
    #         src_name = uid
    #         dst_name = f'{uid}-{method}'
    #         # self.search_rename_folder(CHROME_PROFILES, uid, f'{uid}-mobile')
    #         list_profiles = [name for name in os.listdir(folder) if os.path.isdir(os.path.join(folder, name))]
    #         for profile in list_profiles:
    #             if str.lower(dst_name) == str.lower(profile):
    #                 logging.info(f'[{src_name}][Rename - File Exits]')
    #                 return
    #             if src_name in profile:
    #                 if ('-mobile' in str.lower(profile)) or ('-computer' in str.lower(profile)):
    #                     logging.info(f'[{src_name}][Rename - Error - ({profile})]')
    #                     return
    #                 os.rename(f'{folder}/{profile}', f'{folder}/{dst_name}')
    #                 logging.info(f'[{src_name}][Rename - Complete]({folder}/{profile})({folder}/{dst_name})')
    #                 return

    def remove_dir(self, path):
        try:
            """ param <path> could either be relative or absolute. """
            if os.path.isfile(path) or os.path.islink(path):
                os.remove(path)  # remove the file
            elif os.path.isdir(path):
                shutil.rmtree(path)  # remove dir and all contains
            else:
                raise ValueError("file {} is not a file or dir.".format(path))
        except:
            pass

    def delete_profiles(self, mobile):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        for row in rows:
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            # find uid
            _info = MYDATA.select_data(int(_uid))
            # if _info.status == 'Live':
            #     reply = QMessageBox.question(
            #         self,
            #         "Warning !!",
            #         "Status: Live. Are you delete it ?",
            #         QMessageBox.Yes,
            #         QMessageBox.No,
            #     )
            #     if reply == QMessageBox.No:
            #         logging.info(f'Status: Live - Not delete')
            #         continue

            # delete
            if mobile:
                _profile = f'{_uid}-mobile'
            else:
                _profile = f'{_uid}-dolphin'
                # update data
                MYDATA.update_data(int(_uid), {'last_profile_computer': False})
            try:
                list_profiles = [name for name in os.listdir(CHROME_PROFILES) if
                                 os.path.isdir(os.path.join(CHROME_PROFILES, name))]
                for profile in list_profiles:
                    if str.lower(_profile) == str.lower(profile):
                        _path = f'{CHROME_PROFILES}/{profile}'
                        try:
                            self.remove_dir(_path)
                            logging.info(f'Success - Deleted: {_path}')
                        except:
                            logging.info(f'Fail - Deleted: {_path}')
            except:
                QMessageBox.about(self, "WARNING", f'Error delete : {_profile}')

    def open_profile(self, method):
        infos = self.select_rows()
        for info in infos:
            uid = str(info.uid)
            if method == 'emulator':
                # print(f'explorer.exe "search-ms:query={uid}&crumb=location:{APPS_DATA}&"')
                Popen(
                    f'explorer.exe "search-ms:query={uid}&crumb=location:{APPS_DATA}&"')
            else:
                path = f"{CHROME_PROFILES}/{uid}-{method}"
                if os.path.exists(path):
                    Popen(f'explorer {os.path.realpath(path)}')
                else:
                    QMessageBox.about(self, "ERROR", "Warning ! Not create profile chrome.")

    def thread_stop(self):
        try:
            services = ["chromedriver.exe", "geckodriver.exe"]
            self.killer_services(services)
            if self._thread.isRunning():
                # print(int(self._thread.currentThreadId()))
                self._thread.quit()
                # del self._thread
                # del self._worker
        except:
            pass

    ######################## Emulator ########################
    def emulator_select_rows(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            # update: Action Last
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            # update data
            MYDATA.update_data(int(_uid), {'action_last': action_last})
            # select data
            info = MYDATA.select_data(int(_uid))
            infos.append({
                'fb_user': str(info.uid),
                'fb_pass': info.info_password,
                # 'fb_type': info.type,
                'ip_services': self.comboBox_proxy_services.currentText(),
                'ip_location': self.comboBox_ip_location.currentText(),
                'ip_list': str(self.plainTextEdit_tethering_proxy.toPlainText()).split('\n'),
                'fb_agent_mobile': info.fake_agent_mobile,
                # 'fb_browsers': info.fake_agent_computer,
                'fb_2fa': info.info_f2a,
                'fb_cookie': info.info_cookie,

            })
        return infos

    def stopThreads(self, thread):
        try:
            if thread.isRunning():
                thread.quit()
                # thread.terminate()
                thread.wait()
        except:
            pass

    def fb_update(self, infos):
        action, info = infos
        if action == 'fb_reactions':
            self.stopThreads(self.thread_fb_reactions)
        if action == 'fb_pass_multi':
            self.stopThreads(self.thread_fb_pass_multi)
        if action == 'fb_login_multi':
            self.stopThreads(self.thread_fb_login_multi)

    @pyqtSlot()
    def emulator_reactions(self):
        column_total = self.tableWidget.columnCount()
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in list(set(rows)):
            # Color
            # for c in range(0, column_total):
            #     self.tableWidget.item(row.row(), c).setBackground(QColor(236, 239, 164))
            #
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            fakephone = MYDATA.select_fakephone(info.fakephone_id)
            if isinstance(fakephone.last_backup, str) is False:
                logging.info(f'[{_uid}] - Error: Not find backup')
                continue
            _info = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'phone_info': fakephone,
                'proxy_private': str(info.proxy_private),
                'fb_reactions_notifications_loops': 5,
                'fb_reactions_photos_loops': 7,
                'infoPath': CURRENT_FOLDER + '/data/emulator',
                'mydata': MYDATA
            }
            infos.append(_info)
        self.thread_fb_reactions = QThread()
        self.worker = EmulatorLoops('fb_reactions', infos)
        self.thread_fb_reactions.started.connect(self.worker.run)
        self.worker.sig.connect(self.fb_update)
        self.worker.moveToThread(self.thread_fb_reactions)
        # self.emulator_reactions_action_stop.triggered.connect(self.thread_fb_reactions.quit)
        self.thread_fb_reactions.start()

    @pyqtSlot()
    def emulator_fb_login_multi(self):
        column_total = self.tableWidget.columnCount()
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in list(set(rows)):
            # # Color
            # for c in range(0, column_total):
            #     self.tableWidget.item(row.row(), c).setBackground(QColor(236, 239, 164))
            #
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'proxy_private': str(info.proxy_private),
                'infoPath': CURRENT_FOLDER + '/data/emulator',
                'mydata': MYDATA
            }
            infos.append(_info)
        self.thread_fb_login_multi = QThread()
        self.worker = EmulatorLoops('fb_login_multi', infos)
        self.thread_fb_login_multi.started.connect(self.worker.run)
        self.worker.sig.connect(self.fb_update)
        self.worker.moveToThread(self.thread_fb_login_multi)
        self.thread_fb_login_multi.start()

    @pyqtSlot()
    def emulator_fb_pass_multi(self):
        column_total = self.tableWidget.columnCount()
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in list(set(rows)):
            # # Color
            # for c in range(0, column_total):
            #     self.tableWidget.item(row.row(), c).setBackground(QColor(236, 239, 164))
            #
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            fakephone = MYDATA.select_fakephone(info.fakephone_id)
            if isinstance(fakephone.last_backup, str) is False:
                logging.info(f'[{_uid}] - Error: Not find backup')
                continue
            _info = {
                'index': v_index,
                'fb_user': str(info.uid),
                'fb_pass': str(info.info_password),
                'mail_user': str(info.mail_user),
                'mail_pass': str(info.mail_pass),
                'fb_2fa': str(info.info_f2a),
                'fb_agent_mobile': str(info.fake_agent_mobile),
                'ip_services': info.fake_service_proxy,
                'phone_info': fakephone,
                'proxy_private': str(info.proxy_private),
                'infoPath': CURRENT_FOLDER + '/data/emulator',
                'mydata': MYDATA
            }
            infos.append(_info)
        self.thread_fb_pass_multi = QThread()
        self.worker = EmulatorLoops('fb_pass_multi', infos)
        self.thread_fb_pass_multi.started.connect(self.worker.run)
        self.worker.sig.connect(self.fb_update)
        self.worker.moveToThread(self.thread_fb_pass_multi)
        # self.emulator_reactions_action_stop.triggered.connect(self.thread_fb_pass_multi.quit)
        self.thread_fb_pass_multi.start()

    @pyqtSlot()
    def emulator_folder(self):
        t12 = threading.Thread(target=self.open_profile('emulator'))
        # t.setDaemon(True)
        t12.start()

    def select_rows(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            # update: Action Last
            action_last = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
            # update data
            MYDATA.update_data(int(_uid), {'action_last': action_last})

            # select data
            info = MYDATA.select_data(int(_uid))
            # infos.append(
            #     (info.uid, info.type, self.comboBox_ip_location.currentText(),
            #      self.comboBox_proxy_services.currentText(),
            #      str(self.plainTextEdit_tethering_proxy.toPlainText()).split('\n'), info.fake_agent_mobile,
            #      info.fake_agent_computer, info.info_password, info.info_f2a, info.info_cookie, info.proxy_private))
            infos.append(info)
        return infos

    ######################## COMPUTER ########################
    def statusBarInfos(self, infos):
        self.statusBar_main.showMessage(infos)

    @pyqtSlot()
    def computer_open_profile(self):
        self.open_profile('dolphin')

    @pyqtSlot()
    def computer_delete_profile(self):
        self.delete_profiles(False)

    def robot_facebook_cmd(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                # 'fb_browsers': info.fake_agent_computer,
                'fb_infos': info,
                'last_profile_computer': info.last_profile_computer,
                'fb_user': str(info.uid),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_cmd', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def robot_facebook_cmd_cookies(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                # 'fb_browsers': info.fake_agent_computer,
                'fb_infos': info,
                'last_profile_computer': info.last_profile_computer,
                'fb_cookies': info.info_cookie,
                'fb_user': str(info.uid),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_cmd_cookies', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def robot_facebook_cmd_extensions(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                # 'fb_browsers': info.fake_agent_computer,
                'fb_infos': info,
                'fb_user': str(info.uid),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
                'last_profile_computer': info.last_profile_computer,
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_cmd_extensions', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    # def computer_profile(self):
    #     infos = self.select_rows()
    #     for info in infos:
    #         self.statusBarInfos(f'{info.uid} - Running')
    #         if (info.fake_agent_computer == '') or (info.fake_agent_computer is None):
    #             logging.info(f'[{info.uid}] - Not UserAgent')
    #             break
    #         self._thread = QThread(self)
    #         self._worker = ChromeProfileManager(info, False, 'computer_profile')
    #         self._worker.moveToThread(self._thread)
    #         self._thread.started.connect(self._worker.worker)
    #         self._thread.start()
    #         self._worker.sig.connect(self.computer_status)
    #         time.sleep(random.randint(2, 5))

    def computer_status(self, infos):
        # self.thread_stop()
        method, info = infos
        if method == 'computer_profile_cmd' and info[1] == 'Error_Timezone':
            QMessageBox.about(self, "WARNING", "Error get Timezone from Ip !!")
        if method == 'computer_profile_get_cookies':
            logging.info(f'{info[0]} - [{info[1]}]')

    def robot_facebook_status(self, infos):
        # self.thread_stop()
        return

    def robot_computer_facebook_reactions(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_computer_facebook_reactions', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def robot_mobile_facebook_cmd(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                # 'fb_browsers': info.fake_agent_computer,
                'fb_infos': info,
                'fb_user': str(info.uid),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_mobile_facebook_cmd', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def robot_mobile_facebook_reactions(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_mobile_facebook_reactions', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def robot_facebook_page(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        # Page Name
        with open(f'{DATA}/page/names.txt', 'r', encoding="utf8") as f:
            page_names = f.readlines()
        # Photo Profile
        photo_profile = f"{DATA}/page/photo_profile"
        photo_profiles = []
        for folder, subs, files in os.walk(photo_profile):
            for filename in files:
                photo_profiles.append(os.path.abspath(os.path.join(folder, filename)))
        # Photo Cover
        photo_cover = f"{DATA}/page/photo_cover"
        photo_covers = []
        for folder, subs, files in os.walk(photo_cover):
            for filename in files:
                photo_covers.append(os.path.abspath(os.path.join(folder, filename)))
        #
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            # page_create
            pages_info = MYDATA.search_pages(str(info.uid))
            #
            _info = {
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
                'page_names': page_names,
                'page_photo_profile': photo_profiles,
                'page_photo_cover': photo_covers,
                'page_create': 5
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_page', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def robot_facebook_infos(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            # page_create
            pages_info = MYDATA.search_pages(str(info.uid))
            #
            _info = {
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_infos', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    def robot_facebook_login_status(self, infos):
        while True:
            try:
                services = ["chromedriver.exe", "geckodriver.exe"]
                self.killer_services(services)
                if self._thread_robot_facebook_login.isRunning():
                    self._thread_robot_facebook_login.quit()
                    del self._thread_robot_facebook_login
                    return
            except:
                pass

    def robot_facebook_login(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        # Extensions: Trace
        extensions_trace = []
        for folder, subs, files in os.walk(CHROME_EXTENSIONS):
            for filename in files:
                if filename == 'TraceSettings.json':
                    extensions_trace.append(os.path.abspath(os.path.join(folder, filename)))
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            _info = {
                # 'fb_browsers': info.fake_agent_computer,
                'fb_infos': info,
                'fb_user': str(info.uid),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
                'extensions_trace': extensions_trace[0]
            }
            infos.append(_info)
        self._thread_robot_facebook_login = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_login', infos)
        self._worker.moveToThread(self._thread_robot_facebook_login)
        self._thread_robot_facebook_login.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_login_status)
        self._thread_robot_facebook_login.start()

    # ROBOT - ADS
    def robot_facebook_business_add_infos(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        # # Card
        # with open(ADS_CARD, 'r', encoding='utf-8') as f:
        #     ads_card = f.readlines()
        # # ADS_CARD_ads_card
        # _ads_card = random.choice(ads_card)
        # with open(ADS_CARD, 'w', encoding='utf-8') as f:
        #     for line in ads_card:
        #         if line.strip("\n") != _ads_card:
        #             f.write(line)
        #
        infos = []
        for row in rows:
            # ADS_ADDRESS
            with open(ADS_ADDRESS, 'r', encoding='utf-8') as f:
                ads_address = f.readlines()
            _ads_address = str(random.choice(ads_address)).strip()
            with open(ADS_ADDRESS, 'w', encoding='utf-8') as f:
                for line in ads_address:
                    if line.strip() != _ads_address:
                        f.write(line)
            #
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            #
            _info = {
                'fb_infos': info,
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
                'ads_address': _ads_address
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_business_add_infos', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    # ROBOT - Mail change password
    def robot_mail_changepass(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        # Mail: IMAP
        with open(MAIL_IMAP, 'r', encoding='utf-8') as f:
            mail_backup_imap = f.readlines()
        # ['codesim.net','a919c843-e221-4a70-9f5c-1d0117f1c1a7', '20']
        # ['chothuesimcode.com','46e24484','1017']
        # ["viotp.com","a68b58d2cb6646c6a2d4f1805196d4af","5"]
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            #
            _info = {
                'fb_infos': info,
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,

                # mail
                'mail_backup_imap': mail_backup_imap,
                # 'phone_services': ["viotp.com", "a68b58d2cb6646c6a2d4f1805196d4af", "5"],
                'phone_services': ["codesim.net", "a919c843-e221-4a70-9f5c-1d0117f1c1a7", "20"],
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_mail_changepass', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    # ROBOT - Mail - Login
    def robot_mail_login(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            #
            _info = {
                'fb_infos': info,
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
                # mail
                # 'phone_services': ["viotp.com", "a68b58d2cb6646c6a2d4f1805196d4af", "5"],
                'phone_services': ["codesim.net", "a919c843-e221-4a70-9f5c-1d0117f1c1a7", "20"],
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_mail_login', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    # ROBOT
    def robot_facebook_setups(self):
        rows = self.tableView_Facebook.selectionModel().selectedRows()
        infos = []
        # Extensions: Trace
        extensions_trace = []
        for folder, subs, files in os.walk(CHROME_EXTENSIONS):
            for filename in files:
                if filename == 'TraceSettings.json':
                    extensions_trace.append(os.path.abspath(os.path.join(folder, filename)))

        for row in rows:
            debug_port = random.randint(1000, 9999)
            _uid = self.tableView_Facebook.model().index(row.row(), 0).data()
            info = MYDATA.select_data(_uid)
            #
            _info = {
                'fb_infos': info,
                'fb_user': str(info.uid),
                # 'fb_browsers': str(info.fake_agent_computer),
                'proxy_private': str(info.proxy_private),
                'debug_port': debug_port,
                'extensions_trace': extensions_trace[0]
            }
            infos.append(_info)
        self._thread = QThread(self)
        self._worker = FacebookBrowser('robot_facebook_setups', infos)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.sig.connect(self.robot_facebook_status)
        self._thread.start()

    ######################## OTHER ########################
    # def keyPressEvent(self, event):
    #     clipboard = QApplication.clipboard()
    #     if event.matches(QKeySequence.Copy):
    #         print('Ctrl + C')
    #         clipboard.setText("some text")
    #     if event.matches(QKeySequence.Paste):
    #         print(clipboard.text())
    #         print('Ctrl + V')
    #     QtableWidget.keyPressEvent(self, event)

    def _random_infos_computer(self):
        # with open(USERAGENT_COMPUTER, 'r', encoding='utf-8') as f:
        #     agent_c = f.readlines()
        # useragent = random.choice(agent_c)
        # self.lineEdit_fake_agent_computer.setText(useragent.strip())
        with open(BROWSERS_USERAGENT_WINDOW, 'r', encoding='utf-8') as f:
            agent_c = f.readlines()
        with open(BROWSERS_WINDOW_SIZE, 'r', encoding='utf-8') as f:
            _window_size = f.readlines()
        with open(BROWSERS_MAC, 'r', encoding='utf-8') as f:
            _mac = f.readlines()
        with open(BROWSERS_LAN_IP, 'r', encoding='utf-8') as f:
            _lanip = f.readlines()

        while True:
            useragent = random.choice(agent_c).strip()
            mac = str(random.choice(_mac)).upper().strip()
            lanip = random.choice(_lanip).strip()
            name_computer = str(f'DESKTOP-{id_generator()}').upper().strip()

            cpu = random.randint(2, 16)
            ram = random.randint(5, 32)
            while True:
                windowsize = random.choice(_window_size).split('|')
                if windowsize[0].strip() == 'Mobile':
                    continue
                break
            computer = {
                "user_agent": useragent,
                "name_computer": name_computer,
                "cpu": cpu,
                "ram": ram,
                "swidth": windowsize[1].strip(),
                "sheight": windowsize[2].strip(),
                "pixelratio": windowsize[3].strip(),
                "mac_address": mac,
                "lan_ip": lanip,
            }
            return computer

    def add_data(self):
        data_clipboard = QApplication.clipboard().text()
        datas = data_clipboard.split('\n')
        for line in datas:
            if line.strip() == "":
                continue
            info = line.strip().split('|')
            # random useragent
            # with open(USERAGENT_COMPUTER, 'r', encoding='utf-8') as f:
            #     agent_computer = f.readlines()
            with open(USERAGENT_MOBILE, 'r', encoding='utf-8') as f:
                agent_mobile = f.readlines()

            # # Mail
            # path_mail = 'library/mail/live.txt'
            # with open(path_mail, 'r') as f:
            #     mails = f.readlines()
            # if len(mails) == 0:
            #     QMessageBox.about(self, "Error", "Mail = 0")
            #     return
            # mail = random.choice(mails)
            # mails.remove(mail)
            # with open(path_mail, 'w') as f:
            #     f.writelines(mails)

            # print(info)
            # uid|pass|cookie|2fa|mail|mailpass

            _proxy = ''
            if info[0] == 'US':
                utilities = Utilities()
                _proxy = utilities.proxies_get('LA,US', './data/spoof_proxy.txt')
            if info[0] == 'VIA':
                _proxy = 'socks5:127.0.0.1:1113'

            infos = dict()
            try:
                    infos['uid'] = info[1]
                    infos['status'] = 'Live'
                    infos['camps_plans'] = ''
                    infos['camps_groups'] = ''
                    infos['camps_pixels'] = ''
                    infos['ads_tuts'] = ''
                    infos['ads_groups'] = info[7]
                    infos['fake_ip'] = 'US'
                    infos['fake_service_proxy'] = 'Proxy'
                    infos['fake_agent_mobile'] = str(random.choice(agent_mobile)).strip()
                    infos['info_name'] = ''
                    infos['info_password'] = info[2]
                    infos['info_f2a'] = info[3].strip()
                    infos['info_cookie'] = info[8]
                    infos['info_token'] = ''
                    infos['info_birthday'] = ''
                    infos['info_gender'] = ''
                    infos['info_friend'] = ''
                    infos['info_country'] = info[6]
                    infos['info_createdate'] = ''
                    infos['mail_user'] = info[4].strip()
                    infos['mail_pass'] = info[5].strip()
                    infos['mail_recovery'] = ''
                    infos['action_begin'] = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
                    infos['action_last'] = datetime.now().strftime("%m/%d/%Y-%H.%M.%S")
                    # infos['last_profile_mobile'] = ''
                    infos['last_profile_computer'] = ''
                    infos['info_register_date'] = ''
                    infos['ip_last_location'] = ''
                    infos['histories'] = ''
                    infos['proxy_private'] = _proxy
                    infos['location_spoof'] = ''
                    infos['info_change_mail'] = 'n'
                    infos['info_change_pass'] = 'n'

                    # browsersInfos = [
                    #     # "gologin|97|Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
                    #     # "gologin|100|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
                    #     # "gologin|102|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
                    #     # "gologin|103|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
                    #     # "dolphin|99|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                    #     "dolphin|100|Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
                    # ]
                    # _browsersInfos = random.choice(browsersInfos).split('|')
                    # infos['fake_agent_computer'] = str({
                    #     'browser': _browsersInfos[0],
                    #     'version': _browsersInfos[1],
                    #     'useragent': _browsersInfos[2]
                    # })
                    MYDATA.insert_data(infos)
                    logging.info(line)
            except:
                    QMessageBox.about(self, "Loaded", "Error")
            
        # self._sort_begin()
        QMessageBox.about(self, "Loaded", "Success")

    def killer_services(self, services):
        for service in services:
            for proc in psutil.process_iter():
                if proc.name() == service:
                    proc.kill()

    def backup_daily(self):
        now = datetime.now()  # current date and time
        time = now.strftime("%m.%d.%Y-%H.%M")
        head, tail = os.path.split(SQLITE)
        _backup = BACKUP + tail.replace("mydb", f"{time}_mydb")
        try:
            if os.path.exists(_backup) is False:
                shutil.copyfile(SQLITE, _backup)
        except:
            QMessageBox.about(self, "ERROR", f"Error Backup - {_backup}")


def killer_services():
    services = ["chromedriver.exe", "adb.exe", "nox_adb.exe", "naive.exe", "geckodriver.exe"]
    for service in services:
        for proc in psutil.process_iter():
            if proc.name() == service:
                proc.kill()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    # mail = 'd2a5d2002@yahoo.com.br|efcladvjlsybyngs12345'
    # emailChecker = EmailChecker()
    # emailChecker.checker(mail)
    
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(True)
    app.lastWindowClosed.connect(killer_services)
    # app.aboutToQuit.connect(myExitHandler)
    w = AppWindow()
    w.show()
    sys.exit(app.exec_())

    # import difflib
    # infos = MYDATA.query_all_accounts('action_begin_days')
    # with open('./data/_countries.txt', 'r', encoding='utf8') as f:
    #     countries = f.readlines()
    # for info in infos:
    #     for country in countries:
    #         _diff = str(int(difflib.SequenceMatcher(None, str(info['info_country']), str(country)).ratio() * 100))
    #         if int(_diff) > 60:
    #             print(f'{info["uid"]} - {info["info_country"]} - {country} - {_diff}')
    #             MYDATA.update_data(int(info['uid']), {'info_country': str(country).strip()})
    #             break

    # infos = MYDATA.query_all_accounts('ads_groups')
    # for info in infos:
    # if 'Yes' in info['info_change_pass']:
    #     MYDATA.update_data(int(info['uid']), {'info_change_pass': 'Y'})
    # if 'No' in info['info_change_pass']:
    #     MYDATA.update_data(int(info['uid']), {'info_change_pass': 'n'})
    # if ((('@hotmail.com' in str(info['mail_user'])) or ('@outlook.com' in str(info['mail_user']))) and ('@' not in info['mail_recovery'])) or ('@web.de' in info['mail_user']):
    #     MYDATA.update_data(int(info['uid']), {'info_change_mail': 'n'})
    # else:
    #     MYDATA.update_data(int(info['uid']), {'info_change_mail': 'Y'})

    # infos = MYDATA.query_all_accounts('ads_groups')
    #
    # with open(BROWSERS_USERAGENT_WINDOW, 'r', encoding='utf-8') as f:
    #     agent_c = f.readlines()
    # with open(BROWSERS_WINDOW_SIZE, 'r', encoding='utf-8') as f:
    #     _window_size = f.readlines()
    # with open(BROWSERS_MAC, 'r', encoding='utf-8') as f:
    #     _mac = f.readlines()
    # with open(BROWSERS_LAN_IP, 'r', encoding='utf-8') as f:
    #     _lanip = f.readlines()
    #
    # count = 0
    # for info in infos:
    #     useragent = random.choice(agent_c).strip()
    #     mac = str(random.choice(_mac)).upper().strip()
    #     lanip = random.choice(_lanip).strip()
    #     name_computer = str(f'DESKTOP-{id_generator()}').upper().strip()
    #
    #     cpu = random.randint(2, 16)
    #     ram = random.randint(5, 32)
    #     while True:
    #         windowsize = random.choice(_window_size).split('|')
    #         if windowsize[0].strip() == 'Mobile':
    #             continue
    #         break
    #     computer = {
    #         "user_agent": useragent,
    #         "name_computer": name_computer,
    #         "cpu": cpu,
    #         "ram": ram,
    #         "swidth": windowsize[1].strip(),
    #         "sheight": windowsize[2].strip(),
    #         "pixelratio": windowsize[3].strip(),
    #         "mac_address": mac,
    #         "lan_ip": lanip,
    #     }
    #     MYDATA.update_data(int(info['uid']),
    #                            {'fake_agent_computer': str(computer)})
    #     count += 1
    #     print('{} - {}'.format(count, info['uid']))

    # while True:
    #     if count > 10000:
    #         break
    #     useragent = random.choice(agent_c).strip()
    #     mac = str(random.choice(_mac)).upper().strip()
    #     lanip = random.choice(_lanip).strip()
    #     name_computer = str(f'DESKTOP-{id_generator()}').upper().strip()
    #
    #     cpu = random.randint(2, 16)
    #     ram = random.randint(5, 32)
    #     while True:
    #         windowsize = random.choice(_window_size).split('|')
    #         if windowsize[0].strip() == 'Mobile':
    #             continue
    #         break
    #     computer = {
    #         "user_agent": useragent,
    #         "name_computer": name_computer,
    #         "cpu": cpu,
    #         "ram": ram,
    #         "swidth": windowsize[1].strip(),
    #         "sheight": windowsize[2].strip(),
    #         "pixelratio": windowsize[3].strip(),
    #         "mac_address": mac,
    #         "lan_ip": lanip,
    #     }
    #     with open('D:\Project - Python\FacebookTools\Gui\TakeCareVia\data\\useragent\\agent.txt', 'a') as file:
    #         file.write(str(computer).strip() + '\n')
    #     count += 1
    #     print('{}'.format(count))

    # infos = MYDATA.query_all_accounts('ads_groups')
    # for info in infos:
    #     if '@hotmail.com' in str(info['mail_user']):
    #         MYDATA.update_data(int(info['uid']),
    #                            {'info_change_mail': 'No'})
    #
    #     if ('@' in str(info['info_password'])) and (str(info['info_change_pass']) == 'No'):
    #         MYDATA.update_data(int(info['uid']),
    #                            {'info_change_pass': 'Yes'})

    # account = MYDATA.select_data('100003166060529')
    # fakephone = MYDATA.select_fakephone(account.fakephone_id)
    # _macaddress = fakephone.macaddress
    # if (_macaddress == '') or (_macaddress is None):
    #     general_info = FakeInfos('F:\Project - Python\FacebookTools\Gui\TakeCareVia\data\emulator')
    #     # _manufacturer = useragent.split('|')[1]
    #     _macaddress = general_info.macaddress('Samsung').replace(':', '').upper()
    # print(_macaddress)

# https://datadome.co/product/
# https://www.controller.com/
# https://intoli.com/blog/making-chrome-headless-undetectable/
# https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
# https://stackoverflow.com/questions/54984185/webpage-is-detecting-selenium-webdriver-with-chromedriver-as-a-bot

# # path chrome driver
# def patch_binary(executable_path):
#     with open(executable_path, "r+b") as binary:
#         for line in iter(lambda: binary.readline(), b""):
#             if b"cdc_" in line:
#                 binary.seek(-len(line), 1)
#                 line = b"  var key = '$azc_abcdefghijklmnopQRstuv_';\n"
#                 binary.write(line)
#                 __IS_PATCHED__ = 1
#                 break
#         else:
#             return False
#         return True
#
#
# if __name__ == '__main__':
#     a = 'tessg1tvhundt@pseudonim.pl'
#     b = 'tessg1tvhundt@pseudonim.paaassaaaaaa'
#     print(id(a))
#     print(id(b))
