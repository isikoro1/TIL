class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def status(self):
        print(f"{self.name}のHPは {self.hp} ")

# インスタンスを作る
h1 = Hero("勇者A", 100)
h2 = Hero("勇者B", 80)

# それぞれのデータを持っている
h1.status()  # 勇者AのHPは100
h2.status()  # 勇者BのHPは80