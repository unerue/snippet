import pandas as pd
import numpy as np
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os
import platform
from IPython import get_ipython

from IPython.core.interactiveshell import InteractiveShell


from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print('Completed setting {:.3f}'.format(time.time() - start_time))
        return
    return wrapper


class InitialAnalysis:
    def __init__(self, *kwargs):
        pass
    
    @timeit
    def setting(self):
        ipython = get_ipython()
        if 'ipython' in globals():
            print('\nWelcome to IPython!')
            ipython.magic('load_ext autoreload')
            ipython.magic('autoreload 2')
            
        InteractiveShell.ast_node_interactivity = 'all'
        
        import numpy as np
        import sys
        print('Python: {}'.format(sys.version))
        import numpy as np
        


        
        print('Initializing analysis environment...')
        self.loadling_libraries()
        print('* current working directory: {}'.format(os.getcwd()))
        for name in glob.glob('input/*'):
            print(name)
#         file_name = input()
        
        print('pandas {}, numpy {}, '.format(pd.__version__, np.__version__))
        

    
    def _set_pandas(self):
        pd.options.display.max_columns = 50
        
        pass
    
    def _set_matplotlib(self):
        if platform.system() == 'Windows':
            font_name = font_manager.FontProperties(fname='c:/Windows/Fonts/malgun.ttf').get_name()
            rc('font', family=font_name)
        else:
            rc('font', family='AppleGothic')
        
#         %matplotlib inline
        sns.set_style(style='white')
        plt.rcParams['axes.unicode_minus'] = kwargs.get('unicode_minus')
        
        pass
    
    def _set_jupyter(self):
        pass
    
    
    def check_datatypes(self):
        pass
    
    def check_missing(self):
        df.isnull().any()
        df.isnull().sum()
        df.isnull().sum()[df.isnull().sum()].to_frame()
        pass
    
    
    def loadling_libraries(self):
        import numpy as np
        

    
if __name__ == '__main__':
    InitialAnalysis().setting()
    
    
    