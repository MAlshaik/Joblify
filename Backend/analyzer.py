from spacy.lang.en import English
import numpy as np

import srsly

from flask import Flask, render_template

patterns = srsly.read_jsonl("Backend/skill_patterns.jsonl")

nlp = English()

ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)

def extract_keywords(txt):

    doc = nlp(txt)
    keywords = list(doc.ents)
    # remove duplicates
    keywords = [str(k) for k in keywords]
    keywords = list(set(keywords))

    return keywords


def calculate_score(resume_kws, job_kws):

    resume_kws = np.array(resume_kws)
    job_kws = np.array(job_kws)

    match_count = 0
    for i in resume_kws:
      for j in job_kws:
        if i == j:
          match_count += 1
          continue

    score = 2 * match_count / (resume_kws.size + job_kws.size)
    return score


def calculate_similarity(resume_str, job_str):
    resume_keywords = extract_keywords(resume_str)
    job_keywords = extract_keywords(job_str)

    score = calculate_score(resume_keywords, job_keywords)
    return score

