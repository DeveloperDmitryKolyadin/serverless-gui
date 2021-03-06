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
import shutil
#
def save_settings():
	with open("settings.json", 'w') as set_prog_f:
		set_prog_f.write(json.dumps(settings))

#losd settings
settings ={'projects':
			[
				'main',
			],
			'current_project':'main',
			'token':'',
			'svazi':{
				'main':{
					"home_b":None,
					'functions':{},
					"apigateways":{},
					"buckets":{}
					}
			}
		  }



try:
	with open("settings.json", 'r') as set_prog_f:
		settings = json.loads(set_prog_f.read())
except:
	save_settings()




def up_from_f(inp, to, out):
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        aws_access_key_id=settings['svazi'][settings['current_project']]['home_b']['aws_access_key_id'],
        aws_secret_access_key=settings['svazi'][settings['current_project']]['home_b']['aws_secret_access_key'],
    )
    s3.upload_file(inp, to, out)



def push_func(path, id_F):
    shutil.make_archive(str(id_F), 'zip', path)
    up_from_f(str(id_F)+'.zip', settings['svazi'][settings['current_project']]['home_b']['b'], str(id_F)+'.zip')
    #up_from_f(str(id_F)+'.zip', 'test-sgui', str(id_F)+'.zip')
    package={
        "bucketName": settings['svazi'][settings['current_project']]['home_b']['b'],
        "objectName": str(id_F)+'.zip',
      }
    return get_createFunction_postVer(iamToken, id_F, package)




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
	dlg.title('?????????????? ?????????? ????????????')
	Label(dlg, text='?????????????? ?????? ???????????? ??????????????:').grid()
	new_name_dlg = Entry(dlg)
	new_name_dlg.grid()
	ttk.Button(dlg, text="??????????????", command= lambda: dlg_dismiss(dlg, new_name_dlg)).grid()
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




def project_new_f():
	gtjtj= dlg_project_new()
	if gtjtj:
		settings['projects'].append(gtjtj)
		settings['svazi'][gtjtj]={
			"home_b":None,
			'functions':{},
			"apigateways":{},
			"buckets":{}
			}
		cloudCombobox['values']=settings['projects']
		cloudCombobox.set(gtjtj)
		settings['current_project']=gtjtj
		inp_b_id(n=gtjtj)
		save_settings()
	else:
		project_new_f()
def project_del_f():
	settings['projects'].remove(cloudCombobox.get())
	del settings['svazi'][cloudCombobox.get()]
	del settings['current_project']
	cloudCombobox['values']=settings['projects']
	cloudCombobox.set('')
	save_settings()
	if settings['projects']:
		settings['current_project']=settings['projects'][0]
		cloudCombobox.set(settings['projects'][0])
		save_settings()
	else:
		project_new_f()


def ComboboxSelected(h):
	settings['current_project']=cloudCombobox.get()
	save_settings()

def setup_inter():
	global iamToken
	iamToken=get_iamToken(settings['token'])
	clouds=get_listCloud(iamToken)
	treeClouds={}
	treeFolders={}
	for cl in clouds['clouds']:
		tmp=treeCloud.insert('', 'end', text=cl['name'],tags=('c'),  values=(cl['id']))
		treeCloud.item(tmp, open=1)
		treeClouds[cl['id']]=tmp
		folders=get_listFolders(iamToken, Cloud=cl['id'])
		for fd in folders['folders']:
			tmpfd=treeCloud.insert(tmp, 'end', text=fd['name'],tags=('f'), values=(fd['id']))
			treeFolders[fd['id']]=tmp


	for s_fun in settings['svazi'][settings['current_project']]['functions']:
		name_f =  get_Func(iamToken, s_fun)['name']
		treeSvazi.insert('', 'end', text='F "' + name_f  + '"', tags=('f', s_fun), values=(settings['svazi'][settings['current_project']]['functions'][s_fun]))
	for s_api in settings['svazi'][settings['current_project']]['apigateways']:
		pass
	for s_st in settings['svazi'][settings['current_project']]['buckets']:
		pass


