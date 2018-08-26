"""
Package to provide CLI interface to the word exporter application
"""

import os
import sys
from exporter import Exporter

import click

# source apikey from environment variable. If unset, raise exception and alert user
try:
    apiKey = os.environ['apiKey']
except KeyError as e:
    print "[Error] API Key not configured.\nexport apiKey=xxxxx"
    sys.exit(1)


@click.command()
@click.option('--transcription_id', default=None, help='The transcription ID')
@click.option('--output', default='sample_output.docx', help='Name of output docx file')
def run(transcription_id, output):
    if transcription_id is None:
        click.echo("Transcription ID required")
    else:
        obj = Exporter(apiKey)
        transcripts = obj.get_transcriptions(transcription_id)
        if transcripts is None:
            sys.exit(1)
        parsed_data = obj.parse_data(transcripts)
        obj.save_to_file(parsed_data, output)

if __name__ == '__main__':
    run()