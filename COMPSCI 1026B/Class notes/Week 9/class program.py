
class Section:
    def __init__(self,course,students):
        self._course = course
        self._students = students
    def getCourse(self):
        return self._course
    def setCourse(self, newVal):
        self._course = newVal
    def getStudents(self):
        return self._students
    def setStudents(self, newVal):
        self._students = newVal
    def getStudentsAsText(self):
        text = ""
        for stu in self._students:
            text+= "-"+ stu.getInfo()+ '\n'
        return text
    def addStudent(self,newStudent):
        self._students.append(newStudent)
    def bonusForAllStudent(self, howMany, passMark):   ## long names are always welcome. Thedse are sometimes called self-commented names
        for stu in self._students:
            if stu.getMark() < passMark:
                stu.bonusToMe(howMany)

    def getAvg(self):
        sum = 0 
        for stu in self._students:
            sum+= stu.getMark()
        return sum/len(self._students)
    

    def getPassStudents(self):
        passing = []
        for stu in self._students:
            if stu.getMark() >= 50:
                passing.append(stu)
        return passing
class Student:
    def __init__(self, name, mark):
        self._name = name
        self._mark = mark
    def getName(self):
        return self._name
    def setName(self, newValue):
        self._name = newValue
    def getMark(self):
        return self._mark
    def setMark(self, newList):
        self._students = newList
    def getInfo(self):
        return "My name is %s and mark = %d" %(self._name, self._mark)
    def bonusToMe(self,howMany):
        self._mark += howMany

def main():
    sec1 = Section("1026B", None)
    print(sec1.getCourse())
    lst= []
    for i in range (3):
        stu = Student("stu name"+ str(i),0)
        lst.append(stu)
    sec1.setStudents(lst)
    print("original section:")
    print(sec1.getStudentsAsText())

    newStu = Student("New stu", 80)
    print("section after addding new student")
    sec1.addStudent(newStu)
    print(sec1.getStudentsAsText())

    print("section after giving bonus:")
    sec1.bonusForAllStudent(10,50)
    print(sec1.getStudentsAsText())
    print("Avg = ", sec1.getAvg())
    print("Passing students =", sec1.getPassStudents())



main()


