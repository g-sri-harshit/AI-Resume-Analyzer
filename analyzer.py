import spacy

nlp = spacy.load("en_core_web_sm")

def analyze_resume(text):

    doc = nlp(text)

    skills = []
    
    keywords = ["python","machine learning","data science","sql","java","deep learning"]

    for word in doc:
        if word.text.lower() in keywords:
            skills.append(word.text)

    return {
        "skills_found": list(set(skills)),
        "suggestion": "Consider adding more AI/ML projects and technical skills."
    }