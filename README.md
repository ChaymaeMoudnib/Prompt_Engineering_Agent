# Prompt Engineering Lab

An interactive learning environment for understanding and practicing prompt engineering techniques with Large Language Models (LLMs). Built with Google Gemini API, this project provides hands-on experience with 10 core prompting strategies used in production AI systems.

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Prompting Techniques](#prompting-techniques)
- [Usage Examples](#usage-examples)
- [Learning Resources](#learning-resources)
- [Advanced Usage](#advanced-usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

Prompt engineering is the practice of designing inputs to guide LLM behavior and improve output quality. This project goes beyond theoretical explanations by providing an interactive environment where you can:

- Test different prompting techniques side-by-side
- Understand when and why to use each approach
- Build intuition through immediate feedback
- Apply patterns to real-world problems

**Who is this for?**
- Data scientists working with LLMs
- ML engineers building AI applications
- Students learning about generative AI
- Anyone wanting to improve their prompting skills

---

## Key Features

### 10 Prompt Engineering Techniques
Implementations of research-backed prompting strategies including zero-shot, few-shot, chain-of-thought, role-based prompting, and more.

### Interactive Testing
Switch between techniques using simple commands (`/cot`, `/few`, `/role`) and see immediate differences in outputs.

### Comparison Mode
Use the `demo` command to run the same query through multiple techniques simultaneously, making differences explicit.

### Web Search Integration
Built-in search functionality to test prompting techniques on current information retrieval tasks.

### Production-Ready Patterns
Code structure follows best practices for building LLM applications, making it easy to adapt for real projects.

---

## Installation

### Prerequisites
- Python 3.8+
- Google Gemini API key ([Get one here](https://ai.google.dev/))
- Serper API key for web search ([Get one here](https://serper.dev/))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent

cd Prompt_Engineering_Agent
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure API keys**

Create a `.env` file in the project root:
```bash
Gemini_api_key=your_gemini_api_key_here
Serper_api_key=your_serper_api_key_here
```

---

## Quick Start

```bash
python main.py
```

### Basic Commands

```
You: What is machine learning?
Agent: [Responds using zero-shot prompting]

You: /cot What is 15% of 240?
Agent: [Uses chain-of-thought reasoning]

You: demo What causes rain?
Agent: [Compares multiple techniques]

You: search latest AI news
Agent: [Searches web and summarizes results]

You: help
Agent: [Shows all available commands]
```

---

## Prompting Techniques

### 1. Zero-Shot Prompting
**Description:** Direct instruction without examples.  
**Best for:** Simple, well-understood tasks.  
**Example:**
```
Translate "Hello" to Spanish.
```

**Research basis:** Models pre-trained on large corpora can perform many tasks without task-specific training.

---

### 2. Few-Shot Prompting
**Description:** Provide 2-5 examples demonstrating the desired input-output pattern.  
**Best for:** Tasks requiring specific format, style, or pattern recognition.  
**Example:**
```
Convert adjectives to adverbs:
- Quick → Quickly
- Careful → Carefully

Now convert: Happy → ?
```

**Research basis:** Demonstrated in GPT-3 paper (Brown et al., 2020) to dramatically improve task performance without fine-tuning.

**Command:** `/few [your query]`

---

### 3. Chain-of-Thought (CoT)
**Description:** Prompt the model to articulate its reasoning process step-by-step.  
**Best for:** Math problems, logic puzzles, complex reasoning tasks.  
**Example:**
```
Problem: A store has 50 apples. They sell 60% of them. How many remain?

Let's solve this step-by-step:
1. Calculate 60% of 50: 0.60 × 50 = 30 apples sold
2. Subtract from original: 50 - 30 = 20 apples
3. Answer: 20 apples remain
```

**Research basis:** "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022) showed dramatic accuracy improvements on reasoning tasks.

**Command:** `/cot [your query]`

---

### 4. Role-Based Prompting
**Description:** Assign a specific expertise, persona, or perspective to the model.  
**Best for:** Domain-specific tasks, creative writing, specialized explanations.  
**Example:**
```
You are an experienced software architect.
Explain microservices architecture to a junior developer.
```

**Why it works:** Guides the model's tone, depth, and terminology by activating relevant training data patterns.

**Command:** `/role [your query]`

---

### 5. Structured Output
**Description:** Explicitly request specific formatting (JSON, tables, bullet points, etc.).  
**Best for:** Data extraction, API integrations, consistent formatting needs.  
**Example:**
```
List three benefits of exercise in this format:
{
  "benefits": [
    {"name": "...", "description": "..."},
    ...
  ]
}
```

**Production value:** Essential for integrating LLM outputs into downstream systems.

**Command:** `/structured [your query]`

---

### 6. Self-Consistency
**Description:** Generate multiple reasoning paths and select the most consistent answer.  
**Best for:** Problems where multiple solution approaches exist.  
**Implementation:** Model generates 3-5 solutions using different reasoning strategies, then identifies consensus.

**Research basis:** "Self-Consistency Improves Chain of Thought Reasoning" (Wang et al., 2022) showed significant accuracy gains.

---

### 7. Emotion/Motivation Prompting
**Description:** Add emotional context or stakes to encourage careful responses.  
**Best for:** Tasks requiring attention to detail or thoroughness.  
**Example:**
```
This code review is critical for production deployment.
Please analyze this function carefully for potential bugs.
```

**Research basis:** Recent studies show emotionally-loaded prompts can improve response quality and reduce errors.

**Command:** `/emotion [your query]`

---

### 8. Context Enrichment
**Description:** Provide relevant background information before the main task.  
**Best for:** Domain-specific questions, scenarios requiring specialized knowledge.  
**Example:**
```
Context: Python lists are mutable and use zero-based indexing.
The append() method adds elements to the end.

Question: What happens when you call my_list.append(5)?
```

---

### 9. Meta Prompting
**Description:** Ask the model to design or optimize the prompt structure itself.  
**Best for:** Complex tasks where optimal prompting strategy is unclear.  
**Example:**
```
Design an optimal prompt for analyzing customer feedback sentiment
that considers context, tone, and intent.
```

---

### 10. Instruction Breakdown
**Description:** Decompose complex tasks into clear steps with explicit constraints.  
**Best for:** Multi-step processes, tasks with multiple requirements.  
**Example:**
```
Task: Create a product description

Constraints:
- Maximum 100 words
- Include 3 key features
- Target audience: software developers

Steps:
1. Write attention-grabbing opening
2. List three technical features with benefits
3. End with clear call-to-action
```

---

## Usage Examples

### Example 1: Comparing Techniques

```python
# Test the same query with different techniques
python main.py

You: demo What is recursion in programming?

# Output shows responses using:
# - Zero-shot (direct answer)
# - Chain-of-thought (step-by-step explanation)
# - Role-based (as a CS professor)
# - Emotion prompt (with careful attention)
```

### Example 2: Web Search with Structured Output

```python
You: search quantum computing breakthroughs 2024

# Agent uses structured output prompting to format:
# - Key findings as bullet points
# - 2-3 sentence summary
# - Source citations
```

### Example 3: Chain-of-Thought for Math

```python
You: /cot If a car travels 60 mph for 2.5 hours, how far does it go?



### Core Components

**agent.py**
- `agent_reply()`: Main function handling user queries
- `demonstrate_techniques()`: Comparison utility
- Technique routing logic

**prompt_techniques.py**
- `PromptTechniques` class with static methods
- Each method implements one prompting pattern
- Reusable across different LLM providers

**tools.py**
- `google_search()`: Web search integration
- Extensible for additional tools (calculator, database, etc.)

---

## Learning Resources

### Research Papers

1. **Few-Shot Learning**
   - "Language Models are Few-Shot Learners" (Brown et al., 2020)
   - [arXiv:2005.14165](https://arxiv.org/abs/2005.14165)

2. **Chain-of-Thought**
   - "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" (Wei et al., 2022)
   - [arXiv:2201.11903](https://arxiv.org/abs/2201.11903)
   

3. **Self-Consistency**
   - "Self-Consistency Improves Chain of Thought Reasoning" (Wang et al., 2022)
   - [arXiv:2203.11171](https://arxiv.org/abs/2203.11171)

### Online Courses

1. **DeepLearning.AI**
   - ChatGPT Prompt Engineering for Developers (with Andrew Ng)
   - [Course Link](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

2. **Anthropic**
   - Prompt Engineering Interactive Tutorial
   - [Claude Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)

3. **OpenAI**
   - Prompt Engineering Guide
   - [OpenAI Documentation](https://platform.openai.com/docs/guides/prompt-engineering)

### Documentation & Guides

- **Prompt Engineering Guide** (dair-ai): [https://www.promptingguide.ai/](https://www.promptingguide.ai/)
- **LangChain Documentation**: [https://python.langchain.com/docs/](https://python.langchain.com/docs/)
- **Learn Prompting**: [https://learnprompting.org/](https://learnprompting.org/)

### Books

1. **"The Prompt Engineer's Handbook"** - Draft available online
2. **"Building LLM Applications"** - Practical patterns and architectures

---

## Advanced Usage

### Adapting to Other LLM Providers

The codebase is designed to be provider-agnostic. To switch from Google Gemini to another provider:

**OpenAI Example:**
```python
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def agent_reply(user_prompt: str, technique: str = "zero_shot"):
    # Apply technique to format prompt
    final_prompt = apply_technique(user_prompt, technique)
    
    response = client.chat.completions.create(
        model="gpt-4-mini-",
        messages=[{"role": "user", "content": final_prompt}]
    )
    return response.choices[0].message.content
```

**Anthropic Claude Example:**
```python
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def agent_reply(user_prompt: str, technique: str = "zero_shot"):
    final_prompt = apply_technique(user_prompt, technique)
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": final_prompt}]
    )
    return response.content[0].text
```

### Integrating with LangChain

See `langchain_agent.py` for complete examples of:
- PromptTemplate usage
- Few-shot prompting with example selectors
- Chain composition
- Memory integration

### Building Custom Techniques

Add your own prompting techniques to `prompt_techniques.py`:

```python
@staticmethod
def your_technique(task: str, custom_param: str) -> str:
    """
    Your Technique: Description of what it does
    Best for: When to use this technique
    """
    return f"""[Your prompt template here]
    
Task: {task}
Custom Parameter: {custom_param}

Instructions:
..."""
```

Then register it in `agent.py`:

```python
elif technique == "your_technique":
    final_prompt = pt.your_technique(user_prompt, param_value)
```

---

## Best Practices

### When to Use Each Technique

| Technique | Use Case | Avoid When |
|-----------|----------|------------|
| Zero-shot | Simple, clear tasks | Complex reasoning needed |
| Few-shot | Specific format required | Examples are ambiguous |
| Chain-of-thought | Math, logic, reasoning | Simple factual queries |
| Role-based | Domain expertise needed | Generic queries |
| Structured | Data extraction, APIs | Creative/open-ended tasks |
| Self-consistency | High-stakes decisions | Speed is critical |

### Prompt Design Principles

1. **Be Specific**: Vague prompts get vague responses
2. **Provide Context**: Give the model necessary background
3. **Show Examples**: When format matters, demonstrate it
4. **Iterate**: Test and refine based on outputs
5. **Consider Token Limits**: Balance detail with efficiency

### Common Pitfalls

- **Over-prompting**: Too many instructions can confuse the model
- **Ambiguity**: Unclear requirements lead to inconsistent outputs
- **Ignoring Context Windows**: Long prompts may be truncated
- **Not Testing Variations**: First attempt rarely optimal
- **Forgetting Edge Cases**: Test with diverse inputs

---

## Contributing

Contributions are welcome! Here's how you can help:

### Types of Contributions

- **New Techniques**: Implement additional prompting strategies
- **Provider Support**: Add integrations for other LLM APIs
- **Documentation**: Improve explanations or add examples
- **Bug Fixes**: Report and fix issues
- **Use Cases**: Share interesting applications

### Contribution Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-technique`)
3. Make your changes with clear commit messages
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

### Guidelines

- Follow existing code style and structure
- Include docstrings for new functions
- Add usage examples for new techniques
- Update README if adding major features

---

## Troubleshooting

### API Rate Limits

**Problem:** `429 RESOURCE_EXHAUSTED` error

**Solutions:**
- Switch to `gemini-2.5-flash` (better free tier)
- Add delay between requests
- Upgrade to paid API tier

### Module Import Errors

**Problem:** `ImportError: cannot import name 'X'`

**Solutions:**
- Ensure all files are in the same directory
- Check that `prompt_techniques.py` exists
- Verify virtual environment is activated

### API Key Issues

**Problem:** Authentication failures

**Solutions:**
- Verify `.env` file exists in project root
- Check API key format (no quotes in `.env`)
- Ensure key has necessary permissions
- Test key with simple API call

---

## Roadmap

### Planned Features

- [ ] Evaluation metrics for comparing techniques
- [ ] Prompt version control and A/B testing
- [ ] Multi-modal prompting examples (text + images)
- [ ] RAG (Retrieval-Augmented Generation) integration
- [ ] Cost tracking per technique
- [ ] GUI interface for non-technical users
- [ ] Prompt templates library
- [ ] Automated prompt optimization

### Research Areas

- Investigating newest prompting techniques from academic papers
- Testing technique effectiveness across different model sizes
- Building benchmark datasets for comparison
- Exploring prompt injection security implications

---

## Citation

If you use this project in your research or work, please cite:

```bibtex
@software{prompt_engineering_lab,
  author = {Chaymae Moudnib},
  title = {Prompt Engineering Lab: Interactive Learning Environment for LLM Prompting},
  year = {2025-2026},
  url = {https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent}
}
```


## Acknowledgments

- Research papers that formed the foundation of these techniques
- Google Gemini team for API access
- Open source community for inspiration and tools
- Future Contributors who will improve this project and add their touches

---

## Contact

- **GitHub Issues**: @chaymaemoudnib
- **Discussions**: @chaymaemoudnib
- **Email**: chaymaemoudnibe@gmail.com (for direct inquiries)

---

**Built with the goal of making prompt engineering accessible, practical, and immediately useful for real-world applications.**