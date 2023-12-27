# Generic Code Generation

This workspace contains the following files and directories:

- [`.gitignore`](".gitignore"): This file specifies patterns of files and directories that should be ignored by Git version control.
- [`LICENSE`]("LICENSE"): This file contains the MIT License, which is the license under which the software in this workspace is distributed.
- [`README.md`]("README.md"): This file is the README for the workspace itself, providing information and instructions.
- [`main.py`]("main.py"): This file contains the main Python script of the project.

## Project Description

The main purpose of this project is to generate code and test cases based on a given task and programming language. It utilizes the `langchain` library, which provides a set of classes and templates for generating code and tests using OpenAI's language models.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set up your environment by creating a [`.env`](".env") file and adding any necessary environment variables.
4. Run the [`main.py`]("main.py") script with the desired command-line arguments.

## Usage

The [`main.py`]("main.py") script accepts the following command-line arguments:

- `--task`: Specifies the task for which code and tests should be generated. Defaults to "return a list of numbers".
- `--language`: Specifies the programming language for which code and tests should be generated. Defaults to "python".

Example usage:

```shell
python main.py --task "calculate the factorial of a number" --language "java"
```

## Code Generation

The code generation process involves the following steps:

1. Loading environment variables from the [`.env`](".env") file.
2. Creating an instance of the `OpenAI` class from the `langchain.llms` module.
3. Defining prompt templates for generating code and tests using the `PromptTemplate` class from the `langchain.prompts` module.
4. Creating instances of the `LLMChain` class from the `langchain.chains` module for generating code and tests.
5. Creating a `SequentialChain` instance that chains the code and test generation steps together.
6. Running the chain with the specified task and language to generate the code and tests.
7. Printing the generated code and tests to the console.

## Contributing

Contributions to this project are welcome! If you find any issues or have any suggestions, please open an issue or submit a pull request.

## License

This project is licensed under the terms of the MIT License. See the [`LICENSE`]("LICENSE") file for more information.