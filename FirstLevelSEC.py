import os
import pyautogui
import PySimpleGUI as sg
from time import sleep
from tkinter import *
from tkinter import ttk

def opcao_pingvnc():
    ip = en_ip.get().lower()
    if var1.get() == 1:
        pinger(ip)
    elif var1.get() == 2:
        vnc(ip)
    else:
        print("Erro")

def pinger(ip):
    if ip != '' and (ip[0].isnumeric() or (ip[:4] == 'sme-' and len(ip) == 10 and ip[4:].isnumeric() == True)): # NOTE: isnumeric implementado
        os.startfile('C:/Windows/system32/cmd.exe')
        sleep(1)
        pyautogui.write('ping ' + ip)
        pyautogui.press('enter')
    else:
        print ('Informe o Ip ou Sme Correto\n(XXX.XXX.XX.XX) ou (sme-XXXXXX)')

def vnc(ip):
    if ip != '' and (ip[0].isnumeric() or (ip[:4] == 'sme-' and len(ip) == 10 and ip[4:].isnumeric() == True)):
        os.startfile('G:\\\\Informatica\\Suporte\\1º Nível\\PROCEDIMENTOS - Estagiarios Novos\\FIRST LEVEL\\vncviewer.exe')
        sleep(1)
        pyautogui.write(ip)
        pyautogui.press('enter')
        senha = pyautogui.confirm(text='Solicitou a senha?', title='VNC', buttons=['Sim'])
        if senha == 'Sim':
            pyautogui.write('h4rdw4r3')
            pyautogui.press('tab')
            pyautogui.press('enter')
    else:
        print ('Informe o Ip ou Sme Correto\n(XXX.XXX.XX.XX) ou (sme-XXXXXX)')

def iniciarPrograma(x):
    os.startfile(x)

def iniciarVNC():
    ip = en_ip.get().lower()
    os.startfile('C:/Windows/system32/cmd.exe')
    sleep(1)
    pyautogui.write('sc \\\\' + ip + ' start uvnc_service')
    pyautogui.press('enter')

def pararVNC():
    ip = en_ip.get().lower()
    os.startfile('C:/Windows/system32/cmd.exe')
    sleep(1)
    pyautogui.write('sc \\\\' + ip + ' stop uvnc_service')
    pyautogui.press('enter')

def limpar():
    en_ip.delete(0,END)
    en_ip.focus_set()

janela_principal = Tk()
janela_principal.title("First level - Help Desk Software")
janela_principal.configure(background='#354f65') 
janela_principal.geometry("490x580")     

titulo = Label(janela_principal, text="First level", font=("Times New Roman", 18, "bold"), fg="white", background='#354f65')
titulo.pack(pady=10)

texto_ip= Label(text=" 🖥️IP OU SME",font=("Ariel", 13), fg="white", background='#354f65')
texto_ip.place( x=40, y=55)
en_ip = Entry(janela_principal, bd=5, font=("Calibri", 15), justify=CENTER)
en_ip.place(width=385, height=38, x=49, y=80)

janela_principal.resizable(False,False)

style = ttk.Style()
style.map("Custom.TRadiobutton", [("selected", "!focus", "foreground", "blue"),("active", "foreground", "red")])
style.configure("Custom.TRadiobutton", background="#354f65",foreground="white")

var1 = IntVar()
sel_ping=ttk.Radiobutton(janela_principal, text="Pinger", variable=var1, value=1, style="Custom.TRadiobutton")
sel_ping.place(x=49, y=140)
sel_vnc=ttk.Radiobutton(janela_principal, text="VNC", variable=var1, value=2, style="Custom.TRadiobutton")
sel_vnc.place(x=200, y=140)

bt_ok = Button(janela_principal,text='OK',command=opcao_pingvnc, bd=1,cursor="hand2", background='#b0b8be')
bt_ok.place(width=40, height=35, x=395, y=135)

bt_X = Button(janela_principal,text='X',command=limpar, bd=1,cursor="hand2", background='#b0b8be', fg="red")
bt_X.place(width=25, height=20, x=440, y=90)

