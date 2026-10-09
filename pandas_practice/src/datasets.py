import pandas as pd


mydataset = {
    'cars': ["BMW ", "Volvo","Ford"],
    'passings':[3,7,2]

}
myvar = pd.DataFrame(mydataset,index=['car1','car2','car3'])

print(myvar)
