# coding=utf-8
import json

__author__ = 'nlfox'
from libmproxy import controller, proxy
from libmproxy.proxy.server import ProxyServer
from libmproxy.protocol.http import decoded


class StickyMaster(controller.Master):
    def __init__(self, server):
        controller.Master.__init__(self, server)
        self.stickyhosts = {}

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, flow):
        flow.reply()

    def handle_response(self, flow):
        with decoded(flow.response):
            print flow.request.url
            import re
            if 'moocplayer.js' in flow.request.url:
                flow.response.content = re.sub(r'(MoocPlayer.prototype.switchWindow.*?)\/\*','/*',flow.response.content,flags=re.DOTALL)
            if 'initdatawithviewer' in flow.request.url:
                flow.response.content =re.sub(r'\"startTime\"\:(\d+)','"startTime":10',flow.response.content)
                jsonData = json.loads(flow.response.content)
                print "问题:",jsonData[0]["datas"][0]["description"],"答案:",
                for i in jsonData[0]["datas"][0]["options"]:
                    if i["isRight"]:
                        print i["description"]
            flow.reply()

config = proxy.ProxyConfig(port=8080)
server = ProxyServer(config)
m = StickyMaster(server)
m.run()