bt_iniciar = Button(janela_principal,text='INICIAR VNC', bd=1,cursor="hand2", background='#b0b8be', command=iniciarVNC)
bt_iniciar.place(width=75, height=20, x=50, y=195)
bt_parar = Button(janela_principal,text='PARAR VNC', bd=1,cursor="hand2", fg="white", background='red', command=pararVNC)
bt_parar.place(width=70, height=20, x=135, y=195)

linhabranca= Label(text=' '*127,background='white')
linhabranca.place(height=2,x=48, y=250)

#=========================
texto_programas= Label(text="PROGRAMAS", fg="white", background='#354f65')
texto_programas.place( x=48, y=260)

bt_listatell = Button(janela_principal,text='LISTA\nTELEFÔNICA', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('G:/Informatica/Administrativo/Telefones/Lista/addressbook.exe'))
bt_listatell.place(width=100, height=35, x=50, y=285)

bt_activedirectory = Button(janela_principal,text='ACTIVE\nDIRECTORY', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('C:/Windows/system32/dsa.msc'))
bt_activedirectory.place(width=100, height=35, x=195, y=285)

bt_bloconotas = Button(janela_principal,text='MODELO\nRESPOSTAS', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('G:\Informatica\Administrativo\PROCEDIMENTOS - Estagiarios Novos\modelo.txt'))
bt_bloconotas.place(width=100, height=35, x=335, y=285)

#===================

texto_utilitarios= Label(text="UTILITÁRIOS", fg="white", background='#354f65')
texto_utilitarios.place( x=48, y=340)

bt_sol = Button(janela_principal,text='SOL', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('http://sol:8080/front/ticket.php'))
bt_sol.place(width=100, height=35, x=50, y=368)

bt_webemail = Button(janela_principal,text='WEB-EMAIL', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('https://webmail.sjc.sp.gov.br/rcmail/?_task=mail&_mbox=INBOX'))
bt_webemail.place(width=100, height=35, x=195, y=368)

bt_esec = Button(janela_principal,text='E-SEC', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('https://webapp.sjc.sp.gov.br:8443/esec/f?p=117:LOGIN_DESKTOP:1795173015328:::::'))
bt_esec.place(width=100, height=35, x=335, y=368)

bt_zabbix = Button(janela_principal,text='ZABBIX', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('http://smezabbix/zabbix.php?action=dashboard.view'))
bt_zabbix.place(width=100, height=35, x=50, y=410)

bt_mv = Button(janela_principal,text='MÁQUINAS\nVIRTUAIS', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('G:\\\\Informatica\\Suporte\\1º Nível\\PROCEDIMENTOS - Estagiarios Novos\\MAQUINA VIRTUAL'))
bt_mv.place(width=100, height=35, x=335, y=480)

bt_infra = Button(janela_principal,text='INFRA\nTABELA', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('https://smesjc-my.sharepoint.com/:x:/g/personal/carlos_junior_sme_sjc_sp_gov_br/EfvDjqqDrZhGqwRu1vwPkEsBIZMw2E7VDFEozvIsW5K9uQ?rtime=rIcAya912Eg'))
bt_infra.place(width=100, height=35, x=335, y=410)

#===================

texto_pastas= Label(text="PASTAS", fg="white", background='#354f65')
texto_pastas.place( x=48, y=460)

bt_programas = Button(janela_principal,text='PROGRAMAS', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('\\\\smeaps06\\Programas'))
bt_programas.place(width=100, height=35, x=50, y=480)

bt_procedimentos = Button(janela_principal,text='PROCEDIMENTOS', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('G:\\\\Informatica\\Suporte\\1º Nível\\PROCEDIMENTOS - Estagiarios Novos'))
bt_procedimentos.place(width=100, height=35, x=195, y=480)

bt_expire = Button(janela_principal,text='EXPIRE', bd=1,cursor="hand2", background='#b0b8be', command=lambda: iniciarPrograma('G:\Informatica\Administrativo\PROCEDIMENTOS - Estagiarios Novos\expire'))
bt_expire.place(width=100, height=35, x=195, y=410)

janela_principal.mainloop()