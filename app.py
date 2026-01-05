from users import users

def login(username, password):
    if username in users:
        if users[username]["password"] == password:
            return users[username]["role"]
    return None
  
st.set_page_config(page_title="Enterprise RAG Login")

st.title("Enterprise Knowledge Assistant")

if "role" not in st.session_state:
    st.session_state.role = None

if st.session_state.role is None:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        role = login(username, password)
        if role:
            st.session_state.role = role
            st.success(f"Logged in as {role}")
        else:
            st.error("Invalid credentials")
else:
    st.success(f"Welcome! Your role is: {st.session_state.role}")
    if st.button("Logout"):
        st.session_state.role = None
