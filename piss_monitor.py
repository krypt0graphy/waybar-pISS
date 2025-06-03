#!/usr/bin/env python
import sys
import time
import json
from lightstreamer.client import *

sub = Subscription("MERGE", ["NODE3000005"], ["Value"])
sub.setRequestedSnapshot("yes")


class SubListener(SubscriptionListener):
    def onItemUpdate(self, update):
        value = update.getValue("Value")

        text = f"{value}%"
        data = {"text": text, "percentage": int(value)}
        print(json.dumps(data), flush=True)


sub.addListener(SubListener())

client = LightstreamerClient("http://push.lightstreamer.com", "ISSLIVE")
client.subscribe(sub)
client.connect()

while True:
    time.sleep(1)
