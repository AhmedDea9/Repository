def Atm (Request):

    Money = 500
    if Request > Money:
        return "There is not enough money"

    if Request <= 0 :

        return "You must withdraw more than zero"

    if Request < Money :

        while Request > 100:

            Request = Request - 100

            print "Give 100"

        while Request > 50:

            Request = Request - 50

            print "Give 50"

        while Request > 10:

            Request = Request - 10

            print "Give 10"

        while Request > 5:

            Request = Request - 5

            print "Give 5"

        while Request > 1:

            Request = Request - 1

            print "Give 1"
        return "The receipt of the request"

    else:
        return "There is not enough money"

print Atm()