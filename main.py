from agent import agent_reply

print('Gemini agent is ready! type "exit" to quit.\n')


while True:
    user = input('You:')
    if user.lower() == 'exit':
        break
    answer = agent_reply(user)
    print('Agent:', answer, "\n")