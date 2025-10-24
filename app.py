# This is your actual app that connects Streamlit (UI) with SQLite (database):--
import streamlit as st
import sqlite3

# --- Create or connect to database ---
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# --- Create table if not exists ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    note TEXT
)
""")
conn.commit()

# --- Streamlit UI ---
st.title("My DevOps Demo App (Free Streamlit + CI/CD)")

menu = ["Add Note", "View Notes"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Note":
    st.subheader("Add a New Note")
    name = st.text_input("Enter Name:")
    note = st.text_area("Enter Note:")
    if st.button("Save Note"):
        cursor.execute("INSERT INTO notes (name, note) VALUES (?, ?)", (name, note))
        conn.commit()
        st.success("✅ Note saved successfully!")

elif choice == "View Notes":
    st.subheader("All Notes")
    cursor.execute("SELECT * FROM notes")
    data = cursor.fetchall()
    for row in data:
        st.write(f"📝 **{row[1]}:** {row[2]}")

st.sidebar.info("Built with ❤️ using Streamlit, SQLite, GitHub Actions, and Docker.")