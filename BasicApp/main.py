import streamlit as st

#Give your app a title
st.title("Your Title")

#Header
st.header("Main Header")

#Subheader
st.subheader("This is a Subheader!")

#Markdown
st.markdown("This is Markdown! **text**")
st.markdown("# Header1")
st.markdown("## Header2")
st.markdown("### Header3")

#Caption
st.caption("This is caption!")

#Code block
st.code("""
        import pandas as pd
        pd.read_csv(my_csv_file)
        """)


#Preformatted text
st.text("Some Text!")

#LaTex
st.latex("x = 2^2")

#Divider
st.text("Text above devider")
st.divider()
st.text("Text below divider")

#st.write
st.write("Some Text")



 