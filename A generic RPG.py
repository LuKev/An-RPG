import random

ARMORS = ("cloth", "leather", "copper", "bronze", "iron", "steel",
          "silver-gold alloy thingy", "quartz plated", "ruby plated",
          "diamond plated")
WIZ_HATS = ("black", "blue", "green", "yellow", "red",
            "rainbow", "enchanted", "blessed", "iridescent", "minnesota twins cap")
PHYS_WEAPONS = ("dagger", "broadsword", "claymore", "longsword", "scimitar",
                "bludgeon", "mace", "flail", "battle ax", "zweihander")
MAG_WEAPONS = ("plastic wand", "walking stick", "enchanted wand", "staff", "Tizona",
               "Kusanagi", "Gungnir", "Excalibur", "Andúril", "elder wand")

class Enemy(object):
    """A class for any non-boss enemy"""

    def __init__(self, name):
        self.name = name
        self.health = self.health_points
        print("A ", + name + "appeared!")

    def __str__(self, stats):
        print("I am a " + self.name + "!")
        print("These are my stats:  ")
        print(stats)

#sets stats for easy reference
    def stats(self, stats):
        strength = stats[0]
        health = stats[1]
        intellegence = stats[2]
        dexterity = stats[3]
#sets maximum aka starting hp
    def health_points(self, stats):
        self.stats(stats)
        health_points = health*20+100
        return health_points
#reduces physical damage by up to 50%, based on armor. NOTE: it would be better
    #if I could figure out how to return "0" for the first thing in the list, etc.
    #it'll be kinda awkward syntax with invisible inventories and such...:(
    def physical_defense(self, inventory):
        phys_def = 0
        for i in ARMORS:
            if i in inventory:
                phys_def += 5
        return phys_def
#equiv to phys. def, but with magic :D
    def magical_defense(self, inventory):
        mag_def = 0
        for i in WIZ_HATS:
            if i in inventory:
                mag_def += 5
        return mag_def
#weapon attack bonus for phys attacks
    def physical_attack_bonus(self, inventory):
        phys_att_bonus = 0
        for i in PHY_WEAPONS:
            if i in inventory:
                phys_att_bonus += 10
        return phys_att_bonus
#see above
    def magical_attack_bonus(self, inventory):
        mag_att_bonus = 0
        for i in MAG_WEAPONS:
            if i in inventory:
                mag_attack_bonus += 10
        return mag_att_bonus
#ability to dodge moves b/c of speed
    def dodge(self):
        #dodge_chance should be a int from 0 to 100
        #it is equivalent to 2*speed
        dodged = None
        self.stats()
        dodge_chance = 2*speed
        random_number = random.randint(0, 100)
        if random_number > dodge chance:
            dodged = False
        else:
            dodged = True
        return dodged
#the hp in the battle; also takes care of taking damage and healing.
    def health(self, damage):
        self.health = health
        if damage == True:
            health -= damage
        if health > self.health_points:
            health = self.health_points
        if health <= 0:
            self.die()
#enemy dies
    def die(self, custom_message, gold, xp):
        print("you have defeated me!")
        print(custom_message)
        spoils_of_war = [gold, xp]
        return spoils_of_world
#attacks (finally).
    def physical_attack(self, ally):
        damage1 = None
        bonus = self.physical_attack_bonus()
        defense = ally.physical_defense()
        self.stats()
        damage1 = (strength*5+10)*(bonus/100+1)*(1-(defense/100))
        if ally.dodge == False:
            print("You did not miss!")
            #attacks an ally/hero
            ally.health(damage = damage1)
        else:
            print("You missed!")
#sets up the mana system; will most likely be similar to health. The first one is the maximum mana.
    def max_mana(self, stats):
        self.stats(stats)
        maximum_mana = intelligence * 20 + 10
        return maximum_mana
#gain/lose mana:
    def mana(self, amount):
        self.mana = mana
        mana -= amount
        return mana
#various spells; first one is generic fireball...it attacks 1 enemy,
#and varies depending on the magic power of the player
    def fireball(self, stats, ally):
        damage = None
        bonus = self.magical_attack_bonus()
        defense = ally.magical_defense()
        self.stats()
        #calculates damage here; it's a little more than the physical
        #attack, because it uses up mana
        damage = (intelligence*6+15)*(bonus/100+1)*(1-(defense/100))
        #takes away 25 mana
        mana = self.mana(25)
        #checks to make sure there's enough mana to cast the spell
