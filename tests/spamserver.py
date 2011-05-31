import socket
import fibra
import fibra.net

port = 4200

def handler(transport):
    try:
        while True:
            try:
                line = yield transport.recv_line()
                n = parse_request(line)
                yield transport.send_line("100 SPAM FOLLOWS")
                for i in xrange(n):
                    yield transport.send_line("spam glorious spam")
            except BadRequest:
                yield transport.send_line("400 WE ONLY SERVE SPAM")
    except socket.error:
        pass 
      
class BadRequest(Exception):
    pass
  
def parse_request(line):
    tokens = line.split()
    if len(tokens) != 2 or tokens[0] != "SPAM":
      raise BadRequest
    try:
      n = int(tokens[1])
    except ValueError:
      raise BadRequest
    if n < 1:
      raise BadRequest
    return n

schedule = fibra.schedule()
schedule.install(fibra.net.listen(('localhost', port), handler))
schedule.run()
