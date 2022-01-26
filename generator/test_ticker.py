from time import perf_counter
from __drafts.process_ticker import TickerProcess
from multiprocessing import Manager
from time import perf_counter, sleep

# TODO:
# Maybe printer can be child of logger?


class Printer(TickerProcess):

    def __init__(self,
                 #  labels,
                 freq=100,
                 name='printer',
                 digits=4,
                 niceness=10):

        TickerProcess.__init__(self, freq, name=name, niceness=niceness)
        # manager = Manager()
        # self.output = manager.dict()
        # self.digits = digits
        self.variables = Manager().Namespace()
        self.variables.i = 0

    def on_init(self):
        self.variables.i += 1

    def on_interrupt(self):
        print('\n')

    def target(self):
        # print('The data\n', end=" ", flush=True)
        # for label in self.labels:
        self.variables.i += 1
        # print(self.i,end="\n", flush=True)

        # print((self.label_size)*'\033[A', end="\r", flush=True)


freq = 100
printer = Printer(freq=freq)
printer.start()
printer.pause()
# sleep(1.0)
# printer.resume()
# printer.
t0 = perf_counter()
t = 0

scale = 5
while t <= 20:
    t = (perf_counter() - t0)*scale
    if t >=1 and t<11:
        printer.resume()    
    if t >= 11 and t<16:
        printer.pause()
    if t >= 16:
        printer.resume()
    print(t,printer.variables.i)
printer.pause()
print(printer.variables.i)
print(scale*100*printer.variables.i/(14*freq))
printer.close()
