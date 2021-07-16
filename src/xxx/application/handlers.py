# pylint: disable=unused-argument
from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING
from xxx.domain import commands, events

if TYPE_CHECKING:
    from xxx.adapters import notifications
    from . import unit_of_work


def example_event_handler(event: events.Event):
    pass

def example_command_handler(cmd: commands.Command):
    pass


EVENT_HANDLERS = {
    events.Event: [example_event_handler]

}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.Command: [example_command_handler]

}  # type: Dict[Type[commands.Command], Callable]