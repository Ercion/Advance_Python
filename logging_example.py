#Demonstrate the loggig api in Python

import logging

def main():
    #use basicConfig to configure logging
    logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        filemode="w")

    #Try out each of the log level
    logging.debug("Debug Message")
    logging.info("info")
    logging.warning("Warning")
    logging.error("Eroor")
    logging.critical("Critical")
    logging.info("Here is a {} variable".format("string"))


if __name__=="__main__":
    main()