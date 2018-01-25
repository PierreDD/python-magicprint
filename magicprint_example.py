# A simple demonstration of a solution to a common problem in python.
# This is merely a suggested reference example.
# Please adapt the technique to your particular needs.

# This method has NOT BEEN TESTED in any of the following scenarios:
# 1. Threaded execution / multiprocessing execution
# 2. Alternative logging handlers (streams, remote etc)
# 3. Lots of stuff

import traceback
import logging
from  termcolor import colored
def stryellow(arg):
    return colored(arg, 'yellow', attrs=['bold'])


# when trying out various methods to solve this problem, this was helpful
# https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function
def magicprint(arg):
    strx = traceback.format_list(traceback.extract_stack(limit=2))[0]
    strx = strx.split('\n')[1].strip()
    strx = '** ' + strx[ strx.find('(') : ] + ' **'
    arg = str(arg)
    print (stryellow(strx) + '\n' + arg + '\n')


def magiclog(arg):
    strx = traceback.format_list(traceback.extract_stack(limit=2))[0]
    strx = strx.split('\n')[1].strip()
    arg = str(arg)
    logging.debug (strx + '\n' + arg + '\n')


def demo():
    demovar = 'I am a demo string'
    demolist = ['I', 'am', 'a', 'demo', 'list']
    demodict = {'name': 'demodict',
        'purpose': 'to take over the world',
        'deadline': 'tonight'}
    print("These are ordinary prints: \n\n")
    print(demovar)
    print(demolist)
    print(demodict)
    print(demodict['purpose'])
    print("\n")

    print("This is the manual, labor-intensive, DUMB way to document prints . . .\n")
    print('demovar:', demovar)
    print('demolist:', demolist)
    print('demodict:', demodict)
    print('demodict[\'purpose\']:', demodict['purpose'])
    print("\n")

    print("Ugly, hard to read, are not self-describing.  Now get ready for magic . . .\n")
    # demonstrate magicprint
    magicprint(demovar)
    magicprint(demolist)
    magicprint(demodict)
    magicprint(demodict['purpose'])

    print("Magic with logging . . .\n")
    # demonstrate with logging
    logging.basicConfig(level=logging.DEBUG,
                    format=('%(asctime)s: '    
                            '%(levelname)s: '
                            '%(message)s')
                    )    
    magiclog(demovar)
    magiclog(demolist)
    magiclog(demodict)
    magiclog(demodict['purpose'])


if __name__ == "__main__":
    demo()