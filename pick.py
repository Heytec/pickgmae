import streamlit as st
import random

def generate_random_number():
    return random.randint(100, 999)

def play_pick_game(user_pick):
    random_number = generate_random_number()

    random_number_list = list(str(random_number))
    user_pick_list = list(str(user_pick))

    matching_digits = sum([1 for i, j in zip(random_number_list, user_pick_list) if i == j])

    result = {
        "random_number": random_number,
        "matching_digits": matching_digits
    }

    return result

def main():
    st.title("Pick Game App")
    st.write("Welcome to the Pick Game! Try to pick a 3-digit number and win if 2 or 3 numbers match the randomly generated number.")

    user_pick = st.text_input("Enter your 3-digit number:")
    
    if st.button("Play"):
        try:
            user_pick = int(user_pick)
            if 100 <= user_pick <= 999:
                result = play_pick_game(user_pick)
                st.write(f"The randomly generated number was: {result['random_number']}")
                if result['matching_digits'] == 3:
                    st.success("Congratulations! You matched all 3 digits. You win a big reward!")
                elif result['matching_digits'] == 2:
                    st.success("Great! You matched 2 digits. You win a reward!")
                else:
                    st.info("Sorry, no matches this time. Better luck next time!")
            else:
                st.error("Please enter a valid 3-digit number.")
        except ValueError:
            st.error("Please enter a valid number.")

if __name__ == "__main__":
    main()
