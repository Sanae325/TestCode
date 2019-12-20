# class Student(object):

#     def __init__(self, name, score):
#     #通过定义一个特殊的__init__方法，
#     #在创建实例的时候，就把name，score等属性绑上去：    
#         self.name = name
#         self.score = score

#     def print_score(self):  #定义打印格式
#         print('%s : %s' % (self.name, self.score))

# bart = Student('Bart Simpson', 59)
# lisa = Student('Lisa Simpson', 87)
# bart.print_score()
# lisa.print_score()



class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 59)
print(bart.get_name())
bart.set_score(60)
print(bart.get_score())

