secret_answer="sour diesel"
guess=""
guess_count=0
guess_limit=3
out_of_guesses = False

while guess != secret_answer and not (out_of_guesses):
    if  guess_count < guess_limit:
        guess = input("Guess the secret answer:")
        guess_count += 1
    else:
         out_of_guesses = True

    if out_of_guesses:
        print("You suck and Lose!")
    else:
        print("You win but you probably cheated."
       ) 