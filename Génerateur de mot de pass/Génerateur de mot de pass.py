


##############################   importing mudules  ########################""

import random
import string
import datetime
import threading
import pyfiglet
from playsound import playsound
import winsound

# declaring lists
LIST_PASS=[]     # add the password to this list
LST_ALL=[]       # add our three list to one list
numbers=list(string.digits) # list one
alphabet_list = list(string. ascii_lowercase)   # list two
alphabet1_list=list(string.ascii_uppercase)  # list two
espace="    "
sound = pyfiglet.figlet_format(espace+"Générateur de mot de passe")

LST_ALL.extend(numbers)
LST_ALL.extend(alphabet1_list)
LST_ALL.extend(alphabet_list)
# decalring variables
fichier_Name="Password"
click=""


datetime_object = str(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')) # to add a dynamique name to files

# function



def play_sound():
    """winsound.PlaySound('Hacker Sound Effect Efeito Sonoro Hacker - Hacking the System.mp3', winsound.SND_ALIAS|winsound.SND_ASYNC)"""
    playsound('Hacker Sound Effect Efeito Sonoro Hacker - Hacking the System.mp3')


def generateur_Mot_De_Pass():  
    print(sound)

   
    password=int(input("entrez la longeur de votre mot de pass \n"))
    for i in range(password):
            
        x=random.choice(LST_ALL)
        LIST_PASS.append(x)
        print(x,end="")
        
    
    print("\n")    
    confirmation=str(input("voullez vous ce mot de pass(oui/non/Q(pour quiter) ) ? \n"))
    if confirmation =="oui":
        print("ce mot de pass a éte enregistre dans le fichie",fichier_Name+datetime_object)
        fichier=open(fichier_Name+datetime_object,"x")
        fichier=open(fichier_Name+datetime_object,"a")
        for i in range(len(LIST_PASS)):
            if i==0:
                fichier.write(" votre mot de pass est :")
                
            fichier.write(LIST_PASS[i]) 
    else:
        generateur_Mot_De_Pass()
generateur_Mot_De_Pass()




