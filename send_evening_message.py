import json
from datetime import datetime, timedelta
import pytz
import requests
from config import loadConfig

# Load configuration
config = loadConfig("config.yaml")
qywxWebhookKey = config.weChatWork.webhookKey
wxpushAppToken = config.wxPusher.appToken
wxpushTopicIds = config.wxPusher.topicIds

from datetime import datetime

def getDaysUntil(target_date):
    target_date = datetime.strptime(target_date, "%Y-%m-%d")
    now = datetime.now().replace(tzinfo=None)  # 确保当前时间是偏移不感知的
    return (target_date - now).days

# 示例用法
days_until_end = getDaysUntil("2024-10-27")
print(days_until_end)

def sendAlarmMsg(mdTex):
    wechatwork(mdTex)

def wechatwork(tex):
    webhook = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={qywxWebhookKey}"
    header = {"Content-Type": "application/json", "Charset": "UTF-8"}
    message = {"msgtype": "markdown", "markdown": {"content": tex}}
    message_json = json.dumps(message)
    try:
        requests.post(url=webhook, data=message_json, headers=header)
    except requests.exceptions.RequestException as e:
        print("unable to connect to wechat server, err:", e)
    except Exception as e2:
        print("send message to wechat server, err:", e2)
        sendAlarmMsg(str(e2))

def wxPusher(tex):
    url = "http://wxpusher.zjiecode.com/api/send/message"
    header = {"Content-Type": "application/json", "Charset": "UTF-8"}
    message = {
        "appToken": wxpushAppToken,
        "content": tex,
        "summary": "按时吃药提醒",
        "contentType": 2,
        "topicIds": wxpushTopicIds,
        "url": "http://wxpusher.zjiecode.com",
    }
    message_json = json.dumps(message)
    try:
        info = requests.post(url=url, data=message_json, headers=header)
        print(info.text)
    except requests.exceptions.RequestException as e:
        print("unable to connect to wx, err:", e)
        sendAlarmMsg(str(e))
    except Exception as e:
        print("send message to wx, err:", e)
        sendAlarmMsg(str(e))

if __name__ == "__main__":
    
    # 新增的提醒内容
    medication_reminder = (
    '宝宝快要下班了呢，记得按时吃药哦：<br>'
    '饭前半小时：雷贝拉唑 * 1，枸酸秘钾 * 2；<br>'
    '饭后半小时：阿莫西林 * 4，克拉霉素 * 2。'
)

    # 发送提醒内容到企业微信
    wechatwork(medication_reminder)

    # 发送提醒内容到WxPusher
    wxPusher(medication_reminder)
