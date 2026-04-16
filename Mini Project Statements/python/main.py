from parser import extract_text
from matcher import match_skills, extract_skills_nlp
from suggestions import generate_suggestions

# Paths to files
resume_path = "resumes/Ravinandan's_Resume.pdf"
job_desc_path = "job_desc/sample_job_description.txt"

# Extract text
resume_text = extract_text(resume_path)
job_desc_text = extract_text(job_desc_path)

# Extract skills using NLP
resume_skills = extract_skills_nlp(resume_text)
job_desc_skills = extract_skills_nlp(job_desc_text)

# Match skills
match_percentage, matched_skills, missing_skills = match_skills(resume_skills, job_desc_skills)

# Generate suggestions
suggestions = generate_suggestions(missing_skills, match_percentage)

# Output results
print("--- MATCH RESULT ---\n")
print(f"Match Percentage: {match_percentage:.2f}%")

print("\nMatched Skills:")
print(matched_skills)

print("\nMissing Skills:")
print(missing_skills)

print("\n-Suggestions:")
for s in suggestions:
    print("-", s)