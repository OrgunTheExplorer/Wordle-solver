import colorama
from colorama import Fore
screen="""
(-) Word does not contain letter
(+) Word contains letter
(q) see outputs 
(break) exit from the program
Give the command:
"""
while True:
    required = input(Fore.BLUE + screen)
    if required == "-":
        while True:
            quest = input(Fore.BLUE + "Doesn't contain (break to exit):")
            if quest == "break":
                break
            else:
                if quest.find("1") != -1 or quest.find("2") != -1 or quest.find("3") != -1 or quest.find("4") != -1 or quest.find("5") != -1:
                    num = int(quest[1])-1
                    quest = quest.replace(quest[1],"")
                    try:
                        with open('wraten.txt','r') as fr:
                            lines = fr.readlines()
                            with open('wraten.txt','w') as fw:
                                for line in lines:
                                    if line.find(quest) != -1 and line.find(quest,num,num+1) == -1:
                                        fw.write(line)
                    except:
                        print(Fore.RED+"Ops!!! something went wrong")
                else:
                    try:
                        with open('wraten.txt','r') as fr:
                            lines = fr.readlines()
                            with open('wraten.txt','w') as fw:
                                for line in lines:
                                    if line.find(quest) == -1:
                                        fw.write(line)
                    except:
                        print(Fore.RED+"Ops!!! something went wrong")
    elif required == "+":
        while True:
            quest = input(Fore.BLUE + "Does contain (break to exit):")
            if quest == "break":
                break
            else:
                if quest.find("1") != -1 or quest.find("2") != -1 or quest.find("3") != -1 or quest.find("4") != -1 or quest.find("5") != -1:
                    num=int(quest[1])-1
                    quest=quest.replace(quest[1],"")
                    try:
                        with open('wraten.txt','r') as fr:
                            lines = fr.readlines()
                            with open('wraten.txt','w') as fw:
                                for line in lines:
                                    if line.find(quest,num,num+1) != -1:
                                        fw.write(line)
                    except:
                        print(Fore.RED+"Ops!!! something went wrong")
                else:
                    try:
                        with open('wraten.txt','r') as fr:
                            lines = fr.readlines()
                            with open('wraten.txt','w') as fw:
                                for line in lines:
                                    if line.find(quest) != -1:
                                        fw.write(line)
                    except:
                        print(Fore.RED+"Ops!!! something went wrong")
    elif required == "q":
        fr = open("wraten.txt","r")
        for line in sorted(fr):
            line=line.rstrip()
            print(Fore.GREEN + line)
    elif required == "break":
        with open('wrat.txt','r') as fr:
            lines = fr.readlines()
            with open('wraten.txt','w') as fw:
                for line in lines:
                        fw.write(line)
                break
    else:
        print(Fore.RED + "Falsa input")
        continue
