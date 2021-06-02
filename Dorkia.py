#this is a project to google dork easier
#made by JaCrispy4939
#art by IntelScripter#8313
#discord: Ja'Crispy#6927
#educational purpouses only, i am not the cause of any damage done
from googlesearch import search
import webbrowser
import time
from colorama import Fore


while True:
    print(Fore.GREEN+ """
     ___     ___   ____   __  _  ____   ____ 
    |   \   /   \ |    \ |  |/ ]|    | /    |
    |    \ |     ||  D  )|  ' /  |  | |  o  |
    |  D  ||  O  ||    / |    \  |  | |     |
    |     ||     ||    \ |     \ |  | |  _  |
    |     ||     ||  .  \|  .  | |  | |  |  |
    |_____| \___/ |__|\_||__|\_||____||__|__|""")
    
    query = input("\n \n1. Cameras \n2. More Cameras \n3. Leaked passwords\n\nOption (type exit to quit):  ")
    
    if query == "exit":
        print("closing")
        time.sleep(1.5)
        quit()
    
    if query == "1":
        webcam = "inurl:mobile.html intitle:webcamXP"
        #  iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % webcam)

    if query == "2":
        More_cams = ('''inurl:"view.shtml" "camera"''')
        #  iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % More_cams)

    if query == "3":
        Leaked_pass = ('''intext:"username"= AND "password"=ext:log''')
         #  iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % Leaked_pass)