"""
Prompt Engineering Techniques Library
Demonstrates various prompting techniques for better LLM responses
"""

class PromptTechniques:
    """Collection of prompt engineering techniques"""
    
    @staticmethod
    def zero_shot(task: str) -> str:
        """
        Zero-shot: Direct instruction without examples
        Best for: Simple, well-understood tasks
        """
        return f"{task}"
    
    @staticmethod
    def few_shot(task: str, examples: list) -> str:
        """
        Few-shot: Provide examples to guide the model
        Best for: Tasks needing specific format or style
        
        Args:
            task: The task description
            examples: List of dicts with 'input' and 'output' keys
        """
        prompt = f"{task}\n\nExamples:\n"
        for i, ex in enumerate(examples, 1):
            prompt += f"\nExample {i}:\n"
            prompt += f"Input: {ex['input']}\n"
            prompt += f"Output: {ex['output']}\n"
        prompt += "\nNow complete the following:\n"
        return prompt
    
    @staticmethod
    def chain_of_thought(problem: str) -> str:
        """
        Chain-of-Thought: Ask model to show reasoning steps
        Best for: Complex reasoning, math, logic problems
        """
        return f"""{problem}

Let's approach this step-by-step:
1. First, identify the key information
2. Then, work through the logic
3. Finally, provide the answer

Think through this carefully and show your reasoning:"""
    
    @staticmethod
    def role_based(role: str, task: str, context: str = "") -> str:
        """
        Role-based: Assign a persona/expertise to the model
        Best for: Domain-specific tasks, creative writing
        """
        prompt = f"You are a {role}."
        if context:
            prompt += f" {context}"
        prompt += f"\n\n{task}"
        return prompt
    
    @staticmethod
    def structured_output(task: str, format_spec: str) -> str:
        """
        Structured Output: Request specific format (JSON, table, list)
        Best for: Data extraction, structured information
        """
        return f"""{task}

Provide your response in the following format:
{format_spec}

Response:"""
    
    @staticmethod
    def self_consistency(problem: str, num_approaches: int = 3) -> str:
        """
        Self-Consistency: Generate multiple reasoning paths
        Best for: Problems with multiple solution approaches
        """
        return f"""{problem}

Solve this problem using {num_approaches} different approaches or reasoning paths.
For each approach:
1. Explain your reasoning
2. Show your work
3. State your answer

Then compare the answers to find the most consistent solution."""
    
    @staticmethod
    def emotion_prompt(task: str, motivation: str = "This is very important to my career") -> str:
        """
        Emotion Prompt: Add emotional/motivational context
        Best for: Getting more detailed, careful responses
        """
        return f"""{task}

{motivation}. Please give this your full attention and provide a thorough, high-quality response."""
    
    @staticmethod
    def instruction_breakdown(task: str, constraints: list = None, steps: list = None) -> str:
        """
        Clear Instructions: Break down complex tasks with constraints
        Best for: Complex multi-step tasks
        """
        prompt = f"Task: {task}\n"
        
        if constraints:
            prompt += "\nConstraints:\n"
            for c in constraints:
                prompt += f"- {c}\n"
        
        if steps:
            prompt += "\nFollow these steps:\n"
            for i, step in enumerate(steps, 1):
                prompt += f"{i}. {step}\n"
        
        return prompt
    
    @staticmethod
    def context_enriched(task: str, context: str) -> str:
        """
        Context Enrichment: Provide background information
        Best for: Tasks requiring domain knowledge
        """
        return f"""Context:
{context}

Based on the context above, {task}"""
    
    @staticmethod
    def meta_prompting(task_type: str, specific_task: str) -> str:
        """
        Meta Prompting: Ask model to create optimal prompt structure
        Best for: Optimizing prompts for specific tasks
        """
        return f"""Create an optimal prompt structure for the following type of task: {task_type}

The specific task is: {specific_task}

Design a prompt that:
1. Clearly defines the objective
2. Provides necessary context
3. Specifies the desired output format
4. Includes relevant constraints

Optimal Prompt:"""