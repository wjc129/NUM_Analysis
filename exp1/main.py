import numpy as np
from calways import *


true_data = np.log(2)
value1 = func1(1)
value2 = func2(-0.5)
value3 = func3(1/3)

print("true_data:",true_data)
print("value1:",value1,'accuracy:',(true_data-value1)/true_data)
print("value2:",value2,'accuracy:',(true_data-value2)/true_data)
print("value3:",value3,'accuracy:',(true_data-value3)/true_data)

value2_1,i2 = fun2_1(-0.5)
value3_1,i3 = fun3_1(1/3)
print("value2_1:",value2_1,'accuracy:',(true_data-value2_1)/true_data,'num:',i2)
print("value3_1:",value3_1,'accuracy:',(true_data-value3_1)/true_data,'num:',i3)

print("ok"*52)