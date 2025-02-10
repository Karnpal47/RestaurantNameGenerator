from langchain.llms import openai
from langchain.chains import sequentialchain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

import os
os.environ["OPENAI_API_KEY"]="openapi_key"

llm=openai(temperature=0.6)



def restaurant_name_genearator(cuisine):
    #chain for Restaurantname 
    prompt_temp_name=PromptTemplate(
    input_variables=['cuisine'],
    template="I want to open a restaurant for {cuisine} food .Sujjest a fency name for a restaurant "
)

name_chain=LLMChain(llm=llm,prompt=prompt_temp_name,output_key="restaurant_name")




prompt_temp_name=PromptTemplate(
    input_variables=['restaurant_name'],
    template="I want menu list for {restaurant_name}.Give me some dishes for {restaurant_name} "
)

menu_name_chain=LLMChain(llm=llm,prompt=prompt_temp_name,output_key="restaurant_name")



    

