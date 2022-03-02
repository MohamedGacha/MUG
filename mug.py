# -*- coding: utf-8 -*-
from colorama import Back, Fore, Style, deinit, init
import csv
import time
import os
import keyboard as key
from pygame import mixer



with open("frame_2.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    empty_cup = list(csv_reader)

with open("frame_1.txt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    full_cup = list(csv_reader)

mixer.init()
mixer.music.load("notifi.mp3")


def timer(t):
    while t > 0:
        mins, secs = int(t//60), int(t % 60)
        timer = f'Timer: {mins}:{secs} remaining'
        print(timer, end='\r')
        time.sleep(1)
        t -= 1


def coffee(interval):
    _ = os.system('mode con: cols=28 lines=20')
    init()
    for i in range(4,15):
        _ = os.system('cls')
        print('time to sip some coffee ^_^\n')
        mixer.music.play()
        for j in range(i):
            tmpStr = str(empty_cup[j])
            tmpStr = tmpStr.replace("['", "", 1)
            tmpStr = tmpStr.replace("']", "", 1)
            print(Fore.WHITE+tmpStr)
        for j in range(i, 15):
            tmpStr = str(full_cup[j])
            tmpStr = tmpStr.replace("['", "",1)
            tmpStr = tmpStr.replace("']", "",1)
            for k in tmpStr:
                if k == '@':
                    print(Fore.LIGHTBLACK_EX+k,end='')
                else :
                    print(Fore.WHITE+k,end='')
            print()

        timer(interval)

    deinit()
    print('Oops no more drink')
    time.sleep(3)




while True:
    _ = os.system('mode con: cols=60 lines=10')

    print("Hey!\nI wish you are having a nice day ^^")
    print("Get yourself a drink and let's start working.\n")
    try:
        duration = eval(input('For how long are you gonna stay working (in minutes) ?\n'))
        coffee(duration*60/15)
    except:
        pass

    _ = os.system('mode con: cols=60 lines=10')
    choice = input('Are you are you tired ? (y/n) : ')
    if choice == 'y':
        break
    else:
        pass
        

    