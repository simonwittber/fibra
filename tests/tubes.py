import fibra

def a(tube):
    print 'Pushing "a" into tube.'
    yield tube.push('a')
    print "Push is completed."
    yield 5
    yield tube.push('b')

def b(tube):
    print 'Blocking for 1 second.' 
    yield 1
    x = yield tube.pop()
    print 'Received "%s" from tube.'%x
    print "Waiting for pop..."
    x = yield tube.pop()
    print 'Received "%s" from tube.'%x

t = fibra.Tube()
schedule = fibra.schedule()
schedule.install(a(t))
schedule.install(b(t))
schedule.run()
