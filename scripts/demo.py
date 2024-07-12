try:
    from ..bnns.SSGE import func
    print("relative import worked")
except:
    try:
        from bnns.SSGE import func
        print("absolute import worked")
    except:
            import os
            import sys
            path = os.getcwd()
            context, dirname = os.path.split(path)
            while not dirname=="bnns":
                print("path")
                path = context
                context, dirname = os.path.split(path)
                if len(dirname)==0:
                    raise Exception(f"bnns is not an ancestor of {os.getcwd()}")
            sys.path.append(path)
            print(f"adding {path} to the PATH")
            from bnns.SSGE import func
            print("hacked import worked")

func()
