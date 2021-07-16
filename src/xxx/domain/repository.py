import abc
from typing import Set
from . import model

class AbstractRepository(abc.ABC):
    def __init__(self):
        self.seen = set()  # type: Set[model.AggregationObject]

    def add(self, aggregation_object: model.AggregationObject):
        self._add(aggregation_object)
        self.seen.add(aggregation_object)

    def get(self, id) -> model.AggregationObject:
        aggregation_object = self._get(id)
        if aggregation_object:
            self.seen.add(aggregation_object)
        return aggregation_object


    @abc.abstractmethod
    def _add(self, aggregation_object: model.AggregationObject):
        raise NotImplementedError

    @abc.abstractmethod
    def _get(self, id) -> model.AggregationObject:
        raise NotImplementedError
