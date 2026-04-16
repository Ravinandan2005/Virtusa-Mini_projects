from skills import SKILLS

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