Introduction:

BizCardX is a user-friendly tool for extracting information from business cards using Optical Character Recognition (OCR) technology. This project leverages the EasyOCR library to recognize text on business cards and extracts the data into a SQL database after classification using regular expressions. The extracted information is then accessible through a GUI built using Streamlit. The BizCardX application provides an intuitive interface for users to upload business card images, extract information, and manage the data within a database.

Objective:

To achieve these objectives, the project will leverage Python, Streamlit, easyOCR, and a database management system such as SQLite or MySQL. The application should prioritize a user-friendly interface, guiding users through the process of uploading business card images and extracting their information. The architecture of the application should be thoughtfully designed, ensuring scalability, maintainability, and extensibility. Additionally, the project emphasizes the importance of meticulous documentation and code organization to facilitate understanding and future development efforts.


Tools: 

1.Python
2.Streamlit
3.OCR technology (e.g.EasyOCR)
4.SQL database (e.g. Sqlite3)
5.Data extraction libraries (e.g. OpenCV)
6.Data analysis libraries (e.g. Pandas)

Features:

BizCardX to simplify the process of extracting and managing information from business cards. The tool offers the following features:

1.Extraction of key information from business cards: company name, cardholder name, designation, contact details, etc.
2.Storage of extracted data in a MySQL database for easy access and retrieval.
3.GUI built with Streamlit for a user-friendly interface.
4.User options to upload, extract, and modify business card data.

Workflow:

1.Install the required libraries using the command pip install [Name of the library]. Install streamlit, Sqlite3, pandas, and easyocr.
2.Execute the BizCardX.py script using the command streamlit run BizCardX.py.
3.The web application opens in a browser, presenting the user with three menu options: HOME, DATA MANAGEMENT, MODIFY.
4.Users can upload a business card image in the DATA MANAGEMENT menu to INSERT option.
5.The EasyOCR library extracts text from the uploaded image.
6.Extracted text is classified using regular expressions to identify key information such as company name, cardholder name, etc.
7.The classified data is displayed on the screen and can be edited by the user if needed.
8.Clicking the "Upload to Database" button stores the data in a MySQL database.
9.The MODIFY menu allows users to read, update, and delete data in the MySQL database.

Conclusion:

The result of this project is a functional Streamlit application that enables users to upload business card images, extract relevant information using easyOCR, and display the extracted details in a clean and organized graphical user interface (GUI). The application allows users to save the extracted information and associated images into a database, supporting multiple entries. Python, Streamlit, easyOCR, and a database management system (e.g., SQLite or MySQL) are used for development. The application features a user-friendly interface for easy image upload and information extraction. Users can add, read, update, and delete data through the Streamlit UI. The project requires expertise in image processing, OCR, GUI development, and database management. Careful consideration is given to designing a scalable, maintainable, and extensible application architecture. Proper documentation and code organization are emphasized for clarity and future development.
