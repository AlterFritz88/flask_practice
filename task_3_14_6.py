class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100
        # if deposit_cents + self.cents > 99:
        #     print('here')
        #     print((deposit_cents + self.cents) % 100)
        #     self.dollars += (deposit_cents + self.cents) // 100
        #     self.cents += (deposit_cents + self.cents) % 100
        # else:
        #     self.cents += deposit_cents


pig = PiggyBank(10, 20)
pig.add_money(0, 90)
print(pig.dollars, pig.cents)