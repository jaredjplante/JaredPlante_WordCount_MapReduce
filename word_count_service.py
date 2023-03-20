import rpyc
from map_reduce_functions import reduce
from map_reduce_functions import map

class word_count_service(rpyc.Service):
    def exposed_map(self, filename):
        return map(filename)

    def exposed_reduce(self, count_list):
        return reduce(count_list)

if __name__ == '__main__':
    from rpyc.utils.server import ThreadedServer

    t = ThreadedServer(word_count_service, port=18861)
    t.start()