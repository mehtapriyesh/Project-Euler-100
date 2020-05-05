
#letter count
from time import time
s=time()
import inflect
p=inflect.engine()
a=''
for n in range(1,1000+1):    
    a+=p.number_to_words(n)

print(len(a.replace(" ","").replace("-","")))
print(time()-s)

#21124
#0.07395458221435547
