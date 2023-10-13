import jinja2
from flask import Flask, render_template, request
import os

from database.models import Database
import database.models as models

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

from analyzer import calculate_similarity
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(jinja_env.get_template("Home.html"))

@app.route('/login.html')
def login():
    return render_template(jinja_env.get_template("login.html"))

@app.route('/sign-up.html')
def sign_up():
    return render_template(jinja_env.get_template("sign-up.html"))

@app.route('/upload.html')
def upload():
    return render_template(jinja_env.get_template("upload.html"))



@app.route('/api/resume', methods=['POST'])
# @cross_origin(supports_credentials=True)
def upload_resume():
    print("uploaded")

    data = request.form
    print("resume data", data)

    # resume = models.Resume(content=data, user=user)
    # resume.save()

    print(data)
    return "success"



@app.route('/api/job-posting', methods=['POST'])
# @cross_origin(supports_credentials=True)
def upload_posting():
    print("uploaded")

    # job_posting = models.JobPosting(description="I work", user=user)
    # job_posting.save()

    # print(data)
    return "success"


@app.route('/api/matches-resume', methods=['GET'])
# @cross_origin(supports_credentials=True)
def get_matches_resume():

    print("getting matches")

    args = request.args

    username = args.get('username')

    # get the user
    print(username)

    user = models.User.objects.get(name=username)

    try:
        resume = models.Resume.objects.get(user=user)
    except models.me.DoesNotExist:
        return "No document found", 404

    print(user, user.name)

    # get the content
    content = resume.content

    # Get all the job postings
    job_postings = models.JobPosting.objects()

    match_scores_dict = {}

    for posting in job_postings:
        match_scores_dict[posting.user.name] = calculate_similarity(content, posting.description)

    match_scores = pd.DataFrame(columns=["job_posting", "score"], data=match_scores_dict.items())
    # sort by score
    match_scores = match_scores.sort_values(by="score", ascending=False).reset_index(drop=True)

    print(match_scores)

    result = match_scores.to_json(orient="records")

    print(result)

    return result


@app.route('/api/matches-job-posting', methods=['GET'])
# @cross_origin(supports_credentials=True)
def get_matches_job_posting():

        # get the user
        username = "Business Intelligence Developer"

        user = models.User.objects.get(name=username)

        try:
            job_posting = models.JobPosting.objects.get(user=username)
        except models.me.DoesNotExist:
            return "No document found", 404

        # get the content
        content = job_posting.description

        # Get all the job postings
        resumes = models.Resume.objects()

        match_scores_dict = {}

        for resume in resumes:
            match_scores_dict[resume.user.name] = calculate_similarity(content, resume.content)

        match_scores = pd.DataFrame(columns=["resume", "score"], data=match_scores_dict.items())
        # sort by score
        match_scores = match_scores.sort_values(by="score", ascending=False)

        return match_scores.to_json(orient="records")




def get_string(filename):
    with open(filename, 'r') as file:
        data = file.read()
        file.close()
    return data


if __name__ == '__main__':
    db = Database("development")
    db.run_migrations()

    models.Resume.drop_collection()
    models.User.drop_collection()
    models.JobPosting.drop_collection()

    student1 = models.User(name="Business Intelligence Developer")
    student1.save()
    student2 = models.User(name="Graphic Designer")
    student2.save()
    student3 = models.User(name="Senior Account Executive")
    student3.save()

    resume1 = models.Resume(content=get_string("Backend/sample-data/resume1.txt"), user=student1)
    resume1.save()
    resume2 = models.Resume(content=get_string("Backend/sample-data/resume2.txt"), user=student2)
    resume2.save()
    resume3 = models.Resume(content=get_string("Backend/sample-data/resume3.txt"), user=student3)
    resume3.save()

    hirer1 = models.User(name="Data Warehouse Company")
    hirer1.save()
    hirer2 = models.User(name="Graphic Designing Company")
    hirer2.save()
    hirer3 = models.User(name="Business Company")
    hirer3.save()

    job1 = models.JobPosting(user=hirer1, description=get_string("Backend/sample-data/job1.txt"))
    job1.save()
    job2 = models.JobPosting(user=hirer2, description=get_string("Backend/sample-data/job2.txt"))
    job2.save()
    job3 = models.JobPosting(user=hirer3, description=get_string("Backend/sample-data/job3.txt"))
    job3.save()

    app.run(debug=True, port=5001)
