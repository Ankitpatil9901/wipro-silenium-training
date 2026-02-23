# multiple Inheritance is 2 parents and 1 child

class Parent1:
    pass

class Parent2:
    pass

class child(Parent1, Parent2):
    pass

class Father:
    def driving(self):
        print("Father has the skills to drive")

class MOther:
    def cooking(self):
        print("Mother has the skills to cook")

class Child(Father, MOther):
    def bothskills(self):
        print("Child has both skills")
        print("Child has a skill to study")


c = Child()
c.driving()
c.cooking()
c.bothskills()