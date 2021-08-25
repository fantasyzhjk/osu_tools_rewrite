import os

os.system("pip install -r requirements.txt")
try:
    os.system("python -m pip install git+https://github.com/The-CJ/oppadc.py.git#egg=oppadc")
except:
    os.system("python -m pip install git+https://hub.fastgit.org/The-CJ/oppadc.py.git#egg=oppadc")
