#!/usr/bin/env python3
import os
import sys
import config
import logging
import parser

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format="%(message)s")

try:
    arguments = parser.parse()
    setup = config.Setup(arguments)
    setup.arguments()
    os.system("/usr/local/bin//$JUPYTER_ARGS")
except:
    logging.exception('failed!')
