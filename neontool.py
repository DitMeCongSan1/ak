import requests
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pystyle import Colorate,Colors,Col,Center
purple = Colors.StaticMIX((Col.purple, Col.blue))
dark = Col.dark_gray
    
def getme(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data['ok']:
            bot_info = data['result']
            print("\n\n\x1b[38;5;51m==⟨ Thông Tin Bot ⟩==")
            print(f"\x1b[38;5;129mID: \x1b[38;5;255m{bot_info['id']}")
            print(f"\x1b[38;5;129mUsername: \x1b[38;5;255m@{bot_info['username']}")
            if 'first_name' in bot_info:
                print(f"\x1b[38;5;129mTên Hiển Thị: \x1b[38;5;255m{bot_info['first_name']}\n")
            else:
                print("\x1b[38;5;129mTên Hiển Thị: \x1b[38;5;255mKhông có tên\n")
        else:
            print("\x1b[38;5;196mCó lỗi xảy ra khi lấy thông tin bot.\x1b[38;5;255m")
    else:
        print(f"\x1b[38;5;196mLỗi: \x1b[38;5;255m{response.status_code}")

def forward_message(token, chatid1, chatid2, msg_id):
    base_url = f"https://api.telegram.org/bot{token}/forwardMessage"
    url = f"{base_url}?from_chat_id={chatid1}&message_id={msg_id}&chat_id={chatid2}"
    response = requests.get(url)
    if response.status_code == 200:
        return f"\x1b[38;5;10mSuccessfully forwarded message \x1b[38;5;255m{msg_id}"
    else:
        return f"\x1b[38;5;196mFailed \x1b[38;5;255m{msg_id}: {response.text}"

def forward_messages(token, chatid1, chatid2, end_msg_id):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(forward_message, token, chatid1, chatid2, msg_id) for msg_id in range(1, end_msg_id + 1)]
        for future in as_completed(futures):
            print(future.result())


def forward_nguoc_message(token, chatid1, chatid2, start_msg_id):
    current_msg_id = start_msg_id
    with ThreadPoolExecutor(max_workers=10) as executor:
        while current_msg_id > 0:
            # Submit forward task to thread pool
            future = executor.submit(forward_message, token, chatid1, chatid2, current_msg_id)
            print(future.result())
            
            # Giảm message ID để forward tin nhắn tiếp theo
            current_msg_id -= 1

def get_updates(bot_token):
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates?offset=0"
    response = requests.get(url)
    return response.json()

