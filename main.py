from agent import agent_reply, demonstrate_techniques

def print_menu():
    """Display available prompting techniques"""
    print("\n" + "="*60)
    print(" GEMINI PROMPT ENGINEERING AGENT")
    print("="*60)
    print("\nAvailable Commands:")
    print("  search [query]     - Search the web and get summary")
    print("  demo [query]       - Compare different prompt techniques")
    print("  help              - Show this menu")
    print("  exit              - Quit the agent")
    print("\nPrompting Techniques:")
    print("  /zero             - Direct instruction (default)")
    print("  /cot              - Chain-of-thought reasoning")
    print("  /few              - Few-shot with examples")
    print("  /role             - Role-based prompting")
    print("  /structured       - Structured output format")
    print("  /emotion          - Emotion/motivation prompt")
    print("\nUsage Examples:")
    print("  /cot What is 15% of 240?")
    print("  /role Write a poem as a Shakespeare expert")
    print("  demo What is photosynthesis?")
    print("="*60 + "\n")

def main():
    print_menu()
    
    current_technique = "zero_shot"
    
    while True:
        user_input = input('You: ').strip()
        
        if not user_input:
            continue
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        if user_input.lower() == 'help':
            print_menu()
            continue
        
        # Check for technique switches
        if user_input.startswith('/'):
            parts = user_input.split(maxsplit=1)
            technique_map = {
                '/zero': 'zero_shot',
                '/cot': 'chain_of_thought',
                '/few': 'few_shot',
                '/role': 'role_based',
                '/structured': 'structured',
                '/emotion': 'emotion'
            }
            
            technique_cmd = parts[0].lower()
            if technique_cmd in technique_map:
                current_technique = technique_map[technique_cmd]
                if len(parts) > 1:
                    # Process with technique
                    query = parts[1]
                    print(f"\n[Using {current_technique} technique]\n")
                    answer = agent_reply(query, technique=current_technique)
                    print(f'Agent: {answer}\n')
                else:
                    print(f"Switched to {current_technique} mode. Enter your query:")
            else:
                print(f" Unknown technique: {technique_cmd}")
            continue
        
        # Handle demo command
        if user_input.lower().startswith('demo '):
            query = user_input[5:].strip()
            demonstrate_techniques(query)
            continue
        
        # Regular query
        try:
            answer = agent_reply(user_input, technique=current_technique)
            print(f'\nAgent: {answer}\n')
        except Exception as e:
            print(f" Error: {e}\n")
            print("Tip: Wait a minute if you hit rate limits\n")

if __name__ == "__main__":
    main()