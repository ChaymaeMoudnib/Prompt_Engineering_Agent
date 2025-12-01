"""
LangChain Integration Example (Optional)
Install: pip install langchain langchain-google-genai
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import (
    PromptTemplate,
    ChatPromptTemplate,
    FewShotPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)
from langchain.chains import LLMChain

load_dotenv()

# Initialize LangChain LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-exp",
    google_api_key=os.getenv("Gemini_api_key"),
    temperature=0.7
)

class LangChainExamples:
    """Examples of LangChain prompt templates"""
    
    @staticmethod
    def simple_template():
        """Basic PromptTemplate with variables"""
        template = """
You are a {role}. 
Answer the following question professionally:

Question: {question}

Answer:"""
        
        prompt = PromptTemplate(
            input_variables=["role", "question"],
            template=template
        )
        
        # Create chain
        chain = LLMChain(llm=llm, prompt=prompt)
        
        # Run
        result = chain.run(
            role="software engineer",
            question="What is dependency injection?"
        )
        return result
    
    @staticmethod
    def few_shot_template():
        """Few-shot learning with examples"""
        
        # Define examples
        examples = [
            {
                "input": "happy",
                "output": "sad"
            },
            {
                "input": "tall",
                "output": "short"
            },
            {
                "input": "fast",
                "output": "slow"
            }
        ]
        
        # Create example template
        example_template = """
Input: {input}
Output: {output}
"""
        
        example_prompt = PromptTemplate(
            input_variables=["input", "output"],
            template=example_template
        )
        
        # Create few-shot template
        few_shot_prompt = FewShotPromptTemplate(
            examples=examples,
            example_prompt=example_prompt,
            prefix="Give the opposite of every input word:\n",
            suffix="\nInput: {adjective}\nOutput:",
            input_variables=["adjective"]
        )
        
        chain = LLMChain(llm=llm, prompt=few_shot_prompt)
        return chain.run(adjective="bright")
    
    @staticmethod
    def chat_template():
        """Multi-message chat template"""
        
        system_template = "You are a {role} who answers in a {style} style."
        system_prompt = SystemMessagePromptTemplate.from_template(system_template)
        
        human_template = "{user_input}"
        human_prompt = HumanMessagePromptTemplate.from_template(human_template)
        
        chat_prompt = ChatPromptTemplate.from_messages([
            system_prompt,
            human_prompt
        ])
        
        chain = LLMChain(llm=llm, prompt=chat_prompt)
        
        return chain.run(
            role="pirate",
            style="theatrical",
            user_input="Tell me about machine learning"
        )
    
    @staticmethod
    def partial_template():
        """Template with partial variables (pre-filled)"""
        
        template = """
Translate the following {source_language} text to {target_language}:

Text: {text}

Translation:"""
        
        prompt = PromptTemplate(
            input_variables=["source_language", "target_language", "text"],
            template=template
        )
        
        # Partially fill some variables
        partial_prompt = prompt.partial(
            source_language="English",
            target_language="Spanish"
        )
        
        chain = LLMChain(llm=llm, prompt=partial_prompt)
        return chain.run(text="Hello, how are you?")


# Usage examples
if __name__ == "__main__":
    examples = LangChainExamples()
    
    print("\n=== Simple Template ===")
    print(examples.simple_template())
    
    print("\n=== Few-Shot Template ===")
    print(examples.few_shot_template())
    
    print("\n=== Chat Template ===")
    print(examples.chat_template())
    
    print("\n=== Partial Template ===")
    print(examples.partial_template())