def dedupe(dname="", recurse=True, display=True):
    '''
    Remove duplicate files from a given directory or tree.
    
    Arguments:
        dname (str)                 -- directory name
        recurse (bool) default=True -- recursive search or not
        display (bool) default=True -- send info to console
    '''
    import os

    res = {dirpath: filenames for dirpath, dirname, filenames in os.walk(dname)}
    for key, value in res.items():
        print(key, value)
    return res