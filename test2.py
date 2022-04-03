import boto3
import os, sys
from tkinter import *
import tkinter as tk
import codecs
from tkinter import ttk
from tkinter import filedialog
import time
from threading import Thread
import requests
import json
import traceback
from tkinter import messagebox
import webbrowser
login_bas=1
import time
from hurry.filesize import size
from tkinter.ttk import Combobox
from tkinter import colorchooser
from tkinter.filedialog import asksaveasfile
import tkinter.messagebox
from rich import print
from rich.pretty import pprint
from rich import inspect
import yandexcloud
from clApi import *
import webbrowser

token = ''

import shutil

iamToken=get_iamToken(token)


access_key = ''
secret_key = ''


def up_from_f(inp, to, out):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3.upload_file(inp, to, out)




def push_func(path, id_F):
    shutil.make_archive(str(id_F), 'zip', path)
    #up_from_f(str(id_F)+'.zip', settings['svazi'][settings['current_project']]['home_b'][0], str(id_F)+'.zip')
    up_from_f(str(id_F)+'.zip', 'test-sgui', str(id_F)+'.zip')
    package={
        "bucketName": "test-sgui",
        "objectName": "d4e8p5vegal67cklbsrc.zip",
      }
    print(get_createFunction_postVer(iamToken, 'd4e8p5vegal67cklbsrc', package))






#push_func('C:/dev/test-sgui/func', 'd4e8p5vegal67cklbsrc')




















f=3
