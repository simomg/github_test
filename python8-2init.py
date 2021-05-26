# __init__

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# 이닛 함수에 셀프를 제외 정의된 갯수만큼 똑같이 만들어야 객체를 보낼수 있슴
marine3 = Unit("마린")
marine3 = Unit("마린", 40)