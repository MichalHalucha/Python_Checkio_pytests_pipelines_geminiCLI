class Warrior:
    health = 50
    attack = 5
    defense = 0
    last_hit = True

    @property
    def is_alive(self):
        return self.health > 0

    def turn_attack(self, other, *army):
        self.last_hit = False
        if other.defense < self.attack:
            self.last_hit = True
            other.health -= self.attack - other.defense
            self.custom_attack(other, *army)

    def custom_attack(self, *_):
        pass

    def equip_weapon(self, weapon):
        for attr in vars(weapon):
            if getattr(self, attr, None):
                setattr(
                    self, attr, max(0, (getattr(self, attr) + getattr(weapon, attr)))
                )


class Knight(Warrior):
    attack = 7


class Defender(Warrior):
    health = 60
    attack = 3
    defense = 2


class Vampire(Warrior):
    health = 40
    attack = 4
    vampirism = 50

    def custom_attack(self, other, *army):
        if self.vampirism:
            self.health += int((self.attack - other.defense) / (100 / self.vampirism))


class Lancer(Warrior):
    health = 50
    attack = 6

    def custom_attack(self, _, *army):
        if not army:
            return
        # pół ataku na drugą jednostkę
        self.attack //= 2
        self.turn_attack(army[0])
        self.attack *= 2


class Healer(Warrior):
    health = 60
    attack = 0
    heal_power = 2

    def heal(self, unit):
        unit.health = min(type(unit).health, unit.health + self.heal_power)


class Warlord(Warrior):
    health = 100
    attack = 4
    defense = 2


def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_1.turn_attack(unit_2)
        if not unit_2.is_alive:
            return True
        unit_2.turn_attack(unit_1)
    return False


class Army(list):

    units = property(lambda self: self)

    def add_units(self, unit, n):
        for _ in range(n):
            # tylko 1 Warlord na armię
            if unit is Warlord and any(isinstance(u, Warlord) for u in self):
                continue
            self.append(unit())

    def has_warlord(self):
        return any(isinstance(u, Warlord) for u in self)

    def move_units(self):
        # jeśli nie ma Warlorda – nie robimy nic
        if not self.has_warlord():
            return

        # odfiltruj martwych (na wszelki wypadek)
        # UWAGA: nie wołamy tu remove_deaths(), żeby nie robić pętli
        alive_units = [u for u in self if u.is_alive]

        # jeśli nic lub tylko Warlord – nic do ustawiania
        warlords = [u for u in alive_units if isinstance(u, Warlord)]
        if not warlords:
            # nie powinno się zdarzyć, ale dla bezpieczeństwa
            self[:] = alive_units
            return

        warlord = warlords[0]
        others = [u for u in alive_units if not isinstance(u, Warlord)]

        if not others:
            # armia z samym Warlordem
            self[:] = [warlord]
            return

        # 1. front – Lancer, jeśli jest
        front_unit = None
        for u in others:
            if isinstance(u, Lancer):
                front_unit = u
                break

        # 2. jeśli nie ma Lancera – pierwszy inny wojownik z attack > 0 (nie Healer)
        if front_unit is None:
            for u in others:
                if not isinstance(u, Healer) and getattr(u, "attack", 0) > 0:
                    front_unit = u
                    break

        # 3. jeśli nie ma nikogo kto zadaje dmg (np. tylko Healerzy) – bierzemy pierwszą jednostkę
        if front_unit is None:
            front_unit = others[0]

        # Healerzy – wszyscy za pierwszą jednostką
        healers = [u for u in others if isinstance(u, Healer)]

        # Reszta wojowników (z zachowaniem oryginalnej kolejności), bez front_unit i Healerów
        rest = []
        for u in others:
            if u is front_unit:
                continue
            if isinstance(u, Healer):
                continue
            rest.append(u)

        # Nowy porządek: [front] + healerzy + reszta + [warlord]
        new_order = [front_unit] + healers + rest + [warlord]
        self[:] = new_order

    def fight(self, other):
        # początkowe ustawienie, jeśli są Warlordzi
        if self.has_warlord():
            self.move_units()
        if other.has_warlord():
            other.move_units()

        while self and other:
            killed = self.attack(other)
            if not other:
                return True
            if not killed:
                other.attack(self)
        return False

    def attack(self, other):
        self[0].turn_attack(*other)
        if self[0].last_hit and len(self) > 1 and type(self[1]) is Healer:
            self[1].heal(self[0])
        res = not other[0].is_alive
        other.remove_deaths()
        return res

    def remove_deaths(self):
        before = len(self)
        while self and not self[0].is_alive:
            del self[0]
        # jeśli coś się zmieniło i mamy Warlorda – przestawiamy jednostki
        if self and len(self) != before and self.has_warlord():
            self.move_units()


class Battle:
    def fight(self, a1, a2):
        return a1.fight(a2)

    def straight_fight(self, a1, a2):
        while a1 and a2:
            for s1, s2 in zip(a1, a2, strict=False):
                fight(s1, s2)
            a1.remove_deaths()
            a2.remove_deaths()
        return bool(a1)


class Weapon:
    def __init__(self, health, attack, defense, vampirism, heal_power):
        vars(self).update(locals())


class Sword(Weapon):
    def __init__(self):
        super().__init__(5, 2, 0, 0, 0)


class Shield(Weapon):
    def __init__(self):
        super().__init__(20, -1, 2, 0, 0)


class GreatAxe(Weapon):
    def __init__(self):
        super().__init__(-15, 5, 2, 10, 0)


class Katana(Weapon):
    def __init__(self):
        super().__init__(-20, 6, -5, 50, 0)


class MagicWand(Weapon):
    def __init__(self):
        super().__init__(30, 3, 0, 0, 3)
