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
def save_settings():
	with open("settings.json", 'w') as set_prog_f:
		set_prog_f.write(json.dumps(settings))

#losd settings
settings ={'projects':
			[
				'main',
			],
			'current_project':'main'
		  }



try:
	with open("settings.json", 'r') as set_prog_f:
		settings = json.loads(set_prog_f.read())
except:
	save_settings()


#
def  alert(msg_alert):
	messagebox.showinfo(message=msg_alert)

#
def obrtka(f_ober):
	try:
		f_ober()
	except BaseException as err:
		print(err)
		print(traceback.format_exc())

def dlg_project_new():
	global htyjtyjtyjytyjyj
	dlg = Toplevel(root)


	w = root.winfo_width()
	h = root.winfo_height()

	stgg = 0
	xcord = ''
	ycord = ''
	for kjkd in root.geometry():
		if kjkd == '+':
			stgg = stgg +1
		elif stgg==1:
			xcord = xcord + kjkd
		elif stgg==2:
			ycord = ycord + kjkd
		else:
			pass
	xcord=int(xcord)
	ycord=int(ycord)
	dlg.title('Создать новый проект')
	Label(dlg, text='Введите имя нового проекта:').grid()
	new_name_dlg = Entry(dlg)
	new_name_dlg.grid()
	ttk.Button(dlg, text="Создать", command= lambda: dlg_dismiss(dlg, new_name_dlg)).grid()
	w = w//2
	h = h//2
	w1 = xcord + w
	w2 = ycord + h

	dlg.transient(root)   # dialog window is related to main
	dlg.wait_visibility() # can't grab until window appears, so we wait
	dlg.grab_set()        # ensure all input goes to our window

	w11 = dlg.winfo_width() //2
	w21 = dlg.winfo_height() //2
	dlg.geometry('+{}+{}'.format(w1 - w11, w2 - w21))

	dlg.protocol("WM_DELETE_WINDOW", lambda:  dlg_dismiss(dlg, new_name_dlg)) # intercept close button
	dlg.wait_window()     # block until window is destroyed
	return htyjtyjtyjytyjyj

def dlg_dismiss (dlg, new_name_dlg):
	global htyjtyjtyjytyjyj
	htyjtyjtyjytyjyj = new_name_dlg.get()
	dlg.grab_release()
	dlg.destroy()

def test():
    print('test')
    print(cloudCombobox.get())

token = 'AQAAAaQVovAA1amHsz0zw3kG2Q'

#iamToken=get_iamToken(token)
#Organization=get_listOrganization(iamToken)
#clouds=get_listCloud(iamToken, Organization=Organization['organizations'][1]['id'])
#clouds=get_listCloud(iamToken)
#folders=get_listFolders(iamToken, Cloud=clouds['clouds'][1]['id'])
#functions=get_listFunction(iamToken, folders['folders'][4]['id'])
#print(functions)
#print(get_yaInfo(token))


def project_new_f():
	gtjtj= dlg_project_new()
	settings['projects'].append(gtjtj)
	cloudCombobox['values']=settings['projects']
	cloudCombobox.set(gtjtj)
	settings['current_project']=gtjtj
	save_settings()

def project_del_f():
	settings['projects'].remove(cloudCombobox.get())
	cloudCombobox['values']=settings['projects']
	cloudCombobox.set('')
	settings['current_project']=''
	save_settings()

root = tk.Tk()
root.geometry("500x475")
root.title('Serverless-GUI')


#f1
frame1 = tk.Frame(master=root,borderwidth=5)

Label(master=frame1, text="Serverless-GUI").pack(side=tk.LEFT)
buttons={'account':
            {'text':'Аккаунт',
            'cmd':test},
		'project_new':
			{'text':'+',
            'cmd':project_new_f},
		'project_del':
			{'text':'-',
            'cmd':project_del_f},
        }


countryvar = StringVar()
cloudCombobox = ttk.Combobox(frame1, textvariable=countryvar)
cloudCombobox.state(["readonly"])
cloudCombobox['values']=settings['projects']
cloudCombobox.set(settings['current_project'])

tk.Button(frame1, text=buttons['account']['text'],
    command=buttons['account']['cmd']).pack(fill=tk.Y, side=tk.RIGHT, padx=10 )

tk.Button(frame1, text=buttons['project_new']['text'],
    command=buttons['project_new']['cmd']).pack(fill=tk.Y, side=tk.RIGHT)

tk.Button(frame1, text=buttons['project_del']['text'],
    command=buttons['project_del']['cmd']).pack(fill=tk.Y, side=tk.RIGHT)

cloudCombobox.pack(fill=tk.Y, side=tk.RIGHT)
Label(master=frame1, text="Проект: ").pack(fill=tk.Y, side=tk.RIGHT)


###########################################################
frame2 = tk.Frame(master=root,borderwidth=5)

clouds_frame = tk.Frame(master=frame2)

Label(master=clouds_frame, text="Облако").pack(fill=tk.X)

treeCloud = ttk.Treeview(clouds_frame)
treeCloud['columns'] = ('id')

treeCloud.pack()

#################
resurs_frame = tk.Frame(master=frame2)


Label(master=resurs_frame, text="Ресурс").pack(fill=tk.X)

treeFunc = ttk.Treeview(resurs_frame)
treeFunc['columns'] = ('id')

treeFunc.pack()

#########################
clouds_frame.pack(fill=tk.X, side=tk.LEFT)
resurs_frame.pack(fill=tk.X, side=tk.LEFT)
#################################################
frame1.pack(fill=tk.X)
frame2.pack(fill=tk.X)

root.mainloop()






































eng=1
