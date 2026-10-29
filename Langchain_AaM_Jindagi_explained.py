"""
Goal of this file: show WHY LangChain exists, before we learn Runnables.

Real flow of any LLM app:   inputs -> build prompt -> call LLM -> get answer
We fake each piece with a small class so you can see the idea without an API key.

PYTHON RULE #1: put every class at the LEFT margin (no indent). Only things
that BELONG to a class (its methods) are indented one level (4 spaces).
Your original file had classes nested inside classes -> that was the bug.
"""
import random


# ---------------------------------------------------------------------------
# PIECE 1: the fake LLM
# WHEN to write a class: when you need an object that holds some state
# and has several actions (methods).
# ---------------------------------------------------------------------------
class NakliLLM:
    def __init__(self):
        # __init__ runs automatically when you write NakliLLM().
        # Use it to set up the object.
        print("Nakli LLM initialized")

    def predict(self, prompt):
        # A real LLM would read `prompt`. Ours ignores it and picks a random answer.
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence",
        ]
        # Real LLM APIs return a dict-like object, so we return a dict too.
        return {"response": random.choice(response_list)}


# ---------------------------------------------------------------------------
# PIECE 2: the prompt template
# Problem it solves: the prompt text is the same, only a few words change.
# ---------------------------------------------------------------------------
class NakliPromptTemplate:
    def __init__(self, template, input_variables):
        # `self.x = x` means: "remember this value inside the object".
        # Without self., the value disappears when __init__ ends.
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        # str.format(**d) unpacks a dict into keyword arguments:
        #   "Write a {length} poem".format(**{"length": "short"})
        #   == "Write a {length} poem".format(length="short")
        return self.template.format(**input_dict)


# ---------------------------------------------------------------------------
# PIECE 3: the chain = glue between prompt and LLM
# Problem it solves: without it you must manually call format() then predict()
# every single time, in the right order.
# ---------------------------------------------------------------------------
class NakliLLMChain:
    def __init__(self, llm, prompt):
        # We store OTHER objects inside this object (this is called composition).
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):
        final_prompt = self.prompt.format(input_dict)   # step 1: fill the template
        result = self.llm.predict(final_prompt)          # step 2: call the LLM
        return result["response"]                        # step 3: pull out the text


# ---------------------------------------------------------------------------
# USING THEM. This part is plain script code: NO indentation, no class.
# `if __name__ == "__main__":` means "only run this when I run THIS file
# directly, not when another file imports it".
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    template = NakliPromptTemplate(
        template="Write a {length} poem about {topic}",
        input_variables=["length", "topic"],
    )
    llm = NakliLLM()

    # --- Way 1: WITHOUT a chain (manual, you do every step) ---
    prompt = template.format({"length": "short", "topic": "india"})
    print("Manual :", llm.predict(prompt)["response"])

    # --- Way 2: WITH a chain (one call does everything) ---
    chain = NakliLLMChain(llm, template)
    print("Chain  :", chain.run({"length": "short", "topic": "india"}))
