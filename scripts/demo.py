# try:
#     from ..bnns.SSGE import func
#     print("relative import worked")
# except:
#     try:
#         from bnns.SSGE import func
#         print("absolute import worked")
#     except:
import os
import sys
path = os.getcwd()
context, dirname = os.path.split(path)
while not dirname=="bnns":
    path = context
    context, dirname = os.path.split(path)

sys.path.append(path)
from bnns.SSGE import func

func()
