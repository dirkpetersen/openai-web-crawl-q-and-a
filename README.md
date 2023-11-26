# Web  Q&A with Embeddings

Learn how to crawl your website and build a Q/A bot with the OpenAI API. You can find the full tutorial in the [OpenAI documentation](https://platform.openai.com/docs/tutorials/web-qa-embeddings).


# Modified example of a local chatbot called `docbot`

In this modified example we are going to put settings and API keys into envionment variables. We want to  read content from a legacy Jira website with an older https config. We require some workarounds.

First make sure that your openai api key is set yo envionment var OPENAI_API_KEY:

```
echo "export OPENAI_API_KEY=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" >> ~/.openairc
```

Then set the website you want to crawl in `docbotrc` along with some other configs:

```
export DOC_URL=https://wiki.yourdomain.edu/display/MYWIKI
export DOC_DOMAIN=wiki.yourdomain.edu
export OPENSSL_CONF=./openssl.cnf
source ~/.openairc
```

and source `docbotrc` 

```
source ./docbotrc
```

