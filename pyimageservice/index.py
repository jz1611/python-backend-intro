import tornado.web
import tornado.ioloop

if __name__ == "__main__":
    app = tornado.web.Application([
        ("/img/(.*)", tornado.web.StaticFileHandler, {"path" : "img"})
    ])

    app.listen(8080)
    print("Listening on port 8080")

    tornado.ioloop.IOLoop.instance().start()