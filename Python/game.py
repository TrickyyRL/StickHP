from stickmanskins import *
from shop import *

def GameLaunched():
    while True:
        clear()
        print("                                       StickHP")
        print("""Commands:
        Skin shop: Will open the skin shop.
        Start match: Will start a match.
        exit: Will close the game.""")
        command = input("Insert Command: ")
      
        if command == "skin shop":
            ShopHasOpened()
        elif command == "Skin shop":
            ShopHasOpened()
        elif command == "Skin Shop":
            ShopHasOpened()
          
        elif command == "start match":
            print("You started a match.")
        elif command == "Start match":
          print( "You started a match.")
        elif command == "Start Match":
          print( "You started a match.")
          
        elif command == "exit":
          print("You exited the game.")
          exit()
        elif command == "exit":
          print("You exited the game.")
          exit()
          
        else:
            print("Invalid command.")
# imports standard packages, os and random
import os
import random
#defines players' money that the players start with
player1money = 10
player2money = 10

# long list of definitions for each skin price
stickman1price=10
stickman2price=30
stickman3price=40
stickman4price=1000
stickman5price=100
stickman6price=20
stickman7price=10
stickman8price=15
stickman9price=25
stickman10price=50
stickman11price=51
stickman12price=10
stickman13price=100
stickman14price=200
stickman15price=20
stickman16price=30
stickman17price=182
stickman18price=289
stickman19price=10
stickman20price=75
stickman21price=23
stickman22price=459
stickman23price=random.randint(1,699)
stickman24price=100
stickman25price=222
stickman26price=111
stickman27price=600
stickman28price=120
stickman29price=5000
stickman30price=5000
stickman31price=2500
stickman32price=2500
stickman33price=1250
stickman34price=1250
stickman35price=random.randint(1,200)

#this function makes it easier to clear the console
def clear():
  os.system("clear")

#This function is the main script that will be worked on for the shop
def ShopHasOpened():
  #this is how the clear() command works
  clear()
  #adds placeholder
  print(StickMan1())
  #makes a loop for shop
  while True:
    print("""0: exits shop
1-35: Look for numbered stickman (35 skins)""")
    # line 61 is asking for an skin number input for purchase
    next=int(input("Enter a number to see what skin is avaliable: "))
    
    # lots of if statements checking if the number is avaliable and what skin is the number
    if next==0:
      # if the number is 0, the shop will exit
      break
    if next==1:
      clear()
      print(StickMan1())
      print(next,"/ 35")
      print("Price:",stickman1price,"coins")
    
    if next==2:
      clear()
      print(StickMan2())
      print(next,"/ 35")
      print("Price:",stickman2price,"coins")
       
    if next==3:
      clear()
      print(StickMan3())
      print("Price:",stickman3price,"coins")
      print(next,"/ 35")
      
    if next==4:
      clear()
      print(StickMan4())
      print("Price:",stickman4price,"coins")
      print(next,"/ 35")
      
    if next==5:
      clear()
      print(StickMan5())
      print("Price:",stickman5price,"coins")
      print(next,"/ 35")
      
    if next==6:
      clear()
      print(StickMan6())
      print("Price:",stickman6price,"coins")
      print(next,"/ 35")
      
    if next==7:
      clear()
      print(StickMan7())
      print("Price:",stickman7price,"coins")
      print(next,"/ 35")
    
    if next==8:
      clear()
      print(StickMan8())
      print("Price:",stickman8price,"coins")
      print(next,"/ 35")
      
    if next==9:
      clear()
      print(StickMan9())
      print("Price:",stickman9price,"coins")
      print(next,"/ 35")
      
  
    if next==10:
      clear()
      print(StickMan10())
      print("Price:",stickman10price,"coins")
      print(next,"/ 35")
      
   
    if next==11:
      clear()
      print(StickMan11())
      print("Price:",stickman11price,"coins")
      print(next,"/ 35")
      
      
    if next==12:
      clear()
      print(StickMan12())
      print("Price:",stickman12price,"coins")
      print(next,"/ 35")
      
      
    if next==13:
      clear()
      print(StickMan13())
      print("Price:",stickman13price,"coins")
      print(next,"/ 35")
      
      
    if next==14:
      clear()
      print(StickMan14())
      print("Price:",stickman14price,"coins")
      print(next,"/ 35")
      
      
    if next==15:
      clear()
      print(StickMan15())
      print("Price:",stickman15price,"coins")
      print(next,"/ 35")
      
      
    if next==16:
      clear()
      print(StickMan16())
      print("Price:",stickman16price,"coins")
      print(next,"/ 35")
      
      
    if next==17:
      clear()
      print(StickMan17())
      print("Price:",stickman17price,"coins")
      print(next,"/ 35")
     
      
    if next==18:
      clear()
      print(StickMan18())
      print("Price:",stickman18price,"coins")
      print(next,"/ 35")
      
      
    if next==19:
      clear()
      print(StickMan19())
      print("Price:",stickman19price,"coins")
      print(next,"/ 35")
      
  
    if next==20:
      clear()
      print(StickMan20())
      print("Price:",stickman20price,"coins")
      print(next,"/ 35")
     
      
    if next==21:
      clear()
      print(StickMan21())
      print("Price:",stickman21price,"coins")
      print(next,"/ 35")
      
      
    if next==22:
      clear()
      print(StickMan22())
      print("Price:",stickman22price,"coins")
      print(next,"/ 35")
     
      
    if next==23:
      clear()
      print(StickMan23())
      print("Price:",stickman23price,"coins")
      print(next,"/ 35")
      
      
    if next==24:
      clear()
      print(StickMan24())
      print("Price:",stickman24price,"coins")
      print(next,"/ 35")
     
      
    if next==25:
      clear()
      print(StickMan25())
      print("Price:",stickman25price,"coins")
      print(next,"/ 35")
      
      
    if next==26:
      clear()
      print(StickMan26())
      print("Price:",stickman26price,"coins")
      print(next,"/ 35")
      
      
    if next==27:
      clear()
      print(StickMan27())
      print("Price:",stickman27price,"coins")
      print(next,"/ 35")
      
    if next==28:
      clear()
      print(StickMan28())
      print("Price:",stickman28price,"coins")
      print(next,"/ 35")
      
    if next==29:
      clear()
      print(StickMan29())
      print("Price:",stickman29price,"coins")
      print(next,"/ 35")
      
    if next==30:
      clear()
      print(StickMan30())
      print("Price:",stickman30price,"coins")
      print(next,"/ 35")
      
    if next==31:
      clear()
      print(StickMan31())
      print("Price:",stickman31price,"coins")
      print(next,"/ 35")
      
    if next==32:
      clear()
      print(StickMan32())
      print("Price:",stickman32price,"coins")
      print(next,"/ 35")
  
    if next==33:
      clear()
      print(StickMan33())
      print("Price:",stickman33price,"coins")
      print(next,"/ 35")
      
    if next==34:
      clear()
      print(StickMan34())
      print("Price:",stickman34price,"coins")
      print(next,"/ 35")
      
    if next==35:
      clear()
      print(StickMan35())
      print("Price:",stickman35price,"coins")
      print(next,"/ 35")


GameLaunched()
