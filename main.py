import argparse
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain


class CodeGenerator:
    def __init__(self, language, task):
        self.language = language
        self.task = task
        self.llm = OpenAI()
        self.code_chain = self._create_code_chain()
        self.test_chain = self._create_test_chain()

    def _create_code_chain(self):
        code_prompt = PromptTemplate(
            template="Write a very short {} function that will {}".format(
                self.language, self.task
            ),
            input_variables=["language", "task"],
        )
        return LLMChain(llm=self.llm, prompt=code_prompt, output_key="code")

    def _create_test_chain(self):
        test_prompt = PromptTemplate(
            template="Write a test code for the following {} code:\n{{code}}".format(
                self.language
            ),
            input_variables=["language", "code"],
        )
        return LLMChain(llm=self.llm, prompt=test_prompt, output_key="test")

    def generate_code_and_test(self):
        chain = SequentialChain(
            chains=[self.code_chain, self.test_chain],
            input_variables=["language", "task"],
            output_variables=["code", "test"],
        )
        return chain({"language": self.language, "task": self.task})


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", default="return a list of numbers")
    parser.add_argument("--language", default="python")
    args = parser.parse_args()

    load_dotenv()

    code_generator = CodeGenerator(language=args.language, task=args.task)
    result = code_generator.generate_code_and_test()

    print("Generated Code:")
    print(result["code"])
    print("Generated Test:")
    print(result["test"])


if __name__ == "__main__":
    main()
