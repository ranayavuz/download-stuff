import time
import random
health = 10
sp = 5
damageblocked = 0
L = "penguin's house"
while True:
   ans = input("you just woke up, theres a penguin, what do u do? (how dare you, ok, I WANT TO KILL U) ").lower()
   if ans == "how dare you":
       print("\npenguin: ok...")
       time.sleep(1)
       print("WELL HOW DARE U!")
       time.sleep(1)
       print("FOR SLEEPING IN MY BED!")
       time.sleep(1)
       print("well, we need to go outside now")
       L = "bisville"
       break
   elif ans == "ok":
       print("\npenguin: LES go")
       time.sleep(1)
       L = "bisville"
       break
   elif ans == "i want to kill u":
       print("LETS FIGHT\n")
       playercategorychoices = ["ball"]
       playermove = input("ur choices" + str(playercategorychoices))
       if playermove == playercategorychoices[0]:
           print("U USED BALL!")
           time.sleep(1)
           enemymoves = ["penguinbomb"]
           enemymove = enemymoves[0]
           print("PENGUIN USED PENGUINBOMB!")
           time.sleep(1)
           print("\nyou lost...")
           print("run the program again\n")
           time.sleep(1)
           print(" "+0)
       else:
           print("STOP RIGHT THERE!\n")
           time.sleep(1)
           print(" " + 0)
   else:
       continue
while True:
   print("what do you do?\n")
   print("1, check health and sp")
   print("2, move to")
   print("3, check location")
   ans = input("")
   if ans == "1":
       print("health: ", health)
       print("sp: ", sp, "\n")
   elif ans == "2":
       ans = input("where?(directions of the earth) ")
       if ans == "west":
           if L == "bisville" or L == "penguin's house":
               L = "penguin's house"
               print("you are in", L)
               continue
           if L == "dog park":
               L = "bisville"
               print("you are in", L)
               continue
       if ans == "east":
           if L == "penguin's house":
               L = "bisville"
               print("you are in", L)
               continue
           if L == "bisville":
               L = "dog park"
               print("you are in", L)
               continue
           if L == "dog park":
               L = "HQ"
               print("you are in", L)
       if ans == "north":
           if L == "HQ":
               L = "corparite building"
               print("you are in", L)
               print("TINY noob: LETS FIGHT\n")
              
               enemyhealth = 2
               while enemyhealth > 0:
                   playercategorychoices = ["ball", "run", "defend"]
                   playermove = input("your choices are" + str(playercategorychoices))
                   if playermove == "ball":
                       print("U USED BALL!\n")
                       enemyhealth -= 1
                   elif playermove == "run":
                       print("you ran away!")
                       print("oh no, you shouldnt have run...\n")
                       time.sleep(1)
                       print(1/0)
                   elif playermove == "defend":
                       damageblocked = random.randint(1, 2)
                   else:
                       print("DISQUALIFIED!!!\n")
                       time.sleep(1)
                       print(1/0)
                   if enemyhealth < 1:
                       print("tiny noob collapsed!")
                       break
                   time.sleep(1)
                   if health < 1:
                       print("\n you died... \n")
                       time.sleep(1)
                   enemymoves = ["stab"]
                   enemymove = enemymoves[0]
                   print("tiny noob used stab!")
                   health -= 1 - damageblocked
   elif ans == "3":
       print("you are in", L)
