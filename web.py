import streamlit as st
import func
import time

todos = func.get_todos()


def add_todo():
    todo_l = st.session_state['new_todo'] + '\n'
    todos.append(todo_l)
    func.write_todos(todos)


now = time.strftime("Date-%d %B %Y")


st.title("Sax ToDo App")
st.button(now)

for todo in todos :
    st.checkbox(todo)

st.text_input(label="",placeholder="Enter new To-Do...",on_change=add_todo,
              key='new_todo')