def CL_selection_e(event):
	event = treeCloud.item(treeCloud.focus())
	text_info_frame.delete('1.0', 'end')
	print(event)
	type_sel=event['tags'][0]
	if type_sel=='c':
		Cloud_info= get_Cloud(iamToken, event['values'][0])
		info_v=''
		for parametr_cl in Cloud_info:
			if parametr_cl == 'id':
				info_v=info_v+'Id: '+Cloud_info[parametr_cl]+'\n'
			elif parametr_cl == 'createdAt':
				info_v=info_v+'????????????????: '+Cloud_info[parametr_cl]+'\n'
			elif parametr_cl == 'name':
				info_v=info_v+'??????: '+Cloud_info[parametr_cl]+'\n'
			elif parametr_cl == 'organizationId':
				info_v=info_v+'Id ??????????????????????: '+Cloud_info[parametr_cl]+'\n'
			elif parametr_cl == 'description':
				info_v=info_v+'????????????????: '+Cloud_info[parametr_cl]+'\n'

		text_info_frame.replace('1.0', 'end', chars=info_v)
		__ = treeFunc.get_children(treeFuncFunc)
		for _ in __:
			treeFunc.delete(_)
	elif type_sel=='f':
		Folder_info= get_Folder(iamToken, event['values'][0])
		info_v=''
		for parametr_cl in Folder_info:
			if parametr_cl == 'id':
				info_v=info_v+'Id: '+Folder_info[parametr_cl]+'\n'

			elif parametr_cl == 'createdAt':
				info_v=info_v+'????????????????: '+Folder_info[parametr_cl]+'\n'

			elif parametr_cl == 'name':
				info_v=info_v+'??????: '+Folder_info[parametr_cl]+'\n'

			elif parametr_cl == 'cloudId':
				info_v=info_v+'Id ????????????: '+Folder_info[parametr_cl]+'\n'

			elif parametr_cl == 'description':
				info_v=info_v+'????????????????: '+Folder_info[parametr_cl]+'\n'

			elif parametr_cl == 'status':
				info_v=info_v+'????????????: '+Folder_info[parametr_cl]+'\n'

		text_info_frame.replace('1.0', 'end', chars=info_v)



		__ = treeFunc.get_children(treeFuncFunc)
		for _ in __:
			treeFunc.delete(_)
		functions=get_listFunction(iamToken, event['values'][0])
		#print(functions)
		if functions:
			for fn in functions['functions']:
				tmpfd=treeFunc.insert(treeFuncFunc, 'end', text=fn['name'],tags=('Func'), values=(fn['id']))
def RE_selection_e(event):
	event = treeFunc.item(treeFunc.focus())
	text_info_frame.delete('1.0', 'end')
	print(event)
	type_sel=event['tags'][0]
	if type_sel=='API':
		pass
	elif type_sel=='Storage':
		pass
	elif type_sel=='Func':

		Func_info= get_Func(iamToken, event['values'][0])
		info_v=''
		for parametr_cl in Func_info:
			if parametr_cl == 'id':
				info_v=info_v+'Id: '+Func_info[parametr_cl]+'\n'

			elif parametr_cl == 'createdAt':
				info_v=info_v+'????????????????: '+Func_info[parametr_cl]+'\n'

			elif parametr_cl == 'name':
				info_v=info_v+'??????: '+Func_info[parametr_cl]+'\n'

			elif parametr_cl == 'folderId':
				info_v=info_v+'Id ????????????????: '+Func_info[parametr_cl]+'\n'

			elif parametr_cl == 'description':
				info_v=info_v+'????????????????: '+Func_info[parametr_cl]+'\n'

			elif parametr_cl == 'httpInvokeUrl':
				info_v=info_v+'Ur: '+Func_info[parametr_cl]+'\n'

			elif parametr_cl == 'status':
				info_v=info_v+'????????????: '+Func_info[parametr_cl]+'\n'

		text_info_frame.replace('1.0', 'end', chars=info_v)


def sinxr_one():
	item = treeSvazi.item(treeSvazi.focus())
	path=item['values'][0]
	id_F=item['tags'][1]
	print(item)
	print(path)
	print(id_F)
	print(push_func(path, id_F))


root = tk.Tk()
root.geometry("1225x600")
root.title('Serverless-GUI')


#f1
frame1 = tk.Frame(master=root,borderwidth=5)

