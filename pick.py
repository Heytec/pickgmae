import streamlit as st
import random

def generate_random_number():
    return random.randint(100, 999)

def play_pick_game(user_pick, random_number, total_tries, total_plays):
    random_number_list = list(str(random_number))
    user_pick_list = list(str(user_pick))

    matching_digits = sum([1 for i, j in zip(random_number_list, user_pick_list) if i == j])

    if matching_digits == 3:
        st.success("Congratulations! You matched all 3 digits. You win a big reward!")
        total_plays += 1
    elif matching_digits == 2:
        st.success("Great! You matched 2 digits. You win a reward!")
        total_plays += 1
    else:
        st.info("Sorry, no matches this time. Better luck next time!")
        total_tries += 1

    return total_tries, total_plays

def main():
    st.title("Pick Game App")
    st.write("Welcome to the Pick Game! Try to pick a 3-digit number and win if 2 or 3 numbers match the randomly generated number.")
    
    # Initialize variables
    user_pick = st.text_input("Enter your 3-digit number:")
    total_tries = st.session_state.get("total_tries", 0)
    total_plays = st.session_state.get("total_plays", 0)
    random_number = st.session_state.get("random_number", generate_random_number())

    if st.button("Play"):
        try:
            user_pick = int(user_pick)
            if 100 <= user_pick <= 999:
                total_tries, total_plays = play_pick_game(user_pick, random_number, total_tries, total_plays)
                random_number = generate_random_number()
                st.session_state.total_tries = total_tries
                st.session_state.total_plays = total_plays
                st.session_state.random_number = random_number
                st.write(f"The randomly generated number was: {random_number}")
                st.write(f"Total number of tries: {total_tries}")
                st.write(f"Number of  wins: {total_plays}")
            else:
                st.error("Please enter a valid 3-digit number.")
        except ValueError:
            st.error("Please enter a valid number.")

if __name__ == "__main__":
    main()
