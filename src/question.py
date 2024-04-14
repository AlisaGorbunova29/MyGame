import random

class Question():
    def __init__(self, cnt_vals, vals_name, units_of_measurement):
        self.cnt_vals = cnt_vals
        self.vals_name = vals_name
        self.units_of_measurement = units_of_measurement

    def creat_question(self):
        vals = [random.randint(1, 100) for i in range(self.cnt_vals)]
        vals[0] = vals[1]
        for i in range(2, self.cnt_vals):
            vals[0] *= vals[i]
        unknown_id = random.randint(0, self.cnt_vals - 1)

        given = f"Дано:"
        for i in range(0, self.cnt_vals):
            if (i != unknown_id):
                given = f"{given} {self.vals_name[i]} = {vals[i]} {self.units_of_measurement[i]}"
                if (i + 1 != self.cnt_vals):
                    given = f"{given},"
                else:
                    given = f"{given}."
        find = f"Найди значение {self.vals_name[unknown_id]} в {self.units_of_measurement[unknown_id]}"

        right_answer =  random.randint(0, 3)
        varient_answer = []
        flag_right = []
        for i in range(4):
            if (i != right_answer):
                varient_answer.append(f"{random.randint(1, 100)} {self.units_of_measurement[unknown_id]}")
                flag_right.append(False)
            else:
                varient_answer.append(f"{vals[unknown_id]} {self.units_of_measurement[unknown_id]}")
                flag_right.append(True)


        return [given, find, varient_answer, flag_right]




