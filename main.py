import time
import requests


def main(event, context):
    """Background Cloud Function to be triggered by Cloud Storage.
       This generic function logs relevant data when a file is changed.

    Args:
        event (dict):  The dictionary with data specific to this type of event.
                       The `data` field contains a description of the event in
                       the Cloud Storage `object` format described here:
                       https://cloud.google.com/storage/docs/json_api/v1/objects#resource
        context (google.cloud.functions.Context): Metadata of triggering event.
    Returns:
        None; the output is written to Stackdriver Logging
    """
    url = "https://github-mjpcollins-bullrisk-model-nmgxkhvw5a-nw.a.run.app/model"
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(event['bucket']))
    print('File: {}'.format(event['name']))
    print('Metageneration: {}'.format(event['metageneration']))
    print('Created: {}'.format(event['timeCreated']))
    print('Updated: {}'.format(event['updated']))
    print('Waiting 10 seconds to ensure file has finished uploading...')
    time.sleep(5)
    print('5')
    time.sleep(4)
    print('4')
    time.sleep(3)
    print('3')
    time.sleep(2)
    print('2')
    time.sleep(1)
    print('1')
    requests.post(url=url,
                  data=event)
    print(f'Posted event {event} to {url}')

