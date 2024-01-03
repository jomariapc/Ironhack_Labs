import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health-= damage
    

# Viking


class Viking(Soldier):
    mensaje=''
    def __init__(self, name, health, strength):
        self.name= name
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        #self.health -= damage
        if(self.health>0):
            return self.name + " has received " + str(damage) + " points of damage"
        if(self.health<=0):
            return self.name + " has died in act of combat"
        
    def battleCry(self):
        return "Odin Owns You All!"
    

# Saxon


class Saxon(Soldier):

    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if(self.health>0):
            return "A Saxon has received "+ str(damage)+ " points of damage"
        if(self.health<=0):
            return "A Saxon has died in combat"


#War
class War:
    vikingArmy= []
    saxonArmy=[]   

    def __init__(self):
        self.vikingArmy= []
        self.saxonArmy= []

    def addViking(self, vikingo):
        self.vikingArmy.append(vikingo)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        #Elijo al Vikingo aleatoriamente
        vikingoRandom = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        
        #Elijo al Saxon aleatoriamente
        saxonRandom = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        #Debilito al saxon
        resultado=saxonRandom.receiveDamage(vikingoRandom.attack())

        #Elimina el Saxon muerto
        for s in self.saxonArmy:
            if(s.health<=0):
                self.saxonArmy.remove(s)

        return resultado

    def saxonAttack(self):
        #Elijo al Vikingo aleatoriamente
        vikingoRandom = self.vikingArmy[random.randint(0,len(self.vikingArmy)-1)]
        
        #Elijo al Saxon aleatoriamente
        saxonRandom = self.saxonArmy[random.randint(0,len(self.saxonArmy)-1)]

        #Debilito al vikingo 
        resultado=vikingoRandom.receiveDamage(saxonRandom.attack())

        #Elimina el Vikingo muerto
        for s in self.vikingArmy:
            if(s.health<=0):
                self.vikingArmy.remove(s)

        return resultado

    def showStatus(self):
        if(len(self.saxonArmy)==0):
            return "Vikings have won the war of the century!"
        if(len(self.vikingArmy)==0):
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."