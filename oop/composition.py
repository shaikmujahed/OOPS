class Leg:
    pass

class Back:
    pass

class Chair:
    def __init__(self,num_legs):
        self.leg = [Leg() for leg in range(num_legs)]
        self.back = Back()

    def __repr__(self):
        return "I have {} legs and backs.".format(len(self.leg))

print(Chair(5))
