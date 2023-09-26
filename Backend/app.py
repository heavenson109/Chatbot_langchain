import os
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain

llm = OpenAI(openai_api_key="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")
# memory = ConversationBufferMemory()

# conversation = ConversationChain(
#    llm=llm,
#    memory=memory
# )

# print(conversation.predict(input="Hello, my name is Andrea"))
# print(conversation.predict(input="What is 1+1?"))
# print(conversation.predict(input="What is my name?"))

memory = ConversationSummaryBufferMemory(llm=llm, max_token_limit=100)
schedule = "There is a meeting at 8am with your product team. \
            You will need your powerpoint presentation prepared. \
            9am-12pm have time to work on your LangChain \
            project which will go quickly because Langchain is such a powerful tool. \
            At Noon, lunch at the italian resturant with a customer who is driving \
            from over an hour away to meet you to understand the latest in AI. \
            Be sure to bring your laptop to show the latest LLM demo."

memory.save_context({"input": "Hello"}, {"output": "What's up"})
memory.save_context({"input": "Not much, just hanging"}, {"output": "Cool"})
memory.save_context({"input": "What is on the schedule today?"}, {"output": f"{schedule}"})

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=true
)

print(conversation.predict(input="what would be a good time for a coffee break?"))



 