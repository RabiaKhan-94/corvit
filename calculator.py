import streamlit as st

st.set_page_config(page_title="Python Calculator", page_icon="🧮", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: black;'>Python Calculator</h1>",
    unsafe_allow_html=True,
)

# Session state to store expression
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Function to handle button clicks
def press(button):
    if button == "CE":
        st.session_state.expression = ""
    elif button == "=":
        try:
            # Replace 'x' with '*' and evaluate
            result = eval(st.session_state.expression.replace("x", "*"))
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += str(button)

# Display current expression
st.text_input("Display", value=st.session_state.expression, key="display", disabled=True)

# Layout buttons like a calculator
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["0", "CE", "=", "+"]
]

# Button styling
for row in buttons:
    cols = st.columns(4)
    for i, label in enumerate(row):
        btn_color = "white"
        if label in {"+", "-", "x", "/"}:
            btn_color = "#f67280"
        elif label == "=":
            btn_color = "#355c7d"
        elif label == "CE":
            btn_color = "#6c5b7b"
        cols[i].button(label, key=label, on_click=press, args=(label,), help=f"Press {label}")
