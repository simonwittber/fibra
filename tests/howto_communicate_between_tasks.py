
import fibra

def task_a(tube):
    yield tube.push('this string is pushed to a waiting task')

def task_b(tube):
    x = yield tube.pop()
    print "Received:", x

def task_c():
    tube = fibra.Tube("Named Tube")
    yield tube.push('this string is pushed into a named tube.')

def task_d():
    tube = fibra.Tube("Named Tube")
    x = yield tube.pop()
    print "Received from Named Tube:", x



t = fibra.Tube()
schedule = fibra.schedule()
schedule.install(task_a(t))
schedule.install(task_b(t))
schedule.install(task_c())
schedule.install(task_d())
schedule.run()
