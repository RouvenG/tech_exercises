# Imports the Cloud Logging client library
import logging
import google.cloud.logging
from google.cloud.logging_v2.handlers import CloudLoggingHandler
from google.cloud.logging.resource import Resource

res = Resource(
    type="generic_node",
    labels={
        "location": "us-central1-a",
        "namespace": "default",
        "node_id": "10.10.10.1",
    },
)

client = google.cloud.logging.Client()
handler = CloudLoggingHandler(client)

cloud_logger = logging.getLogger('cloudLoggers')
cloud_logger.setLevel(logging.INFO)
cloud_logger.addHandler(handler)

cloud_logger.error('bad news')  # API call