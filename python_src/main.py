import json
import numpy as np
from biosppy import storage
from biosppy.signals import ecg


# load raw ECG signal
signal, mdata = storage.load_txt('python_src/Files/1 NSR/100m (3).txt')

rate = mdata['sampling_rate']

out = ecg.ecg(signal=signal, sampling_rate=rate, show=False)


class NDArrayEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


json_str = json.dumps({'test': out["templates"], "time" : out["ts"], "filtered" : out['filtered']}, cls=NDArrayEncoder)

print(json_str)

# f = 1/T
