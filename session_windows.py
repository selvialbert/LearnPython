import argparse
import time
import random
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions


class AddKeyInfoFn(beam.DoFn):
    """output tuple of window(key) + element(value)"""

    def process(self, element, window=beam.DoFn.WindowParam):
        yield (element['serverID'], element)


class PrintElements(beam.DoFn):
    """print each element and its window information"""

    def process(self, element, window=beam.DoFn.WindowParam):
        (serverID, elements) = element
        window_start = str(window.start).replace(" ", "_")
        window_end = str(window.end).replace(" ", "_")
        # window_start = str(window.start.to_utc_datetime()).replace(" ", "_")
        # window_end = str(window.end.to_utc_datetime()).replace(" ", "_")
        for row in elements:
            print(
                f"serverID - {serverID}, window - {window_start},{window_end}, timestamp -  {row['timestamp']}, CPU_Utilization - {row['CPU_Utilization']}")


def run(argv=None):
    # argument parser
    parser = argparse.ArgumentParser()

    known_args, pipeline_args = parser.parse_known_args(argv)

    pipeline_options = PipelineOptions(pipeline_args)
    setup_options = pipeline_options.view_as(SetupOptions)
    setup_options.save_main_session = True

    # randomly generate data
    # data = [{'serverID': 'server_{}'.format(i%3), 'CPU_Utilization': round(random.uniform(10.0, 99.0),2),'timestamp': time.time() + 2**i} for i in range(10)]
    data = [
        {'serverID': 'server_1', 'CPU_Utilization': 0, 'timestamp': 1},
        {'serverID': 'server_2', 'CPU_Utilization': 10, 'timestamp': 1},
        {'serverID': 'server_3', 'CPU_Utilization': 20, 'timestamp': 3},
        {'serverID': 'server_1', 'CPU_Utilization': 30, 'timestamp': 2},
        {'serverID': 'server_2', 'CPU_Utilization': 40, 'timestamp': 3},
        {'serverID': 'server_3', 'CPU_Utilization': 50, 'timestamp': 6},
        {'serverID': 'server_1', 'CPU_Utilization': 60, 'timestamp': 7},
        {'serverID': 'server_2', 'CPU_Utilization': 70, 'timestamp': 7},
        {'serverID': 'server_3', 'CPU_Utilization': 80, 'timestamp': 14},
        {'serverID': 'server_2', 'CPU_Utilization': 85, 'timestamp': 8.5},
        {'serverID': 'server_1', 'CPU_Utilization': 90, 'timestamp': 14}
    ]
    # print(data)
    p = beam.Pipeline(options=pipeline_options)

    events = p | 'Create Events' >> beam.Create(data) \
             | 'Add Timestamps' >> beam.Map(lambda x: beam.window.TimestampedValue(x, x['timestamp'])) \
             | 'keyed on serverID' >> beam.ParDo(AddKeyInfoFn()) \
             | 'Add Window info' >> beam.WindowInto(beam.window.Sessions(5)) \
             | 'Group by key' >> beam.GroupByKey() \
             | 'write session elements' >> beam.ParDo(PrintElements())

    result = p.run()
    result.wait_until_finish()


if __name__ == "__main__":
    run()
