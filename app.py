# -*- coding: utf-8 -*-

#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import re
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('kU4ar4S8kbgto4jk3y0N57JPsB5pRxWvI4yNkj31m1uqZaFtIvJnptg7J48moDnXB90oGVcNLO1nwiFwAQx+klALKYS6ACnWsdF8qYQe+4Ae+4gOlTrE7ww/M88SECkzylc7Cl6xTyijyFcvQdqrwgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('9c842edd49ecf2de4d59f754e476a760')

line_bot_api.push_message('U543945277c78ffc1f634f3b96cb60f17', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text=event.message.text
    if re.match('推薦餐廳',message):
        image_carousel_template_message = TemplateSendMessage(
            alt_text='這是TemplateSendMessage',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://imgur.com/cJ7xDKq',
                        action=PostbackAction(
                            label='日式料理',
                            display_text='https://www.google.com/search?q=%E6%97%A5%E5%BC%8F%E6%96%99%E7%90%86&oq=%E6%97%A5%E5%BC%8F%E6%96%99%E7%90%86&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIGCAcQRRg80gEIMTU2NGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8',
                            data='action=001'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://imgur.com/dhzPsMT',
                        action=PostbackAction(
                            label='西式料理',
                            display_text='https://www.google.com/search?q=%E8%A5%BF%E5%BC%8F%E6%96%99%E7%90%86&sca_esv=f73d2c36e6ea8307&sxsrf=ADLYWILKv-VJzqm4kpk16sEaRkvelXDyng%3A1734353605531&ei=xSJgZ6uTIP7i1e8PlIn-8A4&ved=0ahUKEwjricrUqqyKAxV-cfUHHZSEH-4Q4dUDCBA&uact=5&oq=%E8%A5%BF%E5%BC%8F%E6%96%99%E7%90%86&gs_lp=Egxnd3Mtd2l6LXNlcnAiDOilv-W8j-aWmeeQhjIKEAAYgAQYQxiKBTIFEAAYgAQyChAAGIAEGEMYigUyBRAAGIAEMgoQABiABBhDGIoFMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIIEAAYgAQYogRIy1NQAFjSTXABeAGQAQKYAVugAZcKqgECMja4AQPIAQD4AQL4AQGYAgKgAlGoAhTCAgcQLhgnGOoCwgIHECMYJxjqAsICFBAAGIAEGOMEGLQCGOkEGOoC2AEBmAMJ8QUhJW-_HEsg4boGBggBEAEYAZIHATKgB4tX&sclient=gws-wiz-serp',
                            data='action=002'
                        )
                    ),
                     ImageCarouselColumn(
                        image_url='https://imgur.com/X1EdkKp',
                        action=PostbackAction(
                            label='中式料理',
                            display_text='https://www.google.com/search?q=%E4%B8%AD%E5%BC%8F%E6%96%99%E7%90%86&oq=%E4%B8%AD%E5%BC%8F%E6%96%99%E7%90%86&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhDGIAEGIoFMgwIARAAGEMYgAQYigUyDAgCEAAYQxiABBiKBTIHCAMQABiABDIMCAQQABhDGIAEGIoFMgwIBRAAGEMYgAQYigUyBwgGEAAYgAQyBwgHEAAYgAQyBwgIEAAYgAQyDAgJEAAYQxiABBiKBdIBCDEwNjhqMGo5qAIAsAIA&sourceid=chrome&ie=UTF-8',
                            data='action=003'
                        )
                    ),
                     ImageCarouselColumn(
                        image_url='https://imgur.com/G3DGczB',
                        action=PostbackAction(
                            label='法式料理',
                            display_text='https://www.google.com/search?q=%E6%B3%95%E5%BC%8F%E6%96%99%E7%90%86&oq=%E6%B3%95%E5%BC%8F%E6%96%99%E7%90%86&gs_lcrp=EgZjaHJvbWUyDggAEEUYORhDGIAEGIoFMgwIARAAGEMYgAQYigUyDAgCEAAYQxiABBiKBTIMCAMQABhDGIAEGIoFMgcIBBAAGIAEMgcIBRAuGIAEMgcIBhAAGIAEMgYIBxBFGDzSAQc2ODhqMGo5qAIAsAIA&sourceid=chrome&ie=UTF-8',
                            data='action=004'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
