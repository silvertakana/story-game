from os import walk
import json
from time import sleep


class Reader:

	def __init__(self, file_name):
		self.file_name = file_name
		self.data = self.load()
		self.jump_locations = {"a":"b"}

	def load(self):
		with open(self.file_name, 'r') as f:
			return json.load(f)

	def play(self):
		print("Title:", self.data['title'])
		print("Description:", self.data['description'], "\n")
		sleep(1)
		self.find_jump_locations(self.data['start'])
		self.play_block(self.data['start'])

	def find_jump_locations(self, block):
		if 'jump_loc' in block:
			self.jump_locations[block['jump_loc']] = block
		if 'choices' in block:
			for choice in block['choices']:
				self.find_jump_locations(block['choices'][choice])

	def play_block(self, block):
		if 'text' in block:
			print(block['text'])
		if 'jump' in block:
			sleep(1)
			print()
			self.play_block(self.jump_locations[block['jump']])
			return
		if not ('choices' in block) or len(block['choices']) == 0:
			print("The end!")
			return

		sleep(2)
		print("\nchoices:")
		choices = []
		for choice in block['choices']:
			print(f"{len(choices)+1}: {choice}")
			choices.append(choice)

		while True:
			choice = int(input("Enter your choice: "))
			if choice < 0 and choice > len(choices):
				print("Invalid choice")
			else:
				break
		if choice == 0:
			print("Goodbye!")
			return
		print("\n")
		self.play_block(block['choices'][choices[choice - 1]])


# welcome to the game
print(
 "Welcome players to this story based adventure game! There are many choices to be made, so choose wisely!"
)
print(
 "You will be given a choice of what to do next, and you will be able to choose from the options given."
)
print("If you want to quit the game, type 0 when prompted for your choice.")
print("\nWhich adventure would you like to play?\n")
libraryDirectory = "./Library/"
filenames = next(walk(libraryDirectory), (None, None, []))[2]  # [] if no file
print("Available stories:")
for i in range(len(filenames)):
	print(f"{i+1}: {filenames[i]}")
while True:
	choice = int(input("Enter your choice: "))
	if choice < 0 and choice > len(filenames):
		print("Invalid choice")
	else:
		break
reader = Reader(libraryDirectory + filenames[choice - 1])
print("are you ready to play?\n")
sleep(1)
reader.play()
