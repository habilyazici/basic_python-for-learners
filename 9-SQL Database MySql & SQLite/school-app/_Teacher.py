import datetime
class Teacher:
    def __init__(self, id, branch, name, surname, birthdate, gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.branch = branch
        self.name = name
        self.surname = surname
        self.birthdate = datetime.strptime(birthdate, '%Y-%m-%d').date()
        self.gender = gender

    @staticmethod
    def CreateTeacher(obj):
        list = []

        if isinstance(obj, tuple):
            list.append(Teacher(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5]))
        else:
            for i in obj:
                list.append(Teacher(i[0],i[1],i[2],i[3],i[4],i[5]))
        return list