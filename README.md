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

