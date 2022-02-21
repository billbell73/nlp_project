import streamlit as st
from scipy.spatial import distance
import pandas as pd
import pickle

with open('doc_topic_5_copy.pickle', 'rb') as handle:
    doc_topic_5 = pickle.load(handle)

df = pd.read_pickle("big_job_df_copy.pickle")

def clear_pick():
    if 'jobs' in st.session_state:
        st.session_state.pop('jobs')

def best_jobs(input_0, input_1, level, df):
    value_0 = input_0/1000
    value_1 = input_1/1000
    target = [value_0, value_1, 0, 0, 0]
    distances = distance.cdist([target], doc_topic_5, "cosine")[0]
    sorted_indexes = distances.argsort()

    jobs = []
    for index in sorted_indexes:
        job = df.iloc[index]
        if job['level'] == str.lower(level):
            jobs.append(job)

        if len(jobs) >= 10:
            break

    st.session_state.jobs = jobs


st.title('Linkedin job listing finder')

topic_0_input = st.sidebar.slider('Pick a number for topic 0', min_value=0, max_value=135, step=1, on_change=clear_pick)

topic_1_input = st.sidebar.slider('Pick a number for topic 1', 0, 124, on_change=clear_pick)

# this stype hack was taken from https://discuss.streamlit.io/t/horizontal-radio-buttons/2114/3
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

level = st.sidebar.radio("Experience Level:", ('Junior', 'Mid', 'Senior'), index=1, on_change=clear_pick)

st.sidebar.button("Search", on_click=best_jobs, args=(topic_0_input, topic_1_input, level, df))

if 'jobs' in st.session_state:
    for i, job in enumerate(st.session_state.jobs):

        with st.expander(f"{str(i+1)}. {job['title']} - {job['companyName']}"):
            st.markdown(job['description'], unsafe_allow_html=True)
            st.write("")
            st.write(f"**Location**: {job['location']}")
            link = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job.name}"
            st.write(f"**Listing on Linkedin**: {link}")
