# Lemmatize Text with TEI XML Output

This project provides a Python script for lemmatizing text and generating TEI XML output. The script utilizes the spaCy library for text processing and generates TEI XML conforming to the specified format.

## Requirements

- Python 3.x
- spaCy library (`pip install spacy`)
- spaCy model for the desired language (e.g., `es_core_news_md` for Spanish)

## Usage

1. **Installation**:
    - Clone or download this repository to your local machine.

2. **Prepare Input**:
    - Create a text file containing the text you want to process. Ensure that the text file is UTF-8 encoded.

3. **Edit Configuration**:
    - Open the `config.py` file and modify the variables according to your requirements:
        - `title`: Title of the document.
        - `author`: Author of the document.
        - `recipient`: Recipient of the document.
        - `date`: Date of the document (format: YYYY-MM-DD).
        - `place`: Place mentioned in the document.
        - `language`: Language of the document (e.g., "Spanish").
        - `keywords`: List of keywords relevant to the document.

4. **Run the Script**:
    - Execute the `main.py` script by running the following command in your terminal:
      ```
      python main.py
      ```

5. **Output**:
    - After running the script, the TEI XML output will be generated and saved as `sample_letter.xml` in the same directory.

## Example

An example text file (`sample.txt`) and the resulting TEI XML output (`sample_letter.xml`) have been provided in the repository for reference.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
