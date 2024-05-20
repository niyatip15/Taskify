import streamlit as st
from custom_functions import read_todos, write_todos

todos = read_todos()

def add_todo():
    '''This function is for taking the user todo value and add it in
        the list.
        session_state: contains pair of data that the user enters in input.'''
    todo = st.session_state['id_todo'] + '\n'
    todos.append(todo)
    write_todos(todos)


st.title("Todo-list")

for index,todo in enumerate(todos):
   checkbox =  st.checkbox(todo,key=todo)
   if checkbox:
       '''session state returns a dict containing true and false for the checkbox
       so we checked that if the user has checked any todo-item then the checked item should be 
       popped.'''
       todos.pop(index)
       write_todos(todos) #to write the updated value after removing any todo item
       del st.session_state[todo] # it should delete the pair of the checked value.
       st.experimental_rerun()

st.text_input(label="",placeholder="Add a new todo..",
              on_change=add_todo,key='id_todo')
