import json


class Reader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = self.load()

    def load(self):
        with open(self.file_name, 'r') as f:
            return json.load(f)

    def play(self):
        print("Title:", self.data['title'])
        print("Description:", self.data['description'], "\n")
        self.play_block(self.data['start'])

    def play_block(self, block):
        print(block['text'])
        if ('end' in block) and block['end'] or not ('choices' in block) or len(block['choices']) == 0:
            print("The end!")
            return

        print("choices:")
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
        self.play_block(block['choices'][choices[choice-1]])


reader = Reader('./story2.json')

reader.play()
