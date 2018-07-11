import random

print """
		--- 20 Sided Die Rolling Simulator ---
"""


while True:
		try:
			#Get Input
			WantToRoll = raw_input("Would you like to roll the die (y/n): ")
			
			#If user opts to roll
			if str(WantToRoll) == 'y': 
				start = 1
				stop = 21
				step = 1
				#Random Number from defined range
				roll = random.choice(range(start,stop,step))
				#If single digit roll
				if roll <= 9:
					print"""
                               *                               
                              ***                              
                             * """ + str(roll) + """ *                             
                            *******                            """
					
				else :
				#If 2 digit roll
					print"""
                               *                               
                              ***                              
                             *""" + str(roll) + """ *                             
                            *******                            """
				continue
				
			#If doesn't want to roll
			if str(WantToRoll) == 'n':
				print("Thank you, Goodbye...")
				break
			#If entry doesn't match y or n
			else:
				print "Check your entry and try again."
		except ValueError:
			print("Sorry, I didn't understand that.")
			#try again... Return start
			continue