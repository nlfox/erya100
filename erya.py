# coding=utf-8
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
            if 'courseAction!toCourseVideo' in flow.request.url:
                flow.response.content = re.sub("eval\(function.*?onStopMove\|mouseHander\|intervalTime\|function\|eryaPlayer.*?\)\,0\,\{\}\)\)",'',flow.response.content)
                print flow.response.content
            if 'playerAction!getResourceUrl' in flow.request.url:
                flow.response.content =re.sub(r'\"startTime\"\:(\d+)','"startTime":10',flow.response.content)
            flow.reply()

config = proxy.ProxyConfig(port=8080)
server = ProxyServer(config)
m = StickyMaster(server)
m.run()
