# -*- coding: utf-8 -*-
"""Copy of Assignment_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d8rzyhdvdvYPi59OIsSoTQJdnzvikLvb

# Basic Python

## 1. Split this string
"""

s = "Hi there Sam!"

s = "Hi there sam"
s.split()

"""*`italicized text`*## 2. Use .format() to print the following string. 

### Output should be: The diameter of Earth is 12742 kilometers.
"""

planet = "Earth"
diameter = 12742

planet = "Earth"
diameter = 12742
print = ("The diameter of {} is {} kilometors.".format(planet,diameter))

"""## 3. In this nest dictionary grab the word "hello"
"""

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
d['k1'][3]['tricky'][3]['target'][3]

"""# Numpy"""

import numpy as np

"""## 4.1 Create an array of 10 zeros? 
## 4.2 Create an array of 10 fives?
"""

import numpy as np
array = np.zeros(10)
array

import numpy as np
array = np.ones(10)*5
(array)

"""## 5. Create an array of all the even integers from 20 to 35"""

import numpy as np
array = np.arange(20,36)
("array of all the even integer from 20 to 35 ")
(array)

"""## 6. Create a 3x3 matrix with values ranging from 0 to 8"""

c=np.arange(9).reshape(3,3)

"""## 7. Concatinate a and b 
## a = np.array([1, 2, 3]), b = np.array([4, 5, 6])
"""

import numpy as np 
a=np.array([1,2,3])
b=np.array([4,5,6])
np.concatenate((a,b))

"""# Pandas

## 8. Create a dataframe with 3 rows and 2 columns
"""

import pandas as pd

import pandas as pd
import numpy as np
A= np.random. randint(10,size=(3,2))

"""## 9. Generate the series of dates from 1st Jan, 2023 to 10th Feb, 2023"""



"""## 10. Create 2D list to DataFrame

lists = [[1, 'aaa', 22],
         [2, 'bbb', 25],
         [3, 'ccc', 24]]
"""

lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]

lists=[[1,'aaa',22],[2,'bbb',25],[3,'ccc'24]]
df=pd.DataFrame(lists,columns=['Index','letter','num'])