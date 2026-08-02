import pandas as pd
print(pd.__version__)

# pip install pandas # install the panda in global
# pip install virtualenv # install the virtualenv in global
# virtualenv venv # create a virtual environment in current directory
# # activate the virtual environment
# source venv/bin/activate

# # install the package in the virtual environment
# pip install pandas -v
# # with this command, the package will be installed in the virtual environment and not in the global environment.

# # deactivate the virtual environment
# deactivate

# # list the packages installed in the virtual environment
# pip freeze

# # save the list of packages installed in the virtual environment to a file
# pip freeze > req.txt