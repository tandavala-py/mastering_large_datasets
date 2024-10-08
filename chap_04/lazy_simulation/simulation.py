import random, itertools
from operator import methodcaller

class Village:
    def __init__(self):
        self.population = random.uniform(1000, 5000)
        self.cheat_rate = random.uniform(0.5, .15)

    def go_fishing(self):
        if random.uniform(0, 1) < self.cheat_rate:
            cheat = 1
            fish_taken = self.population * 2
        else:
            cheat = 0
            fish_taken = self.population * 1
        return fish_taken, cheat

    def update(self, sim):
        if sim.cheaters >= 2:
            self.cheat_rate += .05
        self.population = int(self.population*1.025)

class LakeSimulation:
    def __init__(self):
        self.villages = [Village() for _ in range(4)]
        self.fish = 80000
        self.year = 1
        self.cheaters = 0

    def simulate(self):
        for _ in itertools.count():
            yearly_result = map(methodcaller("go_fishing"), self.villages)
            fishes, cheats = zip(*yearly_result)
            total_fished = sum(fishes)
            self.cheaters = sum(cheats)

            if self.year > 1000:
                print("Wow! your villeges lasted 1000 years!")
                break
            if self.fish < total_fished:
                print(f"The lake was overfished in {self.year}")
                break
            else:
                self.fish -= total_fished
                self.fish = self.fish*1.15
                map(lambda x:x.update(self), self.villages)
                print("Year {:<5} Fish: {}".format(self.year, int(self.fish)))
                self.year += 1


if __name__ == '__main__':
    random.seed("map and reduce")
    Lake = LakeSimulation()
    Lake.simulate()
    Lake.simulate()
    Lake.simulate()
    Lake.simulate()
