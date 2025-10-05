# 2025-09-15
# オブジェクト指向プログラミングの基本

# 基本クラス(Animal)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

# サブクラス (Dog)
class Dog(Animal):
    def speak(self):
        print(f"{self.name}: woof!")


# サブクラス (Cat)
class Cat(Animal):
    def speak(self):
        print(f"{self.name}: meow!")

# メイン処理
if __name__ == "__main__":
    dog = Dog("pochi")
    cat = Cat("tama")

    dog.speak()  # Output: pochi: woof!
    cat.speak()  # Output: tama: meow!