# Module installation 
from art import *
from datetime import datetime
import time
from colorama import Fore, Back, Style
import shutil
import calendar 
from plyer import notification

class Timer:
    global_number = 0

    """Timer"""
    def intervalo(sec=0, min=5, color="MAGENTA", times = 1, min_aux = 25):
        
        color = color.upper()
        min_intervalo_aux = min
        
        if min > 0:
            min -= 1
            sec = 60 - sec
        while min > 0 or sec > 0:
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
        
        color = color.upper()
        min_aux = min
        Timer.global_number += 1
        if min > 0:
            min -= 1
            sec = 60 - sec
        while min > 0 or sec > 0:
            print(eval(f"Fore.{color}"))
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
        
        tprint("FINISHED!!!")
        notification.notify(
            title = "Clock", 
            message="All sessions ended")   
            
            
if __name__ == "__main__":
   min_sessao = int(input("Minutos de uma sessão: "))
   min_intervalo = int(input("Minutos de um intervalo: "))
   num_sessao = int(input("Número de sessões: "))
   Timer.timer(0, min_sessao, "WHITE", num_sessao, min_intervalo)
