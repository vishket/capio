"""
Package that returns an exporter object and its associated methods
"""

import requests
from datetime import datetime

import docx

base_url = "https://api.capio.ai/v1/speech/transcript/"


class Exporter(object):
    def __init__(self, apiKey):
        self.apiKey = apiKey

    def get_transcriptions(self, transcript_id):
        """
        Function to return list of all transcripts for provided transcription ID
        :param str transcript_id: The transcription ID
        :return: list resp: JSON collection of transcriptions
        """
        url = base_url + transcript_id
        try:
            resp = requests.get(url, data={'apiKey': self.apiKey})
            if resp.status_code != 200:
                print "[Error] Unable to find object with provided transcription ID\n." \
                      "Request failed with HTTP error code: {}".format(resp.status_code)
                return None
            else:
                return resp.json()
        except requests.exceptions.RequestException as e:
            print "[Error] Request failed with error: {}".format(e)
            return None

    def parse_data(self, json_data):
        """
        Function to parse all data and return only timestamp, transcript
        :param list raw_data: Collection of all transcriptions
        :return: list parsed_data: Collection of timestamps and transcript for all records
        """
        parsed_data = []
        for x in json_data:
            try:
                parsed_data.append(str(x.get('result')[0].get('alternative')[0].get('words')[0].get('from'))
                       + '\t' + x.get('result')[0].get('alternative')[0].get('transcript'))
            except KeyError as e:
                print "[Error] Parsing data failed with error: {}".format(e)
                return None
            except IndexError as e:
                print "[Error] Parsing data failed with error: {}".format(e)
                return None
            except TypeError as e:
                print "[Error] Parsing data failed with error: {}".format(e)
                return None
        return parsed_data


    def format_timestamp(self, raw_timestamp):
        """
        24.26 --> 00:00:24.27
        0.6899999976158142 --> 00:00:00.69
        20.149999618530273 --> 00:00:20.15

        Convert from float to HH:MM:SS
        :param raw_timestamp:
        :return:
        """
        d = datetime.now()
        d.strftime("%H:%M:%S:%f").rsplit(':')[-1] = d.strftime("%H:%M:%S:%f").rsplit(':')[-1][:2]


    def save_to_file(self, data, filename):
        """
        Function to save data to a file in the docx format
        :param list data: List consisting of each timestamp, transcript record
        :param str filename: The name of file to save to
        """
        doc = docx.Document()
        for each in data:
            doc.add_paragraph(each)
        doc.save(filename)
