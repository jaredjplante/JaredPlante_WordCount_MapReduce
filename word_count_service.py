import rpyc
from map_reduce_functions import reduce
from map_reduce_functions import mapper

class word_count_service(rpyc.Service):
    def exposed_mapper(self, data):
        return mapper(data)

    def exposed_reduce(self, key, value):
        return reduce(key, value)

if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(word_count_service, port=18861)
    t.start()