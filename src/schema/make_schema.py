# -*- coding: utf-8 -*-
import os
import click
import logging
import json
import io
import csv
from dotenv import find_dotenv, load_dotenv

from tableschema import infer


SCHEMA_LOCATION = 'schema/schema.json'


@click.command()
@click.argument('input_filepath', type=click.Path(exists=True))
def main(input_filepath):
    """ Loads the data from input_filepath and infers the data schema,
        finally saving a JSON table schema representing your data.
        (recommended to run this file with a sliced dataset of max 100 lines)
    """
    logger = logging.getLogger(__name__)
    logger.info('making data schema for workbench')
    logger.info('(recommended to run this file with a sliced dataset of max 100 lines)')

    with io.open(input_filepath) as stream:
        headers = stream.readline().rstrip('\n').split(',')
        valid_headers = True
        for header in headers:
            if not header.islower():
                logger.error("ensure that all header names are lowercase: %s", header)
                valid_headers = False
        if valid_headers:
            values = csv.reader(stream)
            schema = infer(headers, values)
            schema_to_json(schema, logger)

def schema_to_json(schema, logger):
    logger.info('created table schema: {0}'.format(schema))
    table_schema_json = json.dumps(schema)
    output_file = os.path.join(project_dir, SCHEMA_LOCATION)
    with open(output_file, 'w') as out:
        out.write(table_schema_json)
        out.close()
    logger.info('written table schema to {0}'.format(SCHEMA_LOCATION))
    logger.info('you should now commit and push the schema/schema.json file')


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
