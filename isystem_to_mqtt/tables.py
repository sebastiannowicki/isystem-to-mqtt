from .tag_definition import TagDefinition, WriteTagDefinition, MultipleTagDefinition
from . import convert

READ_TABLE = {
    231: TagDefinition("zone-a/program", convert.unit),
    507: TagDefinition("boiler/start-count", convert.unit_and_ten),
    509: TagDefinition("boiler/hours-count", convert.unit_and_ten),
    601: TagDefinition("outside/temperature", convert.tenth),
    602: TagDefinition("boiler/temperature", convert.tenth),
    607: TagDefinition("boiler/return-temperature", convert.tenth),
    610: TagDefinition("boiler/pressure", convert.tenth),
    614: TagDefinition("zone-a/temperature", convert.tenth),
    615: TagDefinition("zone-a/calculated-temperature", convert.tenth),
    620: TagDefinition("boiler/calculated-temperature", convert.tenth),
    650: TagDefinition("zone-a/day-target-temperature", convert.tenth),
    651: TagDefinition("zone-a/night-target-temperature", convert.tenth),
    652: TagDefinition("zone-a/antifreeze-target-temperature", convert.tenth),
    653: MultipleTagDefinition([("zone-a/mode", convert.derog_bit),
                                ("zone-a/mode-raw", convert.unit)]),
    654: TagDefinition("zone-a/sensor-influence", convert.unit),
    655: TagDefinition("zone-a/curve", convert.tenth),
    656: TagDefinition("zone-b/day-target-temperature", convert.tenth),
    657: TagDefinition("zone-b/night-target-temperature", convert.tenth),
    658: TagDefinition("zone-b/antifreeze-target-temperature", convert.tenth),
    659: MultipleTagDefinition([("zone-b/mode", convert.derog_bit),
                                ("zone-b/mode-raw", convert.unit)]),
    721: TagDefinition("zone-a/antifreeze-duration", convert.unit)
 
}

WRITE_TABLE = {
    "zone-a/program/SET": WriteTagDefinition(231, convert.write_unit),
    "zone-a/mode-raw/SET": WriteTagDefinition(653, convert.write_unit),
    "zone-a/antifreeze-duration/SET": WriteTagDefinition(721, convert.write_unit),
    "zone-a/day-target-temperature/SET": WriteTagDefinition(650, convert.write_tenth),
    "zone-a/night-target-temperature/SET": WriteTagDefinition(651, convert.write_tenth),
    "zone-b/mode-raw/SET": WriteTagDefinition(659, convert.write_unit)
}
