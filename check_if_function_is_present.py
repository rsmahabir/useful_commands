#This example uses the imp package and 'pip' as the package to search for
import imp
imp.find_module('pip')

#OUTPUT: (None,'/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/pip',
 ('', '', 5))
# In this case the location of the package is shown

#Searching for a made up package called 'errorDUDE' that does not exist will produce an error
#OUTPUT: imp.find_module('errorDUDE')
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/IPython/core/interactiveshell.py", line 2882, in run_code
    exec(code_obj, self.user_global_ns, self.user_ns)
  File "<ipython-input-29-78878b70c712>", line 1, in <module>
    imp.find_module('errorDUDE')
ImportError: No module named errorDUDE
