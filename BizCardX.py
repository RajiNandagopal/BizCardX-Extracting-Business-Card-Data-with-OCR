#%%writefile sy.py
import pandas as pd
import numpy as np
import streamlit as st
import easyocr
import cv2
import sqlite3
from sqlite3 import Error
import time
from streamlit_option_menu import option_menu



conn = sqlite3.connect('Business_card_info.db')
cur = conn.cursor()


# Create a table to store the business card information
cur.execute('''CREATE TABLE IF NOT EXISTS Business_card
              (id INT AUTO_INCREMENT PRIMARY KEY,
              name TEXT,
              position TEXT,
              address TEXT,
              pincode VARCHAR(25),
              phone VARCHAR(25),
              email TEXT,
              website TEXT,
              company TEXT
              )''')

# Using easyOCR for reading data
reader = easyocr.Reader(['en'])


# Set the page title and page icon
st.set_page_config(page_title= "BizCardX", page_icon=':credit_card:', layout='wide')

#st.sidebar.image("/content/5.png")

# Create a sidebar menu with options to Add, Show, Update business card information

with st.sidebar:
    selected = option_menu("Menu", ["🏡Home","🌏Data Management","🙏My-Profile"],
                          #icons=["","",""],
                          default_index=0,
                          orientation="vertical",
                          styles={"nav-link": {"font-size": "35px", "text-align": "centre", "margin": "0px", "--hover-color": "#6495ED"},
                                  "icon": {"font-size": "20px"},
                                  "container" : {"max-width": "6000px"},
                                  })
    

if selected == "🏡Home":
    col1,col2,col3 =st.columns(3)
    with col2:
       st.image("/content/5.png")
    st.title(":blue[BizCardX: Extracting Business Card Data with OCR]")
    st.subheader(":red[**Technologies**]")
    st.write("------------------------------------------------")
    st.markdown("👉 Python")
    st.write("Python is a computer programming language often used to build websites and software, automate tasks, and analyze data.")
    st.markdown("👉 EasyOCR")
    st.write("EasyOCR is a Python computer language Optical Character Recognition (OCR) module that is both flexible and easy to use. OCR technology is useful for a variety of tasks, including data entry automation and image analysis. It enables computers to identify and extract text from photographs or scanned documents.")
    st.markdown("👉 Streamlit")
    st.write("Streamlit is a promising open-source Python library, which enables developers to build attractive user interfaces in no time.")
    st.markdown("👉 Sqlite3")
    st.write("A standalone command-line shell program called sqlite3 is provided in SQLite's distribution. It can be used to create a database, define tables, insert and change rows, run queries and manage an SQLite database file. ")
    st.markdown("👉 Pandas")
    st.write("Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data.")
    st.write("------------------------------------------------")
    st.subheader(":green[**Outline**]")
    st.write("-------------------------------------------------")
    st.markdown("🟩 In this streamlit web app you can upload an image of a business card and extract relevant information from it using easyOCR")
    st.markdown("🟩 You can view, modify or delete the extracted data in this app")
    st.markdown("🟩 This app would also allow users to save the extracted information into a database along with the uploaded business card image")
    st.markdown("🟩 The database would be able to store multiple entries, each with its own business card image and extracted info")
    st.write("------------------------------------------------")

if selected == "🌏Data Management":

    #data = ['Insert Data', 'Show Data', 'Edit Card Info', 'Delete Data']
    choose = st.sidebar.selectbox("**BizCardX**",('select','Insert Data', 'Show Data', 'Edit Card Info', 'Delete Data'))

    if choose == 'Insert Data':

        # Create a file uploader
        file_upload = st.file_uploader("[UPLOAD CARD IMAGE>>>:credit_card:]",
                                        type=["jpg", "jpeg", "png", "tiff", "tif", "gif"])

        if file_upload is not None:

            # Read the image using OpenCV
            image = cv2.imdecode(np.fromstring(file_upload.read(), np.uint8), 1)

            # Display the uploaded image
            st.image(image, caption='Uploaded Successfully', use_column_width=True)

            # Button to extract information from the image
            if st.button('Extract Data And Added'):
                bsc = reader.readtext(image, detail=0)
                text = "\n".join(bsc)

                # Insert the extracted information and image into the database
                sql_data = "INSERT INTO Business_card (name, position, address, pincode, phone, email, website, company) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)"
                values = (bsc[0], bsc[1], bsc[2], bsc[3], bsc[4], bsc[5], bsc[6], bsc[7])
                cur.execute(sql_data, values)
                conn.commit()
                with st.spinner("Wait for it...."):
                    time.sleep(5)

                # Display message
                st.success("Data Inserted")

    elif choose == 'Show Data':

        # Display the stored business card information
        cur.execute("SELECT * FROM Business_card")
        result = cur.fetchall()
        df = pd.DataFrame(result,
                          columns=['id', 'name', 'position', 'address', 'pincode', 'phone', 'email', 'website', 'company'])
        st.write(df)
        st.snow()


    elif choose == 'Edit Card Info':

        # Create a dropdown menu to select a business card to edit
        cur.execute("SELECT id, name FROM Business_card")
        result = cur.fetchall()
        business_cards = {}

        for row in result:
            business_cards[row[1]] = row[0]
        select_card_name = st.selectbox("Select Card To Edit", list(business_cards.keys()))

        # Get the current information for the selected business card
        cur.execute("SELECT * FROM Business_card WHERE name=?", (select_card_name,))
        result = cur.fetchone()

        # Get edited information
        name = st.text_input("Name", result[1])
        position = st.text_input("Position", result[2])
        address = st.text_input("Address", result[3])
        pincode = st.text_input("Pincode", result[4])
        phone = st.text_input("Phone", result[5])
        email = st.text_input("Email", result[6])
        website = st.text_input("Website", result[7])
        company = st.text_input("Company_Name", result[8])


        # Create a button to update the business card
        if st.button("Edit Card Data"):
            # Update the information for the selected business card in the database
            cur.execute(
                "UPDATE Business_card SET name=?, position=?, address=?, pincode=?, phone=?, email=?, website=?, company=? WHERE name=?",
                (name, position, address, pincode, phone, email, website, company, select_card_name))
            conn.commit()
            st.success("Card Data Updated")
            st.balloons()

    if choose == 'Delete Data':

        # Create a dropdown menu to select a business card to delete
        cur.execute("SELECT id, name FROM Business_card")
        result = cur.fetchall()
        business_cards = {}

        for row in result:
            business_cards[row[1]] = row[0]
        select_card_name = st.selectbox("Select Card To Delete", list(business_cards.keys()))

        # Create a button to delete the selected business card
        if st.button("Delete Card"):
            # Delete the selected business card from the database
            cur.execute("DELETE FROM Business_card WHERE name=?", (select_card_name,))
            conn.commit()
            st.success("⚠Card Data Deleted")


if selected == "🙏My-Profile":
    name = "Rajalakshmi N"
    mail = (f'{"Mail :"}  {"rajinandagopal02@gmail.com"}')
    description = "An Aspiring DATA-SCIENTIST..!"
    social_media = {
        "GITHUB": "https://github.com/RajiNandagopal",
        "LINKEDIN": "www.linkedin.com/in/rajalakshmi-nandagopal-2ba0b416a"}

    col1, col2 = st.columns(2)
    with col2:
        st.title('Insights, What I learn from this Project')
        st.write("")
        st.write("---")
        st.subheader(mail)
    st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")

