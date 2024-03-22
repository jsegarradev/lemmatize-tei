import xml.etree.ElementTree as ET
import spacy
from config import *

# Load spaCy model
nlp = spacy.load("es_core_news_md")


def lemmatize_text(text):
    # Process text with spaCy
    doc = nlp(text)
    # Create a list to hold the lemmatized tokens
    lemmatized_tokens = []
    # Iterate over each token in the document
    for token in doc:
        # Create a dictionary to hold attributes of the token
        token_attributes = {
            "form": token.text,
            "lemma": token.lemma_,
            "id": f"w-{token.i}"
        }
        # Append the dictionary to the list
        lemmatized_tokens.append(token_attributes)
    return lemmatized_tokens


def create_TEI_xml(title, author, recipient, date, place, language, keywords, paragraphs):
    # Create TEI root element
    tei = ET.Element("TEI", {"xmlns": "http://www.tei-c.org/ns/1.0", "xml:id": ""})

    # Add XML declaration and DOCTYPE
    xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
    doctype = '<!DOCTYPE TEI SYSTEM "tei_all.dtd">\n'

    # Create teiHeader element
    teiHeader = ET.SubElement(tei, "teiHeader")

    # Add fileDesc element
    fileDesc = ET.SubElement(teiHeader, "fileDesc")

    # Add titleStmt element
    titleStmt = ET.SubElement(fileDesc, "titleStmt")
    title_element = ET.SubElement(titleStmt, "title")
    title_element.text = title
    author_element = ET.SubElement(titleStmt, "author")
    author_element.text = author

    # Add sourceDesc element
    sourceDesc = ET.SubElement(fileDesc, "sourceDesc")
    msDesc = ET.SubElement(sourceDesc, "msDesc")
    msIdentifier = ET.SubElement(msDesc, "msIdentifier")
    country_element = ET.SubElement(msIdentifier, "country")
    country_element.text = "España"
    settlement_element = ET.SubElement(msIdentifier, "settlement")
    settlement_element.text = "Castellón"
    repository_element = ET.SubElement(msIdentifier, "repository")
    repository_element.text = "Archivo Municipal de Castellón"

    # Add profileDesc element
    profileDesc = ET.SubElement(teiHeader, "profileDesc")
    creation_element = ET.SubElement(profileDesc, "creation")
    persName_remitente = ET.SubElement(creation_element, "persName")
    persName_remitente.set("type", "remitente")
    persName_remitente.text = author
    persName_destinatario = ET.SubElement(creation_element, "persName")
    persName_destinatario.set("type", "destinatario")
    persName_destinatario.text = recipient
    date_element = ET.SubElement(creation_element, "date")
    date_element.set("when", date)
    placeName_element = ET.SubElement(creation_element, "placeName")
    placeName_element.text = place

    langUsage_element = ET.SubElement(profileDesc, "langUsage")
    language_element = ET.SubElement(langUsage_element, "language")
    language_element.set("id", "es")
    language_element.text = language

    textClass_element = ET.SubElement(profileDesc, "textClass")
    keywords_element = ET.SubElement(textClass_element, "keywords")
    for keyword in keywords:
        term_element = ET.SubElement(keywords_element, "term")
        term_element.text = keyword

    # Add text element
    text = ET.SubElement(tei, "text")
    body = ET.SubElement(text, "body")
    div_element = ET.SubElement(body, "div")
    div_element.set("type", "Carta")

    # Add paragraphs with lemmatization
    for index, paragraph in enumerate(paragraphs, start=1):
        lemmatized_tokens = lemmatize_text(paragraph)
        p_element = ET.SubElement(div_element, "p")
        p_element.set("id", "p-" + str(index))
        for token in lemmatized_tokens:
            tok_element = ET.SubElement(p_element, "tok")
            for attr_name, attr_value in token.items():
                tok_element.set(attr_name, attr_value)
            tok_element.text = token["form"]

    # Create XML tree
    tree = ET.ElementTree(tei)

    # Combine XML declaration, DOCTYPE, and XML tree
    xml_content = xml_declaration + doctype + ET.tostring(tei, encoding="unicode")

    # Return XML content
    return xml_content


def read_text_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
    return text


# Example usage
if __name__ == "__main__":

    # Read text from file
    filename = "sample.txt"
    text = read_text_from_file(filename)

    # Split text into paragraphs
    paragraphs = text.split("\n")

    # Create TEI XML
    xml_content = create_TEI_xml(title, author, recipient, date, place, language, keywords, paragraphs)

    # Write XML content to file
    output_filename = "sample_letter.xml"
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(xml_content)

    print(f"XML written to '{output_filename}'")
