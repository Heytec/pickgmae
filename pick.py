import streamlit as st
import random

def generate_random_number():
    return random.randint(100, 999)

def calculate_prize(matching_digits, bet_amount):
    if matching_digits == 3:
        if bet_amount == 20:
            return 10000
        elif bet_amount == 50:
            return 15000
        elif bet_amount == 100:
            return 20000
    elif matching_digits == 2:
        if bet_amount == 20:
            return 200
        elif bet_amount == 50:
            return 500
        elif bet_amount == 100:
            return 1000
    return 0

def play_pick_game(user_pick, random_number, total_tries, total_plays, bet_amount, total_won, total_lost):
    random_number_list = list(str(random_number))
    user_pick_list = list(str(user_pick))

    matching_digits = sum([1 for i, j in zip(random_number_list, user_pick_list) if i == j])

    if matching_digits == 3 or matching_digits == 2:
        prize = calculate_prize(matching_digits, bet_amount)
        total_won += prize
        st.success(f"Congratulations! You matched {matching_digits} digits. You win ksh{prize}!")
        total_plays += 1
    else:
        st.info("Sorry, no matches this time. Better luck next time!")
        total_lost += bet_amount
        total_tries += 1

    return total_tries, total_plays, total_won, total_lost

def main():
    st.title("Pick Game App")
    st.write("Welcome to the Pick Game! Try to pick a 3-digit number and win based on the bet amount and matching digits.")
    
    # Initialize variables
    user_pick = st.text_input("Enter your 3-digit number:")
    bet_amount_options = [20, 50, 100]
    bet_amount = st.selectbox("Select Bet Amount", bet_amount_options, index=0)
    total_tries = st.session_state.get("total_tries", 0)
    total_plays = st.session_state.get("total_plays", 0)
    total_won = st.session_state.get("total_won", 0)
    total_lost = st.session_state.get("total_lost", 0)
    random_number = st.session_state.get("random_number", generate_random_number())

    if st.button("Play"):
        try:
            user_pick = int(user_pick)
            if 100 <= user_pick <= 999:
                total_tries, total_plays, total_won, total_lost = play_pick_game(user_pick, random_number, total_tries, total_plays, bet_amount, total_won, total_lost)
                random_number = generate_random_number()
                st.session_state.total_tries = total_tries
                st.session_state.total_plays = total_plays
                st.session_state.total_won = total_won
                st.session_state.total_lost = total_lost
                st.session_state.random_number = random_number
                st.write(f"The randomly generated number was: {random_number}")
                st.header( "Game Stats ")
                st.write(f"Total number of tries: {total_tries}")
                st.write(f"Number of times of wins: {total_plays}")
                st.write(f"Total amount won: ksh{total_won}")
                st.write(f"Total amount lost: ksh{total_lost}")
            else:
                st.error("Please enter a valid 3-digit number.")
        except ValueError:
            st.error("Please enter a valid number.")

if __name__ == "__main__":
    main()
