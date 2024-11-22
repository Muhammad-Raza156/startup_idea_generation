import cohere

# get api key from .env
from dotenv import load_dotenv
import os
load_dotenv()
# get api key from .env
cohere_api_key = os.getenv(COHERE_API_KEY)


co= cohere.ClientV2(cohere_api_key)

def generate_idea(industry, temperature=0.7):
    
    prompt = f"""
Generate a startup idea given the industry. Return the startup idea and without additional commentary.

Industry: Workplace
Startup Idea: A platform that generates slide deck contents automatically based on a given outline

Industry: Home Decor
Startup Idea: An app that calculates the best position of your indoor plants for your apartment

Industry: Healthcare
Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week

Industry: Education
Startup Idea: An online primary school that lets students mix and match their own curriculum based on their interests and goals

Industry: {industry}
Startup Idea:"""

    # Call the Cohere Chat endpoint
    response = co.chat( 
            messages=[{"role": "user", "content": prompt}],
            model="command-r-plus-08-2024",
            temperature=temperature)
        
    return response.message.content[0].text


def generate_name(idea, temperature=0.7):
    
    prompt= f"""
Generate a startup name given the startup idea. Return the startup name and without additional commentary.

Startup Idea: A platform that generates slide deck contents automatically based on a given outline
Startup Name: Deckerize

Startup Idea: An app that calculates the best position of your indoor plants for your apartment
Startup Name: Planteasy 

Startup Idea: A hearing aid for the elderly that automatically adjusts its levels and with a battery lasting a whole week
Startup Name: Hearspan

Startup Idea: An online primary school that lets students mix and match their own curriculum based on their interests and goals
Startup Name: Prime Age

Startup Idea: {idea}
Startup Name:"""

    # Call the Cohere Chat endpoint
    response = co.chat( 
            messages=[{"role": "user", "content": prompt}],
            model="command-r-plus-08-2024",
            temperature=temperature)
        
    return response.message.content[0].text
