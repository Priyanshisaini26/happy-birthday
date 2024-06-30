import streamlit as st
import smtplib, ssl


st.set_page_config("wide")
st.audio("Happy_birthday_A_cappella_K4Ei6x1ofCk_140.mp3", format="audio/mpeg", loop=True)
st.balloons()
st.title(':crown::tada::confetti_ball: :violet[Happy Birthday Kashish babu] :sunglasses::watermelon::gift::ribbon:')
st.header(":red[LOVE YOUUUU!!!!]:heartbeat:	:gift_heart::revolving_hearts:")
st.balloons()

col1, empty_col, col2 = st.columns([1.5, 0.5, 1.5])
with col1:
    st.image("hihi_kash.jpg", width=400)

with col2:
    st.image("kash.jpg", width=400)

st.balloons()

message = """
Happy Birthday Kashish, we fight alot but still i love you very much. I want to thank you, for being the most loving
and caring sister in this entire world.  
"""
st.write(f':green[{message}]')

st.write(':blue[_From Priyanshi!!!_]')




def send_mail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "priyanshisaini2603@gmail.com"
    password = "zssptpxqvcxtjbaq"

    receiver = "kashishsaini3000@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context= context) as server:
        server.login(username)
        server.sendmail(username, receiver, message)


st.header("Wish kashish a happy birthday!!!")

with st.form(key="email_form"):
    user_email = st.text_input("enter your name")

    option = st.selectbox("How much love do you want to give her",
                          ("very much", "very very v v v much", "infinite love"),
                          index=None,)

    raw_message = st.text_area("Your message")
    message = f"""\
    Subject: New message from {user_email}

    From: {user_email}
    {raw_message}
    """
    button = st.form_submit_button("Submit")
    if button:
        send_mail(message)
        st.info("Your wishes was sent successfully!!!")
st.balloons()