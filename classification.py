import streamlit as st

tags = {
    "machine_learning": ["machine-learning", "ml"],
    "deep_learning": ["deep-learning", "dl"],
    "nlp": ["nlp", "natural-language-processing"],
    "generative_ai": ["generative-ai"],
    "computer_vision": ["computer-vision", "cv"],
    "python_project": ["python-project", "general"]
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
            classification.append("Unclassified")
    return classification