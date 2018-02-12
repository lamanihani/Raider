# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Date: Janvier 01, 2018 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%% Weather: It's always cool in the lab %%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Health: Overweight %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%% Caffeine: 12975 mg %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%% Hacked: All the things %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# By :                       Lamani Fodil Hani (VEGETA-LFH)     
# Fb :                           Lamani Fodil Hani              
# Github :                    www.github.com/lamanihani      
# Gmail :                       lamanihani1@gmail.com     
# 
#
#                                
#
#----------------------------------------------

# import some lib
import os
import re
import random
import time
import urllib.request
import time
#----------------------------
# Install Some Thing : 
os.system('clear')
print('[*] Install \033[91mPackage  \033[97m:')
os.system('apt-get install espeak')
os.system('clear')
os.system('espeak  Hello-Friend')
os.system('clear')
#---------------------------------------------
#the Banner (logo) & Art 
rania1 = ("            #do you even \033[91mexist\033[97m ")
rania2 = ('''          #Im \033[92mgood\033[97m at reading \033[93mpeople
          \033[97mMy \033[91msecret\033[97m ? I look for the \033[96mworst\033[97m in them\033[97m''')
rania3 = ("            #'\033[91mlove \033[97mis foreever' \033[97mbullshit\033[97m")
rania4 = ("            #we live in a kingdom of \033[91mbullshit\033[97m")
rania5 = ("            #LEAVE ME \033[91mHERE \033[97m!")
rania6 = ("            #LEAVE ME \033[91mHERE \033[97m!")
def kf_art():
    arts = [rania1, rania2, rania3,rania4,rania5,rania6]
    return random.choice(arts)
os.system('clear')
print('''\033[1;31m \033[97m
              ▄████████    ▄████████  ▄█  ████████▄     ▄████████    ▄████████      
             ███    ███   ███    ███ ███  ███   ▀███   ███    ███   ███    ███      
             ███    ███   ███    ███ ███▌ ███    ███   ███    █▀    ███    ███      
            ▄███▄▄▄▄██▀   ███    ███ ███▌ ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀      
           ▀▀███▀▀▀▀▀   ▀███████████ ███▌ ███    ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀        
           ▀███████████   ███    ███ ███  ███    ███   ███    █▄  ▀███████████      
             ███    ███   ███    ███ ███  ███   ▄███   ███    ███   ███    ███      
             ███    ███   ███    █▀  █▀   ████████▀    ██████████   ███    ███      
             ███    ███                                             ███    ███      
                                               By : Lamani Hani VEGETA-LFH                         
''') 
print(kf_art())
#------------------------------------
# here where the user type the target site 
print(" ")
hani = input("\033[95m[?] \033[97mEnter The \033[91mSite \033[97m(hacked-index) : \033[93m")
#rania = input("\033[95m[?]\033[97m Enter the \033[91mSite (official) : \033[93m")
gosto = re.sub('.html', '.php', hani)
listSplit = hani.split("/")
rania = listSplit[0]
if ("http" or "https") in rania :
    rania = listSplit[0]+"//"+listSplit[2]


#--------------------------------------------

#here the script building the wordlist [!] Script use " CEWL" to build the word-list
print("\033[95m[!] \033[97mBuilding The \033[93mWORD-LIST\033[97m :")
print(" ")
os.system('cewl -k -w lylia.txt '+(hani))
#----------------------------------
#reading the wordlist :
bara = open("lylia.txt")
lylia = bara.readlines()
os.system('clear')
os.system('clear')
os.system('clear')

#---------------------------------------------
os.system('espeak start')
os.system('clear')
print("\033[95m[!]\033[92m Start \033[97m:")
#_------------------------------------------
#try :
#        openurl = urllib.request.urlopen(gosto)
#        print("                                                             ")
#        print("\033[92m [✔] Shell Found ::: \033[97m"+gosto)
#        print("")
#except urllib.error.URLError as msg :
#        print ("\033[91m [✘] Shell Not Found \033[97m"+gosto)

#check if the site+word existe or no 
for fodil in lylia :
    sohaib = re.sub('\n', '', fodil)
    curl = rania+'/'+sohaib+'.php'
    try :
        openurl = urllib.request.urlopen(curl)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+curl)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+curl)

#Check with add 1 
for fodilos in lylia :
    sohaibos = re.sub('\n', '', fodilos)
    curlos = rania+'/'+sohaibos+'1'+'.php'
    try :
        openurl = urllib.request.urlopen(curlos)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+curlos)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+curlos)


#Check with add 123 
for fodilv in lylia :
    sohaibv = re.sub('\n', '', fodilv)
    curlv = rania+'/'+sohaibv+'123'+'.php'
    try :
        openurl = urllib.request.urlopen(curlv)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+curlv)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+curlv)



#check 2 with add /wp-content/ :
for fodil in lylia :
    malak = re.sub('\n', '', fodil)
    surl = rania+'/wp-content/'+malak+'.php'
    try :
        openurl = urllib.request.urlopen(surl)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+surl)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+surl)

#check 3  with add 'wp-content/plugins/akismet/ :
for fodil in lylia :
    malake = re.sub('\n', '', fodil)
    ssurl = rania+'/wp-content/plugins/akismet/'+malake+'.php'
    try :
        openurl = urllib.request.urlopen(ssurl)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+ssurl)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+ssurl)


# Check 4 with add /templates/beez/ :
 
for fodil in lylia :
    malakes = re.sub('\n', '', fodil)
    sssurl = rania+'/templates/beez/'+malakes+'.php'
    try :
        openurl = urllib.request.urlopen(sssurl)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+sssurl)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+sssurl)


# Check 5 with add /includes/ :
for fodil in lylia :
    malakess = re.sub('\n', '', fodil)
    sssurls = rania+'/includes/'+malakess+'.php'
    try :
        openurl = urllib.request.urlopen(sssurls)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+sssurls)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+sssurls)


# Boring !? Its the last :) , Check with /images/ :

for fodil in lylia :
    malakesss = re.sub('\n', '', fodil)
    sssurlse = rania+'/images/'+malakesss+'.php'
    try :
        openurl = urllib.request.urlopen(sssurlse)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+sssurlse)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+sssurlse)
# check with : /templates/rhuk_milkyway/
for fodil in lylia :
    malakessszz = re.sub('\n', '', fodil)
    sssurlsedw = rania+'/templates/rhuk_milkyway/'+malakessszz+'.php'
    try :
        openurl = urllib.request.urlopen(sssurlsedw)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+sssurlsedw)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+sssurlsedw)



# check with : /wp-content/plugins/google-sitemap-generator/
for fodil in lylia :
    malakesssq = re.sub('\n', '', fodil)
    sssurlsedwff = rania+'/wp-content/plugins/google-sitemap-generator/'+malakesssq+'.php'
    try :
        openurl = urllib.request.urlopen(sssurlsedwff)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+sssurlsedwff)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+sssurlsedwff)

# check with : /wp-content/plugins/disqus-comment-system/tmp/
for fodil in lylia :
    malakesssqf = re.sub('\n', '', fodil)
    sssurlsedwfff = rania+'/wp-content/plugins/disqus-comment-system/tmp/'+malakesssqf+'.php'
    try :
        openurl = urllib.request.urlopen(sssurlsedwfff)
        print("                                                             ")
        print("\033[92m [✔] Shell Found ::: \033[97m"+sssurlsedwfff)
        print("")
    except urllib.error.URLError as msg :
        print ("\033[91m [✘] Shell Not Found \033[97m"+sssurlsedwfff)







#-----------------------------------------------------
# removing all the trash 
os.remove('lylia.txt')


