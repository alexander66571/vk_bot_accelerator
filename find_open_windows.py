from tkinter import *
from tkinter import ttk
import requests as web
import time

weekends = False

with open("./user_data/groups.txt", "r") as file:
    groups = file.read().split(";")
    
with open("./user_data/http.txt", "r") as file:
    http = file.read()

    
def link_data():
    struct = {i: {l: {g: "" for g in groups} for l in ['08:30-10:05', '10:15-11:50', '12:40-14:15', '14:25-16:00', '16:10-17:45', '17:55-19:30', '19:40-21:15']} for i in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]}
    date = time.strftime("%Y-%m-%d", time.localtime())
    
    for group in groups:
        for lesson in web.get(f"{http}/api/Rasp?idGroup={group}&sdate={date}", timeout=10).json()["data"]["rasp"]:
            
<<<<<<< Updated upstream
    with open("./user_data/output_request.txt", "w") as file:
        file.write(text)
        
    
    
    return text


if __name__ == "__main__":
    print(link_data())
=======
            b = lesson["датаНачала"][lesson["датаНачала"].find("T")+1:-3]+"-"+lesson["датаОкончания"][lesson["датаОкончания"].find("T")+1:-3]
            struct[lesson["день_недели"]][b][group] = lesson["дисциплина"]
            
    return struct


def open_windows():
    struct = link_data()

    ans = "Свободные окна\n"
    for i in struct.keys():
        if i in ["Суббота", "Воскресенье"] and weekends == False:
            continue
        else:
            ans += i+":"
        for l in struct[i].keys():
            p = 0
            for k in struct[i][l].keys():
                if struct[i][l][k] == "":
                    p += 1
            if p == 4:
                ans += l+"; "
        ans += "\n"

    return ans


def rasp():
    struct = link_data()

    ans = "Расписание \n"
    for i in struct.keys():
        if i in ["Суббота", "Воскресенье"] and weekends == False:
            continue
        else:
            ans += i + ":\n"
        for l in struct[i].keys():
            ans += l + "\t"
            for k in struct[i][l].keys():
                if struct[i][l][k] == "":
                    ans += "          \t"
                else:
                    ans += struct[i][l][k][:10] + "\t"
            ans += "\n"
        ans += "\n"

    return ans

















if __name__ == "__main__":
    #print(link_data())
    print(open_windows())
    print(rasp())
>>>>>>> Stashed changes
