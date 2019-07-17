import speech_recognition as sr
from os import path
from kivy.app import App
from check_host import check
import time
from kivy.uix.widget import Widget
import os
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.clock import mainthread
import pyttsx3
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import threading
from kivy.loader import Loader

engine = pyttsx3.init()

im = Image(source='./gif/jpg/00-load.jpg')
image = Loader.image('./gif/jpg/00-load.jpg')
#im2 = Image(source='./gif/07_smile.gif')

class Imglayout(FloatLayout):
    def __init__(self, **args):
        super(Imglayout, self).__init__(**args)
 
        with self.canvas.before:
            Color(0, 0, 0, 0)
            self.rect = Rectangle(size=self.size, pos=self.pos)
 
        self.bind(size=self.updates, pos=self.updates)

    def updates(self,instance,value):
        self.rect.size=instance.size
        self.rect.pos=instance.pos


class MainTApp(App):

    
    im = Image(source='./gif/loading.zip')
    #im3 = image
    #im2 = Image(source='./gif/05_curious.gif')
    #im2.size_hint_y = 0
    c = Imglayout()
    
    def build(self):
        root = BoxLayout()
        
        root.add_widget(self.c)

        self.im.keep_ratio= False
        self.im.keep_data= True
        #self.im.allow_stretch = False
        self.im.anim_delay = 0.2
        #cat=Button(text="Categories", size_hint=(1,.07))
        #cat.bind(on_press=self.callback)
        self.c.add_widget(self.im)
        #self.c.add_widget(self.im2)
        #root.add_widget(cat);
        #self.apresentacao()
        Clock.schedule_once(self.callback, 2.0)
        return root
        
    
    def falainit(self, value):
        engine.say('Hi, my name is Theta. I`m a domestic robot.')
        engine.runAndWait()
 
    def callback(self, value):
        
        self.im.source='./gif/novos/00_loading.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        self.im.anim_delay = 0.2
        #self.c.add_widget(self.im2)
        #Clock.schedule_once(self.falainit(0))
        #Clock.schedule_once(self.apresentacao, 2.0)
        #self.c.clear_widgets()
        #Clock.schedule_once(self.chamaspeech(0))
        Clock.schedule_once(self.falainit, 0)
        Clock.schedule_once(self.curious, 0)
        #Clock.schedule_once(self.fala, 0)
        
        #Clock.schedule_once(self.callback1, 2.0)
        print('caraca')
    
    def chamaspeech(self, value):
        #fala
        Clock.schedule_once(self.fala(0))
    
    
    def callback1(self, value):
        #entendeu a fala e esta esperando a execucao
        print('callback 1')
        self.im.source ='./gif/novos/05_curious.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        self.im.anim_delay = 0.004
        Clock.schedule_once(self.callback2, 2.0)
        Clock.schedule_once(self.falaok, 2.0)
        
    def callback2(self, value):
        self.im.source ='./gif/novos/01_happy.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        time.sleep(15)
        Clock.schedule_once(self.callback3, 2.0)
    def callback3(self, value):
        self.im.source ='./gif/novos/03_sleep.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        time.sleep(15)
        Clock.schedule_once(self.callback4, 2.0)
    def callback4(self, value):
        self.im.source ='./gif/novos/09_quiet.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        time.sleep(15)
        
    def falaok(self, value):
        #fala ok e escreve no topic do ros e fica esperando
        engine.say('Ok, lets do!')
        engine.runAndWait()
        #rostopic escreve
        #rostopic espera retorno
        time.sleep(10)
        Clock.schedule_once(self.executou, 2.0)
        
    def executou(self, value):
        #fala ok e escreve no topic do ros e fica esperando
        engine.say('Done!')
        engine.runAndWait()
        Clock.schedule_once(self.chamaspeech, 2.0)
        
        #engine.say('Hello, everyone!')
        #engine.runAndWait()
        #Clock.schedule_once(self.callback4, 3.0)
    def curious(self, value):
        #entendeu a fala e esta esperando a execucao
        print('callback curious')
        self.im.source ='./gif/novos/05_curious.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        self.im.anim_delay = 0.004
        time.sleep(2)
        Clock.schedule_once(self.fala, 0)
        
    #def fala(self, value):
     #   self.curious()
    def fala(self, value):
        engine.say('Would you like something?')
        engine.runAndWait()
        r = sr.Recognizer()
        #help(r)
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
        #help(r)
        text = ""
        palavra = 'bad'
        while palavra != 'ok':
            with sr.Microphone() as source:
                ck = check()
                teste_conexao = ck.check_host()
                print(teste_conexao)
                audio = r.listen(source)
                print('tes')
                if teste_conexao:
                    #se on line
                    print("google")
                    try:
                        print("google try")
                        text = r.recognize_google(audio)
                    except:
                        pass
                else:
                    #se off line
                    print("pocket")
                    try:
                        text = r.recognize_sphinx(audio, grammar='palavras.gram')
                    except:
                        pass
                try:
                    print(text)
                except:
                    pass
                #if text == 'stop' or text == 'turn left' or text == 'turn right' or text == 'Hello' or text == 'dance' or text == 'go ahead' or text == 'move':
                if text == 'stop':
                    palavra = 'ok'
                    print("Palavra=", text)
                    Clock.schedule_once(self.callback1, 2.0)
                else:
                    engine.say('I dont understand, can you repeat?')
                    engine.runAndWait()


if __name__ == '__main__':
    #Clock.schedule_once(callback1, 3.0)
    MainTApp().run()
