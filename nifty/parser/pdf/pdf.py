from pathlib import Path

import PyPDF2


def pdf_to_text(pdf_filepath: str | Path, output_filepath: str | Path) -> None:
    pdf_filepath_extension = Path(pdf_filepath).suffix
    if pdf_filepath_extension != '.pdf':
        raise ValueError(f'pdf_filepath `{pdf_filepath} is not .pdf filepath`')

    output_filepath_extension = Path(output_filepath).suffix
    if output_filepath_extension != '.txt':
        raise ValueError(f'output_filepath `{output_filepath}` is not .txt filepath')

    with open(pdf_filepath, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)

        with open(output_filepath, "w", encoding="utf-8") as text_file:
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()

                text_file.write(text)
