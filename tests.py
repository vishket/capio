#!/usr/bin/env python

import os
import sys
import unittest

# Local import
from word_exporter.exporter import Exporter

try:
    apiKey = os.environ['apiKey']
except KeyError as e:
    print "[Error] API Key not configured.\nexport apiKey=xxxxx"
    sys.exit(1)


class TestExporter(unittest.TestCase):
    """
    Tests for Word exporter
    """
    def test_get_transcriptions(self):
        """
        Test if transaction ID exists and returns all speech transcripts
        Expect transcripts to be not None
        """
        obj = Exporter(apiKey)
        transcript_id = '593f237fbcae700012ba8fcd'
        transcripts = obj.get_transcriptions(transcript_id)
        assert transcripts is not None

    def test_get_transcriptions_invalid(self):
        """
        Test for invalid transcription ID.
        Expect None object to be returned
        """
        obj = Exporter(apiKey)
        transcript_id = '123'
        transcripts = obj.get_transcriptions(transcript_id)
        assert transcripts is None

    def test_parse_data(self):
        """
        Test for parsing all transcriptions and returning a collection of timestamp, transcripts
        Expect list with timestamp, transcript separated by tab
        """
        json_data = [{'result':[{'alternative':[{"confidince":1, "transcript": "um", "words": [{"from": 0.678}]}]}], "result_index":0}]
        obj = Exporter(apiKey)
        parsed_data = obj.parse_data(json_data)
        assert parsed_data[0].rsplit('\t')[0] == '0.678' and parsed_data[0].rsplit('\t')[1] == 'um'

    def test_parse_data_invalid(self):
        """
        Test to parse a json data with missing keys
        Expect None object to be returned
        """
        json_data = [{'result': [{'alternative': [{"confidince": 1, "words": [{"from": 0.678}]}]}],
                      "result_index": 0}]
        obj = Exporter(apiKey)
        parsed_data = obj.parse_data(json_data)
        assert parsed_data is None
