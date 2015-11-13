#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
iperf_driver.py: Implementation of iperf driver for WiSHFUL agent

Usage:
   iperf_driver.py [options] [-q | -v]
   iperf_driver.py --config

Options:
   -f                               foo
   -i, --interface interface        interfaces
   -p, --port port                  port for communication with server

Other options:
   -h, --help          show this help message and exit
   -q, --quiet         print less text
   -v, --verbose       print more text
   --version           show version and exit
"""

import logging
import time
import zmq
import random
import sys

__author__ = "Piotr Gawlowicz, Mikolaj Chwalisz"
__copyright__ = "Copyright (c) 2015, Technische Universität Berlin"
__version__ = "0.1.0"
__email__ = "{gawlowicz, chwalisz}@tkn.tu-berlin.de"

def main(args):
    log = logging.getLogger('iperf_driver.main')
    log.debug(args)

    port = args['--port']
    interfaces = args['--interface']

    #START client
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://localhost:%s" % port)

    while True:
        msg = socket.recv()
        print "IPERF driver recived ",msg
        socket.send("Msg from iperf_driver")
        time.sleep(1)

if __name__ == "__main__":
    try:
        from docopt import docopt
    except:
        print("""
        Please install docopt using:
            pip install docopt==0.6.1
        For more refer to:
        https://github.com/docopt/docopt
        """)
        raise

    args = docopt(__doc__, version=__version__)

    log_level = logging.INFO  # default
    if args['--verbose']:
        log_level = logging.DEBUG
    elif args['--quiet']:
        log_level = logging.ERROR

    logging.basicConfig(level=log_level,
        format='%(asctime)s - %(name)s.%(funcName)s() - %(levelname)s - %(message)s')

    main(args)
