import sqlite3
import tkinter as tk
from tkinter import ttk

#описываем класс Окно
class Main_Window():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("700x550")
        self.root.title("Компьютерынй салон")
        
        #создаем меню
        self.main_menu = tk.Menu()
        
        self.file_menu = tk.Menu(tearoff=0) #подменю
        self.ref_menu = tk.Menu(tearoff=0) #подменю
        self.komp_menu = tk.Menu(tearoff=0) #подменю
        self.kompl_menu = tk.Menu(tearoff=0) #подменю
        self.otch_menu = tk.Menu(tearoff=0) #подменю
        self.help_menu = tk.Menu(tearoff=0) #подменю
        
        self.file_menu.add_command(label="Выход", command = quit)
        
        self.ref_menu.add_command(label="Проставщики", command=self.open_win_provider)
        self.ref_menu.add_command(label="Модель", command=self.open_win_model)
        self.ref_menu.add_command(label="Тип устройста", command=self.open_win_type_ystr)
        self.ref_menu.add_command(label="Производитель", command=self.open_win_proizv)

        self.komp_menu.add_command(label='Поступление Компьютеров')
        self.komp_menu.add_command(label='Список компьютеров') 
        self.komp_menu.add_command(label='Продажа компьютеров')

        self.kompl_menu.add_command(label='Поступление Комплектующих')
        self.kompl_menu.add_command(label='Список комплектующих') 
        self.kompl_menu.add_command(label='Продажа комплектующих')

        self.otch_menu.add_command(label="Отчет по поступлению")
        self.otch_menu.add_command(label="Отчет по остаткам")
        self.otch_menu.add_command(label="Отчет по продажам")
        
        self.help_menu.add_command(label="Руководство пользователя")
        self.help_menu.add_command(label="О программе")
        
        self.main_menu.add_cascade(label="Файл", menu=self.file_menu)
        self.main_menu.add_cascade(label="Справочники", menu=self.ref_menu)
        self.main_menu.add_cascade(label="Компьютеры", menu=self.komp_menu)
        self.main_menu.add_cascade(label="Комплектующие", menu=self.kompl_menu)
        self.main_menu.add_cascade(label="Отчеты", menu=self.otch_menu)
        self.main_menu.add_cascade(label="Справка", menu=self.help_menu)

        
        #привязываем меню к созданному окну
        self.root.config(menu=self.main_menu)

    def open_win_provider(self):
        '''метод Открыть окно Поставщики'''
        self.root.withdraw() #скрыть окно
        open_win_provider()
        
    def open_win_model(self):
        '''метод Открыть окно Модель'''
        self.root.withdraw() #скрыть окно
        model()
    
    def open_win_type_ystr(self):
        '''метод Открыть окно Тип устройства'''
        self.root.withdraw() #скрыть окно
        type_ystr()
    
    def open_win_proizv(self):
        '''метод Открыть окно производитель'''
        self.root.withdraw() #скрыть окно
        proizv()
    
