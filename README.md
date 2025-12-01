<div align="center">

# Prompt Engineering Lab

### *Master the Art of Talking to AI*

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gemini API](https://img.shields.io/badge/Powered%20by-Gemini%20API-4285F4?logo=google)](https://ai.google.dev/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

**An interactive learning environment for understanding and practicing prompt engineering techniques with Large Language Models.**

[Getting Started](#-quick-start) • [Techniques](#-prompting-techniques) • [Examples](#-usage-examples) • [Resources](#-learning-resources)

</div>

---

##  What is This?

Ever wondered why some people get amazing results from ChatGPT while others struggle? It's all about **how you ask**.

This project is your hands-on playground for mastering **10 research-backed prompt engineering techniques** that professionals use to build production AI systems. No fluff, just practical learning.

```bash
You: /cot What is 15% of 240?
Agent: Let me break this down step-by-step...
       1. Convert percentage to decimal: 15% = 0.15
       2. Multiply: 240 × 0.15 = 36
       3. Answer: 36
```

###  Why This Matters

- **For Data Scientists**: Build better AI applications
- **For ML Engineers**: Understand LLM behavior deeply  
- **For Students**: Learn by doing, not just reading
- **For Everyone**: Get 10x better results from AI tools

---

##  Key Features

<table>
<tr>
<td width="50%">

### 🔬 **10 Proven Techniques**
Research-backed strategies from papers published by Google, OpenAI, and leading AI labs.

</td>
<td width="50%">

###  **Interactive Testing**
Switch techniques with `/cot`, `/few`, `/role` and see instant differences in outputs.

</td>
</tr>
<tr>
<td width="50%">

###  **Side-by-Side Comparison**
Use `demo` to run identical queries through multiple techniques simultaneously.

</td>
<td width="50%">

### 🌐 **Web Search Integration**
Test prompting on real-time information retrieval tasks.

</td>
</tr>
</table>

---

##  Quick Start

### Prerequisites

```bash
# You'll need:
✓ Python 3.8+
✓ Google Gemini API key (free tier available)
✓ Serper API key for web search (optional)
```

### Installation

```bash
# 1. Clone the repo
git clone https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent
cd Prompt_Engineering_Agent

# 2. Set up environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your API keys to .env
echo "Gemini_api_key=your_key_here" > .env
echo "Serper_api_key=your_serper_key" >> .env
```

### First Run

```bash
python main.py
```

```
🤖 GEMINI PROMPT ENGINEERING AGENT
═══════════════════════════════════════════════════════════

Available Commands:
  /cot    - Chain-of-thought reasoning
  /few    - Few-shot with examples
  /role   - Role-based prompting
  demo    - Compare techniques side-by-side
  
You: /cot What is 25% of 80?
```

---

## 🎓 Prompting Techniques

<details>
<summary><b>1- Zero-Shot Prompting</b> - Direct instructions, no examples needed</summary>

<br>

**When to use:** Simple, well-understood tasks

```
Translate "Hello" to Spanish.
```

**Why it works:** Pre-trained models can handle many tasks without examples due to their vast training data.

**Command:** Just type naturally

</details>

<details>
<summary><b>2- Few-Shot Prompting</b> - Learn from 2-5 examples</summary>

<br>

**When to use:** Tasks requiring specific format or pattern

```
Convert adjectives to adverbs:
- Quick → Quickly
- Careful → Carefully

Now convert: Happy → ?
```

**Research:** GPT-3 paper (Brown et al., 2020) showed dramatic improvements with just a few examples.

**Command:** `/few [your query]`

</details>

<details>
<summary><b>3- Chain-of-Thought (CoT)</b> - Step-by-step reasoning</summary>

<br>

**When to use:** Math, logic puzzles, complex reasoning

```
Problem: Store has 50 apples, sells 60%. How many remain?

Step-by-step:
1. Calculate 60% of 50: 0.60 × 50 = 30 apples sold
2. Subtract from original: 50 - 30 = 20 apples
3. Answer: 20 apples remain
```

**Research:** Wei et al. (2022) demonstrated 3x accuracy improvement on reasoning tasks.

**Command:** `/cot [your query]`

</details>

<details>
<summary><b>4- Role-Based Prompting</b> - Assign expertise to the model</summary>

<br>

**When to use:** Domain-specific tasks, specialized explanations

```
You are an experienced software architect.
Explain microservices to a junior developer.
```

**Why it works:** Activates specific training data patterns matching the assigned role.

**Command:** `/role [your query]`

</details>

<details>
<summary><b>5- Structured Output</b> - Request specific formats</summary>

<br>

**When to use:** Data extraction, API integration, consistent formatting

```
List 3 benefits of exercise as JSON:
{
  "benefits": [
    {"name": "...", "description": "..."},
    ...
  ]
}
```

**Production value:** Essential for programmatic use of LLM outputs.

**Command:** `/structured [your query]`

</details>

<details>
<summary><b>6- Self-Consistency</b> - Multiple reasoning paths</summary>

<br>

**When to use:** High-stakes decisions, uncertain problems

Generates 3-5 different solution approaches, then selects the most consistent answer.

**Research:** Wang et al. (2022) showed significant accuracy gains on complex reasoning.

</details>

<details>
<summary><b>7- Emotion Prompting</b> - Add stakes for better responses</summary>

<br>

**When to use:** Tasks requiring careful attention

```
This code review is critical for production.
Please analyze thoroughly for potential bugs.
```

**Research:** Recent studies show emotional context improves response quality.

**Command:** `/emotion [your query]`

</details>

<details>
<summary><b>8- Context Enrichment</b> - Provide background information</summary>

<br>

**When to use:** Domain-specific questions

```
Context: Python lists use zero-based indexing.
Question: What does my_list[0] return?
```

</details>

<details>
<summary><b>9- Meta Prompting</b> - Let AI design the prompt</summary>

<br>

**When to use:** Complex tasks with unclear optimal strategy

```
Design an optimal prompt for analyzing customer feedback
that considers context, tone, and intent.
```

</details>

<details>
<summary><b>10- Instruction Breakdown</b> - Clear steps + constraints</summary>

<br>

**When to use:** Multi-step processes

```
Task: Write a product description

Constraints:
- Max 100 words
- Include 3 features
- Target: developers

Steps:
1. Catchy opening
2. List features
3. Call-to-action
```

</details>

---

## 💻 Usage Examples

### Example 1: Compare Techniques

```bash
You: demo What is recursion in programming?
```

<details>
<summary>See Output</summary>

```
══════════════════════════════════════════════════════════
Testing Query: What is recursion in programming?
══════════════════════════════════════════════════════════

--- Using Zero-Shot Technique ---
Response: Recursion is when a function calls itself...

--- Using Chain of Thought Technique ---
Response: Let me explain step-by-step:
1. First, understand what a function is...
2. Now, imagine a function calling itself...
3. This creates a loop that continues until...

--- Using Role-Based Technique ---
Response: As a computer science professor, I'd explain recursion
as a fundamental programming concept where...

--- Using Emotion Prompt Technique ---
Response: [Careful, detailed explanation with examples]
```

</details>

### Example 2: Math with Chain-of-Thought

```bash
You: /cot If a car travels 60 mph for 2.5 hours, how far does it go?
```

### Example 3: Web Search with Structured Output

```bash
You: search quantum computing breakthroughs 2024
```
---

##  Learning Resources

### 📄 Research Papers

| Paper | Authors | Key Finding |
|-------|---------|-------------|
| [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) | Brown et al., 2020 | Introduced few-shot learning with GPT-3 |
| [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) | Wei et al., 2022 | Step-by-step reasoning improves accuracy |
| [Self-Consistency](https://arxiv.org/abs/2203.11171) | Wang et al., 2022 | Multiple paths increase reliability |

### 🎥 Free Courses

- **[ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/)** by Andrew Ng
- **[Anthropic's Prompt Engineering Guide](https://docs.anthropic.com/claude/docs/prompt-engineering)**
- **[OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)**

### 📚 Online Guides

- **[Prompting Guide](https://www.promptingguide.ai/)** - Comprehensive reference
- **[Learn Prompting](https://learnprompting.org/)** - Interactive tutorials
- **[LangChain Docs](https://python.langchain.com/docs/)** - Advanced patterns

---

## 🔧 Advanced Usage

### Adapt to Other LLMs

<details>
<summary><b>OpenAI GPT-4</b></summary>

```python
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def agent_reply(user_prompt, technique="zero_shot"):
    final_prompt = apply_technique(user_prompt, technique)
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": final_prompt}]
    )
    return response.choices[0].message.content
```

</details>

<details>
<summary><b>Anthropic Claude</b></summary>

```python
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def agent_reply(user_prompt, technique="zero_shot"):
    final_prompt = apply_technique(user_prompt, technique)
    
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": final_prompt}]
    )
    return response.content[0].text
```

</details>

### Build Your Own Technique

```python
# In prompt_techniques.py
@staticmethod
def your_custom_technique(task: str) -> str:
    """Your innovative prompting approach"""
    return f"""[Your creative prompt structure]
    
Task: {task}
..."""
```

---

## 📊 Best Practices

### Quick Reference Table

| Technique | Best For | Avoid When | Speed |
|-----------|----------|------------|-------|
| Zero-shot | Simple tasks | Complex reasoning | ⚡⚡⚡ |
| Few-shot | Format consistency | Limited examples | ⚡⚡ |
| Chain-of-Thought | Math/Logic | Simple facts | ⚡ |
| Role-based | Domain expertise | Generic queries | ⚡⚡ |
| Structured | Data extraction | Creative tasks | ⚡⚡ |

### Golden Rules

1. **Be Specific** → Vague input = vague output
2. **Show, Don't Tell** → Examples beat explanations
3. **Test & Iterate** → First attempt rarely perfect
4. **Consider Context** → Background info matters
5. **Mind the Tokens** → Longer ≠ better

---

## 🤝 Contributing

We love contributions! Here's how you can help:

-  **Report bugs** via [Issues](https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent/issues)
-  **Suggest features** in [Discussions](https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent/discussions)
-  **Submit PRs** for improvements
-  **Share use cases** you've built
- ⭐ **Star the repo** if you find it useful!

---

## 🛠️ Troubleshooting

<details>
<summary><b> API Rate Limits (429 Error)</b></summary>

**Solutions:**
- Switch to `gemini-2.5-flash` (better free tier)
- Wait 60 seconds between requests
- Upgrade to paid tier

</details>

<details>
<summary><b> Import Errors</b></summary>

**Solutions:**
- Verify all files are in same directory
- Check `prompt_techniques.py` exists
- Ensure virtual environment is activated

</details>

<details>
<summary><b> API Key Issues</b></summary>

**Solutions:**
- Confirm `.env` file exists in root
- No quotes around keys in `.env`
- Test key with simple API call

</details>

---

## 🗺️ Roadmap

### Coming Soon
- [ ] Evaluation metrics for technique comparison
- [ ] Prompt A/B testing framework
- [ ] Multi-modal prompting (text + images)
- [ ] RAG integration examples
- [ ] Cost tracking per technique
- [ ] Web UI for non-technical users

### Research Areas
- Newest techniques from 2024-2025 papers
- Cross-model effectiveness comparison
- Prompt injection security testing

---

## 📬 Get in Touch

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-ChaymaeMoudnib-181717?logo=github)](https://github.com/ChaymaeMoudnib)
[![Email](https://img.shields.io/badge/Email-chaymaemoudnibe@gmail.com-D14836?logo=gmail&logoColor=white)](mailto:chaymaemoudnibe@gmail.com)

**Questions?** Open an [Issue](https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent/issues)  
**Discussions?** Start a [Discussion](https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent/discussions)

</div>

---

##  Citation

```bibtex
@software{prompt_engineering_lab,
  author = {Chaymae Moudnib},
  title = {Prompt Engineering Lab: Interactive Learning Environment for LLM Prompting},
  year = {2024},
  url = {https://github.com/ChaymaeMoudnib/Prompt_Engineering_Agent}
}
```

---

## 🙏 Acknowledgments

Built with insights from groundbreaking research by Google, OpenAI, Anthropic, and the broader AI community. Special thanks to future contributors who will help this project grow.

---

<div align="center">

### ⭐ Star this repo if it helped you master prompt engineering!

**Made with 💙 for the AI learning community**

</div>