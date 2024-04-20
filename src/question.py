import random

class Question():
    def __init__(self, cnt_vals, vals_name, units_of_measurement, description):
        self.cnt_vals = cnt_vals
        self.vals_name = vals_name
        self.units_of_measurement = units_of_measurement
        self.description = description
    @staticmethod
    def round(x):
        s = str(x)
        i = s.find(".")
        if i != -1 and len(s) > 6:
                return s[:i+2]
        return s

    
    def creat_question(self):
        vals = [random.randint(2, 8) * 10**(random.randint(0,1) * 2 - 1) for i in range(self.cnt_vals)]
        vals[0] = vals[1]
        for i in range(2, self.cnt_vals):
            vals[0] *= vals[i]
        unknown_id = random.randint(0, self.cnt_vals - 1)

        randpermn = []
        for i in range(self.cnt_vals):
            if i != unknown_id:
                randpermn.append(i)
        random.shuffle(randpermn) # случайная перестановка
        given = f"Given:"
        for i in randpermn:
            given = f"{given} {self.vals_name[i]} = {Question.round(vals[i])} {self.units_of_measurement[i]}, "
        given = given[:-2] + "."
        find = f"Find {self.vals_name[unknown_id]}."
        
        # генерация неправильных ответов
        wrong_anss = [0,0,0,0]
        if unknown_id == 0:
            wrong_anss[0] = vals[unknown_id] * 10**(random.randint(0,1) * 2 - 1) # *10 or *0.1
            wrong_anss[1] = vals[unknown_id] / vals[1]**2
            wrong_anss[2] = 1 / vals[unknown_id]
            wrong_anss[3] = vals[unknown_id] / vals[2]**2
        else:
            index = 1 if unknown_id == 2 else 2
            wrong_anss[0] = vals[unknown_id] * 10**(random.randint(0,1) * 2 - 1) # *10 or *0.1
            wrong_anss[1] = vals[unknown_id] * vals[index]**2
            wrong_anss[2] = vals[unknown_id] * vals[index]**2 * 10**(random.randint(0,1) * 2 - 1)
            wrong_anss[3] = 1 / vals[unknown_id]

        randperm4 = [0,1,2,3]
        random.shuffle(randperm4) # случайная перестановка
        
        variant_answer = [f"{Question.round(wrong_anss[randperm4[i]])} {self.units_of_measurement[unknown_id]}" for i in range(4)] # неправильные ответы в случ. порядке
        flag_right = [False] * 4

        right_answer_ind =  random.randint(0, 3)
        variant_answer[right_answer_ind] = f"{Question.round(vals[unknown_id])} {self.units_of_measurement[unknown_id]}"
        flag_right[right_answer_ind] = True

        return [given, find, variant_answer, flag_right, self.description]




