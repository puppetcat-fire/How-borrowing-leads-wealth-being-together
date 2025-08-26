import random
class Human:
    def __init__(self):
        self.money = 1000
        self.cost_need = 1
        self.preduct = 1
        self.repay_list = []
    
    def step(self, human_list, remove_list, Rate):
        if random.random()<0.0001:
            self.cost_need += 0.01
        if random.random()<0.0002:
            self.preduct += 0.01

        if random.random()<0.05:
            self.borrow(human_list)
        
        rm_list = []
        for i, item in enumerate(self.repay_list):
            self.repay_list[i][1] -= 1
            if self.repay_list[i][1] == 0:
                self.money -= 101
                self.repay_list[i][0].money += 101
                rm_list.append(item)

        for item in rm_list:
            self.repay_list.remove(item)
        
        if self.money<self.cost_need:
            for i in range(10):
                self.borrow(human_list)

        if self.money<self.cost_need:
            remove_list.append(self)
        
        self.money -= self.cost_need/Rate
        self.money += self.preduct

    def borrow(self, human_list):
        target = random.choice(human_list)
        if random.random()>0.3:
            if target.money>500:
                target.money -= 100
                self.money += 100
                self.repay_list.append([target, 30])



if __name__=="__main__":
    human_list = [Human() for _ in range(100000)]
    for _ in range(100000):
        all_cost = sum([human.cost_need for human in human_list])
        all_preduct = sum([human.preduct for human in human_list])

        Rate = all_preduct/all_cost
        # for human in human_list:
        #     human.cost_need /= all_preduct/all_cost

        remove_list = []
        for human in human_list:
            human.step(human_list, remove_list, Rate)

        for item in remove_list:
            human_list.remove(item)

        print(f"{len(human_list):.2f}, {all_cost:.2f}, {all_preduct:.2f}, {max([human.money for human in human_list]):.2f}, {min([human.money for human in human_list]):.2f} ,{sum([human.money for human in human_list])/len(human_list):.2f}")


        
