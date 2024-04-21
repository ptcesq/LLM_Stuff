# A simple Question and Answer model 
# Demonstrates the model - does not training, just prompt engineering 
# Author:   PTC
# Date:     4/18/24 

# Import libraries 
from transformers import pipeline

# ## Select the model 
qa_model = pipeline("question-answering", "timpal0l/mdeberta-v3-base-squad2")


# ## Provide Context and Prompt Question 
Context = "My name is Patrick T. Cronin and I live in Haddonfield NJ"
Question = "Where does Patrick Cronin live?"

# ## Posit the Prompt to the model 
completion = qa_model(question = Question, context = Context)
print('\n')
print("Completion: ", completion)
