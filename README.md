# NLP Project

## Data Science Job Listing Recommender

### Abstract
The aim of this project was to create a recommender for job listings that helps data science job candidates find roles that suit them. I obtained the text of job listings by scraping Linkedin.com. Using the search term "Data Scientist" for about 50 locations in the English-speaking world, I obtained nearly 10,000 unique job listings with with either "Data Scientist" or "Machine Learning" in the title. Using regex, I attempted to extract from each job listings the section relevant to my recommender: i.e. that relating to what the actual job would entail doing. I then performed text-preprocessing before transforming the corpus into a 'bag of words' and undertaking topic modelling. The topic modelling technique I had most success with was NMF. I created a webapp using streamlit, which obtains user input for preference relating to topics / aspects of job. Having filtered on experience level, the app renders the 10 closest job listings in terms of cosine similarity to those expressed user preferences. The user can read the job listing on the app or click on a link to see the listing on Linkedin. The app is accessible [here](https://share.streamlit.io/billbell73/nlp_project/main/streamlit_app/my_app.py).

### Data
* Scraped web with Linkedin search on “data scientist” for about 50 locations
* Only stored job listings with either “data scientist” or “machine learning” in title
* Obtained nearly 13,000 listings of which roughly one third were duplicates 
* Extracting only the section of each job listing describing contents of job was difficult
* Tackling this task with regex, I ended up with a corpus of just under 4000 observations

### Algorithms
* I experimented with the following: LSA, NMF (with different vectorizers), LDA, CorEx
* CorEx with anchor words produced clean and useful-looking topics, but this didn't seem to translate into relevant job listings
* As a result TF-IDF and NMF won out as the topic modelling methodology for this project.

### Tools

* Web-scraping: Selenium and Beautiful soup
* Data manipulation: Pandas
* Data storage: Pickle
* Text preprocessing: Python re and spaCy
* Vectoriser: TF-IDF
* Topic Modelling: NMF 
* App: Streamlit

### Communication
The methodology and results of this project have been communicated via this document, and via a recorded presentation and its slide-deck.

The URL for the app is: https://share.streamlit.io/billbell73/nlp_project/main/streamlit_app/my_app.py