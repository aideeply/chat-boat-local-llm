from typing import List
from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained('zoltanctoth/orca_mini_3B-GGUF', model_file="orca-mini-3b.q4_0.gguf")

# prompt = "the name of the capital of india is"
# print(prompt + llm(prompt))
# for word in llm(prompt, stream=True):
# print(word, end="", flush=True)
# -----------------------------------------------
# prompt = "the name of the capital of india is"
# def get_prompt(instruction: str) -> str:
# 	system = "You are an AI assistant that gives helpful answers. You answer in a concise and clear manner. If you don't know the answer, just say that you don't know. Do not try to make up an answer."
# 	prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Response:\n"
# 	print(prompt)
# 	return prompt

# questions = "Which city is the capital of India?"
# for word in llm(get_prompt(questions), stream=True):
# 	print(word, end="", flush=True)

# questions = "And which is at the united states?"
# for word in llm(get_prompt(questions), stream=True):
# 	print(word, end="", flush=True)
# ------------------------------------------------
prompt = "the name of the capital of india is"
def get_prompt(instruction: str, history: List[str] = None) -> str:
	system = "You are an AI assistant that gives helpful answers. You answer in a concise and clear manner. If you don't know the answer, just say that you don't know. Do not try to make up an answer."
	prompt = f"### System:\n{system}\n\n### User:\n"
	if history is not None:
		prompt += f"This is the conversation history: {' '.join(history)}.\nNow answer the question: "
	prompt += f"{instruction}\n\n### Response:\n"
	print(prompt)
	return prompt

history = []
questions = "Which city is the capital of India?"
answer = ""
for word in llm(get_prompt(questions), stream=True):
	print(word, end="", flush=True)
	answer += word
print()
	
# Add history to the conversation
# Implementing Memory
history.append(answer)
questions = "And which is at the united states?"
for word in llm(get_prompt(questions, history), stream=True):
	print(word, end="", flush=True)
print()
