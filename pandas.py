#import pandas as pd
import scipy

with open('C:/Users/giripranay/Desktop/readme.txt','r') as rfile:
    filecontent=rfile.read()
    print(filecontent)
    with open('C:/Users/giripranay/Desktop/write.txt','w') as wfile:
        wfile.write(filecontent)
print(scipy.__version__)
