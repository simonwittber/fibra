import fibra


def task_a():
    for i in xrange(5):
        print 'Task A is going to sleep.'
        yield 1.0
        print 'Task A is awake.'
        yield None

def task_b():
    print "Task B is sleeping for 10 seconds."
    yield 10.0
    print 'Task B is awake.'

idle_count = 0
def idle():
    globals()["idle_count"] += 1
    

def test():
    s = fibra.schedule()
    s.install(task_a())
    s.install(task_b())
    s.register_idle_func(idle)
    s.run()

if __name__ == "__main__":
    test()
    print "Idle was called", idle_count, "times."
