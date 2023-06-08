from modules import GUI
import time
import threading

def Decrypto(x, y, step):                                  #ФУНКЦИЯ ШИФРОВАНИЯ
    global binList                                       #
    for i in range (x, y, step):                         #ПАРАМЕТРЫ
        thirdByte = ''
        firstByte = binList[i]
        secondByte = binList[i+step]
        if len(firstByte) > 3 and len(secondByte) > 3:
            for n in range(0, 3):
                if firstByte[n] == secondByte[n]:
                    thirdByte += '1'
                else:
                    thirdByte += '0'
            thirdByte += firstByte[3:]
        else:
            continue
        binList[i] = thirdByte
def startDecrypto(fileName, key):
    global binList
    binList = []                                            #список, содержащий бинарные коды символов из файла
#________________________________________________________________________________
    binKey = ('')                                 #ключ шифрования в двоичном виде
    binKeyInvert = ('')                           #отраженный двоичный код ключа шифрования
#________________________________________________________________________________
    start = time.time()
#________________________________________________________________________________
    for i in range (0, len(key)):                 #
        binKey += (bin(ord(key[i]))[2:])          # ПЕРЕВОЖУ КЛЮЧ ШИФРОВАНИЯ В ДВОИЧНЫЙ ВИД
    for i in range (0, len(binKey)):              #
        binKeyInvert += binKey[len(binKey)-i-1]   # ОТРАЖАЮ ПОЛУЧЕННЫЙ ДВОИЧНЫЙ КЛЮЧ
#________________________________________________________________________________
    listData = list(open(fileName, 'rb').read())       #               
    for i in listData:
        binList.append(bin(i)[2:])                                      
