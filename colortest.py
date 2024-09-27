import time
from time import sleep
import pygame
import os
import threading



print('''
                                                                                    Decida rápido!
      ''')
sleep(0.3)
print('''
                                                                    [1] Pular em um arbusto
      ''')
sleep(0.3)
print('''
                                                                    [2] Pular em uma árvore
      ''')
sleep(0.3)
print('''
                                                                    [3] Pular do telhado
      ''')
sleep(0.6)



def countdown():
      global timer

      timer = 3

      for x in range(3):
            timer = timer - 1
            sleep(1)
            
      print('yay')
      quit()

countdown_thread = threading.Thread(target = countdown)

countdown_thread.start()


      
escolha = input('=> ') 



if escolha == '1':
      print('''
                                                                                    ok
            ''')
      sleep(2)
      quit()

if escolha == '2':
      print('''
                                                                                    ok
            ''')
      sleep(2)
      quit()
    
if escolha == '3':
      print('''
                                                                                    ok
            ''')
      sleep(2)
      quit()


