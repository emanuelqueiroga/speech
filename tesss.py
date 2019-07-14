import speech_recognition as sr
from os import path
from kivy.app import App
from check_host import check
import time
from kivy.uix.widget import Widget
import os
from kivy.base import EventLoop
from kivy.clock import Clock
import pyttsx3
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import threading

engine = pyttsx3.init()

im = Image(source='./gif/00_loading.gif')
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

 
    im = Image(source='./gif/novos/00_loading.gif')
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
        Clock.schedule_once(self.callback, 3.0)
        return root
 
    def callback(self, value):
        
        self.im.source='./gif/novos/07_smile.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        self.im.anim_delay = 0.004
        #self.c.add_widget(self.im2)
        threading.Thread(self.apresentacao())
        #self.c.clear_widgets()
        Clock.schedule_once(self.callback1, 2.0)
        print('caraca')
    
    def callback1(self, value):
        self.im.source ='./gif/novos/05_curious.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        Clock.schedule_once(self.callback2, 2.0)
        
    def callback2(self, value):
        self.im.source ='./gif/novos/01_happy.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        Clock.schedule_once(self.callback3, 2.0)
    def callback3(self, value):
        self.im.source ='./gif/novos/03_sleep.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        Clock.schedule_once(self.callback4, 2.0)
    def callback4(self, value):
        self.im.source ='./gif/novos/09_quiet.gif'
        self.im.keep_ratio= False
        self.im.keep_data= True
        
        #engine.say('Hello, everyone!')
        #engine.runAndWait()
        #Clock.schedule_once(self.callback4, 3.0)
    def apresentacao(self):
        
        engine.say('Hi, my name is Theta. I`m a domestic robot.')
        engine.runAndWait()
        r = sr.Recognizer()
        #help(r)
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)
        #help(r)
        palavra = ''
        while palavra != 'closed':
            with sr.Microphone() as source:
                ck = check()
                teste_conexao = ck.check_host()
                print(teste_conexao)
                audio = r.listen(source)
                if teste_conexao:
                    #se on line
                    print("google")
                    try:
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
                
                if text == 'stop':
                    Clock.schedule_once(self.callback1, 2.0)


if __name__ == '__main__':
    #Clock.schedule_once(callback1, 3.0)
    MainTApp().run()