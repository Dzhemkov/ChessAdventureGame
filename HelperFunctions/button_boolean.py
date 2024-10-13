class GlobalBoolean:
    def __init__(self, boolean_on=False):
        self.boolean_on = boolean_on

    def check_Boolean_On(self):
        return self.boolean_on

    def boolean_Make_On(self):
        self.boolean_on = True

    def boolean_Make_Off(self):
        self.boolean_on = False
