import tornado.ioloop
import tornado.web
import json
import handler


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        data = json.loads(self.request.body)
        handler.handler(data)


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/", MainHandler),
    ])
    application.listen(50383)
    tornado.ioloop.IOLoop.current().start()
