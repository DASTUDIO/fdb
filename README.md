# fdb

记下一个函数的调用，并且保存参数，在以后需要的地方再执行

可以用在 需要第三方回调触发服务端创建数据，因为某种原因又不想预创建的地方。

```python
import fdb

def hello(name, age):
    print('My name is '+name+', I am '+str(age)+' years old.')


fdb.set('say', hello, 'xiaoming', 18)

r = fdb.get('say')

r()

```
