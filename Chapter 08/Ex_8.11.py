import pandas as pd
#Creating a Dataset
mydataset = {
    'Fruits': ["Orange", "Banana", "Apple", "Peer"],
    'Quantity' : [3,7,2,10]
}
#Creating DataFrame using Dataset
myvar=pd.DataFrame(mydataset)
print(myvar)
