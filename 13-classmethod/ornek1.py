class Student(object):
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @classmethod
    def from_string(cls, name_str):
        first_name, last_name = map(str, name_str.split(' '))
        student = cls(first_name, last_name)
        return student
    @staticmethod
    def is_full_name(name_str):
        names = name_str.split(' ')
        return len(names) >1
scott = Student('Scott',  'Robinson')

scott2 = Student.from_string('Scott Robinson')
print(scott2.first_name)
print(Student.is_full_name('Scott Robinson'))
 
 