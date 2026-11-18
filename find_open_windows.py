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
        add_list += [[l["датаНачала"], i, l["дисциплина"]] for l in web.get(f"{http}/api/Rasp?idGroup={i}&sdate={date}", timeout=10).json()["data"]["rasp"]]

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
        
    #print(text)
    
    return text


if __name__ == "__main__":
    link_data()
