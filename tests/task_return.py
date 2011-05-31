import fibra


def task_y():
    print "task_y is starting"
    v = yield task_z()
    print "task_y received", v, "from task_z, expected 3."

def task_z():
    print "task_z is starting"
    yield None
    yield None 
    yield fibra.Return(3)
    yield fibra.Return(4)
    print "I should not get here."

    

def test():
    s = fibra.schedule()
    s.install(task_y())
    s.run()


if __name__ == "__main__":
    test()
