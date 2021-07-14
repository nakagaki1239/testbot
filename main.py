from flask import Flask, request, abort
import os
 
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
 
app = Flask(__name__)
 
#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["8b2c68e74a44e81da5ddc84389511a8c"]
 
line_bot_api = LineBotApi("kqaYUl/z6JUk9MwhIQ4GFwAXGRX8S5vjy+g7ULwYokaHRROCXumsR5PdjWsET0TkSPDcKDBfkidoP3juuJbE+ui5SxBZObKzi2v5u5+8w91nEwXIfKIoEAPb9kXQ9lf14XdsZLWy25O9QXKcF3QmdAdB04t89/1O/w1cDnyilFU=")
handler = WebhookHandler("8b2c68e74a44e81da5ddc84389511a8c")
 
@app.route("/")
def hello_world():
    return "hello world!"
 
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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 
if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT"))
    app.run(host="0.0.0.0", port=port)