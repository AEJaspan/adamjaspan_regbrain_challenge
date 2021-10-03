from bs4 import BeautifulSoup
import re

def remove_tags(string):
    return BeautifulSoup(string, "lxml").text

def seperate_ontology(string):
    matches = re.findall(r'(?<=\|)([A-Z0-9-]+_)([^|]+)(?=\|)', f"|{string}|")
    ontologys = []
    for match in matches:
        ontologys.append(match[-1])
    return ontologys

def classification_label(mapping, classifications):
    return [mapping[clf] for clf in classifications]