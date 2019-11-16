import tornado.ioloop
import tornado.web
import json
import handler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        self.write('ok')

    def post(self):
        data = json.loads(self.request.body, encoding='utf-8')
        handler.handler(data)
        self.write('ok')


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(50383)
    tornado.ioloop.IOLoop.current().start()
