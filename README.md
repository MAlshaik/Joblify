# Joblify 
---

# What Inspired This
The traditional job or internship search for college students involves sending similar applications to countless similar jobs. Many automated Applicant Tracking Systems (ATS) do a superficial and narrow evaluation of resumes, only looking for exact keywords, which forces students into a tedious game of “keyword optimizing” their resume to “beat the bot”, which shouldn’t be necessary in today’s world of NLP. Furthermore, employers are usually only exposed to the applicants that take the time to apply to them, instead of all possibly interested candidates.

We hope to expand and personalize the search process through a resume and job posting network, not only for job seekers but also for employers, so that they can reach out to people who are actually likely to be potential candidates. We want the job search to begin as soon as students upload their resumes.

# What does it do?
Joblify is meant for both employers and job seekers, and each group receives a different interface. When a job seeker uploads their resume, it is automatically analyzed using our NLP model and all available jobs are shown to them in order of relevance. When an employer uploads their job posting, all possible candidates are listed for them in order of qualification for the job.


# How we built it?
## Semantic Search Development
The Natural Language Processing model that powers Joblify was written using a semantic search pipeline from the spaCy library combined with a pattern using an existing job skill [dataset](https://github.com/microsoft/SkillsExtractorCognitiveSearch/tree/master/data) by Microsoft to specialize it to select job-related entities, such as fields of expertise, soft skills, and programming languages, rather than just English language entities. 

## Our Exploration
Our machine learning algorithm was ultimately achieved after iterating through different machine learning models (such as whether to use named entity recognition, vector similarity, or semantic search) and libraries (including [Cohere](https://docs.cohere.ai/) and [Pinecone](https://www.pinecone.io/semantic-search/?utm_term=semantic%20search&utm_campaign=General&utm_source=adwords&utm_medium=ppc&hsa_acc=3111363649&hsa_cam=16569728073&hsa_grp=135276647740&hsa_ad=587750423757&hsa_src=g&hsa_tgt=kwd-93086337&hsa_kw=semantic%20search&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=EAIaIQobChMIjPuzguDs_AIVTQqtBh0SgQ-REAAYASAAEgIF7_D_BwE)), and deciding on the most performant one on our mock testing data. We used matplotlib and Plotly to visualize the effectiveness of its ability to match resumes to job descriptions.

# Challenges we ran into
1. Since we are all beginners to web development and SpartaHack8 was the first hackathon for all of us, we had hiccups with getting used to the different coding styles of each of our members and learning how to put together the different components. With help of well-defined comments, group discussions, crystal-clear concept maps on the whiteboards, and patience, we were able to develop version control and coding conventions to synergize better.
2. Extracting entities (like skills, experiences, etc) from the job postings was a nuanced task. We started with a generally named entity recognition model from the Cohere API, but it struggled to extract relevant information. We ended up using a semantic search pipeline from spaCy in Python.
3. Although front-end (involving HTML, CSS, and JavaScript) was the first component of our project that we got started on, at times working out the alignments of the various elements on many web pages was somewhat of a tedious task that required repetitive correction. By delegating the webpages among our 2 front-end developers, we were able to fast-track the alignment-correction process.

# Accomplishments that we're proud of
Some of the accomplishments we’re most proud of include:

1. We developed a fantastic looking front-end design including a brand name, logo, and core values within 14-15 hours, right from scratch
2. We went from no knowledge of full stack development, to being able to work with flask. We 
3. Our Implementation of ML
4. We made a prototype of the video conferencing tool with a shared whiteboard.

This 24-hour journey in which we developed Joblify had several highs and lows. The fact that we were able to enter the event with an idea, build it up bit-by-bit from scratch, create a full-stack application with frameworks we had very little experience with, and submit a project in time is a great feat for us. 

# What we learned
Each of the members of our team had experience in disparate areas of development, such as front-end, machine learning, and MongoDB, but none of us had ever built a full-stack website. The hackathon offered a unique challenge for us to integrate our skills and gain exposure to how various technologies come together to create a fully usable, marketable app. With the help of mentors, tutorials, and trial and error, we learned how to combine a Javascript front-end with a back-end API using Flask. For the first time, we navigated the challenges of debugging communication between the user interface and the analysis code, as well as the database with MongoDB. All of us left with exponentially more experience in web development in Python and JavaScript than we came in with.

# What's next for Joblify
1. One of the constraints of the 24-hour hackathon is being limited to a rough prototype of the ML model without access to much user feedback to help us improve it. If we were given the time to do further research and development, using a transformer embedding model fine-tuned on training data offered by users of the site would help us greatly improve the strength and accuracy of the job and employee matching functionality.
2. Most big employers want to sort job seekers by their ability to lead and work, and their level of experience, not just their type of skills. We will use a model that infers not just using skills, but also the level of experience and ability. 
3. Matching Employers to employees should take into consideration interest as well as expertise. A student might not be interested in a job they are very well qualified for, or vice versa.
4. Certain qualities are more important than others. For example, time and location of availability take precedence over the job’s level of relevance. Joblify should take this into account.
