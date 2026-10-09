import pandas as pd

#getting familiar with datasets :

mydataset = {
    'cars': ["BMW ", "Volvo","Ford"],
    'passings':[3,7,2]

}

fruits = {
    'name' :["apple", "banana", "cherry" , "watermelon"],
     'color' : ["red", "yellow", "blue" , "light green"]
}

myfruits = pd.DataFrame(fruits )

print(myfruits['name'])


myvar = pd.DataFrame(mydataset,index=['car1','car2','car3'])

print(myvar)

print(myvar.head(1))

print(myvar.tail(2))

myseries = pd.Series(myfruits['color'])
print(myseries)
mycars = pd.Series(mydataset['cars'])
print(mycars)
