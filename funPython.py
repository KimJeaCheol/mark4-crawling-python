def f(x):
    return x


var = f(10)
print(var)


def fx(x, y=20):
    return x + y


var2 = fx(10)
var3 = fx(10, 40)
print(var2)
print(var3)


class character:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print("생성자가 초기화되었습니다.")

    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self, 'attack')

    def show_info(self):
        print("hp: %d, attack: %d, defence: %d " %
              (self.hp, self.attack, self.defence))

    def __del__(self):
        print('종료처리')

    def __call__(self):
        print('콜처리')


player_a = character(10, 20, 30)
player_b = character(100, 200, 300)
