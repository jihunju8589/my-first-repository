# 다음은 Calculator 클래스이다.

# class Calculator:
#     def __init__(self):
#         self.value = 0

#     def add(self, val):
#         self.value += val


# 위 클래스를 상속하는 UpgradeCalculator를 만들고 값을 뺄 수 있는 minus 메서드를 추가해 보자. 즉 다음과 같이 동작하는 클래스를 만들어야 한다.

# cal = UpgradeCalculator()
# cal.add(10)
# cal.minus(7)
class Calculator:
    def __init__(self):
        self.value =0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def sub(self, val2):
        self.value-=val2
cal = UpgradeCalculator()
cal.add(10)
cal.sub(7)
print(cal.value)



