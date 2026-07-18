from ai.context_builder import ContextBuilder
from ai.prompt_builder import PromptBuilder


class FinanceAgent:

    def __init__(self):

        self._context = ContextBuilder()

        self._prompt = PromptBuilder()

    def answer(

        self,

        document,

        invoice,

        question

    ):

        context = self._context.build(

            document,

            invoice

        )

        prompt = self._prompt.build(

            context,

            question

        )

        #
        # LLM later
        #

        return prompt
