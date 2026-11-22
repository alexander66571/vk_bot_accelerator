from tkinter import *
from tkinter import ttk
import requests as web
import time


with open("./user_data/groups.txt", "r") as file:
    groups = file.read().split(";")
    
with open("./user_data/http.txt", "r") as file:
    http = file.read()

    
def link_data():
    
    date = time.strftime("%Y-%m-%d", time.localtime())
    add_list = []
    res = dict()
    for i in groups:
        add_list += [[l["датаНачала"]+"---"+l["датаОкончания"], i, l["дисциплина"]] for l in web.get(f"{http}/api/Rasp?idGroup={i}&sdate={date}", timeout=10).json()["data"]["rasp"]]

    add_list.sort()

    for i in add_list:
        if i[0] not in res.keys():
            res[i[0]] = {i[1] : i[2]}
        else:
            res[i[0]][i[1]] = i[2]

        
    text = ""
    g = ""
    for i in res.keys():
        if str(i[:i.find("T")]) != g:
            g = str(i[:i.find("T")])
            text += "\n"
        wrt = str(i) + "\t"
        for l in groups:
            try:
                wrt += str(res[i][l])[:11] + "\t"
            except:
                wrt += "          \t"
        text += wrt + "\n"
            
    with open("./user_data/output_request.txt", "w") as file:
        file.write(text)
        
    
    
    return text

def test():
    
    dict_a = {0: "Понедельник", 1: "Вторник", 2: "Среда", 3: "Четверг", 4: "Пятница", 5: "Суббота", 6: "Воскресенье"}
    dict_b = {"8:30": "1 пара", "10:15": "2 пара", "12:40": "3 пара", "14:25": "4 пара", "16:10": "5 пара", "17:55": "6 пара", "19:40": "7 пара"}
    date = time.strftime("%Y-%m-%d", time.localtime())
    
    add = list()
    for i in groups:
        for l in web.get(f"{http}/api/Rasp?idGroup={i}&sdate={date}", timeout=10).json()["data"]["rasp"]:
            a = time.strptime(l["датаНачала"], "%Y-%m-%dT%H:%M:%S")

            add.append([dict_a[a.tm_wday], dict_b[f"{a.tm_hour}:{a.tm_min}"], i, l["дисциплина"]])
    add.sort()
    print(list(add))
























if __name__ == "__main__":
    #print(link_data())
    test()
