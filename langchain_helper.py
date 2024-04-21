from secret_key import openApi_key
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain
from langchain.chains import SequentialChain

import os
os.environ['OPENAI_API_KEY'] = openApi_key

llm = OpenAI(temperature=0.7)

def generate_restaurant_name_and_items(cuisine):

# CHAIN-1 Name Chain 
    prompt_template_rname = PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
)
    name_chain = LLMChain(llm=llm, prompt=prompt_template_rname, output_key= "restaurant_name")

# CHAIN-2 Menu Items
    prompt_template_items = PromptTemplate(
    input_variables=['restaurant_name'],
    template=" Suggest me some food items name for {restaurant_name}. Return it as a comma separsated list"
)

    food_items_chain = LLMChain(llm=llm, prompt =prompt_template_items , output_key="menu_items")

# SEQUENTIAL CHAIN

    sequentialChain = SequentialChain(chains= [name_chain, food_items_chain ],
                         input_variables=['cuisine'],
                         output_variables=['restaurant_name', 'menu_items']
                         )
    response = sequentialChain.invoke({'cuisine': cuisine} )

    return response






 
    
