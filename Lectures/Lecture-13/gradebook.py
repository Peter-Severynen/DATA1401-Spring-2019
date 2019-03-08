# Create some virtual classes

class base:
    __name=""
    
    def __init__(self,name):
        self.__name=name

    def name(self):
        return self.__name
    

class data(base):
    def __init__(self,name):
        base.__init__(self,name)
        
class alg(base):
    def __init__(self,name):
        base.__init__(self,name)

    
    
class grade(data):
    __value=0
    __numerical=True
    __gradebook_name=str()
    __letter_grades=["F-","F","F+","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
    
    def __init__(self,name,numerical=True,value=None):
        if value:
            if isinstance(value,(int,float)):
                self.__numerical=True
            elif isinstance(value,str):
                self.__numerical=False
            self.set(value)
        else:            
            self.__numerical=numerical
        self.__gradebook_name=name
        data.__init__(self,name+" Grade Algorithm")        

    def set(self,value):
        if isinstance(value,(int,float)) and self.__numerical:
            self.__value=value
        elif isinstance(value,str) and not self.__numerical:
            if value in self.__letter_grades:
                self.__value=value
        else:
            print self.name()+" Error: Bad Grade."
            raise Exception
    
    def value(self):
        return self.__value
    
    def numerical(self):
        return self.__numerical
    
    def gradebook_name(self):
        return self.__gradebook_name
    
    def __str__(self):
        return self.__gradebook_name+": "+str(self.__value)

class student(data):
    __id_number=0
    __grades=dict()
    
    def __init__(self,first_name, last_name,id_number):
        self.__id_number=id_number
        data.__init__(self,first_name+" "+last_name+" Student Data")

    def add_grade(self,a_grade,overwrite=False):
        if overwrite or not a_grade.gradebook_name() in self.__grades:
            self.__grades[a_grade.gradebook_name()]=a_grade
        else:
            print self.name()+" Error Adding Grade "+a_grade.name()+". Grade already exists."
            raise Exception

    def id_number(self):
        return __id_number
    
    def __getitem__(self,key):
        return self.__grades[key]
    
    def print_grades(self):
        for grade in self.__grades:
            print self.__grades[grade]
    

class grade_calculator(alg):
    __stats=False
    
    def __init__(self,name,stats):
        self.__stats=stats
        alg.__init__(self,name)

    def apply(self,a_grade):
        raise NotImplementedError
        

class uncurved_letter_grade_percent(grade_calculator):
    __grades_definition=[ (.97,"A+"),
                          (.93,"A"),
                          (.9,"A-"),
                          (.87,"B+"),
                          (.83,"B"),
                          (.8,"B-"),
                          (.77,"C+"),
                          (.73,"C"),
                          (.7,"C-"),
                          (.67,"C+"),
                          (.63,"C"),
                          (.6,"C-"),
                          (.57,"F+"),
                          (.53,"F"),
                          (0.,"F-")]
    __max_grade=100.
    __grade_name=str()
    
    def __init__(self,grade_name,max_grade=100.):
        self.__max_grade=max_grade
        self.__grade_name=grade_name
        grade_calculator.__init__(self,
                                  "Uncurved Percent Based Grade Calculator "+self.__grade_name+" Max="+str(self.__max_grade),
                                 False)
        

    def apply(self,a_grade):
        if not isinstance(a_grade,grade):
            print isinstance(a_grade,grade)
            print self.name()+ " Error: Did not get an proper grade as input."
            raise Exception
        if not a_grade.numerical():
            print self.name()+ " Error: Did not get a numerical grade as input."
            raise Exception

        percent=a_grade.value()/self.__max_grade
        
        for i,v in enumerate(self.__grades_definition):
            #print percent, i, v
            if percent>=v[0]:
                break
                            
        return grade(self.__grade_name,value=self.__grades_definition[i][1])

class grade_book(data):
    __students=dict()
    
    def __init__(self,name):
        data.__init__(self,name+" Course Grade Book")
        
    def add_student(self,a_student):
        self.__students[a_student.id_number]=a_student
        
    def assign_grade(self,key,a_grade):
        the_student=None
        try:
            the_student=self.__students[key]
        except:
            for id in self.__students:
                if key == self.__students[id].name():
                    the_student=self.__students[id]
                    break
        if the_student:
            the_student.add_grade(a_grade)
        else:
            print self.name()+" Error: Did not find student."
            
    
            
        
        
