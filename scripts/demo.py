try:
    from ..bnns.SSGE import func
except:
    try:
        from bnns import func:
    except:
            import os
            import sys
            path = os.getcwd()
            context, dirname = os.path.split(path)
            while not dirname=="bnns":
                path = context
                context, dirname = os.path.split(path)
                if len(dirname)==0:
                    raise Exception(f"bnns is not an ancestor of {os.getcwd()}")
            sys.path.append(path)

func()
