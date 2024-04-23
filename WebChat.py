import webview

supported_links = ['youtube', 'twitch']

def check_link(chat_link):
    if "twitch" in chat_link or "youtube" in chat_link:
        webview.create_window("StreamChat", chat_link)
        webview.start()
    else:
        print("Link not supported")

chat_link = input("Link on chat: ")
check_link(chat_link)