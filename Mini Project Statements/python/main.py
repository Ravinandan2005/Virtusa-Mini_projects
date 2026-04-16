from parser import extract_text
from matcher import match_skills, extract_skills

#path to the resume and job description files
resume_path = "resumes/Ravinandan's_Resume.pdf"
job_desc_path = "job_desc/sample_job_description.txt"

#extract text from the files
resume_text  = extract_text(resume_path)
job_desc_text = extract_text(job_desc_path)

#extract skills
resume_skills = extract_skills(resume_text)
job_desc_skills = extract_skills(job_desc_text)

#match
match_percentage, matched_skills, missing_skills = match_skills(resume_skills, job_desc_skills)
print("Resume Text:\n", resume_text)
print("\nJob Description Text:\n", job_desc_text)
print(f"\nMatch Percentage: {match_percentage:.2f}%")
print("Matched Skills:", matched_skills)
print("Missing Skills:", missing_skills)