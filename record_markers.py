"""
Test script to see if the markers sent by the MST script are OK.
"""

from pylsl import StreamInlet, resolve_byprop


LSL_SCAN_TIMEOUT = 10


print('Looking for a Markers stream...')
marker_streams = resolve_byprop(
    'name', 'Markers', timeout=LSL_SCAN_TIMEOUT)
inlet_marker = StreamInlet(marker_streams[0])
markers = list()


while True:
    try:
        marker, timestamp = inlet_marker.pull_sample(timeout=0.0)
        if timestamp is not None:
            print(marker, timestamp)
            markers.append([marker, timestamp])
    except KeyboardInterrupt:
        print('Interrupting marker recording.')
        break

print(markers)
# XXX Save markers
