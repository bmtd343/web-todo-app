import streamlit as st
import functions as f

todos = f.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)


st.title("Daily To-Dos")
st.subheader("Created by BM Durbin")
st.write("This is a to-do app I created with basic functionality, "
         "in order to showcase foundational Python web-development skills.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="This is where to-dos are entered",
              placeholder='Add a new to-do...',
              on_change=add_todo, key='new_todo',
              label_visibility='hidden')
