import fdb

def hello(name, age):
    print('My name is '+name+', I am '+str(age)+' years old.')












fdb.set('say', hello, 'xiaoming', 18)

r = fdb.get('say')

r()

