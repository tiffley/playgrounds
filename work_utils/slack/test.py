import slackweb
import requests
import json

url = "https://hooks.slack.com/services/xxxx"

slack = slackweb.Slack(url=url)
slack.notify(text="pythonからslackさんへ")


payload = {"text": "This is a line of text in a channel.\nAnd this is another line of text."}
r = requests.post(url, data=json.dumps(payload))
print(r.text)
