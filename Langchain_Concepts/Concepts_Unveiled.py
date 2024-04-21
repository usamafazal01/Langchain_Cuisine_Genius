# # from secret_key import openApi_key
# # import os
# # from langchain_openai import OpenAI
# # from langchain.prompts import PromptTemplate
# # from langchain.chains import LLMChain
# # from langchain.chains import SimpleSequentialChain
# # from langchain.chains import SequentialChain
# # from langchain.agents.initialize import initialize_agent
# # from langchain.agents import AgentType, load_tools


# # os.environ['OPENAI_API_KEY'] = openApi_key

# # # Create an instance of OpenAI
# # llm = OpenAI(temperature=0.6)

# # # Invoke OpenAI to generate restaurant names for Italian food
# # # name = llm.invoke("I want to open a restaurant for Italian Food. Suggest a fancy name for this. Give me 5 names") ->>>just for testing
# # # print(name)

# # # Restaurant Name Template
# # # prompt_template_rname = PromptTemplate(
# # #     input_variables=['cuisine'],
# # #     template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this."
# # # )

# # # # # Format the prompt template with the desired cuisine
# # # # formatted_prompt = prompt_template_name.format(cuisine="American")  ->>>This is python string formatting

# # # # Create an LLMChain instance with the OpenAI model and prompt template
# # # name_chain = LLMChain(llm=llm, prompt=prompt_template_rname, output_key= "restaurant_name")

# # # # # Invoke the chain with a new cuisine
# # # # # Instead of python string formatting we use ->>>Chain concept in langchain
# # # name_chain_output = name_chain.invoke("Indian")
# # # print(name_chain_output)

# # # Menu items template
# # # prompt_template_items = PromptTemplate(
# # #     input_variables=['restaurant_name'],
# # #     template=" Suggest me some food items name for {restaurant_name}. Return it as a comma separsated list "
# # # )

# # # food_items_chain = LLMChain(llm=llm, prompt = prompt_template_items, output_key="menu_items")

# # # # Now we create a ->>>Simple Sequential Chain concept which take output of chain as input means take resturant name as input 
# # # chain = SimpleSequentialChain(chains= [name_chain, food_items_chain ])
# # # response = chain.invoke("indian")
# # # print("SimpleSequentialChain Response is :")
# # # print(response)


# # # As in this ->>> SimpleSequentialChain there is only a one input and output so we use a concept of 
# # # ->>> Sequential Chain here 
# # # chain2 = SequentialChain(chains= [name_chain, food_items_chain ],
# # #                          input_variables=['cuisine'],
# # #                          output_variables=['restaurant_name', 'menu_items']
# # #                          )
# # # response = chain2.invoke("indian")
# # # print("SequentialChain Response is :")
# # # print(response)


# # # AGENTS IN LANGCHAIN


# try:
    
#     from langchain_community.llms import LLM  # Updated import statement
#     from langchain.agents import AgentType, initialize_agent
#     from langchain.tools import load_tools
#     from secret_key import openApi_key

#     # Create a large language model instance
#     llm = LLM("openai", api_key=openApi_key)

#     # Define the list of tools you want to use
#     tools = load_tools(["wikipedia", "math"], llm=llm)

#     # Create the agent
#     agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

#     # Define your query
#     query = "When was Elon Musk born and what's his age in 2023?"

#     # Invoke the agent with error handling
#     try:
#         agent_response = agent.invoke(query, handle_parsing_errors=True)
#         print(agent_response)  # Print the agent's response
#     except Exception as e:
#         print("An error occurred:", e)  # Handle potential exceptions

# except ImportError:
#     print("Langchain import error. Consider using a compatible version or alternative libraries.")
#     # Alternative approach (if Langchain import fails):
#     # ... (code using a different library or approach for similar functionality)
#     # You'll need to implement this section using a different library or approach that
#     # can interact with Wikipedia to find Elon Musk's birthdate and calculate his age.


# MEMORY IN LANGCHAIN

# class ConversationalBufferMemory:
#     def __init__(self):
#         self.memory = []

#     def add_to_memory(self, sentence):
#         self.memory.append(sentence)

#     def display_memory(self):
#         for i, sentence in enumerate(self.memory, 1):
#             print(f"{i}. {sentence}")


# class LangChain:
#     def __init__(self, memory):
#         self.memory = memory

#     def generate_response(self, prompt):
#         response = ""
#         for sentence in self.memory:
#             if prompt in sentence:
#                 response += sentence.replace(prompt, "").strip() + " "
#         return response.strip()


# # Example usage:
# buffer_memory = ConversationalBufferMemory()
# chain = LangChain(buffer_memory)

# # Add sentences to the memory
# buffer_memory.add_to_memory("What is your name?")
# buffer_memory.add_to_memory("My name is LangChain.")
# buffer_memory.add_to_memory("How are you?")
# buffer_memory.add_to_memory("I am fine, thank you.")

# # Display the memory
# print("Conversation Memory:")
# buffer_memory.display_memory()

# # Ask questions and generate responses
# prompt = "What is your name?"
# print("\nResponse:", chain.generate_response(prompt))

# prompt = "How are you?"
# print("Response:", chain.generate_response(prompt))
