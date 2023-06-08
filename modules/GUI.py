from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox, Checkbutton, Progressbar
class window():
    def __init__(self):
        #Объекты, которые этот класс может разместить на экране:
        self.buttons = [] #кнопки
        self.texts = [] #текст
        self.combos = [] #выпадающие списки
        self.radios = [] #radioButtons
        self.entrys = [] #поле ввода текста
        self.checks = [] #checkButtons
        self.bars = [] #прогрессБар
                        #окно выбора файла(файлов)
                        #окно выбора папки
                        #окно сообщения (информации, об ошибке, и т.д.)

    def create(self, resolution=None, title=None): #метод создания окна
        try:
            self.window = Tk()
            self.window.title(title)
            self.window.geometry(resolution)
        except:
            print('Cant make main window!')

    def loop_window(self): #метод зацикливания окна
        self.window.mainloop()

    def add_button(self, text,  command, text_color=None, font=None, bck_color=None, x=None, y=None, column=0, row=0, width=None, height=None): #метод добавления на экран кнопок с параметрами text, command, x, y
        try:
            self.buttons.append(Button(self.window, text=text, font=font, fg=text_color, bg=bck_color, command=command))
            if x != None:
                self.buttons[-1].place(x=x, y=y, width=width, height=height)
            else:
                self.buttons[-1].grid(column=column, row=row)
        except:
            print('Cant add button!')

    def add_text(self, text, font=None, x=None, y=None, column=0, row=0, width=None, height=None): #метод добавления на экран текста с параметрами text, x, y
        try:
            self.texts.append(Label(self.window, text = text, font=font))
            if x != None and y != None:
                self.texts[-1].place(x=x, y=y, width=width, height=height)
            else:
                self.texts[-1].grid(column=x, row=y)
        except:
            print('Cant add text!')

    def text_configure(self, index=-1, text=''): #редактирует выведенный текст. По умолчанию изменяет последний добавленный текст
        try:
            self.texts[index].configure(text=text)
        except:
            print('Cant change text!')

    def add_combobox(self, text,  current, font=None, x=0, y=0): #метод добавления выпадающего списка
        try:
            self.combos.append(Combobox(self.window, font=font))
            self.combos[-1]['values'] = text #text - кортеж, элементы которого текст. Каждый элемент будет добавлен в поле выбора
            self.combos[-1].current(current) #какой из элементов(по индексу) будет по умолчанию)
            self.combos[-1].grid(column=x, row=y)
        except:
            print('Cant add combobox!')

    def add_checkbutton(self, text, command=False,  x=None, y=None, width=None, height=None, row=0, column=0): #метод добавления кнопки checkButton
        try:
            self.checks.append(Checkbutton(self.window, text=text, command=command))
            if x != None and y != None:
                self.checks[-1].place(x=x, y = y, width = width, height = height)
            else:
                self.checks[-1].grid(column=column, row=row)
        except:
            print('Cant add checkbox!')

    def add_radiobutton(self, text, variable=0, value=0, command=False, x=0, y=0, width=None, font=None, height=None, row=0, column=0): #добавляет radioButton
        try:
            self.radios.append(Radiobutton(self.window, text=text, variable=variable, font=font, value=value, command=command))
            if x != None and y != None:
                self.radios[-1].place(x=x, y=y, width = width, height = height)
            else:
                self.radios[-1].grid(column=column, row=row)
        except:
            print('Cant add radiobutton!')

    def add_entry(self, text='', x=None, y=None, column=0, row=0, width=None, font=None, height=None, focus=False, state=None): #добавляет окно пользовательского ввода
        try:
            self.entrys.append(Entry(self.window, width=10, text=text, font=font, state=state))
            if x != None and y != None:
                self.entrys[-1].place(x = x, y = y, width = width, height = height)
            else:
                self.entrys[-1].grid(column=column, row=row)
            if focus: #если передан параметр focus, то на поле ввода будет сфокусирован курсор(по умолчанию)
                self.entrys[-1].focus()
        except:
            print('Cant add entry!')

    def add_progressbar(self, length=None, x=None, y=None, row=0, column=0, value=0): #добавляет прогрессбар. length - длина в пикселах
        self.bars.append(Progressbar(self.window, length=length))
        self.bars[-1]['value'] = value #0-100 показывает, сколько процентов выполнено
        if x != None and y != None:
            self.bars[-1].place(x = x, y = y)
        else:
            self.bars[-1].grid(column=column, row=row)

    def filedialog(self, num=1): #окно выбора файла (возращает путь к выбранному файлу в переменной files). Если num = 1 или не передан, 
                                 #то выбрать можно только 1 файл. Елси же не 1, то выбрать можно много файлов сразу.
        try:                     #так же как и askdirectory, возвращает путь к выбранному файлу. Прим.: file = app.filedialog(num=1)
            if num == 1:
                files=filedialog.askopenfilename()
            else:
                files=filedialog.askopenfilenames()
            return files
        except:
            print('Cant open file dialog!')

    def askdirectory(self, initialdir=None): #окно выбора каталога (dir присваивает путь к выбранной папке)
                                             #initialdir - начальная директория для диалогового окна.
        try:                                 #метод возвращает путь к выбранному каталогу, поэтому присваивать переменной путь к этому каталогу
            dir = filedialog.askdirectory(initialdir=initialdir) #можно так: choosed_dir = app.askdirectory()
            return dir
        except:
            print('Cant choose directory!')

    def show_message(self, title='', text='', MsgType=None): #вызывает окно сообщения определенного типа
        try:
            if MsgType == 'info': #выводит информационное окно
                msg = messagebox.showinfo(title, text)
            elif MsgType == 'error': #выводит окно ошибки
                msg = messagebox.showerror(title, text)
            elif MsgType == 'warning': #выводит окно предупреждения
                msg = messagebox.showwarning(title, text)
            elif MsgType == 'askquestion': #выводит окно вопроса
                msg = messagebox.askquestion(title, text)
            elif MsgType == 'askyesno': #выводит окно да/нет
                msg = messagebox.askyesno(title, text)
            elif MsgType == 'askyesnocancel': #окно да/нет/отмена
                msg = messagebox.askyesnocancel(title, text) #возвращает True/False/None
            elif MsgType == 'askokcancel': #ок/отмена
                msg = messagebox.askokcancel(title, text)
            elif MsgType == 'askretrycancel': #повтор/отмена
                 msg = messagebox.askretrycancel(title, text)
            return msg #вызвращает True, если была нажата ок/да/далее, и False, если нет/отмена
        except:
            print('Cant show message!')


