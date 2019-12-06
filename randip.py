__author__ = "Julian Huch"
__version__ = "1.0"


"""
This is just a small Module to generate Random IP adresses
The IP and Port return as a string

Usage:
    randomip = RandomIPModule(4, 255, 35535)
    print(randomip)
    ip_dict = randomip.return_dict
    ip_list = randomip.return_list
    ip, port = randomip.return_vals
"""


import random


class IPDetails():
    def __init__(self, blocks: int=4, range: int=255, port: int=35535):
        self.ip_blocks = 4
        self.max_range = 255
        self.max_port = 35535

    def __repr__(self):
        return f"Module: {self.__class__.__name__}\n" \
                f"Blocks: {self.ip_blocks!r}\n" \
                f"MAX Range: {self.max_range!r}\n" \
                f"MAX Port: {self.max_port!r}\n"
        

class RandomIPModule(IPDetails):
    def __init__(self, *args, **kwargs):
        super(RandomIPModule, self).__init__(args, kwargs)
        self.ip, self.port = self.rnd_ip() 
    
    def __repr__(self):
        return IPDetails.__repr__(self) + \
               f"IP: {self.ip!r}\n" \
               f"Port: {self.port!r}"
    

    def return_vals(self):
        return self.ip, self.port
    
    def return_dict(self):
        return {
            "IP": self.ip,
            "Port": self.port,
        }
    
    def return_list(self):
        return list(self.ip, self.port)
 
    def rnd_ip(self):
        def ip():
            ip_list = map(str, [random.randint(0, self.max_range) for _ in range(self.ip_blocks)])
            return ".".join(ip_list)
        def port():
            port = str(random.randint(1, self.max_port))
            return port

        return ip(), port()


if __name__ == "__main__":
    """ This is just for Debugging """
    randomip = RandomIPModule(blocks=4, range=255, port=35535)
    print(randomip)
