import streamlit as st


st.set_page_config(page_title="Rabia's Python Calculator", page_icon="🧮", layout="centered")

st.markdown(
    "<h1 style='text-align: center; color: black;'>Rabia's Python Calculator</h1>",
    unsafe_allow_html=True
)

if "expression" not in st.session_state:
    st.session_state.expression = ""

def press(button):
    if button == "CE":
        st.session_state.expression = ""
    elif button == "=":
        try:
            result = eval(st.session_state.expression.replace("x", "*"))
            st.session_state.expression = str(result)
        except:
            st.session_state.expression = "Error"
    else:
        st.session_state.expression += str(button)

st.markdown("""
    <style>
    .display-box {
        font-size: 28px;
        padding: 15px;
        background-color: #ffffff;
        border: 2px solid #dfe6e9;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: right;
        width: 100%;
        box-sizing: border-box;
    }

    .button {
        width: 100%;
        height: 60px;
        font-size: 20px;
        font-weight: bold;
        border-radius: 15px;
        border: none;
        color: white;
        margin: 5px 0;
    }

    .operator { background-color: #f67280; }
    .equal { background-color: #355c7d; }
    .clear { background-color: #6c5b7b; }
    .number { background-color: #74b9ff; }

    @media (max-width: 600px) {
        .button {
            height: 50px;
            font-size: 18px;
        }
        .display-box {
            font-size: 22px;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='display-box'>{st.session_state.expression}</div>", unsafe_allow_html=True)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["0", "CE", "=", "+"]
]

for row in buttons:
    cols = st.columns(4)
    for i, label in enumerate(row):
        # Choose button style based on label type
        if label in {"+", "-", "x", "/"}:
            style = "operator"
        elif label == "=":
            style = "equal"
        elif label == "CE":
            style = "clear"
        else:
            style = "number"

        with cols[i]:

            button_html = f"""
                <button class="button {style}" onclick="fetch('/?{label}')">{label}</button>
            """
            if st.button(label, key=label):
                press(label)
