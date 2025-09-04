class ClassLesson:
    def __init__(self, classid, lessonid, teacherid):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.classid = classid
        self.lessonid = lessonid
        self.teacherid = teacherid

    @staticmethod
    def CreateClassLesson(obj):
        list = []

        for i in obj:
            list.append(ClassLesson(i[0],i[1],i[2],i[3]))
        return list