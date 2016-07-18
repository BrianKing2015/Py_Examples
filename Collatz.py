# Collatz Sequence

import time
import random
import logging

logging.basicConfig (filename = 'OutputLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

def collatz(collatznumber):
    logging.debug ('Start of Loop, the number was (%s)' %(collatznumber))
    try:
        while collatznumber != 1:
            if collatznumber % 2 == 0:
                logging.debug ('Start of even (%s)' %(collatznumber))
                collatznumber = collatznumber //2
                print collatznumber


            elif collatznumber %2 == 1:
                logging.debug ('Start of odd (%s)' %(collatznumber))
                collatznumber = collatznumber *3 +1
                print collatznumber

    except TypeError:
        print 'Please enter a number!'



if __name__ == "__main__":
    rant = random.randint(1,200)
    #rant = 'puppy'
    collatz(rant)
    time.sleep(5)