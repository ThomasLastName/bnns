try:
    from bnns.SSGE import func
except:
    #
    # ~~~ Add the root directory of the repo to sys.path
    import sys
    import os
    path = os.getcwd()
    while not os.path.exists(os.path.join(path,".git")):
        path, dirname = os.path.split(path)
        if len(dirname)==0:
            raise OSError(f"The stopping criterion was not met by any ancestor of the working directory {os.getcwd()}")
    sys.path.append(path)
    #
    # ~~~ Now import
    from bnns.SSGE import func

func()
