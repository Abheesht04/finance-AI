from ai.context_builder import ContextBuilder
from ai.prompt_builder import PromptBuilder


class FinanceEngine:

    def __init__(self):

        self._context_builder = ContextBuilder()

        self._prompt_builder = PromptBuilder()

    # -------------------------------------------------

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

        #
        # LLM later
        #

        return prompt
