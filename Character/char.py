class character:
    def __init__(self,hit_dice,Class,race,str,dex,con,char,wis,int,speed,level):
        self.race=race
        self.str=str
        self.dex=dex
        self.con=con
        self.char=char
        self.wis=wis
        self.int=int
        self.speed=speed
        self.hit_dice = hit_dice
        self.Class = Class
        self.level = level
        self.charmod=char
        self.strmod=str
        self.dexmod=dex
        self.conmod=con
        self.wismod=wis
        self.intmod=int
    def dex_check(self):
        '''
        Does the dexterity check.
        :return: None
        '''
        check=random.randint(1,20)+self.dex #Rolls the dexterity roll
        print(check)
        if check in range(13,18): #This is the realm of the roll succeeding.
            print("You made the check and continue on your way")
        if check in range(18,20): #Tbe roll went really well.
            print("You are seriously dexterous in the moment.")
        if check>=20: # This roll is the phenomenal role.
            print("You were doing cartwheels as you did this")
        #if check<13: # roll fails.
            # damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6) #rolls 3 dice and adds them together.
            # print("You fail the action and take " +str(damage)+ " damage to your health")
            # self.health=self.health-damage # subtracts the damage.
            # print("Health:" +str(self.health))
    def str_check(self):
        '''
        Does the strength roll
        :return: None
        '''
        check=random.randint(1,20)+self.str
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You are seriously muscular in the moment.")
        if check>=(20):
            print("You were doing pushup and flexing the whole time you did this")
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("You fail the action and take " +str(damage)+ " damage to your health")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
    def con_check(self):
        '''
        Does the constitution check.
        :return: none
        '''
        check=random.randint(1,20)+self.con
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You had a stomach of steel")
        if check>=20:
            print("That was the strangest thing you have ever tasted. You gain extra health")
            gain=random.randint(1,6)
            print("You gained " +str(gain)+ " health.")
            self.health+=gain
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("You fail the action and take " +str(damage)+ " damage to your health")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
    def char_check(self):
        '''
        Does the charisma check.
        :return: None
        '''
        check=random.randint(1,20)+self.char
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You laid the cute animal eyes on thick")
        if check>=20:
            print("You were so smooth they even fed you")
            self.health=self.health+1
            print("Health:" +str(self.health))
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("They hit you and you take " +str(damage)+ " damage to your health. You run by")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
    def wis_check(self):
        '''
        Does the wisdom check
        :return: None
        '''
        check=random.randint(1,20)+self.wis
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("Your wise thoughts made the challenge a breeze.")
        if check>=20:
            print("You were the wisest you have ever been as you did this")
        # if check<13:
        #     damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
        #     print("You fail the action and take " +str(damage)+ " emotional damage to your health")
        #     self.health=self.health-damage
        #     print("Health:" +str(self.health))
    def int_check(self):
        '''
        Does the intelligence check.
        :return: None
        '''
        check=random.randint(1,20)+self.int
        print(check)
        if check in range(13,18):
            print("You made the check and continue on your way")
        if check in range(18,20):
            print("You easily figured out the answer in the moment.")
        if check>=20:
            print("You did so many smart things it would be impossible to remember it")
        if check<13:
            damage=random.randint(1,4)+random.randint(1,6)+random.randint(1,6)
            print("You fail the action and take " +str(damage)+ " brain damage to your health")
            self.health=self.health-damage
            print("Health:" +str(self.health))
    def test(self):
        print("Your hit dice is a "+str(self.hit_dice))
        print(self.Class)
        print(self.level)
    def save(self):
        with open('char.txt', 'w') as file:
            file.write(" ")
            file.close()
        with open('char.txt', 'a') as file:
            file.write("You are a " +self.race+ " " +self.Class+" of level "+self.level+ ".\n")
            file.write(" strength: " +str(self.str)+" with a modifier of: "+str(self.strmod)+'\n')
            file.write(" dexterity: " +str(self.dex)+" with a modifier of: "+str(self.dexmod) + "\n")
            file.write(" wisdom: " +str(self.wis)+" with a modifier of: "+str(self.wismod) + "\n")
            file.write(" charisma: " +str(self.char) + " with a modifier of: "+str(self.charmod) + "\n")
            file.write(" constitution: " +str(self.con)+" with a modifier of: "+str(self.conmod) + "\n")
            file.write(" intelligence: " +str(self.int)+" with a modifier of: "+str(self.intmod) + "\n")
            file.write(" You can move " +str(self.speed)+ " feet with your walk action."+'\n')
            file.close()
    def char_mod(self):
        self.charmod = self.charmod-10
        self.charmod = self.charmod/2
        if self.charmod.is_integer() == False:
            self.charmod=self.charmod-.5
        self.charmod=int(self.charmod)
        print(self.charmod)
    def int_mod(self):
        self.intmod = self.intmod-10
        self.intmod = self.intmod/2
        if self.intmod.is_integer() == False:
            self.intmod=self.intmod-.5
        self.intmod=int(self.intmod)
        print(self.intmod)
    def wis_mod(self):
        self.wismod = self.wismod-10
        self.wismod = self.wismod/2
        if self.wismod.is_integer() == False:
            self.wismod=self.wismod-.5
        self.wismod=int(self.wismod)
        print(self.wismod)
    def str_mod(self):
        self.strmod = self.strmod-10
        self.strmod = self.strmod/2
        if self.strmod.is_integer() == False:
            self.strmod=self.strmod-.5
        self.strmod=int(self.strmod)
        print(self.strmod)
    def dex_mod(self):
        self.dexmod = self.dexmod-10
        self.dexmod = self.dexmod/2
        if self.dexmod.is_integer() == False:
            self.dexmod=self.dexmod-.5
        self.dexmod=int(self.dexmod)
        print(self.dexmod)
    def con_mod(self):
        self.conmod = self.conmod-10
        self.conmod = self.conmod/2
        if self.conmod.is_integer() == False:
            self.conmod=self.conmod-.5
        self.conmod=int(self.conmod)
        print(self.conmod)
