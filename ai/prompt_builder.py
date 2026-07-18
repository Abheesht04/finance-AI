import json


class PromptBuilder:

    def build(self, context, question):

        prompt = ""

        prompt += "You are Clara Finance Worker.\n\n"

        prompt += "Invoice Context\n"

        prompt += "========================\n\n"

        prompt += json.dumps(

            context,

            indent=4

        )

        prompt += "\n\n"

        prompt += "Question:\n"

        prompt += question

        prompt += "\n"

        return prompt
