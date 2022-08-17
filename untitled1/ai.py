from wxpy import *
from ai import *                                #导入上一步构建的ai.py文件
bot = Bot()
friend = bot.friends().search('AIbot')[0]

@bot.register(friend)
def auto_reply(msg):
    a=msg.text
    answer=get_content(a)
    if answer=='':                                 #防止返回内容为空
        for i in range(2):
            time.sleep(2)
            answer=get_content(a)
            if answer!='' and answer!="emmmm，我不是很懂你的意思":
                break
            else:
                answer="emmmm，我不是很懂你的意思"
    return '[Stephen] {} '.format(answer)

bot.join()