class open_win_provider():
    '''Окно Поставщики'''
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.geometry("800x500")
        self.root2.title("Книжный магазин/Поставщики")
        self.root2.protocol('WM_DELETE_WINDOW', lambda: self.quit_win()) #перехват кнопки Х
        self.main_view = win
        self.db = db
        
        #фреймы
        self.table_frame = tk.Frame(self.root2, bg='green')
        self.add_edit_frame = tk.Frame(self.root2, bg='red')

        self.table_frame.place(relx=0, rely=0, relheight=1, relwidth=0.6)
        self.add_edit_frame.place(relx=0.6, rely=0, relheight=1, relwidth=0.4)
    
        #таблица
        self.table_pr = ttk.Treeview(self.table_frame, columns=('name_provider', 'contact_person', 'phone_number'), 
                                 height=15, show='headings')
        self.table_pr.column("name_provider", width=150, anchor=tk.NW)
        self.table_pr.column("contact_person", width=200, anchor=tk.NW)
        self.table_pr.column("phone_number", width=120, anchor=tk.CENTER)

        self.table_pr.heading("name_provider", text='Наименование')
        self.table_pr.heading("contact_person", text='Контактное лицо')
        self.table_pr.heading("phone_number", text='Номер телефона')

        #Полоса прокрутки
        self.scroll_bar = ttk.Scrollbar(self.table_frame)
        self.table_pr['yscrollcommand']=self.scroll_bar.set
        self.scroll_bar.pack(side = tk.RIGHT, fill=tk.Y)

        self.table_pr.place(relx=0, rely=0, relheight=0.9, relwidth=0.97)

        #поле ввода и кнопка для поиска
        self.esearch = ttk.Entry(self.table_frame)
        self.esearch.place(relx=0.02, rely=0.92, relheight=0.05, relwidth=0.7)

        self.butsearch = tk.Button(self.table_frame, text="Найти")
        self.butsearch.place(relx=0.74, rely=0.92, relheight=0.05, relwidth=0.2)
        
        #поля для ввода
        self.lname = tk.Label(self.add_edit_frame, text="Наименование")
        self.lname.place(relx=0.04, rely=0.02, relheight=0.05, relwidth=0.4)
        self.ename = ttk.Entry(self.add_edit_frame)
        self.ename.place(relx=0.45, rely=0.02, relheight=0.05, relwidth=0.5)

        self.lcontact = tk.Label(self.add_edit_frame, text="Контактное лицо")
        self.lcontact.place(relx=0.04, rely=0.12, relheight=0.05, relwidth=0.4)
        self.econtact = ttk.Entry(self.add_edit_frame)
        self.econtact.place(relx=0.45, rely=0.12, relheight=0.05, relwidth=0.5)

        self.lphone = tk.Label(self.add_edit_frame, text="Номер телефона")
        self.lphone.place(relx=0.04, rely=0.22, relheight=0.05, relwidth=0.4)
        
        #валидация номера телефона для поля ввода
        self.ephone = ttk.Entry(self.add_edit_frame)
        self.ephone.place(relx=0.45, rely=0.22, relheight=0.05, relwidth=0.5) 
        self.ephone.insert(0, "+375")      

        #кнопки
        self.butadd = tk.Button(self.add_edit_frame, text="Добавить запись")
        self.butadd.place(relx=0.1, rely=0.33, relheight=0.07, relwidth=0.8)

        self.butdel = tk.Button(self.add_edit_frame, text="Удалить запись")
        self.butdel.place(relx=0.1, rely=0.44, relheight=0.07, relwidth=0.8)

        self.buted = tk.Button(self.add_edit_frame, text="Редактировать запись")
        self.buted.place(relx=0.1, rely=0.55, relheight=0.07, relwidth=0.8)

        self.butsave = tk.Button(self.add_edit_frame, text="Сохранить изменения")
        self.butsave.place(relx=0.1, rely=0.66, relheight=0.07, relwidth=0.8)

        self.butquit = tk.Button(self.add_edit_frame, text="Закрыть")
        self.butquit.place(relx=0.1, rely=0.77, relheight=0.07, relwidth=0.8)
    
    def quit_win(self):
        self.root2.destroy()
        self.main_view.root.deiconify()

