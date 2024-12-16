# -*- coding: utf-8 -*-

# 載入 LineBot 所需要的套件
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

# 必須放上自己的 Channel Access Token
line_bot_api = LineBotApi('kU4ar4S8kbgto4jk3y0N57JPsB5pRxWvI4yNkj31m1uqZaFtIvJnptg7J48moDnXB90oGVcNLO1nwiFwAQx+klALKYS6ACnWsdF8qYQe+4Ae+4gOlTrE7ww/M88SECkzylc7Cl6xTyijyFcvQdqrwgdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的 Channel Secret
handler = WebhookHandler('9c842edd49ecf2de4d59f754e476a760')

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

# 訊息傳遞區塊
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text

    if message == "推薦餐廳":
        imagemap_message = ImagemapSendMessage(
            base_url='https://imgur.com/pCTJVBR',  # 請替換為您的圖片 URL
            alt_text='推薦餐廳',
            base_size=BaseSize(height=1040, width=1040),
            actions=[
                URIImagemapAction(
                    link_uri='https://www.google.com/maps/search/%E6%97%A5%E5%BC%8F%E6%96%99%E7%90%86',
                    area=ImagemapArea(x=0, y=0, width=520, height=520)
                ),
                URIImagemapAction(
                    link_uri='https://www.google.com/maps/search/%E8%A5%BF%E5%BC%8F%E6%96%99%E7%90%86',
                    area=ImagemapArea(x=520, y=0, width=520, height=520)
                ),
                URIImagemapAction(
                    link_uri='https://www.google.com/maps/search/%E4%B8%AD%E5%BC%8F%E6%96%99%E7%90%86',
                    area=ImagemapArea(x=0, y=520, width=520, height=520)
                ),
                URIImagemapAction(
                    link_uri='https://www.google.com/maps/search/%E6%B3%95%E5%BC%8F%E6%96%99%E7%90%86',
                    area=ImagemapArea(x=520, y=520, width=520, height=520)
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)

    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))

# 主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
