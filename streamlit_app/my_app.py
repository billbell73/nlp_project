import streamlit as st
from scipy.spatial import distance
import pickle5 as pickle

with open('../doc_topic_corex.pickle', 'rb') as handle:
    doc_topic = pickle.load(handle)

with open('../big_job_df.pickle', 'rb') as handle2:
    df = pickle.load(handle2)

def clear_pick():
    if 'jobs' in st.session_state:
        st.session_state.pop('jobs')

def best_jobs(topic_inputs, level):
    target = [ element / 10 for element in topic_inputs]
    distances = distance.cdist([target], doc_topic, "cosine")[0]
    sorted_indexes = distances.argsort()

    jobs = []
    for index in sorted_indexes:
        job = df.iloc[index]
        if job['level'] == str.lower(level):
            jobs.append(job)

        if len(jobs) >= 10:
            break

    st.session_state.jobs = jobs

col1, col2 = st.columns([25, 30])
with col1:
    st.image('LI-Logo.png', width=300)
with col2:
    if 'jobs' in st.session_state:
        st.write("")
        st.subheader('**Data Science job listing finder**')

if 'jobs' not in st.session_state:
    st.title('Data Science job listing finder')
st.sidebar.write('**Choose the extent (out of 10) you want your job to involve:**')

input_0 = st.sidebar.slider('Communication with stakeholders', 1, 10, 5, on_change=clear_pick)
input_1 = st.sidebar.slider('Engineering', 1, 10, 5, on_change=clear_pick)
input_2 = st.sidebar.slider('Modelling / developing models', 1, 10, 5, on_change=clear_pick)
input_3 = st.sidebar.slider('Good work environment and work-life balance', 1, 10, 5, on_change=clear_pick)
input_4 = st.sidebar.slider('Startup-like environment', 1, 10, 5, on_change=clear_pick)

# this style hack was taken from https://discuss.streamlit.io/t/horizontal-radio-buttons/2114/3
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.sidebar.write("")
level = st.sidebar.radio('Experience level:', ('Junior', 'Mid', 'Senior'), index=1, on_change=clear_pick)

topic_inputs = [input_0, input_1, input_2, input_3, input_4]

st.sidebar.button("Search", on_click=best_jobs, args=(topic_inputs, level))

if 'jobs' in st.session_state:
    for i, job in enumerate(st.session_state.jobs):

        with st.expander(f"{str(i+1)}. {job['title']} - {job['companyName']}"):
            st.markdown(job['description'], unsafe_allow_html=True)
            st.write("")
            st.write(f"**Location**: {job['location']}")
            link = f"https://www.linkedin.com/jobs-guest/jobs/api/jobPosting/{job.name}"
            st.write(f"**Listing on Linkedin**: {link}")
