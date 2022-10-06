class Cards:
    def __init__(self, number):
        self.Cards_number = number

    def Shuffle_Cards(self):
        times = self.Cards_number
        brand = list(range(0, times))
        brand_copy = brand.copy()
        frequency = 0
        print('还原过程')
        while True:
            brand_1 = brand[:int(times / 2)]
            brand_2 = brand[int(times / 2):]
            brand_3 = list(zip(brand_1, brand_2))
            brand.clear()
            brand = [e for i in brand_3 for e in i]
            frequency += 1
            print(brand)
            if brand == brand_copy:
                print('还原成功')
                print('次数:', frequency)
                break


Cards_1 = Cards(50)
Cards_1.Shuffle_Cards()
