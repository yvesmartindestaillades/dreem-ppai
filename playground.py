import os, sys
path = os.path.dirname('/'.join(os.path.abspath(__file__).split('/')))
sys.path.append(path)

import pandas as pd
import pickle

d = pickle.load(open('/Users/ymdt/src/data/Lauren/470.p', 'rb'))

for name, mh in d.items():
    print(name)

for s,q in d['3407-O-flank_1=lp5-DB'].__dict__.items():
    print(s,q)

for s,q in d['3407-O-flank_1=lp5-DB'].__dict__.items():
    print(s,q)
exit()
