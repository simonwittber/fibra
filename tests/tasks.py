import fibra

def task_a():
    """
    This task will spawn task C which will run to 
    completion, and then this task will finish.
    """
    print 'Task A is starting task C'
    yield task_x('C')
    print 'Task A is finishing'

def task_b():
    """
    This task will spawn task D which will run concurrently.
    It will finish after spawing task D.
    """
    print 'Task B is starting task D'
    yield fibra.Async(task_x('D'))
    print 'Task B is finishing'

def task_x(N):
    print 'Task %s is running' % N
    yield 10.0
    print 'Task %s is finishing' % N
    

def test():
    s = fibra.schedule()
    s.install(task_a())
    s.install(task_b())
    s.run()


if __name__ == "__main__":
    test()
