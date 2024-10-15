import json
from datetime import datetime
import pytz
import requests
from config import loadConfig

# Load configuration
config = loadConfig("config.yaml")
qywxWebhookKey = config.weChatWork.webhookKey
wxpushAppToken = config.wxPusher.appToken
wxpushTopicIds = config.wxPusher.topicIds
city = config.weather.city
monthOfBirthday = config.lover.monthOfBirthday
dayOfBirthday = config.lover.dayOfBirthday
expressLoveTimestamp = config.lover.expressLoveTimestamp
meetingTimestamp = config.lover.meetingTimestamp
weatherApiKey = config.weather.apiKey

def getMsgHeader():
    tz = pytz.timezone("Asia/Shanghai")
    dt = datetime.now(tz)
    return '今天是 <font color="info">{}</font>'.format(dt.strftime("%Y-%m-%d %A"))

class Weather:
    # 同样的Weather类实现...

def getWeather() -> Weather:
    # 同样的getWeather函数实现...

def getMeetingDay():
    # 同样的getMeetingDay函数实现...

def getBirthDayOfLover():
    # 同样的getBirthDayOfLover函数实现...

def getExpressLoveDay():
    # 同样的getExpressLoveDay函数实现...

class DailyWord:
    # 同样的DailyWord类实现...

def getDailyWord() -> DailyWord:
    # 同样的getDailyWord函数实现...

def sendAlarmMsg(mdTex):
    wechatwork(mdTex)

def wechatwork(tex):
    # 同样的wechatwork函数实现...

def wxPusher(tex):
    # 同样的wxPusher函数实现...

if __name__ == "__main__":
    h = getMsgHeader()
    w = getWeather()
    bd = getBirthDayOfLover()
    md = getMeetingDay()
    ed = getExpressLoveDay()
    dw = getDailyWord()

    # 企业微信
    tex1 = (
        '{}\n> 今天是我们相爱的<font color="warning"> {} </font>天（{}）\n'
        '我们已经相遇<font color="warning"> {} </font>天（{}）\n'
        '距离你的生日还有<font color="warning"> {} </font>天'
    ).format(
        h,
        ed,
        datetime.fromtimestamp(expressLoveTimestamp, tz=pytz.utc)
        .astimezone(pytz.timezone("Asia/Shanghai"))
        .strftime("%Y-%m-%d"),
        md,
        datetime.fromtimestamp(meetingTimestamp, tz=pytz.utc)
        .astimezone(pytz.timezone("Asia/Shanghai"))
        .strftime("%Y-%m-%d"),
        bd,
    )

    wechatwork(tex1)
    sendDailyWordToWechatWork(dw)
