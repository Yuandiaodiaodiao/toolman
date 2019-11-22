import tornado.ioloop
import tornado.web
import json

globalMessage = []


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def pullMessage(self):
        return globalMessage
        pass

    def post(self):
        global globalMessage
        js = json.loads(self.request.body)
        print(js)
        if js.get('formBot'):
            res = self.pullMessage()
            self.write(json.dumps(res))
            globalMessage = []
            return
        else:
            if len(self.request.body) > 1:
                globalMessage.append(js)

            self.write('')
        return

def run():
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(9003)
    tornado.ioloop.IOLoop.current().start()
if __name__ == "__main__":
    run()
