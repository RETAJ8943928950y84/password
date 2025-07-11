import streamlit as st

import random as rn

import string as str




def generate_password(length:int)->str:

    all_chars= str.ascii_letters + str.digits +str.punctuation

    #Define the empty password

    password= ''

    # Repeat the random choice

    for n in range (length):

        password +=rn.choice(all_chars)

        # Returning the whole password

    return password



with st.sidebar:

    st.header('🎰Generate password')

    password_number=st.number_input(label='🌃How many password ?',step=1,min_value=1,max_value=100)

    password_length=st.slider('🌌Enter password length:',min_value=8,max_value=100, value=16)

    button=st.button('🚨Generate password')

st.title('🔋Secure password generator')

st.header('🤖 Generated password:')

if button:
    for i in range(password_number):

        result=generate_password(password_length)

        st.code(result)

