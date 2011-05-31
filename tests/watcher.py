import fibra


def task():
    yield None
    print 'raising'
    raise Exception('ARGH')


def watcher(e):
    print "watcher received:", type(e), e


schedule = fibra.schedule()
t = task()
schedule.install(t)
schedule.watch(t, watcher)
schedule.run()
