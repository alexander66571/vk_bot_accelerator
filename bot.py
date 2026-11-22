import vk_api
from find_open_windows import link_data
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


with open("./user_data/token.txt", "r") as file:
    TOKEN = file.read()
    
vk_session = vk_api.VkApi(api_version=5.199, token=TOKEN)
longpoll = VkBotLongPoll(vk_session, 243295689)

def send_for_user(user_id, msg):
    vk_session.method("messages.send", values={"peer_id": user_id, "random_id": 0, "message": str(msg)})

def send_for_group(group_id, msg):
    vk_session.method("messages.send", values={"peer_id": group_id, "random_id": 0, "message": str(msg)})



for event in longpoll.listen():
    
    
    if event.type == VkBotEventType.MESSAGE_NEW:
        #print(event)
        if event.message.peer_id == 2000000001:
            forward_id = event.message.peer_id
            forward_send = send_for_group
            msg = str(event.message.text).split(" ")[1]
            
        else:
            forward_id = event.message.from_id
            forward_send = send_for_user
            msg = str(event.message.text)
            
        
            
            
        print(forward_id)
        #print(msg)
            
        if msg == "Расписание":
            msg = link_data()
            forward_send(forward_id, msg)
        else:
            forward_send(forward_id, "Hello, world!")
        


