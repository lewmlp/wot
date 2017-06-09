import requests
from tkinter import *
from bs4 import BeautifulSoup
import webbrowser
import tkinter.messagebox
import wargaming
import os

root = Tk()

stat = ''
rait = ''
acc_id = ''
my_acc_id = ''
token = ''
isaut = False
i=0
class Stat_but:
    def __init__(self):
        self.butauth = Button(root, text='Авторизироваться')
        self.butauth.bind("<Button-1>", self.auth)
        self.butauth.pack()
        self.butauth1 = Button(root, text='Персональные данные')
        self.butauth1.bind("<Button-1>", self.pers_stat)
        self.butauth1.pack()
        self.butauth2 = Button(root, text='Персональная статистика')
        self.butauth2.bind("<Button-1>", self.pers_dan)
        self.butauth2.pack()
        self.butauth3 = Button(root, text='Персональный рейтинг')
        self.butauth3.bind("<Button-1>", self.pers_rait)
        self.butauth3.pack()

        self.labs = Label(root,text="   ")
        self.labs.pack()
        self.lab =Label(root, text="Введите никнейм игрока:", font="Arial 10")
        self.lab.pack()
        self.ent1 = Entry(root, width=20)
        self.ent1.pack()
        self.button1 = Button(root, text='OK', width=25)
        self.button1.bind("<Button-1>", self.get_id)
        self.button1.pack()
        self.but = Button(root)
        self.but["text"] = "Посмотреть статистику игрока"
        self.but.bind("<Button-1>", self.statistics)
        self.but.pack()
        self.but1 = Button(root)
        self.but1["text"] = "Посмотреть рейтинг игрока"
        self.but1.bind("<Button-1>", self.raiting)
        self.but1.pack()
        self.labs = Label(root,text="   ")
        self.labs.pack()

        self.but2 = Button(root)
        self.but2["text"] = "Статистика серверов"
        self.but2.bind("<Button-1>", self.get_servers)
        self.but2.pack()
        self.but3 = Button(root)
        self.but3["text"] = "Посмотреть новости проекта"
        self.but3.bind("<Button-1>", self.get_news)
        self.but3.pack()
        self.labs11 = Label(root, text="   ")
        self.labs11.pack()
        self.labs12 = Label(root, text="Введите путь до Wot!")
        self.labs12.pack()
        self.labs13 = Label(root, text="По умолчанию")
        self.labs13.pack()
        self.labs14 = Label(root, text="C:\Games\World_of_Tanks\WoTLauncher.exe")
        self.labs14.pack()
        self.entway = Entry(root)
        self.entway.pack()
        self.but51 = Button(root)
        self.but51["text"] = "ОК"
        self.but51.bind("<Button-1>", self.get_way)
        self.but51.pack()
        self.labs121 = Label(root, text="   ")
        self.labs121.pack()
        self.but5 = Button(root)
        self.but5["text"] = "ИГРАТЬ!"
        self.but5.bind("<Button-1>", self.run_wot)
        self.but5.pack()
        self.way = 'C:\Games\World_of_Tanks\WoTLauncher.exe'

    def run_wot(self, event):
        try:
            os.startfile(self.way)
        except:
            tkinter.messagebox.showinfo("Ошибка!", "Введите корректный путь")

    def get_way(self, event):
        ways = self.entway.get()
        print(ways)
        self.way = ways

    def auth(self,event):
        query4 = "https://api.worldoftanks.ru/wot/auth/login/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14"
        webbrowser.open_new_tab(query4)
        self.aut = Tk()
        self.aut.title('Авторизация')
        lab = Label(self.aut, text="Введите URL:", font="Arial 10")
        lab.pack()
        self.entURL = Entry(self.aut, width=20)
        self.entURL.pack()
        button1 = Button(self.aut, text='OK', width=25)
        button1.bind("<Button-1>", self.get_token)
        button1.pack()
        self.aut.mainloop()

    def get_token(self,event):
        def Error2():
            tkinter.messagebox.showinfo("Ошибка!", "Введите корректный URL")
        global token
        global isaut
        global my_acc_id
        resp = self.entURL.get()
        bib = resp.split('&')
        if 'access_token' not in bib[2]:
            Error2()
            return()
        token = bib[2][13:]
        my_acc_id = bib[4][11:]
        isaut = True
        lab = Label(root, text="Вы авторизовались!", font="Arial 10")
        lab.pack()

    def pers_stat(self, event):
        global isaut
        global token
        global my_acc_id
        if isaut is False:
            tkinter.messagebox.showinfo("Ошибка!", "Авторизируйтесь!")
            return()
        params3 = {'token': token, 'my_id': my_acc_id}
        query5 = "https://api.worldoftanks.ru/wot/account/info/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14&access_token={token}&account_id={my_id}".format(**params3)
        personal = (requests.get(query5)).json()['data'][my_acc_id]
        persstat = Tk()
        persstat.title('Персональные данные')
        lab0 = Label(persstat, text = 'Никнейм:')
        lab0.grid(row = 0, column=0)
        lab00 = Label(persstat, text = personal['nickname'])
        lab00.grid(row = 0, column = 1)
        lab1 = Label(persstat, text='Количество кредитов:')
        lab1.grid(row=1, column=0)
        lab11 = Label(persstat, text=personal['private']['credits'])
        lab11.grid(row=1, column=1)
        lab2 = Label(persstat, text='Количество золота:')
        lab2.grid(row=2, column=0)
        lab22 = Label(persstat, text=personal['private']['gold'])
        lab22.grid(row=2, column=1)
        lab3 = Label(persstat, text='Количество свободного опыта:')
        lab3.grid(row=3, column=0)
        lab33 = Label(persstat, text=personal['private']['free_xp'])
        lab33.grid(row=3, column=1)
        lab4 = Label(persstat, text='Наличие премиум-аккаунта:')
        lab4.grid(row=4, column=0)
        lab44 = Label(persstat, text=personal['private']['is_premium'])
        lab44.grid(row=4, column=1)
        persstat.mainloop()

    def pers_dan(self, event):
        global isaut
        global token
        global my_acc_id
        if isaut is False:
            tkinter.messagebox.showinfo("Ошибка!", "Авторизируйтесь!")
            return ()
        params4 = {'token': token, 'my_id': my_acc_id}
        query6 = "https://api.worldoftanks.ru/wot/account/info/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14&access_token={token}&account_id={my_id}".format(
            **params4)
        stat = (requests.get(query6)).json()
        stats = Tk()
        stats.title('Статистика')
        lab0 = Label(stats, text="Никнейм: ")
        lab0.grid(row=0, column=0)
        lab00 = Label(stats, text=stat['data'][my_acc_id]['nickname'])
        lab00.grid(row=0, column=1)
        lab1 = Label(stats, text="Личный рейтинг: ")
        lab1.grid(row=1, column=0)
        lab11 = Label(stats, text=stat['data'][my_acc_id]['global_rating'])
        lab11.grid(row=1, column=1)
        lab2 = Label(stats, text="Клан: ")
        lab2.grid(row=2, column=0)
        lab22 = Label(stats, text=stat['data'][my_acc_id]['clan_id'])
        lab22.grid(row=2, column=1)
        lab3 = Label(stats, text="Количество боёв: ")
        lab3.grid(row=3, column=0)
        lab33 = Label(stats, text=stat['data'][my_acc_id]['statistics']['all']['battles'])
        lab33.grid(row=3, column=1)
        lab4 = Label(stats, text="Средний опыт за бой: ")
        lab4.grid(row=4, column=0)
        lab44 = Label(stats, text=stat['data'][my_acc_id]['statistics']['all']['battle_avg_xp'])
        lab44.grid(row=4, column=1)
        lab5 = Label(stats, text="Произведено выстрелов: ")
        lab5.grid(row=5, column=0)
        lab55 = Label(stats, text=stat['data'][my_acc_id]['statistics']['all']['shots'])
        lab55.grid(row=5, column=1)
        lab6 = Label(stats, text="Уничтожено техники: ")
        lab6.grid(row=6, column=0)
        lab66 = Label(stats, text=stat['data'][my_acc_id]['statistics']['all']['frags'])
        lab66.grid(row=6, column=1)
        lab7 = Label(stats, text="Максимальный урон за бой: ")
        lab7.grid(row=7, column=0)
        lab77 = Label(stats, text=stat['data'][my_acc_id]['statistics']['all']['max_damage'])
        lab77.grid(row=7, column=1)
        lab8 = Label(stats, text="Максимум уничтожено за бой: ")
        lab8.grid(row=8, column=0)
        lab88 = Label(stats, text=stat['data'][my_acc_id]['statistics']['all']['max_frags'])
        lab88.grid(row=8, column=1)
        lab9 = Label(stats, text="Максимальный опыт за бой: ")
        lab9.grid(row=9, column=0)
        lab99 = Label(stats, text=stat['data'][my_acc_id]['statistics']['all']['max_xp'])
        lab99.grid(row=9, column=1)
        stats.mainloop()

    def pers_rait(self, event):
        global isaut
        global token
        global my_acc_id
        if isaut is False:
            tkinter.messagebox.showinfo("Ошибка!", "Авторизируйтесь!")
            return ()
        params6 = {'acc_id': my_acc_id}
        query7 = "https://api.worldoftanks.ru/wot/ratings/accounts/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14&account_id={acc_id}&type=all".format(
            **params6)
        rait = (requests.get(query7)).json()
        raits = Tk()
        raits.title('Рейтинг')
        lab0 = Label(raits, text="Место в рейтинге по количеству проведённых боёв: ")
        lab0.grid(row=0, column=0)
        lab00 = Label(raits, text=rait['data'][my_acc_id]['battles_count']['rank'])
        lab00.grid(row=1, column=0)
        lab1 = Label(raits, text="Место в рейтинге по количеству нанесённого урона: ")
        lab1.grid(row=2, column=0)
        lab11 = Label(raits, text=rait['data'][my_acc_id]['damage_dealt']['rank'])
        lab11.grid(row=3, column=0)
        lab2 = Label(raits, text="Место в рейтинге по количеству уничтоженной техники: ")
        lab2.grid(row=4, column=0)
        lab22 = Label(raits, text=rait['data'][my_acc_id]['frags_count']['rank'])
        lab22.grid(row=5, column=0)
        lab3 = Label(raits, text="Место в рейтинге по личному рейтингу: ")
        lab3.grid(row=6, column=0)
        lab33 = Label(raits, text=rait['data'][my_acc_id]['global_rating']['rank'])
        lab33.grid(row=7, column=0)
        lab4 = Label(raits, text="Место в рейтинге по седнему опыту за бой: ")
        lab4.grid(row=8, column=0)
        lab44 = Label(raits, text=rait['data'][my_acc_id]['xp_avg']['rank'])
        lab44.grid(row=9, column=0)
        raits.mainloop()


    def get_id(self, event):
        global stat
        global acc_id
        global rait
        account = self.ent1.get()
        params1 = {'acc': account}
        query1 = "https://api.worldoftanks.ru/wot/account/list/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14&search={acc}&limit=1".format(
            **params1)
        try:
            acc_id = (requests.get(query1)).json()['data'][0]['account_id']
        except:
            tkinter.messagebox.showinfo("Ошибка!", "Введите корректный никнейм!")
            return()
        params2 = {'acc_id': acc_id}
        query2 = "https://api.worldoftanks.ru/wot/account/info/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14&account_id={acc_id}".format(
            **params2)
        stat = (requests.get(query2)).json()

        query3 = "https://api.worldoftanks.ru/wot/ratings/accounts/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14&account_id={acc_id}&type=all".format(**params2)
        rait = (requests.get(query3)).json()
        print(rait)

    def statistics(self, event):
        global stat
        global acc_id
        try:
            warrior = stat['data'][str(acc_id)]['nickname']
        except:
            tkinter.messagebox.showinfo("Ошибка!", "Введите корректный никнейм!")
            return()

        stats = Tk()
        stats.title('Статистика')
        lab0 = Label(stats, text="Никнейм: ")
        lab0.grid(row=0,column = 0)
        lab00 = Label(stats,text = stat['data'][str(acc_id)]['nickname'])
        lab00.grid(row=0, column = 1)
        lab1 = Label(stats, text = "Личный рейтинг: ")
        lab1.grid(row=1,column=0)
        lab11 = Label(stats, text = stat['data'][str(acc_id)]['global_rating'])
        lab11.grid(row=1,column=1)
        lab2 = Label(stats, text="Клан: ")
        lab2.grid(row=2, column=0)
        lab22 = Label(stats, text=stat['data'][str(acc_id)]['clan_id'])
        lab22.grid(row=2, column=1)
        lab3 = Label(stats, text="Количество боёв: ")
        lab3.grid(row=3, column=0)
        lab33 = Label(stats, text=stat['data'][str(acc_id)]['statistics']['all']['battles'])
        lab33.grid(row=3, column=1)
        lab4 = Label(stats, text="Средний опыт за бой: ")
        lab4.grid(row=4, column=0)
        lab44 = Label(stats, text=stat['data'][str(acc_id)]['statistics']['all']['battle_avg_xp'])
        lab44.grid(row=4, column=1)
        lab5 = Label(stats, text="Произведено выстрелов: ")
        lab5.grid(row=5, column=0)
        lab55 = Label(stats, text=stat['data'][str(acc_id)]['statistics']['all']['shots'])
        lab55.grid(row=5, column=1)
        lab6 = Label(stats, text="Уничтожено техники: ")
        lab6.grid(row=6, column=0)
        lab66 = Label(stats, text=stat['data'][str(acc_id)]['statistics']['all']['frags'])
        lab66.grid(row=6, column=1)
        lab7 = Label(stats, text="Максимальный урон за бой: ")
        lab7.grid(row=7, column=0)
        lab77 = Label(stats, text=stat['data'][str(acc_id)]['statistics']['all']['max_damage'])
        lab77.grid(row=7, column=1)
        lab8 = Label(stats, text="Максимум уничтожено за бой: ")
        lab8.grid(row=8, column=0)
        lab88 = Label(stats, text=stat['data'][str(acc_id)]['statistics']['all']['max_frags'])
        lab88.grid(row=8, column=1)
        lab9 = Label(stats, text="Максимальный опыт за бой: ")
        lab9.grid(row=9, column=0)
        lab99 = Label(stats, text=stat['data'][str(acc_id)]['statistics']['all']['max_xp'])
        lab99.grid(row=9, column=1)
        stats.mainloop()

    def raiting(self,event):
        global acc_id
        global rait
        try:
            warrior = rait['data'][str(acc_id)]['battles_count']['rank']
        except:
            tkinter.messagebox.showinfo("Ошибка!", "Введите корректный никнейм!")
            return()
        raits = Tk()
        raits.title('Рейтинг')
        lab0 = Label(raits, text="Место в рейтинге по количеству проведённых боёв: ")
        lab0.grid(row=0, column=0)
        lab00 = Label(raits, text=rait['data'][str(acc_id)]['battles_count']['rank'])
        lab00.grid(row=1, column=0)
        lab1 = Label(raits, text="Место в рейтинге по количеству нанесённого урона: ")
        lab1.grid(row=2, column=0)
        lab11 = Label(raits, text=rait['data'][str(acc_id)]['damage_dealt']['rank'])
        lab11.grid(row=3, column=0)
        lab2 = Label(raits, text="Место в рейтинге по количеству уничтоженной техники: ")
        lab2.grid(row=4, column=0)
        lab22 = Label(raits, text=rait['data'][str(acc_id)]['frags_count']['rank'])
        lab22.grid(row=5, column=0)
        lab3 = Label(raits, text="Место в рейтинге по личному рейтингу: ")
        lab3.grid(row=6, column=0)
        lab33 = Label(raits, text=rait['data'][str(acc_id)]['global_rating']['rank'])
        lab33.grid(row=7, column=0)
        lab4 = Label(raits, text="Место в рейтинге по седнему опыту за бой: ")
        lab4.grid(row=8, column=0)
        lab44 = Label(raits, text=rait['data'][str(acc_id)]['xp_avg']['rank'])
        lab44.grid(row=9, column=0)
        raits.mainloop()

    def get_news(self,event):
        def go_url0(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[0]).split('">'))[1])[33:])
        def go_url1(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[1]).split('">'))[1])[33:])
        def go_url2(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[2]).split('">'))[1])[33:])
        def go_url3(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[3]).split('">'))[1])[33:])
        def go_url4(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[4]).split('">'))[1])[33:])
        def go_url5(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[5]).split('">'))[1])[33:])
        def go_url6(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[6]).split('">'))[1])[33:])
        def go_url7(event):
            webbrowser.open('https://worldoftanks.ru/' + ((str(tittle[7]).split('">'))[1])[33:])
        resp = requests.get('https://worldoftanks.ru/')
        web_page = resp.text
        soup = BeautifulSoup(web_page, "html5lib")
        tittle = soup.find_all('h5', attrs={'class':'b-imgblock_headerlink '})
        news = soup.find_all('p', attrs={'class':'b-imgblock_text'})
        nw = Tk()
        nw.title('Новости')
        print(((str(tittle[0]).split('">'))))
        i = 0
        p = -1
        while i != 8:
            lab = Label(nw, text=((str(tittle[i]).split('">'))[2])[:-9], font='arial 14')
            lab.grid(row=p+1, column = 0)
            lab0 = Label(nw, text=(str(news[i]))[27:-4])
            lab0.grid(row=p+2, column=0)
            i+=1
            p+=2
        but0 = Button(nw, text='Click!')
        but0.bind("<Button-1>", go_url0)
        but0.grid(row=0, column=1)
        but1 = Button(nw, text='Click!')
        but1.bind("<Button-1>", go_url1)
        but1.grid(row=2, column=1)
        but2 = Button(nw, text='Click!')
        but2.bind("<Button-1>", go_url2)
        but2.grid(row=4, column=1)
        but3 = Button(nw, text='Click!')
        but3.bind("<Button-1>", go_url3)
        but3.grid(row=6, column=1)
        but4 = Button(nw, text='Click!')
        but4.bind("<Button-1>", go_url4)
        but4.grid(row=8, column=1)
        but5 = Button(nw, text='Click!')
        but5.bind("<Button-1>", go_url5)
        but5.grid(row=10, column=1)
        but6 = Button(nw, text='Click!')
        but6.bind("<Button-1>", go_url6)
        but6.grid(row=12, column=1)
        but7 = Button(nw, text='Click!')
        but7.bind("<Button-1>", go_url7)
        but7.grid(row=14, column=1)
        nw.mainloop()

    def get_prem(self, event):
        resp = requests.get('https://ru.wargaming.net/shop/wot/main/')
        web_page = resp.text
        soup = BeautifulSoup(web_page, "html5lib")
        tittle = soup.find_all('div', attrs={'class': 'item_content'})
        price = soup.find_all('span', attrs={'class':'js-price'})
        url = soup.find_all('a', attrs={'class':'item_link'})
        print(tittle[0])
        print(price)
        print(url)

    def get_servers(self, event):
        query = 'https://api.worldoftanks.ru/wgn/servers/info/?application_id=4cdccfaceb27d35b820f9b7f92c9ac14&game=wot'
        resp = (requests.get(query)).json()['data']['wot']
        serv = Tk()
        serv.title('Серверы')
        i = 0
        for r in resp:
            lab = Label(serv, text='Сервер ' + r['server'] + '. Количество игроков: ' + str(r['players_online']))
            lab.grid(row=i, column = 0)
            i+=1
        serv.mainloop()
        print(resp)

stat_but = Stat_but()
root.title('World of Tanks')
root.mainloop()