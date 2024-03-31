class Solution(object):
    def lemonadeChange(self, bills):
        

        register = []

        cost_of_lemonade = 5

        for order in bills:
            if order == 5:
                register.append(5)
            elif order == 10:
                if 5 in register:
                    register.remove(5)
                    register.append(10)
                else:
                    return False
            else:
                if 5 in register and 10 in register:
                    register.remove(5)
                    register.remove(10)
                elif register.count(5) >= 3:
                    for j in range(3):
                        register.remove(5)
                else:
                    return False
        return True
