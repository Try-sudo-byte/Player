from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os
import pygame
from pytube import YouTube
import ffmpy
import PyQt5

pygame.init()
volume = 0.5
pygame.mixer.music.set_volume(0.5)

def open_file():
    file_name = QFileDialog()
    names = file_name.getOpenFileNames(filter = 'MP3, MP4 (*.mp3, *.mp4)')
    song = names[0]
    print(song)
    ui.listWidget.addItems(song)

def play_file():
    i = ui.listWidget.currentRow()
    if i == -1:
        ui.label.setText('Выбери музыку')
        error()
    else:
        melody = ui.listWidget.item(i).text()
    if '.mp3' in melody:
        pygame.mixer.music.load(melody)
        pygame.mixer.music.play()
        ui.label.setText('Играет')
    elif '.mp4' in melody:
        os.startfile(melody)
    else:
        ui.label.setText('Неизвестный формат файла')

def stop_file():
        pygame.mixer.music.stop()
        ui.label.setText('Стоп')

def find_pl():
    import glob
    pl_list = glob.glob('*.pl')
    print(pl_list)
    ui.listWidget_2.clear()
    ui.listWidget_2.addItems(pl_list)


def save_pl():
    global song
    import pickle
    if ui.lineEdit_2.text() != '' and ('.pl' in ui.lineEdit_2.text()):
        filename = ui.lineEdit_2.text()
        print(filename)
        f = open(filename, 'wb')
        pickle.dump(song, f)
        ui.listWidget_2.addItem(filename)


def load_pl():
    global song
    import pickle
    i = ui.listWidget_2.currentRow()
    print(i)
    if i != -1:
        pl_item = ui.listWidget_2.item(i).text()
        print(pl_item)
        f = open(pl_item, 'rb')
        song = pickle.load(f)
        print(song)
        ui.listWidget.addItems(song)

def clear_pl():
    global song
    song = []
    ui.listWidget_2.clear()

def find_files():
    global song
    dir = QFileDialog.getExistingDirectory()
    for dir_put, dn, filenames in os.walk(dir):
        for file in filenames:
            if file.endswith('mp3') or file.endswith('mp4'):
                song.append(os.path.join(dir_put, file))
    ui.listWidget.addItems(song)

def clear_files():
    global song
    song = []
    ui.listWidget.clear()

def error():
    ui.label.setText('ERROR')

def volume_up():
    global volume
    if volume < 0.9:
        volume += 0.1
        ui.label_4.setText(str(round(volume*100)) +'%')
        pygame.mixer.music.set_volume(volume)

def volume_down():
    global volume
    if volume > 0.1:
        volume -= 0.1
        ui.label_4.setText(str(round(volume*100)) +'%')
        pygame.mixer.music.set_volume(volume)

def download_youtube():
    print(ui.lineEdit.text())
    try:
        if ui.radioButton.isChecked():
            print(ui.radioButton.isChecked)
            link = ui.lineEdit.text()
            print(link)
            yt = YouTube(str(link))
            videos = yt.streams.get_audio_only()
            videos.download()
            file_name = videos.title
            print(file_name)
            ff = ffmpy.FFmpeg(inputs = {file_name + '.mp4': None}, outputs={file_name + '.mp3': None})
            ff.run()
            os.remove(file_name + '.mp4')
            ui.listWidget.addItem( file_name + '.mp3' )

        if ui.radioButton_2.isChecked():
            link = ui.lineEdit.text()
            yt = YouTube(str(link))
            videos = yt.streams.get_by_itag(18)
            videos.download()
            file_name = videos.title
            ui.listWidget.addItem( file_name + '.mp4' )

        if ui.radioButton_3.isChecked():
            link = ui.lineEdit.text()
            yt = YouTube(str(link))
            videos = yt.streams.get_by_itag(135)
            videos.download()
            file_name = videos.title
            ui.listWidget.addItem( file_name + '.mp4' )

        if ui.radioButton_4.isChecked():
            link = ui.lineEdit.text()
            yt = YouTube(str(link))
            videos = yt.streams.get_by_itag(136)
            videos.download()
            file_name = videos.title
            ui.listWidget.addItem( file_name + '.mp4' )

        if ui.radioButton_5.isChecked():
            link = ui.lineEdit.text()
            yt = YouTube(str(link))
            videos = yt.streams.get_by_itag(137)
            videos.download()
            file_name = videos.title
            ui.listWidget.addItem( file_name + '.mp4' )


        if ui.radioButton_6.isChecked():
            link = ui.lineEdit.text()
            yt = YouTube(str(link))
            videos = yt.streams.get_by_itag(133)
            videos.download()
            file_name = videos.title
            ui.listWidget.addItem( file_name + '.mp4' )

      

    except:
        ui.label_6.setText('Дай корректную ссылку:')


song = []

app = QApplication([])
ui = uic.loadUi('file_interfice.html')
ui.setWindowTitle('Mp3 Player')
ui.show()

ui.pushButton.clicked.connect(open_file)
ui.pushButton_2.clicked.connect(play_file)
ui.pushButton_3.clicked.connect(find_files)
ui.pushButton_4.clicked.connect(clear_files)
ui.pushButton_5.clicked.connect(save_pl)
ui.pushButton_6.clicked.connect(load_pl)
ui.pushButton_7.clicked.connect(stop_file)
ui.pushButton_8.clicked.connect(volume_up)

ui.pushButton_12.clicked.connect(clear_pl)
ui.pushButton_11.clicked.connect(find_pl)

ui.pushButton_9.clicked.connect(volume_down)
ui.radioButton.setChecked(True)
ui.pushButton_10.clicked.connect(download_youtube)

ui.listWidget.itemDoubleClicked.connect(play_file)

app.exec_()



#https://youtu.be/ByVPVWCQVV8