print("Your Name, Your USN, Your Section")
# Simplified zombie dice bot
import random
dice = ['brain']*3 + ['shotgun']*2 + ['runner']*1
print("Bot rolls:", ', '.join(random.sample(dice, 3)))