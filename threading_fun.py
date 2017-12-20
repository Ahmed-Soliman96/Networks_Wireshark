import threading
import time


class my_thread(threading.Thread):
    """Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition."""

    pkts = []

    def __init__(self):
        super(my_thread, self).__init__()
        self._stop_event = threading.Event()
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True  # Daemonize thread
        thread.start()  # starts by default as soon as called

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
<<<<<<< HEAD

    def run(self, funct, args):
        """
=======
    def run(self, funct, args):
        """ 
>>>>>>> 809105bc74ddb33f9a8201b5c25dc2ab6708784a
        Method that runs forever

        ## Arguments
        + funct : A function object to be called
        + args : List of arguments
<<<<<<< HEAD

=======
        
>>>>>>> 809105bc74ddb33f9a8201b5c25dc2ab6708784a
        ## Usage
        run(print_Hello, ['hello', 'world'])
        will attempt to call print_hello('hello', 'world')
        """
        while not self.stopped():
            # Do something
<<<<<<< HEAD
            funct(args[0])  # , args[1])
            # print('Doing something imporant in the background')
=======
            funct(args[0], args[1])
            #print('Doing something imporant in the background')
>>>>>>> 809105bc74ddb33f9a8201b5c25dc2ab6708784a

    def return_packets():  # this function is to retrive the packets outside the thread
        return my_thread.pkts

"""
t = my_thread()
time.sleep(1)
t.stop()
"""