def clicked(): #функция обработки нажатия кнопки
    app.text_configure(text=app.combos[-1].get()) #изменяет текст в texts[index]. Текст берется из combos[-1].get()
    app.window.geometry(app.combos[-1].get()) #изменяет разрешение окна
    global bar_persent
    bar_persent += 10 #увеличивает значение прогрессбара на 10
    app.bars[-1].configure(value = + bar_persent) #перерисовывает прогрессбар
    if bar_persent > 99: #если проценты превысили 99
        bar_persent = 0  #обнуляю
bar_persent = 0 #объявляю переменную, в которой будут проценты выполнения прогрессбара

def clicked_openFilesButton():   
    fileName = app.filedialog(num=1).split('/') #создает список, последним элементом которого является выбранный файл
    app.text_configure(text=fileName[-1]) #меняю выведеный ранее текст на название выбранного файла

def clicked_askDirectoryButton():
    app.askdirectory() #открываю окно выбора каталога
    app.entrys[0].configure(state='disabled') #делаю поле ввода неактивным
    app.show_message(title='info', text='вы указали каталог', MsgType='info')
if __name__ == '__main__': #если файл был запущен напрямую, а не как модуль, то создать демонстрационное окно
    app = window() #создаю объект app класса window
    app.create(resolution = '360x360', title = 'Test window') #разрешение создаваемого окна и текст в заголовке окна
    app.add_text(text='choose resolution',font = 'gothic', x=200, y=2, height=180, width=180) #вывожу текст на экран в x,y. Font = ('times', 'arial', 'gothic' и т.д.)
    app.add_button(text='open file', command=clicked_openFilesButton,text_color='red',font='gothic', x=180, y=180, height=60, width=80) #создаю кнопку с тектом text и действием command
    app.add_button(text='Edit text', command=clicked, bck_color='yellow', row=0, column=1) #создаю кнопку с тектом text и действием command
                                                                                                    #если указан x,y, height и width, то кнопка будет создана по координатам
                                                                                                    #x и y. Если же нет, а укахан row и column, то кнопка юудет расположена в указаной строке и столбце
    app.add_combobox(text=('320x320', '480x480', '360x640'), current=0, x=0, y=3) #выпадающий список с элементами кортежа text. current - это индекс элемента, который выбран по умолчанию
                                                                                  #что бы получить выбраное значение, используй combo.get()
    app.add_checkbutton(text='EXIT',command='exit', row=0, column=4) #создаю checkButton
    app.add_checkbutton(text='name',command=None, row=0, column=5)   #command будет исполнено сразу, если поставить галочку в это поле
    app.add_radiobutton(text='choose catalog', variable='0', value=0, x=30, y=100, command=clicked_askDirectoryButton) #variable - если у обоих кнопок одинаков, то можно активировать только одну из них одновременно
                                                                                                                       #value - значение, которое будет присвоено, если активирована определенная кнопка
    app.add_radiobutton(text='2', variable='0',font='times', value=1, x=30, y=120)                                     #если передан x и y, но не переданы width, height, то ширина и высота будут определены по умолчанию
    app.add_entry(text='',focus=True, font='roman', x=0, y=190, width=100, height=30, state=None) #добавляю поле ввода текста пользователем. Focus - установка курсора в поле ввода
                                                                                      #state-состояние поля ввода. Может быть None(тогда будет активное), или 'disabled', тогда будет неактивное
    app.add_progressbar(length=200, x=10, y=150) #создаю progressBar длиной в 200 пикселей

                                #HELP
    #Что бы изменить уже созданный объект, примени .configure(param=value)
    #что бы отключить виджет Entry, можно добавить параметр state='disabled' (или изменить его с помощью configure(state='disabled'))
    #Font может применяться к любому виджету(кроме checkBox).
    app.loop_window() #зацикливаю окно 
