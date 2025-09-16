import streamlit as st
import function


st.set_page_config(layout="wide")
todos = function.get_file()
def file_handling():
    todo = st.session_state["new_todo"].strip()+"\n"
    if todo in todos:
        st.warning("⚠️Todo already exit")
    elif todo:
        st.success("🥑Todo added successfully")
        todos.append(todo)
        function.write_to_file(todos)

st.title("Pear's Todo app🥑")
st.subheader("Quik todos during browsing")
st.text_input(label="",placeholder="Enter a quick todo:",
              key="new_todo",
              on_change=file_handling)
st.write("Todos: ")

for index, todo in enumerate(todos):
    check  = st.checkbox(todo, key=todo)
    if check:
        todos.pop(index)
        function.write_to_file(todos)
        del st.session_state[todo]
        st.rerun()


