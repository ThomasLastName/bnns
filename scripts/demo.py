try:
    from ..bnns.SSGE import func
    print("relative import worked")
except:
    try:
        from bnns import func
        print("absolute import worked")
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
            from bnns import func
            print("hacked import worked")

func()