class model(open_win_provider):
    '''Окно модель'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root2.title("Компьютерный салон/модель")

        #таблица
        self.table_pr = ttk.Treeview(self.table_frame, columns=('name_model', 'address', 'phone_number'), 
                                 height=15, show='headings')
        self.table_pr.column("name_model", width=150, anchor=tk.NW)
        self.table_pr.column("address", width=200, anchor=tk.NW)
        self.table_pr.column("phone_number", width=120, anchor=tk.CENTER)

        self.table_pr.heading("name_model", text='Наименование')
        self.table_pr.heading("address", text='Адрес')
        self.table_pr.heading("phone_number", text='Номер телефона')

        self.table_pr.place(relx=0, rely=0, relheight=0.9, relwidth=0.97)

        #обновленные поля для ввода
        self.lcontact = tk.Label(self.add_edit_frame, text="Адрес")
        self.lcontact.place(relx=0.04, rely=0.12, relheight=0.05, relwidth=0.4)
        self.econtact = ttk.Entry(self.add_edit_frame)
        self.econtact.place(relx=0.45, rely=0.12, relheight=0.05, relwidth=0.5)

class proizv():
    '''Окно Места производитель'''
    def __init__(self):
        self.root2 = tk.Tk()
        self.root2.geometry("800x500")
        self.root2.title("Компьютерный салон/Производитель")
        self.root2.protocol('WM_DELETE_WINDOW', lambda: self.quit_win()) #перехват кнопки Х
        self.main_view = win
        self.db = db
        
        #фреймы
        self.table_frame = tk.Frame(self.root2, bg='green')
        self.add_edit_frame = tk.Frame(self.root2, bg='red')

        self.table_frame.place(relx=0, rely=0, relheight=1, relwidth=0.6)
        self.add_edit_frame.place(relx=0.6, rely=0, relheight=1, relwidth=0.4)
    
        #таблица
        self.table_pr = ttk.Treeview(self.table_frame, columns=('name_place'), 
                                 height=15, show='headings')
        self.table_pr.column("name_place", width=150, anchor=tk.NW)
        self.table_pr.heading("name_place", text='Наименование')

        #Полоса прокрутки
        self.scroll_bar = ttk.Scrollbar(self.table_frame, command=self.table_pr.yview)
        self.table_pr['yscrollcommand']=self.scroll_bar.set
        self.scroll_bar.pack(side = tk.RIGHT, fill=tk.Y)
        
        self.table_pr.place(relx=0, rely=0, relheight=0.9, relwidth=0.97)

        #поле ввода и кнопка для поиска
        self.esearch = ttk.Entry(self.table_frame)
        self.esearch.place(relx=0.02, rely=0.92, relheight=0.05, relwidth=0.7)

        self.butsearch = tk.Button(self.table_frame, text="Найти")
        self.butsearch.place(relx=0.74, rely=0.92, relheight=0.05, relwidth=0.2)

        #поля для ввода
        self.lname = tk.Label(self.add_edit_frame, text="Наименование")
        self.lname.place(relx=0.04, rely=0.02, relheight=0.05, relwidth=0.4)
        self.ename = ttk.Entry(self.add_edit_frame)
        self.ename.place(relx=0.45, rely=0.02, relheight=0.05, relwidth=0.5)

        #кнопки
        self.butadd = tk.Button(self.add_edit_frame, text="Добавить запись")
        self.butadd.place(relx=0.1, rely=0.33, relheight=0.07, relwidth=0.8)

        self.butdel = tk.Button(self.add_edit_frame, text="Удалить запись")
        self.butdel.place(relx=0.1, rely=0.44, relheight=0.07, relwidth=0.8)

        self.buted = tk.Button(self.add_edit_frame, text="Редактировать запись")
        self.buted.place(relx=0.1, rely=0.55, relheight=0.07, relwidth=0.8)

        self.butsave = tk.Button(self.add_edit_frame, text="Сохранить изменения")
        self.butsave.place(relx=0.1, rely=0.66, relheight=0.07, relwidth=0.8)

        self.butquit = tk.Button(self.add_edit_frame, text="Закрыть")
        self.butquit.place(relx=0.1, rely=0.77, relheight=0.07, relwidth=0.8)
        
    def quit_win(self):
        self.root2.destroy()
        self.main_view.root.deiconify()

class type_ystr(open_win_provider):
    '''Окно Тип устройства '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.root2.title("Компьютерный салон/Тип устройства")

        #таблица
        self.table_pr = ttk.Treeview(self.table_frame, columns=('name_model', 'address', 'phone_number'), 
                                 height=15, show='headings')
        self.table_pr.column("name_model", width=150, anchor=tk.NW)
        self.table_pr.column("address", width=200, anchor=tk.NW)
        self.table_pr.column("phone_number", width=120, anchor=tk.CENTER)

        self.table_pr.heading("name_model", text='Наименование')
        self.table_pr.heading("address", text='Адрес')
        self.table_pr.heading("phone_number", text='Номер телефона')

        self.table_pr.place(relx=0, rely=0, relheight=0.9, relwidth=0.97)

        #обновленные поля для ввода
        self.lcontact = tk.Label(self.add_edit_frame, text="Адрес")
        self.lcontact.place(relx=0.04, rely=0.12, relheight=0.05, relwidth=0.4)
        self.econtact = ttk.Entry(self.add_edit_frame)
        self.econtact.place(relx=0.45, rely=0.12, relheight=0.05, relwidth=0.5)
        
