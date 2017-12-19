import threading
import time

class my_thread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    pkts=[] 

    def __init__(self):
        super(my_thread, self).__init__()
        self._stop_event = threading.Event()
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                              #starts by default as soon as called

    """
    #########  To call a function in the thread  #########
    
        def __init__(self, target, *args):
            self._target = target
            self._args = args
            threading.Thread.__init__(self)

        def run(self):
            self._target(*self._args)
    """

    def stop(self):
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()
    def run(self, funct, args):
        """ 
        Method that runs forever

        ## Arguments
        + funct : A function object to be called
        + args : List of arguments
        
        ## Usage
        run(print_Hello, ['hello', 'world'])
        will attempt to call print_hello('hello', 'world')
        """
        while not self.stopped():
            # Do something
            funct(args[0], args[1])
            #print('Doing something imporant in the background')

    def return_packets(): # this function is to retrive the packets outside the thread
        return my_thread.pkts

"""
t = my_thread()
time.sleep(1)
t.stop()
"""