#________________________________________________________________________________
    for i in range (0, len(binKeyInvert)):
        persents = (100 * (i + 1) // len(binKey))
        if binKeyInvert[i] == '0':
            Decrypto(0, len(binList)-1, 1)
        else:
            Decrypto(len(binList)-1, 0, -1)
        app.bars[0].configure(value = persents)
        print(str(persents)+'% выполнено')       
        if persents == 100:
            app.add_text(text='ГОТОВО!', x=290, y=110)
#________________________________________________________________________________
    for i in range (0, len(listData)):        #
        listData[i] = int(binList[i] ,2)      #
#________________________________________________________________________________
    open(fileName, 'wb').write(bytes(listData)) #ЗАПИСЫВАЮ В ФАЙЛ ОБРАБОТАННЫЕ ДАННЫЕ В ВИДЕ БАЙТОВ
#________________________________________________________________________________
    finish = time.time()
    try:
        logName = str('decrypt - ' + time.asctime()[:10])
        F = open('logs/' + logName + '.txt', 'a')                          
        F.write('Дата расшифровывания: ' + (str(time.asctime()))  + '\n')     #ЗАПИСЫВАЮ В ФАЙЛ ЛОГИ
        F.write('Файл:            ' + fileName + '\n')
        F.write('Длина ключа:     ' + str(len(binKey)) + ' бит' + '\n')
        if len(binList) > 1023 and len(binList) < 1024000 :
            F.write('Обьем файла:     ' + str(len(binList) // 1024) + '.' + str(len(binList) % 1023 // 100) + ' Кбайт' + '\n')
        elif len(binList) > 1024000 :
            F.write('Обьем файла:     ' + str(len(binList) // 1024 // 1024) + '.' + str(len(binList) % 1024 % 1024 // 100) + ' Мбайт' + '\n')
        else:
            F.write('Обьем файла:     ' + str(len(binList)) + ' байт' + '\n')
        F.write('Расшифровано за: ' + (str(finish - start)[:4]) + ' сек.' + '\n')
        F.write('______________________________________' + '\n')
        F.close()
    except:
        print('Не получилось записать лог!')
def crypto(x, y, step):                                  #ФУНКЦИЯ ШИФРОВАНИЯ
    global binList                                       #
    for i in range (x, y, step):                         #ПАРАМЕТРЫ
        thirdByte = ''
        firstByte = binList[i]
        secondByte = binList[i+step]
        if len(firstByte) > 3 and len(secondByte) > 3:
            for n in range(0, 3):
                if firstByte[n] == secondByte[n]:
                    thirdByte += '1'
                else:
                    thirdByte += '0'
            thirdByte += secondByte[3:]
        else:
            continue
        binList[i+step] = thirdByte
def startCrypto(fileName, key):
    global binList
#________________________________________________________________________________
    binList = []                                             #список, содержащий бинарные коды символов из файла
#________________________________________________________________________________
    binKey = ('')                                 #ключ шифрования в двоичном виде
    for i in range (0, len(key)):                 #
        binKey += (bin(ord(key[i]))[2:])          # ПЕРЕВОЖУ КЛЮЧ ШИФРОВАНИЯ В ДВОИЧНЫЙ ВИД
#________________________________________________________________________________
    start = time.time()
#________________________________________________________________________________
    try:
        listData = list(open(fileName, 'rb').read())       #                                                     
        for i in listData:
            binList.append(bin(i)[2:])
    except:
        print('Файл '+fileName+' не найден!')
#________________________________________________________________________________
    for i in range (0, len(binKey)):
        persents = (100 * (i + 1) // len(binKey))
        if binKey[i] == '1':            
            crypto(0, len(binList) - 1, 1)
        else:
            crypto(len(binList) - 1, 0, -1)

        app.bars[0].configure(value = persents)

        print(str(persents)+'% выполнено')
        
        if persents == 100:
            app.add_text(text='ГОТОВО!', x=290, y=110)
#________________________________________________________________________________
    try:
        for i in range (0, len(listData)):        #
            listData[i] = int(binList[i] ,2)      #
    except:
        print('Ошибка! Файл не найден!')
#________________________________________________________________________________
    try:
        open(fileName, 'wb').write(bytes(listData)) #ЗАПИСЫВАЮ В ФАЙЛ ОБРАБОТАННЫЕ ДАННЫЕ В ВИДЕ БАЙТОВ
    except:
       print('Файл '+fileName+' не найден!')
#________________________________________________________________________________
    finish = time.time()
    logName = str('crypt - ' + time.asctime()[:10])
    try:
        F = open('logs/' + logName + '.txt', 'a')                             #ЗАПИСЫВАЮ В ФАЙЛ ЛОГИ
        F.write('Дата шифрования: ' + (str(time.asctime()))  + '\n')
        F.write('Файл:            ' + fileName + '\n')
        F.write('Длина ключа:     ' + str(len(binKey)) + ' бит' + '\n')
        if len(binList) > 1023 and len(binList) < 1024000 :
            F.write('Обьем файла:     ' + str(len(binList) // 1024) + '.' + str(len(binList) % 1023 // 100) + ' Кбайт' + '\n')
        elif len(binList) > 1024000 :
            F.write('Обьем файла:     ' + str(len(binList) // 1024 // 1024) + '.' + str(len(binList) % 1024 % 1024 // 100) + ' Мбайт' + '\n')
        else:
            F.write('Обьем файла:     ' + str(len(binList)) + ' байт' + '\n')
        F.write('Зашифровано за:  ' + (str(finish - start)[:4]) + ' сек.' + '\n')
        F.write('______________________________________' + '\n')
        F.close()
    except:
        print('Не получилось записать лог!')
file = None
def choose_file():
    global file
    file = GUI.filedialog.askopenfilename()
    fileName = file.split('/')
    app.text_configure(index=0, text='Файл: '+fileName[-1])
    return file
def get_cryptoKey():
    if file == None:
        app.show_message(title='ВНИМАНИЕ!', text='Вы не выбрали файл!', MsgType='warning')
    key = app.entrys[-1].get()
    if len(key)>0:
        if file!=None:
            app.bars[0].configure(value = 0)
            if radio == 1:
                t = threading.Thread(target=startCrypto, args=(file, key,)) #запускаю процесс шифрования в отдельном потоке
                t.daemon = True
                t.start()
            else:
                t = threading.Thread(target=startDecrypto, args=(file, key,)) #запускаю процесс шифрования в отдельном потоке
                t.daemon = True
                t.start()
    else:
        app.show_message(title='ВНИМАНИЕ!', text='Проверьте правильность указания ключа шифрования!', MsgType='warning')
radio = 1
def setRadio1():
    global radio
    radio = 1  
def setRadio0():
    global radio
    radio = 0  

app=GUI.window()
app.create(resolution = '360x200', title = 'Шифратор-дешифратор')
app.add_button(text='Выбрать файл', command=choose_file, x=0, y=0,)
app.add_text(text='Файл:', x=155, y=0)
app.add_text(text='Введите ключ шифрования', x=100, y=30)
app.add_entry(text='',focus=True, font='roman', x=130, y=50, width=100, height=30)
app.add_button(text='Начать!',text_color='red', command=get_cryptoKey, x=150, y=80)
app.add_radiobutton(text='расшифровать', variable=0, value=0, x=0, y=170, command=setRadio0)
app.add_radiobutton(text='зашифровать', variable=0, value=1, x=0, y=140, command=setRadio1)
app.add_progressbar(length=200, x=80, y=110)
app.loop_window()
