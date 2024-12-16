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

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text  # 正確提取用戶訊息文字
    
    # 處理推薦餐廳的邏輯
    if message and re.match('推薦餐廳', message):
        image_carousel_template_message = TemplateSendMessage(
            alt_text='推薦餐廳',  # 替代文字，當用戶無法顯示圖片時會顯示此訊息
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/cJ7xDKq.jpg',  # 正確的圖片 URL
                        action=PostbackAction(
                            label='日式料理',
                            display_text='日式料理',
                            data='action=001'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/dhzPsMT.jpg',  # 正確的圖片 URL
                        action=PostbackAction(
                            label='西式料理',
                            display_text='西式料理',
                            data='action=002'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/X1EdkKp.jpg',  # 正確的圖片 URL
                        action=PostbackAction(
                            label='中式料理',
                            display_text='中式料理',
                            data='action=003'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/G3DGczB.jpg',  # 正確的圖片 URL
                        action=PostbackAction(
                            label='法式料理',
                            display_text='法式料理',
                            data='action=004'
                        )
                    )
                ]
            )
        )
        # 回應圖片輪播訊息
        line_bot_api.reply_message(event.reply_token, image_carousel_template_message)
    else:
        # 回應其他未知指令
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='無法識別的指令'))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
