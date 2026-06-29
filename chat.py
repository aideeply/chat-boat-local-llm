from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained('zoltanctoth/orca_mini_3B-GGUF', model_file="orca-mini-3b.q4_0.gguf")

prompt = "the name of the capital of india is"
# print(prompt + llm(prompt))
# for word in llm(prompt, stream=True):
# print(word, end="", flush=True)

def get_prompt(instruction: str) -> str:
	system = "You are an AI assistant that gives helpful answers. You answer in a concise and clear manner. If you don't know the answer, just say that you don't know. Do not try to make up an answer."
	prompt = f"### System:\n{system}\n\n### User:\n{instruction}\n\n### Response:\n"
	print(prompt)
	return prompt

questions = "Which city is the capital of India?"
for word in llm(get_prompt(questions), stream=True):
	print(word, end="", flush=True)

questions = "And which is at the united states?"
for word in llm(get_prompt(questions), stream=True):
	print(word, end="", flush=True)

















