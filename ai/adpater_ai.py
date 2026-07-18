from ollama import chat

from ai.context_builder import ContextBuilder
from ai.prompt_builder import PromptBuilder


# ==========================================================
# OLLAMA ADAPTER
# ==========================================================

class OllamaAdapter:

    def __init__(self, model="qwen3:8b"):

        self._model = model

    def ask(self, prompt):

        response = chat(

            model=self._model,

            messages=[

                {

                    "role": "user",

                    "content": prompt

                }

            ]

        )

        return response["message"]["content"]


# ==========================================================
# AI ENGINE
# ==========================================================

class FinanceEngineAI:

    def __init__(self):

        self._context_builder = ContextBuilder()

        self._prompt_builder = PromptBuilder()

        self._llm = OllamaAdapter()

    # ------------------------------------------------------

    def answer(

        self,

        document,

        invoice,

        question

    ):

        context = self._context_builder.build(

            document,

            invoice

        )

        prompt = self._prompt_builder.build(

            context,

            question

        )

        return self._llm.ask(prompt)


# ==========================================================
# CONSOLE
# ==========================================================

class ClaraConsole:

    def run(self, worker):

        print()
        print("=" * 60)
        print("                 CLARA AI")
        print("=" * 60)
        print("Type 'exit' to quit.")
        print()

        while True:

            question = input("You : ")

            if question.lower() == "exit":

                break

            try:

                answer = worker.ask(question)

                print()

                print("Clara:")

                print(answer)

                print()

            except Exception as e:

                print()

                print("AI Error:")

                print(e)

                print()