class DB:
    def __init__(self):
        self.conn = sqlite3.connect('salon.db') #установили связь с БД (или создали если ее нет)
        self.c = self.conn.cursor() #создали курсор
        #таблица Компьютеры
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "computer" (
                       "id_computer" INTEGER NOT NULL,
                        "ID_proiz" TEXT NOT NULL,
                        "count" TEXT NOT NULL,
                        PRIMARY KEY("id_computer" AUTOINCREMENT)
                        )'''
        )
        #таблица Комплектующие
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "Komplect" (
                        "id_Komplect" INTEGER NOT NULL,
                        "Name" TEXT NOT NULL,
                        "ID_model" INTEGER NOT NULL,
                        "ID_Proiz" INTEGER NOT NULL,
                        "ID_type" INTEGER NOT NULL,
                        "Count" INTEGER NOT NULL,
                        PRIMARY KEY("id_Komplect" AUTOINCREMENT)
                        )'''
            )
        # таблица Производители
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "Proiz" (
                        "ID_proiz" INTEGER NOT NULL,
                        "NumProiz" TEXT NOT NULL,
                        "TypeProiz" TEXT,
                        "Adress" TEXT,
                        PRIMARY KEY("ID_proiz" AUTOINCREMENT)
                        )'''
            )
        #таблица Поступление компьютеров
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "PostyplenieKomputer" (
                        "id_Postypl" INTEGER NOT NULL,
                        "ID_kompyter" INTEGER NOT NULL,
                        "Date_Postypl" TEXT NOT NULL,
                        "Num" INTEGER,
                        "ID_post" INTEGER NOT NULL,
                        PRIMARY KEY("id_Postypl" AUTOINCREMENT)
                        )''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "PostyplenieKomputer" (
                        "id_Postypl" INTEGER NOT NULL,
                        "ID_kompl" INTEGER NOT NULL,
                        "Date_Postypl" TEXT NOT NULL,
                        "Num" INTEGER,
                        "ID_post" INTEGER NOT NULL,
                        PRIMARY KEY("id_Postypl" AUTOINCREMENT)
                        )''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "TypeKompl" (
                        "id_Type" INTEGER NOT NULL,
                        "NameType" TEXT NOT NULL,
                        PRIMARY KEY("id_Type" AUTOINCREMENT)
                        )''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "Model" (
                        "id_model" INTEGER NOT NULL,
                        "NameModel" TEXT NOT NULL,
                        PRIMARY KEY("id_Model" AUTOINCREMENT)
                        )''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "Post" (
                        "id_Post" INTEGER NOT NULL,
                        "NamePost" TEXT NOT NULL,
                        PRIMARY KEY("id_Post" AUTOINCREMENT)
                        )''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS "PostyplenieKomputer" (
                        "id_Sell" INTEGER NOT NULL,
                        "Date" Text NOT NULL,
                        "ID_komputer" INTEGER NOT NULL,
                        "Count" TEXT,
                        "Kol-vo" INTEGER NOT NULL,
                        "Summ" TEXT NOT NULL,
                        PRIMARY KEY("id_Sell" AUTOINCREMENT)
                        )''')
        self.conn.commit()
db = DB()
#создаем окно
win = Main_Window()
#запускаем окно
win.root.mainloop()
