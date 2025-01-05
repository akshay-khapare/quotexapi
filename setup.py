[tool.poetry]
name = "quotexapi"
version = "1.40.7"
description = "📈 QuotexPy is a library to easily interact with qxbroker."
authors = [
    'akshay-khapare'
]

repository = "https://github.com/akshay-khapare/quotexapi"
readme = ["README.md"]
keywords = ["quotex", "quotexapi"]
license = "LGPL-2.1"
packages = [
  {include = "quotexapi"}
]

[tool.poetry.dependencies]
python = ">=3.8, <3.13"
beautifulsoup4 = "4.11.2"
certifi = ">=2022.12.7"
greenlet = ">=2.0.1"
undetected-chromedriver = ">=3.5.5"
pyOpenSSL = ">=23.1.1"
pytz = ">=2023.3"
requests = ">=2.31.0"
requests-toolbelt = ">=1.0.0"
urllib3 = ">=2.0.5"
websocket-client = ">=1.6.3"
websockets = ">=11.0.3"
psutil = ">=5.9.8"
setuptools = ">=70.0.0"

[tool.poetry.dev-dependencies]
black = "^23.9.1"
poetry = "^1.6.1"
poetry2setup = "^1.1.0"
pylint = "^2.17.5"
pytest = "^7.4.2"
schedule = ">=1.2.1"
shutup = "0.2.0"
termcolor = "^2.3.0"

[tool.black]
line-length = 120
target-version = ['py310', 'py311', 'py312']
exclude = '''
(
  /(
    \.eggs           # exclude a few common directories in the
    | \.git          # root of the project
    | \.hg
    | \.mypy_cache
    | \.tox
    | \.venv
    | _build
    | buck-out
    | build
    | dist
  )/
  | foo.py           # also separately exclude a file named foo.py in
                     # the root of the project
)
'''


[build-system]
requires = ["poetry-core"]
python_requires = ">=3.10"
build-backend = "poetry.core.masonry.api"