# RegBrain data exploration

## Overview

This project presents a brief dive into a sample of the regulatory data that RegInsight has collected on behalf of a major international bank. The content reflects a range of data sources from official publications, to blog posts and televised speeches from official sources, that may provide the client key insights into the ever changing world of financial regulation, offering them the chance to gain an edge, by being able to better prepare for  the future.

RegInsight also provides it's proprietary Ontological classifications of said insights, offering their clients a powerful way to quickly assess this vast data source.

### Status

This project is broken into two components

* Data exploration
* Word vectorisation

In the first step, the data was simply loaded, cleaned, and prepared for future study. From this deeper look into the data, along with the useful column descriptions provided [here](https://bramble-stamp-15b.notion.site/21ceea6f40c04a70ae6a9b00f271556b?v=4755fb38cd7d415ab1aa63d518a9ee24), it's possible to get a feel for the data. It is important to develop a sense of which governing bodies are considered, and to get a feel for the type of statements that they might make. It's also useful to study the Ontological classifications that are made to learn about the insights that are already provided by the powerful RegOntology tool.

Armed with a good sense for the nature of RegInsight's data content, we can begin to perform analysis over said content to try and further enrich this unique data source.

Unfortunately, due to the limited time frame that is available for this introductory study, the analytics of this data is quite limited. In this study, the corpus of documents gathered is vectorised using the `Word2Vec` algorithm to learn the linguistic relations present within these regulations.

`Word2Vec` uses a neural network to embed a corpus of documents into word vectors. From this, it is possible to find both highly correlated and highly anti-correlated words, as well as the euclidean distance between different word vectors. This information can provide us key insights into the thinking of regulatory bodies.

## Findings

Through doing this, I have learnt some interesting relations such as

* the word 'money' being frequently used in the context of 'misappropriation'
* the word 'money' having a higher simalarity score to the word 'deposit' (0.241) than 'withdrawal' (0.094)

These insights tell us that regulators concern themselves more highly with regulation over the depositing of funds, than the withdrawal of funds, and that the misappropriation of funds is of a key concern to regulaotors, with this being of a higher importance than words such as 'finance' or 'professionals'.

As each jurisdiction will approach regulation from their own direction, it is perhaps a more intelligent to assess specific to a certain geography, instead of aggregating these over the entire data set. For instance, by considering only the jurisdiction's within North America (these being the United States of America, Canada and the US State of New York).

By decomposing the data in this way, we find that in North America;

* 'missapropriation' is less strongly related to 'money', being beaten by concepts such as 'payments' and 'hedge'
* the similarity of 'money' to deposit is (0.185) and to 'withdrawal' is (0.105)

This information can tell us that missapropriation is currently considered a higher priority globally than it is in North America, which is perhaps a reflection on the regions strong existing anti-corruption frameworks. And additionally that the withdrawal of funds is of greater significance in NA, which perhaps demonstrates the strong consumer protections in the region.

## Future plans

Given more time, it would be exciting to discover what insights could be gained from applying machine learning techniques to this data. One way of doing so would be to label the available data into different semantic classifications, and then fit this data using a machine learning model, allowing us to make classifications on future inputs. This approach is obviously unfeasible within the time frame of this study.

Alternatively, one could use the Ontological classifications provided by RegOntology to learn which regulator is most likely to be make which Ontological classifications and which groups of classifications, out of the  273 unique labels available in the data set. Other interesting features that could be used along side the RegInsite classifications would be a simple BOW analysis of the text within each category. This study may help the end users understand the focus of each regulating body, and help them track their shifting priorities over time. Similarly the same analysis could be performed to learn the changing focus within different geographical regions. For this reason, it would be important to re-use, re-train and re-optimise any such machine learning models to provide these insights over a range of different sub-categories, and to continuously keep updating these models via RegInsights near real-time classifications.

# HOW TO RUN

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
