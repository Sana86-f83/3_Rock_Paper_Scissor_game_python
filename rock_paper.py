import streamlit as st
import random

# Define the options
selec_option = ["🪨 rock", "✂️ scissor", "📃 paper"]

# Streamlit app title
st.markdown("<h1 style='text-align: center; color: black; font-weight: bold;'>🎯 Rock-Paper-Scissors Game 🎮 </h1>", unsafe_allow_html=True)

# Apply background gradient (Purple)
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(to bottom, #00CED1, #DA70D6);
    }
    /* Customizing text */
    h1, h2, h3, p, label {
        color: black !important;
        font-weight: bold !important;
    }
    /* Custom Button */
    div.stButton > button {
        background:linear-gradient(to top, #00B0BA, #C05780); 
        color: white !important;
        font-weight: bold !important;
        border-radius: 10px;
        padding: 10px 20px;
    }
    div.stButton > button:hover {
        background: linear-gradient(to top, #00CED1, #DA70D6); 
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state variables
if 'uCount' not in st.session_state:
    st.session_state.uCount = 0
if 'cCount' not in st.session_state:
    st.session_state.cCount = 0
if 'round' not in st.session_state:
    st.session_state.round = 1

# Function to reset the game
def reset_game():
    st.session_state.uCount = 0
    st.session_state.cCount = 0
    st.session_state.round = 1

# Start game button
if st.button("Start Game"):
    st.session_state.round = 1

# Wrap the main content in a container
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)

    # Game logic
    if st.session_state.round <= 5:
        st.markdown(f"<h2>Round {st.session_state.round}</h2>", unsafe_allow_html=True)
        user_input = st.radio("Choose your move:", options=[1, 2, 3], format_func=lambda x: ["🪨 Rock", "✂️ Scissor", "📃 Paper"][x-1])

        if st.button("Play"):
            if user_input == 1:
                uChoice = "🪨 rock"
            elif user_input == 2:
                uChoice = "✂️ scissor"
            elif user_input == 3:
                uChoice = "📃 paper"

            Com_choice = random.choice(selec_option)

            st.markdown(f"<p>Computer Value: <b>{Com_choice}</b></p>", unsafe_allow_html=True)
            st.markdown(f"<p>Your Value: <b>{uChoice}</b></p>", unsafe_allow_html=True)

            if Com_choice == uChoice:
                st.markdown("<p style='color: black; font-weight: bold;'>Game Draw 🤝</p>", unsafe_allow_html=True)
                st.session_state.uCount += 1
                st.session_state.cCount += 1
            elif (uChoice == "🪨 rock" and Com_choice == "✂️ scissor") or (uChoice == "📃 paper" and Com_choice == "🪨 rock") or (uChoice == "✂️ scissor" and Com_choice == "📃 paper"):
                st.markdown("<p style='color: green; font-weight: bold;'>You Win 💥</p>", unsafe_allow_html=True)
                st.session_state.uCount += 1
            else:
                st.markdown("<p style='color: red; font-weight: bold;'>Computer Win 😩</p>", unsafe_allow_html=True)
                st.session_state.cCount += 1

            st.session_state.round += 1

    # Display scores
    if st.session_state.round > 5:
        st.markdown("<h2>Final Results</h2>", unsafe_allow_html=True)
        if st.session_state.uCount == st.session_state.cCount:
            st.markdown("<p>Final Game Draw... 🤝</p>", unsafe_allow_html=True)
        elif st.session_state.uCount > st.session_state.cCount:
            st.markdown("<p style='color: green; font-weight: bold;'>Final You Win the Game 🎉</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='color: red; font-weight: bold;'>Final Computer Win the Game 😩</p>", unsafe_allow_html=True)

        st.markdown(f"<p>User Score: <b>{st.session_state.uCount}</b></p>", unsafe_allow_html=True)
        st.markdown(f"<p>Computer Score: <b>{st.session_state.cCount}</b></p>", unsafe_allow_html=True)

        if st.button("Play Again"):
            reset_game()

    st.markdown('</div>', unsafe_allow_html=True)


# Footer Section
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background:linear-gradient(to bottom, #00B0BA, #C05780); 
        color: black;
        text-align: center;
        font-weight: bold;
        padding: 10px;
        font-size: 16px;
    }
    .footer a {
        color: black;
        text-decoration: none;
        font-weight: bold;
    }
    .footer a:hover {
        color: white;
    }
    .footer b {
        color: white;
    }
    .footer b:hover {
         color:#00B0BA;
    }
    </style>
    <div class="footer">
        Developed by <b>Sana Faisal</b> |  
        <a href="https://www.linkedin.com/in/sana-faisal-developer/" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
)
