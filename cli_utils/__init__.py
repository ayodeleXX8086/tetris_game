import sys
valid_moves = {"up","down","left","right"}
if sys.platform.startswith("win"):
    from .win_utils import *
else:
    from .nx_utils import *
