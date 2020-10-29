import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://stackoverflow.com/questions")

#print(res.text)
soup = BeautifulSoup(res.text,"html.parser")

question_data = {
    "questions":[]
}

questions = soup.select(".question-summary")

for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    vote_count = que.select_one('.vote-count-post').getText()
    views = que.select_one('.views').attrs['title']
    question_data['questions'].append({
        "question":q,
        "views":views,
        "vote_count":vote_count,
    })
#print(questions[0].select_one('.question-hyperlink').getText())
json_data = json.dumps(question_data, sort_keys=True, indent=4)

print(json_data)
