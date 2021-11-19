import json

from numpy import size


class Building:


    def __init__(self, _minFloor, _maxFloor, _id, _speed, _closeTime, _openTime, _startTime, _stopTime,Pos = 0,onJob=0,coolDown = 0):
        self._id = _id
        self._speed = _speed
        self._minFloor = _minFloor
        self._maxFloor = _maxFloor
        self._closeTime = _closeTime
        self._openTime = _openTime
        self._startTime = _startTime
        self._stopTime = _stopTime
        self.Pos= Pos
        self.onJob = onJob
        self.coolDown = coolDown


    def __repr__(self):
        return f'<building{self._id}>'

    @classmethod
    def from_json(cls, json_path):
        with open(json_path) as f:
            json_dict = json.loads(f.read())
            return cls(**json_dict)

def time():
        cycle_time = Building._stopTime + Building._startTime + Building._openTime + Building._closeTime
        return cycle_time



json_path = 'Ex1_Buildings/B4.json'
elvator_list = []
with open(json_path, 'r') as f:
    json_dict = json.loads(f.read())
    for elvator in json_dict['_elevators']:
        elvator_list.append(Building(**elvator))

#print(size(elvator_list))
#elvator_list[0].Pos=1
#print(elvator_list[0].Pos,elvator_list[0].onJob )

#print(elvator_list[1]._stopTime)
