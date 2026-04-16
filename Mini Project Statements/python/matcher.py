from skills import SKILLS
import spacy

#load nlp model
nlp = spacy.load("en_core_web_sm")

def extract_skills_nlp(text):
    doc = nlp(text)
    found_skills = set()
    #token based matching
    for token in doc:
        if token.text.lower() in SKILLS:
            found_skills.add(token.text.lower())
    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)
    return list(found_skills)

#extract skills from the text and return a set of found skills
def extract_skills(text):
    found_skills = []
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    return set(list(found_skills)) #remove duplicates

def match_skills(resume_text, job_desc_text):
    resume_set = set(resume_text)
    job_desc_set = set(job_desc_text)
    matched = resume_set & job_desc_set
    missing = job_desc_set - resume_set
    if len(job_desc_set) ==0:
        match_percentage = 0
    else:
        match_percentage = (len(matched) / len(job_desc_set)) * 100
    return match_percentage, list(matched), list(missing)