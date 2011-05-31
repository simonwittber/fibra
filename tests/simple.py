import fibra

def task_a():
    for i in xrange(10):
        print 'In Task A'
        yield None

def task_b():
    for i in xrange(10):
        print 'In Task B'
        yield None

def test():
    s = fibra.schedule()
    s.install(task_a())
    s.install(task_b())
    s.run()


if __name__ == "__main__":
    test()
