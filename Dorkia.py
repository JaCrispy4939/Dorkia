#this is a project to google dork easier
#made by JaCrispy4939
#discord: Ja'Crispy#6927
#educational purpouses only, i am not the cause of any damage done
from googlesearch import search
import webbrowser

while True:
    
    query = input("\n \n1. Cameras \n2. Leaked Passwords \n3. ")
    if query == "1":
        webcam = "inurl:mobile.html intitle:webcamXP"
        #  iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % webcam)

    if query == "2":
        Leaked_pass = ("intext:username= AND password=ext:log")
         #  iexplorer_path = r'C:\Program Files (x86)\Internet Explorer\iexplore.exe %s'
        chrome_path = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
        for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % Leaked_pass)

    