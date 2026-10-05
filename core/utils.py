import fitz
from docx import Document


# def extract_text(file):

#     if file.name.endswith(".pdf"):

#         pdf = fitz.open(stream=file.read(), filetype="pdf")

#         text = ""

#         for page in pdf:
#             text += page.get_text()

#         return text

#     elif file.name.endswith(".docx"):

#         doc = Document(file)

#         text = ""

#         for paragraph in doc.paragraphs:
#             text += paragraph.text + "\n"

#         return text

#     return ""


def extract_text(file):
    file.seek(0)

    pdf = fitz.open(stream=file.read(), filetype="pdf")

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text