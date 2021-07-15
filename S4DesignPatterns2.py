"""
    Factory Design Pattern
"""
class Plan:

    def __init__(self, plan_name="basic", price=200, validity=1):
        self.plan_name = plan_name
        self.price = price
        self.validity = validity

    def show_plan(self):
        print("PLAN DETAILS: NAME:{plan_name}, PRICE \u20b9:{price}, VALID FOR:{validity}".format_map(vars(self)))

class Plan3G(Plan):

    def activate_plan(self):
        self.plan_name = "Plan 3G"
        self.price += 100

    def show_plan(self):
        print("PLAN 3G DETAILS: NAME:{plan_name}, PRICE \u20b9:{price}, VALID FOR:{validity}".format_map(vars(self)))


class Plan4G(Plan):

    def activate_plan(self):
        self.plan_name = "Plan 4G"
        self.price += 200
        self.validity = 1.5

    def show_plan(self):
        print("PLAN 4G DETAILS: NAME:{plan_name}, PRICE \u20b9:{price}, VALID FOR:{validity}".format_map(vars(self)))


class Plan5G(Plan):

    def activate_plan(self):
        self.plan_name = "Plan 5G"
        self.price += 300

    def show_plan(self):
        print("PLAN 5G DETAILS: NAME:{plan_name}, PRICE \u20b9:{price}, VALID FOR:{validity}".format_map(vars(self)))

# Factory Design Pattern
class PlanFactory:

    @staticmethod
    def get_plan(type_of_plan):

        plan = None

        if type_of_plan == 3:
            plan = Plan3G()
        elif type_of_plan == 4:
            plan = Plan4G()
        elif type_of_plan == 5:
            plan = Plan5G()
        else:
            plan = Plan()

        return plan

def main():

    print("3 -> Plan 3G")
    print("4 -> Plan 4G")
    print("5 -> Plan 5G")
    plan_choice = int(input("Please Select Your Plan Choice: "))

    plan = PlanFactory.get_plan(plan_choice)
    plan.activate_plan()
    plan.show_plan()

if __name__ == '__main__':
    main()
