
import json

with open("data/careers.json") as f:
    CAREERS = json.load(f)

def recommend_career(user_skills):

    results = []

    for career, details in CAREERS.items():

        matched = len(
            set(user_skills).intersection(details["skills"])
        )

        score = int(
            (matched / len(details["skills"])) * 100
        )

        results.append({
            "career": career,
            "score": score,
            "salary": details["salary"],
            "roadmap": details["roadmap"]
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results[:5]