Label(master=frame1, text="Serverless-GUI").pack(side=tk.LEFT)
buttons={'account':
            {'text':'??????????????',
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
cloudCombobox.bind('<<ComboboxSelected>>', ComboboxSelected)

tk.Button(frame1, text=buttons['account']['text'],
    command=buttons['account']['cmd']).pack(fill=tk.Y, side=tk.RIGHT, padx=10 )

tk.Button(frame1, text=buttons['project_new']['text'],
    command=buttons['project_new']['cmd']).pack(fill=tk.Y, side=tk.RIGHT)

tk.Button(frame1, text=buttons['project_del']['text'],
    command=buttons['project_del']['cmd']).pack(fill=tk.Y, side=tk.RIGHT)

cloudCombobox.pack(fill=tk.Y, side=tk.RIGHT)
Label(master=frame1, text="????????????: ").pack(fill=tk.Y, side=tk.RIGHT)


###########################################################
frame2 = tk.Frame(master=root,borderwidth=5)

clouds_frame = tk.Frame(master=frame2)

Label(master=frame2, text="????????????").grid(row=0, column=0)
columns = ('id')
treeCloud = ttk.Treeview(frame2, columns=columns, show="tree headings")
treeCloud.column('#0', width=150)
treeCloud.column('id', width=150)
treeCloud.heading('id', text='Id')
treeCloud.bind(" <<TreeviewSelect>>", CL_selection_e)

treeCloud.grid(row=1, column=0)


#################
resurs_frame = tk.Frame(master=frame2)


Label(master=frame2, text="????????????").grid(row=0, column=1)

columns = ('id')
treeFunc = ttk.Treeview(frame2, columns=columns, show="tree headings")

treeFunc.column('#0', width=150)
treeFunc.column('id', width=150)
treeFunc.heading('id', text='Id')


treeFuncFunc=treeFunc.insert('', 'end',tags=('Funcs'),  text='Cloud Functions')
treeFunc.item(treeFuncFunc, open=1)
treeFuncAPI=treeFunc.insert('', 'end',tags=('APIs'),  text='API Gateway')
treeFunc.item(treeFuncAPI, open=1)
treeFuncStorage=treeFunc.insert('', 'end',tags=('Storages'),  text='Object Storage')
treeFunc.item(treeFuncStorage, open=1)
treeFunc.bind(" <<TreeviewSelect>>", RE_selection_e)
treeFunc.grid(row=1, column=1)

###########################################################
info_frame = tk.Frame(master=frame2, width=300)

Label(master=frame2, text="????????").grid(row=0, column=2)

grid_info_frame = tk.Frame(master=info_frame, width=300)
text_info_frame = Text(grid_info_frame, width=37, height=10)
text_info_frame.pack(anchor=tk.N)
grid_info_frame.pack(fill=tk.X, anchor=tk.N)



#############

btn_info_frame = tk.Frame(master=info_frame)
Buttons = {}
Buttons['1'] = Button(btn_info_frame, text="?????????????? ??????????")
Buttons['2'] = Button(btn_info_frame, text="??????????.", command=sinxr_one)
Buttons['3'] = Button(btn_info_frame, text="????????????")
Buttons['4'] = Button(btn_info_frame, text="????????????")
Buttons['5'] = Button(btn_info_frame, text="????????????")
Buttons['6'] = Button(btn_info_frame, text="????????????")
Buttons['7'] = Button(btn_info_frame, text="????????????")
Buttons['8'] = Button(btn_info_frame, text="????????????")

roww = 0
coll = 0
for but in Buttons:
	Buttons[but].grid(row=roww, column=coll, padx=5 , pady=3 , sticky="nsew")
	coll= coll +1
	if coll==4:
		coll = 0
		roww = roww +1



btn_info_frame.pack(fill=tk.X)
info_frame.grid(row=1, column=2)

###########################################################
svazi_frame = tk.Frame(master=frame2)


Label(master=frame2, text="??????????").grid(row=0, column=3)

columns = ('path')
treeSvazi = ttk.Treeview(frame2, columns=columns, show="tree headings")
treeSvazi.column('#0', width=100)
treeSvazi.column('path', width=200)
treeSvazi.heading('path', text='????????')


treeSvazi.grid(row=1, column=3)

###########################################################


#########################
# clouds_frame.pack(fill=tk.X, side=tk.LEFT)
# resurs_frame.pack(fill=tk.X, side=tk.LEFT)
# info_frame.pack(fill=tk.X, side=tk.LEFT)
# svazi_frame.pack(fill=tk.X, side=tk.LEFT)
# clouds_frame.grid(row=0, column=0)
# resurs_frame.grid(row=0, column=1)
# info_frame.grid(row=0, column=2)
# svazi_frame.grid(row=0, column=3)
#################################################
frame1.pack(fill=tk.X)
frame2.pack(fill=tk.X)


def try_token():
	try:
		meta=get_yaInfo(inp_tkn.get())
		settings['token'] = inp_tkn.get()
		ya_name=meta['first_name']
		save_settings()
		alert(ya_name+', ???? ?????????????? ??????????!')
		reg.destroy()
		setup_inter()
	except Exception as e:
		print(e)
		reg.destroy()
		alert('???? ?????????? ???????????????? ??????????!')
		abraKodabra()

def abraKodabra():
	if 0:
		pass
	else:
		global reg
		reg = tk.Tk()
		reg.title('????????')
		reg.geometry('200x100')
		tk.Label(reg, text='???????????????????? ?????????????? ??????????').pack()
		global inp_tkn
		inp_tkn = tk.Entry(reg)
		inp_tkn.pack()
		tk.Button(reg, text='??????????????????', command=try_token).pack()


def inp_b_id(n=''):
	global nfegeegg
	nfegeegg=0
	if n:
		nfegeegg=n
	global reg_2
	reg_2 = tk.Tk()
	reg_2.title('???????????????? ??????????')
	reg_2.geometry('450x200')
	tk.Label(reg_2, text='???????????????????? ?????????????? ?????? ???????????? ?? ?????????????? ?????????? ???????????????? ?????????????????? ??????????:').pack()

	tk.Label(reg_2, text='(?????? ???????????? ?????????? ???????????????? ?? ??????-??????????????)').pack()
	global inp_b_id_v
	inp_b_id_v={}
	inp_b_id_v['b'] = tk.Entry(reg_2)
	inp_b_id_v['b'].pack()
	tk.Label(reg_2, text='Id ?????????? ???????????????????? ????????????????').pack()
	inp_b_id_v['aws_access_key_id'] = tk.Entry(reg_2)
	inp_b_id_v['aws_access_key_id'].pack()
	tk.Label(reg_2, text='???????? ???????????????????? ????????????????').pack()
	inp_b_id_v['aws_secret_access_key'] = tk.Entry(reg_2)
	inp_b_id_v['aws_secret_access_key'].pack()

	tk.Button(reg_2, text='??????????????????', command=sv_b_id).pack()


def sv_b_id():
	try:
		#meta=get_yaInfo(inp_b_id_v.get())
		print(nfegeegg)
		if nfegeegg:
			settings['svazi'][nfegeegg]['home_b']={}
			settings['svazi'][nfegeegg]['home_b']['b'] = inp_b_id_v['b'].get()
			settings['svazi'][nfegeegg]['home_b']['aws_access_key_id'] = inp_b_id_v['aws_access_key_id'].get()
			settings['svazi'][nfegeegg]['home_b']['aws_secret_access_key'] = inp_b_id_v['aws_secret_access_key'].get()
		else:
			settings['svazi'][settings['current_project']]['home_b']={}
			settings['svazi'][settings['current_project']]['home_b']['b'] = inp_b_id_v['b'].get()
			settings['svazi'][settings['current_project']]['home_b']['aws_access_key_id'] = inp_b_id_v['aws_access_key_id'].get()
			settings['svazi'][settings['current_project']]['home_b']['aws_secret_access_key'] = inp_b_id_v['aws_secret_access_key'].get()
		save_settings()
		reg_2.destroy()
	except Exception as e:
		print(e)
		print(traceback.format_exc())
		reg_2.destroy()
		alert('???? ?????????? ???????????????? ??????????!')
		inp_b_id()




if settings['token']:
	try:
		meta=get_yaInfo(settings['token'])

		ya_name=meta['first_name']
		#alert(ya_name+', ???? ?????????????? ??????????!')
		setup_inter()
	except BaseException as err:
		print(err)
		print(traceback.format_exc())
		alert('?????? ?????????? ???? ??????????????????!')
		alert('???????????? ?????????? ?????????????? ???????????????? ?????????????????? ????????????')
		webbrowser.open('https://oauth.yandex.ru/authorize?response_type=token&client_id=892c9dc6cb794eb9b3339b73962c5317')
		abraKodabra()
else:
	alert('???????????? ?????????? ?????????????? ???????????????? ?????????????????? ????????????')
	webbrowser.open('https://oauth.yandex.ru/authorize?response_type=token&client_id=892c9dc6cb794eb9b3339b73962c5317')
	abraKodabra()

if settings['svazi'][settings['current_project']]['home_b']:
	pass
else:
	inp_b_id()


root.mainloop()






































eng=1
