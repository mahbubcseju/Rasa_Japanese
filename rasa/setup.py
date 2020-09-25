import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# Avoids IDE errors, but actual version is read from version.py
__version__ = None
with open("rasa/version.py") as f:
    exec (f.read())

# Get the long description from the README file
with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

tests_requires = [
    "pytest~=4.5",
    "pytest-cov~=2.7",
    "pytest-localserver~=0.5.0",
    "pytest-sanic~=1.0.0",
    "responses~=0.9.0",
    "freezegun~=0.3.0",
    "nbsphinx>=0.3",
    "aioresponses~=0.6.0",
    "moto~=1.3.8",
]

install_requires = [
    "requests~=2.22",
    "boto3~=1.9",
    "matplotlib~=3.0",
    "simplejson~=3.16",
    "attrs>=18",
    "jsonpickle~=1.1",
    "redis~=3.2",
    "fakeredis~=1.0",
    "pymongo~=3.8",
    "numpy~=1.16",
    "scipy~=1.2",
    "tensorflow>=1.13,<1.16",
    "apscheduler~=3.0",
    "tqdm~=4.0",
    "networkx~=2.3",
    "fbmessenger~=6.0",
    "pykwalify~=1.7.0",
    "coloredlogs~=10.0",
    "scikit-learn~=0.20.2",
    "ruamel.yaml~=0.15.0",
    "scikit-learn~=0.20.0",
    "slackclient~=1.3",
    "python-telegram-bot~=11.0",
    "twilio~=6.0",
    "webexteamssdk~=1.1",
    "mattermostwrapper~=2.0",
    "rocketchat_API~=0.6.0",
    "colorhash~=1.0",
    "pika~=1.0.0",
    "jsonschema~=2.6",
    "packaging~=19.0",
    "gevent~=1.4",
    "pytz~=2019.1",
    "python-dateutil~=2.8",
    "rasa-sdk~=1.1.0",
    "colorclass~=2.2",
    "terminaltables~=3.1",
    "sanic~=19.3.1",
    "sanic-cors~=0.9.0",
    "sanic-jwt~=1.3",
    "aiohttp~=3.5",
    "questionary>=1.1.0",
    "python-socketio~=4.0",
    "pydot~=1.4",
    "async_generator~=1.10",
    "SQLAlchemy~=1.3.0",
    "kafka-python~=1.4",
    "sklearn-crfsuite~=0.3.6",
]

extras_requires = {
    "test": tests_requires,
    "spacy": ["spacy>=2.1,<2.2"],
    "mitie": ["mitie"],
    "sql": ["psycopg2~=2.8.2", "SQLAlchemy~=1.3"],
}

setup(
    name="rasa",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        # supported python versions
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
    ],
    packages=find_packages(exclude=["tests", "tools", "docs", "contrib"]),
    entry_points={"console_scripts": ["rasa=rasa.__main__:main"]},
    version=__version__,
    install_requires=install_requires,
    tests_require=tests_requires,
    extras_require=extras_requires,
    include_package_data=True,
    description="Open source machine learning framework to automate text- and "
    "voice-based conversations: NLU, dialogue management, connect to "
    "Slack, Facebook, and more - Create chatbots and voice assistants",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Rasa Technologies GmbH",
    author_email="hi@rasa.com",
    maintainer="Tom Bocklisch",
    maintainer_email="tom@rasa.com",
    license="Apache 2.0",
    keywords="nlp machine-learning machine-learning-library bot bots "
    "botkit rasa conversational-agents conversational-ai chatbot"
    "chatbot-framework bot-framework",
    url="https://rasa.com",
    download_url="https://github.com/RasaHQ/rasa/archive/{}.tar.gz"
    "".format(__version__),
    project_urls={
        "Bug Reports": "https://github.com/rasahq/rasa/issues",
        "Source": "https://github.com/rasahq/rasa",
    },
)

print ("\nWelcome to Rasa!")
print (
    "If you have any questions, please visit our documentation page: https://rasa.com/docs/"
)
print ("or join the community discussions on https://forum.rasa.com/")
