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
#
token = ''

iamToken=get_iamToken(token)
#print(iamToken)
Organization=get_listOrganization(iamToken)
#print(Organization)
clouds=get_listCloud(iamToken, Organization=Organization['organizations'][1]['id'])
#print(clouds)
clouds=get_listCloud(iamToken)
#print(clouds)
folders=get_listFolders(iamToken, Cloud=clouds['clouds'][1]['id'])
#print(folders)
functions=get_listFunction(iamToken, folders['folders'][4]['id'])
print(functions)
#print(get_yaInfo(token))