def get_chat_members(bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/getChatMembersCount?chat_id={chat_id}"
    response = requests.get(url)
    return response.json()

def main():
    banner = r"""
 /$$$$$$$$        /$$           /$$$$$$$              /$$    
|__  $$__/       | $$          | $$__  $$            | $$    
   | $$  /$$$$$$ | $$  /$$$$$$ | $$  \ $$  /$$$$$$  /$$$$$$  
   | $$ /$$__  $$| $$ /$$__  $$| $$$$$$$  /$$__  $$|_  $$_/  
   | $$| $$$$$$$$| $$| $$$$$$$$| $$__  $$| $$  \ $$  | $$    
   | $$| $$_____/| $$| $$_____/| $$  \ $$| $$  | $$  | $$ /$$
   | $$|  $$$$$$$| $$|  $$$$$$$| $$$$$$$/|  $$$$$$/  |  $$$$/
   |__/ \_______/|__/ \_______/|_______/  \______/    \___/
   
                                            Made By xNeonn
    """
    print(Colorate.Diagonal(Colors.DynamicMIX((purple, dark)), Center.XCenter(banner)))

    while True:
        print("\nEnter Your Choice:\n\x1b[38;5;129m===================\x1b[38;5;255m")
        print("[\x1b[38;5;51m0\x1b[38;5;255m] => Thoát")
        print("[\x1b[38;5;51m1\x1b[38;5;255m] => Get Info Bot")
        print("[\x1b[38;5;51m2\x1b[38;5;255m] => Forward Tin Nhắn")
        print("[\x1b[38;5;51m3\x1b[38;5;255m] => Thông Tin Những Người Sử Dụng (Trong Vòng 24h Qua)")
        print("[\x1b[38;5;51m4\x1b[38;5;255m] => Forward Ngược Tin Nhắn")
        
        choice = input("\x1b[38;5;129m===================\n\x1b[38;5;255mHãy Nhập Lựa Chọn: ")

        if choice == "1":
            token = input("\x1b[38;2;128;0;128m=\x1b[38;2;141;28;141m>\x1b[38;2;155;56;155m \x1b[38;2;169;84;169mT\x1b[38;2;183;112;183mo\x1b[38;2;197;140;197mk\x1b[38;2;211;168;211me\x1b[38;2;225;196;225mn\x1b[38;2;239;224;239m:\x1b[0m ")
            print(getme(token))
        elif choice == "2":
            token = input("\x1b[38;2;128;0;128m=\x1b[38;2;141;28;141m>\x1b[38;2;155;56;155m \x1b[38;2;169;84;169mT\x1b[38;2;183;112;183mo\x1b[38;2;197;140;197mk\x1b[38;2;211;168;211me\x1b[38;2;225;196;225mn\x1b[38;2;239;224;239m:\x1b[0m ")
            chatid1 = input("\x1b[38;2;128;0;128m=\x1b[38;2;135;15;135m>\x1b[38;2;143;30;143m \x1b[38;2;150;45;150mF\x1b[38;2;158;61;158mr\x1b[38;2;166;76;166mo\x1b[38;2;173;91;173mm\x1b[38;2;181;107;181m \x1b[38;2;188;122;188mC\x1b[38;2;196;137;196mh\x1b[38;2;204;153;204ma\x1b[38;2;211;168;211mt\x1b[38;2;219;183;219m \x1b[38;2;227;198;227mI\x1b[38;2;234;214;234mD\x1b[38;2;242;229;242m:\x1b[0m ")
            chatid2 = input("\x1b[38;2;128;0;128m=\x1b[38;2;136;17;136m>\x1b[38;2;145;35;145m \x1b[38;2;154;53;154mT\x1b[38;2;163;71;163mo\x1b[38;2;172;89;172m \x1b[38;2;181;107;181mC\x1b[38;2;190;124;190mh\x1b[38;2;199;142;199ma\x1b[38;2;208;160;208mt\x1b[38;2;216;178;216m \x1b[38;2;225;196;225mI\x1b[38;2;234;214;234mD\x1b[38;2;243;232;243m:\x1b[0m ")
            end_msg_id = int(input("\x1b[38;2;128;0;128m=\x1b[38;2;131;7;131m>\x1b[38;2;135;15;135m \x1b[38;2;139;22;139mĐ\x1b[38;2;143;30;143mế\x1b[38;2;147;38;147mn\x1b[38;2;150;45;150m \x1b[38;2;154;53;154mI\x1b[38;2;158;61;158mD\x1b[38;2;162;68;162m \x1b[38;2;166;76;166mB\x1b[38;2;169;84;169ma\x1b[38;2;173;91;173mo\x1b[38;2;177;99;177m \x1b[38;2;181;107;181mN\x1b[38;2;185;114;185mh\x1b[38;2;188;122;188mi\x1b[38;2;192;130;192mê\x1b[38;2;196;137;196mu\x1b[38;2;200;145;200m \x1b[38;2;204;153;204mT\x1b[38;2;208;160;208mh\x1b[38;2;211;168;211mì\x1b[38;2;215;175;215m \x1b[38;2;219;183;219mD\x1b[38;2;223;191;223mừ\x1b[38;2;227;198;227mn\x1b[38;2;230;206;230mg\x1b[38;2;234;214;234m:\x1b[0m "))
            forward_messages(token, chatid1, chatid2, end_msg_id)
        elif choice == "4":
            token = input("\x1b[38;2;128;0;128m=\x1b[38;2;141;28;141m>\x1b[38;2;155;56;155m Nhập Token: \x1b[0m ")
            chatid1 = input("\x1b[38;2;128;0;128m=\x1b[38;2;141;28;141m>\x1b[38;2;155;56;155m From Chat ID: \x1b[0m ")
            chatid2 = input("\x1b[38;2;128;0;128m=\x1b[38;2;141;28;141m>\x1b[38;2;155;56;155m To Chat ID: \x1b[0m ")
            start_msg_id = int(input("\x1b[38;2;128;0;128m=\x1b[38;2;141;28;141m>\x1b[38;2;155;56;155m Nhập ID của tin nhắn mới nhất để bắt đầu forward: \x1b[0m "))
            forward_nguoc_message(token, chatid1, chatid2, start_msg_id)
    
        elif choice == "3":
            bot_token = input("\x1b[38;2;128;0;128m=\x1b[38;2;141;28;141m>\x1b[38;2;155;56;155m \x1b[38;2;169;84;169mT\x1b[38;2;183;112;183mo\x1b[38;2;197;140;197mk\x1b[38;2;211;168;211me\x1b[38;2;225;196;225mn\x1b[38;2;239;224;239m:\x1b[0m ")
            updates = get_updates(bot_token)

            users = defaultdict(int)
            groups = defaultdict(lambda: {'name': '', 'members': 0, 'messages': 0})

            if updates['ok']:
                for update in updates['result']:
                    if 'message' in update:
                        message = update['message']
                        chat = message['chat']
                        chat_id = chat['id']
                        total_messages = 1

                        if chat['type'] == 'private':
                            username = message['from'].get('username', 'Không có tên người dùng')
                            user_id = message['from']['id']
                            users[username] = user_id
                        elif chat['type'] in ['group', 'supergroup']:
                            group_name = chat.get('title', 'Không có tên nhóm')
                            groups[chat_id]['name'] = group_name
                            groups[chat_id]['messages'] += total_messages
                            members = get_chat_members(bot_token, chat_id)
                            if members['ok']:
                                groups[chat_id]['members'] = members['result']

            print("\n\x1b[38;5;51m==⟨ People ⟩==")
            if users:
                for username, user_id in users.items():
                    print(f"\x1b[38;5;129mUsername: \x1b[38;5;255m@{username} | \x1b[38;5;129mID Chat: \x1b[38;5;255m{user_id}")
            else:
                print('\x1b[38;5;196mKHÔNG CÓ\x1b[38;5;255m')

            print("\n\x1b[38;5;51m==⟨ Group ⟩==")
            if groups:
                for chat_id, group_info in groups.items():
                    print(f"\x1b[38;5;129mName: \x1b[38;5;255m{group_info['name']} | \x1b[38;5;129mID Chat: \x1b[38;5;255m{chat_id} | \x1b[38;5;129mSố Lượng Member: \x1b[38;5;255m{group_info['members']}")
            else:
                print('\x1b[38;5;196mKHÔNG CÓ\x1b[38;5;255m')
        
        elif choice == "0":
            break
        else:
            print("\x1b[38;5;196mLựa Chọn Không Hợp Lệ\x1b[38;5;255m")

if __name__ == "__main__":
    main()