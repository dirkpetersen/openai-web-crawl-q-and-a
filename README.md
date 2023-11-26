# Web  Q&A with Embeddings

Learn how to crawl your website and build a Q/A bot with the OpenAI API. You can find the full tutorial in the [OpenAI documentation](https://platform.openai.com/docs/tutorials/web-qa-embeddings).


## Modified example of a local chatbot called `docbot`

In this modified example we are going to put settings and API keys into envionment variables. We want to  read content from a legacy Jira website with an older https config. This requires some workarounds.

First make sure that your openai api key is set to envionment var OPENAI_API_KEY:

```
echo "export OPENAI_API_KEY=sk-P1Fua1pF5xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" >> ~/.openairc
```

Install the requirements into a virtual environment 

```
python3 -m venv ~/.local/share/docbot
source ~/.local/share/docbot/bin/activate
pip3 install -r requirements.txt

```

Then edit config file `docbotrc` and set DOC_URL_ROOT and optionaly some suffixes where the script is forced to look

```
export DOC_URL_ROOT=https://wiki.yourdomain.edu/display/MYWIKI
export DOC_URL_SUFFIXES=HOWTO,General,Globus
export DOC_DOMAIN=wiki.yourdomain.edu
export OPENSSL_CONF=./openssl.cnf
source ~/.openairc
source ~/.local/share/docbot/bin/activate
```

and source `docbotrc` 

```
source ./docbotrc
```

run `web-qa.py` to crawl the website and ingest your custom data into ChatGPT once and then start `bot.py` for Q+A



