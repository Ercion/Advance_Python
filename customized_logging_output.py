#Demonstrate how to customize logging output

import logging

#add another function to log from
def anotherFunction():
    logging.debug("This is a debug level message")

def main():
    fmtstr="½(asctime)s:%(levelname)s:%(funcName)s:Line:(lineno)d%(message)s"
    datestr="%m/%d/%Y%I:%M:%S %p"

    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    logging.info("This is an info-level lo message")
    logging.warning("This is an warning level message")
    anotherFunction()

if __name__=="__main__":
    main()