import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)
chosen_word=random.choice(word_list)

display=[]
lives=6
#print(f"The word is {chosen_word}")

for letter in chosen_word:
    display+='_'

print(display)
length=len(chosen_word)
while "_" in display:
    guess=input("Guess the letter: ")
    guess=guess.lower()
    for i in range(0,length): 
        letter=chosen_word[i]
        if letter==guess:
            display[i]=guess
            print(display)
    if guess not in chosen_word:
        lives-=1
        print(stages[lives])
        print(f"You have {lives} lives left")
    if lives==0:
        print(f"YOU LOSE and the word was {chosen_word} ")
        break
if "_" not in display:
    print("YOU WIN!!!")  
            
