class clue(object):
    def __init__(self):
        self.value = 0
        self.question = ""
        self.answer = ""
        
class category(object):
    def __init__(self):
        self.cat_name = ""
        self.clue1 = clue()
        self.clue2 = clue()
        self.clue3 = clue()
        self.clue4 = clue()
        self.clue5 = clue()

class jeopardy(object):
    def __init__(self):
        self.category1 = category()
        self.category2 = category()
        self.category3 = category()
        self.category4 = category()
        self.category5 = category()
        self.category6 = category()

class d_jeopardy(object):
    def __init__(self):
        self.category1 = category()
        self.category2 = category()
        self.category3 = category()
        self.category4 = category()
        self.category5 = category()
        self.category6 = category()

class f_jeopardy(object):
    def __init__(self):
        self.category = ""
        self.question = ""
        self.answer = ""

class ep(object):
    def __init__(self):
        self.number = 0
        self.j = jeopardy()
        self.d = d_jeopardy()
        self.f = f_jeopardy()

