class models:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def data_models (self):
        print "Member Name: " ,self.name
        print "Age of the Member: " ,self.age
        print "*"*30


name1 = "Ahmed"
name2 = "Eosef"


mpdels1 = models(name1, 30)
mpdels2 = models(name2, 18)

models.data_models(mpdels1)
models.data_models(mpdels2)


class post:

    def __init__(self, delete, read, create, update):

        self.delete = delete
        self.read = read
        self.create = create
        self.update =update



