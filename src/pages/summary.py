# Import
import streamlit as st

# Create a title
st.title("Summary Page for Student Data")

st.image('https://logos-download.com/wp-content/uploads/2016/09/MongoDB_logo_Mongo_DB.png')
st.write("""
         We spent last week talking over SQL and we spent the last couple days talking about NoSQL or Document Oriented Databases. We talked over the advantages and some
         of the disadvantages of using both technologies. We chose to use the NoSQL format because the data itself was large and could fit in a tabular
         structure, however, a document oriented structure suited the data better and has proven to be faster.
         
         Also, using a database structure is faster than relying on a localized storage method.
         """)

st.write('Other Technologies Used: Streamlit, Python, Pandas, ML Modeling')