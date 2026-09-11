
import random
import streamlit as st

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 10. You have 3 chances!")

# Initialize game state
if "py_choice" not in st.session_state:
    st.session_state.py_choice = random.randint(1, 10)
    st.session_state.chance = 3
    st.session_state.game_over = False
    st.session_state.message = ""

# Restart game
if st.button("🔄 Restart Game"):
    st.session_state.py_choice = random.randint(1, 10)
    st.session_state.chance = 3
    st.session_state.game_over = False
    st.session_state.message = ""
    st.rerun()

st.write(f"Chances remaining: {st.session_state.chance}")

# Number input
cust_num = st.number_input(
    "Guess a number between 1 and 10:",
    min_value=1,
    max_value=10,
    step=1,
    value=1,
    disabled=st.session_state.game_over
)

# Guess button
if st.button("Submit Guess", disabled=st.session_state.game_over):
    if cust_num == st.session_state.py_choice:
        st.session_state.message = "Correct Guess! 🎉"
        st.session_state.game_over = True
    else:
        st.session_state.chance -= 1

        if st.session_state.chance == 0:
            st.session_state.message = (
                f"Game over! The correct number was "
                f"{st.session_state.py_choice}."
            )
            st.session_state.game_over = True
        else:
            st.session_state.message = "Wrong guess, try again!"

# Display result
if st.session_state.message:
    if st.session_state.game_over and "Correct" in st.session_state.message:
        st.success(st.session_state.message)
    elif st.session_state.game_over:
        st.error(st.session_state.message)
    else:
        st.warning(st.session_state.message)