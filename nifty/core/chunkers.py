from pathlib import Path

import nltk


def chunk_text_file(filepath: str | Path, encoding: str = 'utf-8') -> list[str]:
    """ Given a text filepath, returns a list of the sentences in that text """
    with open(filepath, mode='r', encoding=encoding) as file:
        tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
        chunks = tokenizer.tokenize(file.read())
        return chunks
