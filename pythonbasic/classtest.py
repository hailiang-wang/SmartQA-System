#-*- coding:utf-8 -*-
class Person(object):
    pass

xiaoming = Person()
xiaohong = Person()

print xiaoming
print xiaohong
print xiaoming==xiaohong

print cmp(2,3)
#定义类之后，可以实例化后，为不同的实例赋予不同的属性
class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'
p3.job ='programmer'

L1 = [p1, p2, p3]
L2 = sorted(L1,lambda p1,p2:cmp(p1.name,p2.name))

print L2[0].name
print L2[1].name
print L2[2].name
print L2[2].job
#也可以在实例初始化时，就设定好
class Person(object):
    def __init__(self,nam,gender,birth,**kw):
        self.name=nam
        self.gender=gender
        self.birth=birth
        for k,v in kw.iteritems():
            setattr(self,k,v)

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print xiaoming.name
print xiaoming.job
#Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问。
class Person(object):
    def __init__(self, name, score):
        self.name=name
        self.__score=score

p = Person('Bob', 59)

print p.name
try:
    print p.__score
except AttributeError:
    print 'attributeerror'
#实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。类属性发生改变，所有的都改变
class Person(object):
    count= 0
    def __init__(self,name):
        Person.count= Person.count + 1
        self.name= name

p1 = Person('Bob')
print Person.count

p2 = Person('Alice')
print Person.count

p3 = Person('Tim')
print Person.count

#当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。 千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。

class Person(object):

    __count = 0

    def __init__(self, name):
        Person.__count=Person.__count+1
        self.name=name
        print Person.__count

p1 = Person('Bob')
p2 = Person('Alice')

try:
    print Person.__count
except AttributeError:
    print 'attributeerror'

#实例的方法就是在类中定义的函数，它的第一个参数永远是 self，指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的：
#调用实例方法必须在实例上调用：也就是说必须先初始化
class Person(object):

    def __init__(self, name, score):
        self.name=name
        self.__score=score

    def get_grade(self):
        if self.__score>80:
            return 'A'
        elif self.__score>=60:
            return 'B'
        elif self.__score<60:
            return 'C'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


