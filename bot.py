import vk_api
from find_open_windows import link_data
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


with open("./user_data/token.txt", "r") as file:
    TOKEN = file.read()

def send(user_id, msg):
    vk_session.method("messages.send", values={"user_id": user_id, "random_id": 0, "message": str(msg)})

vk_session = vk_api.VkApi(api_version=5.199, token=TOKEN)

longpoll = VkBotLongPoll(vk_session, 243295689)

for event in longpoll.listen():
    
    
    if event.type == VkBotEventType.MESSAGE_NEW:
        user_id = event.message.from_id
        if event.message.text == "Расписание":
            msg = link_data()
            send(user_id, msg)
        else:
            send(user_id, "Hello, world!")
        


