import streamlit as st
import functions

employs = functions.get_employs()


def add_employ():
    employ = st.session_state["new_employ"] + "\n"
    employs.append(employ)
    functions.write_employs(employs)




st.title('My Employs App')
st.subheader('This is my app.')


for index, employ in enumerate(employs):
    checkbox = st.checkbox(employ, key=employ)
    if checkbox:
        employs.pop(index)
        functions.write_employs(employs)
        del st.session_state[employ]
        st.rerun()


st.text_input(label="", placeholder='Add new Employ....',
              on_change=add_employ, key="new_employ")


st.session_state
