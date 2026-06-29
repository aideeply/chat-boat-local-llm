from email.mime import message

import chainlit as cl

from typing import List
from ctransformers import AutoModelForCausalLM


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
# prompt = "the name of the capital of india is"
# def get_prompt(instruction: str, history: List[str] = None) -> str:
# 	system = "You are an AI assistant that gives helpful answers. You answer in a concise and clear manner. If you don't know the answer, just say that you don't know. Do not try to make up an answer."
# 	prompt = f"### System:\n{system}\n\n### User:\n"
# 	if history is not None:
# 		prompt += f"This is the conversation history: {' '.join(history)}.\nNow answer the question: "
# 	prompt += f"{instruction}\n\n### Response:\n"
# 	print(prompt)
# 	return prompt

# history = []
# questions = "Which city is the capital of India?"
# answer = ""
# for word in llm(get_prompt(questions), stream=True):
# 	print(word, end="", flush=True)
# 	answer += word
# print()
	
# # Add history to the conversation
# # Implementing Memory
# history.append(answer)
# questions = "And which is at the united states?"
# for word in llm(get_prompt(questions, history), stream=True):
# 	print(word, end="", flush=True)
# print()
# ------------------------------------------------
# chainlit hello 
	
# prompt = "the name of the capital of india is"
def get_prompt(instruction: str, history: List[str] = None) -> str:
	system = "You are an AI assistant that gives helpful answers. You answer in a concise and clear manner. If you don't know the answer, just say that you don't know. Do not try to make up an answer."
	prompt = f"### System:\n{system}\n\n### User:\n"
	if len(history) > 0:
		prompt += f"This is the conversation history: {' '.join(history)}.\nNow answer the question: "
	prompt += f"{instruction}\n\n### Response:\n"
	print(prompt)
	return prompt

# @cl.on_message
# async def on_message(message: cl.Message):
#     response = f"Hello, you just sent: {message.content}!"
#     await cl.Message(response).send()

# @cl.on_message
# async def on_message(message: cl.Message):
# 	prompt = get_prompt(message.content)
# 	response = llm(prompt)
# 	await cl.Message(response).send()
	
@cl.on_message
async def on_message(message: cl.Message):
	message_history = cl.user_session.get("message_history")
	msg = cl.Message(content="")
	await msg.send()
	
	prompt = get_prompt(message.content, message_history)
	response = ""
	for word in llm(prompt, stream=True):
		await msg.stream_token(word)
		response += word
	await msg.update()
	message_history.append(response)

@cl.on_chat_start
def on_chat_start():
	cl.user_session.set("message_history", [])
	global llm
	llm = AutoModelForCausalLM.from_pretrained('zoltanctoth/orca_mini_3B-GGUF', model_file="orca-mini-3b.q4_0.gguf")

# history = []
# questions = "Which city is the capital of India?"
# answer = ""
# for word in llm(get_prompt(questions), stream=True):
# 	print(word, end="", flush=True)
# 	answer += word
# print()
	
# # Add history to the conversation
# # Implementing Memory
# history.append(answer)
# questions = "And which is at the united states?"
# for word in llm(get_prompt(questions, history), stream=True):
# 	print(word, end="", flush=True)
# print()
