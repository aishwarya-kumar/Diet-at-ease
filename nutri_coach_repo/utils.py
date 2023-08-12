from sentence_transformers import SentenceTransformer
import pinecone
import openai
import streamlit as st
openai.api_key = "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"
model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone.init(api_key='02b2b813-8d68-4456-b421-cda952bd97a7', environment='asia-southeast1-gcp-free')
index = pinecone.Index('llm-chatbot-metabolicdisorders')

def find_match(input):
    input_em = model.encode(input).tolist()
    result = index.query(input_em, top_k=2, includeMetadata=True)
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']

def query_refiner(conversation, query):

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    return response['choices'][0]['text']

def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string