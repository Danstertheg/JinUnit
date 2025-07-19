from setuptools import setup, find_packages

setup(
    name="jinunit",
    version="0.1.0",
    description="Generate Java unit tests using OpenAI",
    author="Danny Silvestre Suarez",
    packages=find_packages(include=["jinunit", "jinunit.*"]),
    install_requires=[
        "typer[all]",
        "openai",
        "python-dotenv"
    ],
    entry_points={
        "console_scripts": [
            "jinunit = jinunit.cli:app"
        ],
    },
    python_requires=">=3.7",
)
