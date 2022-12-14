import argparse


def publish_messages(project_number, cloud_region, zone_id, topic_id, regional):
    # [START pubsublite_quickstart_publisher]
    from google.cloud.pubsublite.cloudpubsub import PublisherClient
    from google.cloud.pubsublite.types import (
        CloudRegion,
        CloudZone,
        MessageMetadata,
        TopicPath,
    )

    # TODO(developer):
    project_number = 322051923317
    cloud_region = "us-central1"
    # zone_id = "a"
    topic_id = "ratings"
    regional = True

    if regional:
        location = CloudRegion(cloud_region)
    else:
        location = CloudZone(CloudRegion(cloud_region), zone_id)

    topic_path = TopicPath(project_number, location, topic_id)

    # PublisherClient() must be used in a `with` block or have __enter__() called before use.
    with PublisherClient() as publisher_client:
        data = "Hello world!"
        api_future = publisher_client.publish(topic_path, data.encode("utf-8"))
        # result() blocks. To resolve API futures asynchronously, use add_done_callback().
        message_id = api_future.result()
        message_metadata = MessageMetadata.decode(message_id)
        print(
            f"Published a message to {topic_path} with partition {message_metadata.partition.value} and offset {message_metadata.cursor.offset}."
        )
    # [END pubsublite_quickstart_publisher]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_number", help="Your Google Cloud Project Number")
    parser.add_argument("cloud_region", help="Your Cloud Region, e.g. 'us-central1'")
    parser.add_argument("zone_id", help="Your Zone ID, e.g. 'a'")
    parser.add_argument("topic_id", help="Your topic ID")
    parser.add_argument("regional", help="True if using a regional resource else zonal")

    args = parser.parse_args()

    publish_messages(
        args.project_number,
        args.cloud_region,
        args.zone_id,
        args.topic_id,
        args.regional,
    )