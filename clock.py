# Module installation 
from art import *
from datetime import datetime
import time
from colorama import Fore, Back, Style
import shutil
import calendar 
from plyer import notification
import climage
import timg

class Timer:
    global_number = 0

    """Timer"""
    def intervalo(sec=0, min=5, color="MAGENTA", times = 1, min_aux = 25):
        
        color = color.upper()
        min_intervalo_aux = min
        output = climage.convert("pomodoro.png")
        #obj = timg.Renderer()                                                                                               
        #obj.load_image_from_file("pomodoro_written.png")                                                                                
        #obj.resize(100,60)
        if min > 0:
            min -= 1
            sec = 60 - sec
        while min > 0 or sec > 0:
            #obj.render(timg.ASCIIMethod)
            print(output)
            print(eval(f"Fore.{color}"))
            tprint(str(min) + " : " + str(sec))
            sec -= 1
            time.sleep(1)
            if(sec == 0):
                min -= 1
                if(min < 0):
                    break 
                sec = 60 - sec
            print("\033[H\033[J")
        notification.notify(
            title = "Clock", 
            message="Session starting in 3 seconds")
        time.sleep(3)
        Timer.timer(0, min_aux, "WHITE", times, min_intervalo_aux)
    
    def timer(sec=0, min=25, color="MAGENTA", times = 2, min_intervalo = 5):
        #output = climage.convert("pomodoro.png")
        obj = timg.Renderer()                                                                                               
        obj.load_image_from_file("actually.jpg")                                                                                
        obj.resize(30,35)

        color = color.upper()
        min_aux = min
        Timer.global_number += 1
        if min > 0:
            min -= 1
            sec = 60 - sec
        while min > 0 or sec > 0:
            print(eval(f"Fore.{color}"))
            #print(output)
            obj.render(timg.ASCIIMethod)
            tprint(str(min) + " : " + str(sec))
            tprint(str(Timer.global_number) + "/" + (str(times + Timer.global_number - 1)))
            sec -= 1
            time.sleep(1)
            if(sec == 0):
                min -= 1
                if(min < 0):
                    times -= 1
                    break 
                sec = 60 - sec
            print("\033[H\033[J")
        
        if(times > 0):
            tprint("BREAK")
            notification.notify(
                title = "Clock", 
                message="Break starting in 3 seconds")
            time.sleep(3)
            Timer.intervalo(0, min_intervalo, "BLUE", times, min_aux)
        
        elif(times == 0):
            tprint("FINISHED!!!")
            notification.notify(
            title = "Clock", 
            message="All sessions ended")   
            
            
if __name__ == "__main__":
   min_sessao = int(input("Minutes in a session: "))
   min_intervalo = int(input("Minutes in a break: "))
   num_sessao = int(input("Number of sessions: "))
   Timer.timer(0, min_sessao, "WHITE", num_sessao, min_intervalo)
