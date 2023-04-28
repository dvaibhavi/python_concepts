import pylint.lint 

import os

cwd = os.getcwd()
print(cwd)
path_for_file = os.path.join(os.getcwd(),'numpy_code.py')
print("path is", path_for_file)
Results = pylint.lint.Run([path_for_file], exit=False)

print(Results.linter.stats.global_note)


