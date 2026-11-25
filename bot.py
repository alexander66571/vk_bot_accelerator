import vk_api
from find_open_windows import rasp, open_windows
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


with open("./user_data/token.txt", "r") as file:
    TOKEN = file.read()
    
vk_session = vk_api.VkApi(api_version=5.199, token=TOKEN)
longpoll = VkBotLongPoll(vk_session, 243295689)

def send(peer_id, msg):
    if msg != "":
        vk_session.method("messages.send", values={"peer_id": peer_id, "random_id": 0, "message": str(msg)})

def msg_clear(msg):
    msg = msg.lower()
    if "  " in msg:
        return msg_clear(msg.replace("  ", " "))
    else:
        return msg.split(" ")


for event in longpoll.listen():
    try:
        if event.type == VkBotEventType.MESSAGE_NEW:
            peer_id = event.message.peer_id
            msg = msg_clear(event.message.text)
            print(msg)
            for i in msg:
                if "all" in i or "online" in i:
                    break

                elif "@" in i:
                    continue
                
                elif i == "расписание":
                    send(peer_id, rasp())

                elif i == "окна":
                    send(peer_id, open_windows())

                else:
                    send(peer_id, i)
                    
    except Exception as error:
        print(f"ERROR!!! : {error}")

