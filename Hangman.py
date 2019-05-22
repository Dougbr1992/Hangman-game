class HangmanBoard(object):
    def __init__(self):
        self.word = []
        self.letters_plays = []
        self.letter_in_word = []
        self.Theme_Data()
    def Apend_word(self, word):                        # [" __ "] * len(word)
        letters = len(word)
        i=0
        while i < letters:
            i += 1
            self.word.append(" __ ")
    def Theme_Data(self):
        self.house = ["door", "window", "gardem", "table", "pia"]
        self.car = ["fusca", "opala","kombi", "scenic"]
        self.fruit = ["uva", "maça", "banana", "melancia"]
        self.profession = ["cozinheira", "engenheiro", "garçom"]
        self.theme = [self.house, self.car, self.fruit, self.profession]
    def Choose_Theme(self):
        from random import randint
        return self.theme[randint(0,3)]                 # instead of 3?
    def Choose_Word(self):
        list = self.Choose_Theme()
        length_list = len(list)-1
        from random import randint
        return list[randint(0,length_list)]
    def Apend_letters (self, word):
        for letra in word:                               # list(word)
           self.letter_in_word.append(letra)
    def Choose_letter (self):
        letter = input("Enter a letter: \n")
        return letter.lower()

    def IsValid (self, letter):
        if len(letter) <= 1 and not letter.isdigit():
            return len(letter) <= 1 and not letter.isdigit()
        else:
            print("value is not a letter")
    def LetterAlreadyChosen(self, letter_chosen):
        all_letter = self.word + self.letters_plays
        this_letter_played = True
        for letter in all_letter:
            arealdy = letter != letter_chosen
            this_letter_played &= arealdy
        if not this_letter_played:
            print("letter already chosen")
        return this_letter_played

    def Check_letter(self, letter_chosen):
        index = []
        i = -1
        for letter in self.letter_in_word:
            i += 1
            if letter == letter_chosen:
                index.append(i)
        return index
    def PutLetter(self, index, letter):
        if len(index) == 0:
            self.letters_plays.append(letter)
            return 1
        else:
            for i in index:
                print(i)
                self.word.pop(i)                        # <--- What's the complexity of this line?
                self.word.insert(i,letter)              # <--- What's the complexity of this line?
                                                        # What if it was "self.word[i] = letter"? What's the complexity of this?
            return 0
    def LeetterPlaying(self, word):                     # ''.join(word)
        j = ""                                          # Try this line above. I'll explain when we talk. ;)
        for i in word:
            j += i
        return j
    def AlreadyPlayed(self, word):                      # ','.join(word)
        j = ""                                          # (yes, python is weird...)
        for i in word:
            j += i + ", "
        return j


############### MAIN CODE ######################

hangman = HangmanBoard()
word = hangman.Choose_Word()
hangman.Apend_letters(word)
hangman.Apend_word(word)
hangman.LeetterPlaying(hangman.word)
print(hangman.LeetterPlaying(hangman.word))
print(word)
tentativas = 0
while True:
    letra = hangman.Choose_letter()
    if hangman.IsValid(letra) and hangman.LetterAlreadyChosen(letra):
        index = hangman.Check_letter(letra)
        tentativas += hangman.PutLetter(index, letra)
        print(hangman.LeetterPlaying(hangman.word))
        print("Letters already played:")
        print(hangman.AlreadyPlayed(hangman.letters_plays))
        if hangman.LeetterPlaying(hangman.word) == word:
            print("You won!")
            break
        if tentativas == 5:
            print("You lose!")
            break
