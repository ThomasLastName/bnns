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
folder_I_want_to_import_from = "bnns"

path = os.getcwd()
context, dirname = os.path.split(path)
while not dirname==folder_I_want_to_import_from:
    path = context
    context, dirname = os.path.split(path)
    if len(dirname)==0:
        raise OSError(f"The directory {folder_I_want_to_import_from} is not an ancestor of the working directory {os.getcwd()}")

sys.path.append(path)
from bnns.SSGE import func

func()
