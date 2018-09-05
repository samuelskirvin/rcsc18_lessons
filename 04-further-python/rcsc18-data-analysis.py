import glob
import numpy as np
import matplotlib.pyplot as plt

import analysis_tools

filenames = sorted(glob.glob('../03-fundamentals-of-python/inflammation*.csv'))

for f in filenames[:3]:
    print(f)
    analysis_tools.analyse(f)
    analysis_tools.detect_problems(f)
