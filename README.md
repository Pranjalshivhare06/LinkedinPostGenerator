Project Name: Post Generator for Linkedin

Description: User can select topic, size for the post, and our app will generate a post for the user.

Tech used: 
    1. Python
    2. Groq API
    3. Sample data generated from GPT


Architechture
    Stage 1: Preprocessing of Data
    Stage 2: Postprocessing of Data

Stage 1
1. Generate the raw data using any llm of your choice.
2. Keep the data in JSON format(text, engagement) 
3. Generate insights from the data like line_count, language, tags
Using chain = prompt_template | llm 
4. Minimize the number of tags.
eg. Job search, Jobhunt, job hunting => "Job search"

Few shots is a prompting technique that is used to generate the output by giving sample answer to the problem.

Building UI
Used streamlit to build simple UI




