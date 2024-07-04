import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

#Hash passwords and store them in the YAML file. only do this once.
# hashed_pwd = Hasher(['12345']).generate()
# st.write(hashed_pwd) 

#Open YAML file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
#Create authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

#Render the login widget
name, authenticate_status, username = authenticator.login()

#Authenticate users
if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome {st.session_state["name"]}')
    st.title('Some Content')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your password and username')
    
#Password reset widget
if authenticate_status:
    try:
        if authenticator.reset_password(username):
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            st.success('Password modified successfully!')
    except Exception as e:
        st.error(e)
        
#Register new user
try:
    if authenticator.register_user(pre_authorization=False):
        with open('config.yaml') as file:
            yaml.dump(config, file, default_flow_style=False)
        st.success('User registered successfully!')
except Exception as e:
    st.error(e)
    
#Forgot password widget
try:
    username_of_forgotten_password, email_of_forgotten_password, new_random_password = authenticator.forgot_password()
    if username_of_forgotten_password:
        st.success('New password to be sent securely')
        # The developer should securely transfer the new password to the user.
    elif username_of_forgotten_password == False:
        st.error('Username not found')
except Exception as e:
    st.error(e)
    
#Forgot username widget
try:
    username_of_forgotten_username, email_of_forgotten_username = authenticator.forgot_username()
    if username_of_forgotten_username:
        st.success('Username to be sent securely')
        # The developer should securely transfer the username to the user.
    elif username_of_forgotten_username == False:
        st.error('Email not found')
except Exception as e:
    st.error(e)
    
    
#Update user details
if authenticate_status:
    try:
        if authenticator.update_user_details(username):
            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
        st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)
    