def generate_suggestions(missing_skills, match_percent):
    suggestions = []

    # Skill-based suggestions
    for skill in missing_skills:
        if skill in ["machine learning", "deep learning"]:
            suggestions.append("Consider adding projects related to Machine Learning or Deep Learning.")

        elif skill in ["power bi", "data analysis"]:
            suggestions.append("Include data visualization projects using Power BI or similar tools.")

        elif skill in ["sql", "mysql"]:
            suggestions.append("Strengthen database skills and mention SQL projects.")

        elif skill in ["api", "automation"]:
            suggestions.append("Highlight automation scripts or API-based projects.")

        elif skill in ["nlp", "computer vision"]:
            suggestions.append("Add AI-based projects such as NLP or Computer Vision applications.")

    # General suggestions based on score
    if match_percent < 50:
        suggestions.append("Your resume has low alignment. Consider tailoring it specifically to the job role.")

    elif match_percent < 75:
        suggestions.append("Good match, but you can improve by adding more relevant projects and skills.")

    else:
        suggestions.append("Strong match! Focus on refining your resume and adding measurable achievements.")

    return list(set(suggestions))  # remove duplicates