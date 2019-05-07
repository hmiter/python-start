# -*- coding: UTF-8 -*-
import signal
import time
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import confs.settings as settings


def _ping_db():
    # Just a simple query
    settings.db.query("select 1")


def start():
    global http_server
    address, port = '0.0.0.0', settings.options.options.port

    import controllers.urls as urls
    application = tornado.web.Application(urls.urls, **settings.tornado_env)
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    http_server.listen(port, address)
    print ('run application on (%s:%s)' % (address, port))

    # ping db periodically to avoid mysql go away
    # tornado.ioloop.PeriodicCallback(_ping_db, int(settings.db_ping_seconds * 1000)).start()
    tornado.ioloop.IOLoop.instance().start()


def stop(_, __):
    dead_time = time.time() + 10

    def stop_loop():
        now = time.time()
        io_loop = tornado.ioloop.IOLoop.instance()
        if dead_time < now and (io_loop._callbacks or io_loop._timeouts):
            io_loop.add_timeout(now + 2, stop_loop)
        else:
            io_loop.stop()  # 处理完现有的 callback 和 timeout 后，可以跳出 io_loop.start() 里的循环

    global http_server
    tornado.ioloop.IOLoop.instance().add_callback(http_server.stop)
    tornado.ioloop.IOLoop.instance().add_timeout(time.time() + 2, stop_loop)


if __name__ == "__main__":
    # 只能在linux下使用
    # signal.signal(signal.SIGUSR1, stop)
    # signal.signal(signal.SIGTERM, stop)
    start()
