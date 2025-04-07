import pandas

my_dataset = {
    'Cars' :['BMW', 'Mercedes', 'Audi'],
    'Year' :[2010, 2015, 2020]
}
df = pandas.DataFrame(my_dataset)

print(df)   

a = [10, 1, 2, 3.3, 4, 4.5, 5, 6, 7, 8, 9]


myvar = pandas.Series(a, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
print(myvar["d"])
print(myvar[0:4])