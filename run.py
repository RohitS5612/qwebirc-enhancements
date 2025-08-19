from twisted.internet import reactor, protocol
import config

class IRCClient(protocol.Protocol):
    def connectionMade(self):
        print(f"Connected to {config.IRCSERVER}:{config.IRCPORT} as {config.NICK}")
        self.transport.write(f"NICK {config.NICK}\r\n".encode())
        self.transport.write(f"USER {config.IDENT} 0 * :{config.NICK}\r\n".encode())

    def dataReceived(self, data):
        print(data.decode(errors='ignore'))

class IRCFactory(protocol.ClientFactory):
    protocol = IRCClient

reactor.connectTCP(config.IRCSERVER, config.IRCPORT, IRCFactory())
reactor.run()
