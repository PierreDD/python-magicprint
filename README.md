# python-magicprint
A pattern for self-documenting `print()` wrapper which introspectively includes its own line of code in the output.

What's the point of this? Allow us to explain:

During development you may find yourself doing this sort of thing:

```py
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
```

After enough of these quick-n-dirty print statements pile up, the console output becomes cluttered, and it is not clear which output comes from which print statement. So you may find yourself then doing THIS sort of thing:

```py
    print('demovar:', demovar)
    print('demolist:', demolist)
    print('demodict:', demodict)
    print('demodict[\'purpose\']:', demodict['purpose'])
```

We hated all the extra typing, and the potential for human error, and the maintenance overhead.  So we looked around for a way to have the `print()` function automatically describe the thing being printed.

## This turned out to be nontrivially hard.

After several hours of reading interesting stack-overflow and python-docs pages, and testing out methods involing the `inspect` module, the `linecache` module, the `sys` module, and others, this is the simplest method we came up with.  First, a demonstration:

```py
    magicprint(demovar)
    magicprint(demolist)
    magicprint(demodict)
    magicprint(demodict['purpose'])
```

The output:
```
** (demovar) **
I am a demo string

** (demolist) **
['I', 'am', 'a', 'demo', 'list']

** (demodict) **
{'name': 'demodict', 'purpose': 'to take over the world', 'deadline': 'tonight'}

** (demodict['purpose']) **
to take over the world
```

This works by walking back up the `traceback` and extracting the text of the line of code from the string.

```py
def magicprint(arg):
    strx = traceback.format_list(traceback.extract_stack(limit=2))[0]
    strx = strx.split('\n')[1].strip()
    strx = '** ' + strx[ strx.find('(') : ] + ' **'
    arg = str(arg)
    print (strx + '\n' + arg + '\n')
```

## As written, this requires Python 3
### This method has NOT BEEN TESTED in any of the following scenarios:
### 1. Threaded execution / multiprocessing execution
### 2. Alternative logging handlers (streams, remote etc)
