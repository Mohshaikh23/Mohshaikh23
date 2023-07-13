import streamlit as st

tags = {
    "MACHINE LEARNING": ["machine-learning", "ml"],
    "DEEP LEARNING": ["deep-learning", "dl"],
    "NATURAL LANGUAGE PROCESSING": ["nlp", "natural-language-processing"],
    "GENERATIVE AI": ["generative-ai"],
    "COMPUTER VISION": ["computer-vision", "cv"],
    "PYTHON PROJECT": ["python-project", "general"]
}

def classify_tags(dataframe, column):
    classification = []
    for value_list in dataframe[column]:
        category_found = False
        for value in value_list:
            for key, value_list in tags.items():
                if value in value_list:
                    classification.append(key)
                    category_found = True
                    break
            if category_found:
                break
        else:
            classification.append("Basic Projects")
    return classification