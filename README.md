# Word Exporter

This repo contains a CLI application that allows you to get a list of 
transcripts using the Capio API 
(https://api.capio.ai/v1/speech/transcript/<transcript_id>), filter
 out just the timestamp and transcripts and save them locally in a word 
  doc

## Repo Structure

The parent word_exporter consists of
 
 - requirements.txt : All packages required to execute this app
 
 - setup.py : To package the CLI app
 
 - tests.py : All unit tests
 
 - README.md: Instructions
 
 - word_exporter
 
The word_exporter sub directory consists of

 - cli.py : Package to provide command line interface using click
 
 - exporter.py : Package to provide the reusable exporter object and 
 its methods

## Getting started

1) Create virtual env

```
virtualenv capio

cd capio/

source bin/activate

```

 **In case you don't have,
 
```
pip install virtualenv
```

2) Download the project locally

```
git clone -b v1 git@github.com:vishket/word_exporter.git

```

3) Install

```
cd word_exporter/

pip install -r requirements.txt

pip intall .
```

4) Run

```
export apiKey=xxxxxx

WordExporter --transcription_id 593f237fbcae700012ba8fcd --output 
 output1.docx
 
WordExporter --help

```

## Tests

To exectue all unit tests

```
pytest tests.py
```

## Assumptions

I wasn't entirely sure on how to convert the timestamp from 
0.6899999976158142 to 00:00:00.69. Due to time constraints, I decided 
to use the default format that is returned by the API. 