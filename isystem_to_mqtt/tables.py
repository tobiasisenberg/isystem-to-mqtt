""" Definition of Modbus adress and convertions to apply """

from .tag_definition import TagDefinition, WriteTagDefinition, MultipleTagDefinition
from . import convert


def get_tables(model):
    """ Return the address definition depending of model. """
    if model == "modulens-o":
        return (READ_TABLE_MODULENS_O, WRITE_TABLE_MODULENS_O, ZONE_TABLE_MODULENS_O)
    return (None, None, None)

ZONE_TABLE_MODULENS_O = [(231, 3),
                         (507, 4),
                         (600, 21),
                         (637, 24),
                         (721, 4)]

READ_TABLE_MODULENS_O = {
    7: TagDefinition("outside/temperature", convert.tenth),
    8: TagDefinition("boiler/summer-setpoint", convert.tenth),
    9: TagDefinition("outside/antifreeze", convert.tenth),
    11: TagDefinition("boiler/pump-postrun", convert.unit),
    14: TagDefinition("zone-a/day-target-temperature", convert.tenth),
    15: TagDefinition("zone-a/night-target-temperature", convert.tenth),
    16: TagDefinition("zone-a/antifreeze-target-temperature", convert.tenth),
    17: MultipleTagDefinition([("zone-a/mode", convert.derog_bit),
                               ("zone-a/mode-raw", convert.unit),
                               ("zone-a/mode-simple", convert.derog_bit_simple)]),
    18: TagDefinition("zone-a/temperature", convert.tenth),
    19: TagDefinition("zone-a/sensor-influence", convert.unit),
    20: TagDefinition("zone-a/curve", convert.tenth),
    21: TagDefinition("zone-a/calculated-temperature", convert.tenth),
    23: TagDefinition("zone-b/day-target-temperature", convert.tenth),
    24: TagDefinition("zone-b/night-target-temperature", convert.tenth),
    25: TagDefinition("zone-b/antifreeze-target-temperature", convert.tenth),
    26: MultipleTagDefinition([("zone-b/mode", convert.derog_bit),
                               ("zone-b/mode-raw", convert.unit),
                               ("zone-b/mode-simple", convert.derog_bit_simple)]),
    27: TagDefinition("zone-b/temperature", convert.tenth),
    28: TagDefinition("zone-b/sensor-influence", convert.unit),
    29: TagDefinition("zone-b/curve", convert.tenth),
    31: TagDefinition("zone-b/water-max-temperatur", convert.tenth),
    32: TagDefinition("zone-b/calculated-temperature", convert.tenth),
    33: TagDefinition("zone-b/water-temperature", convert.tenth),
    35: TagDefinition("zone-c/day-target-temperature", convert.tenth),
    36: TagDefinition("zone-c/night-target-temperature", convert.tenth),
    37: TagDefinition("zone-c/antifreeze-target-temperature", convert.tenth),
    38: MultipleTagDefinition([("zone-c/mode", convert.derog_bit),
                               ("zone-c/mode-raw", convert.unit),
                               ("zone-c/mode-simple", convert.derog_bit_simple)]),
    39: TagDefinition("zone-c/temperature", convert.tenth),
    40: TagDefinition("zone-c/sensor-influence", convert.unit),
    41: TagDefinition("zone-c/curve", convert.tenth),
    43: TagDefinition("zone-c/water-max-temperatur", convert.tenth),
    44: TagDefinition("zone-c/calculated-temperature", convert.tenth),
    45: TagDefinition("zone-c/water-temperature", convert.tenth),
    59: TagDefinition("dhw/target-temperature", convert.tenth),
    61: TagDefinition("dhw/pump-postrun", convert.unit),
    62: TagDefinition("dhw/temperature", convert.tenth),
    74: TagDefinition("boiler/calculated-temperature", convert.tenth),
    75: TagDefinition("boiler/temperature", convert.tenth),
    102: TagDefinition("outside/mean-temperature", convert.tenth),
    117: TagDefinition("boiler/temperature", convert.tenth),
    126: TagDefinition("zone-a/schedule", convert.json_week_schedule, 21),
    147: TagDefinition("zone-b/schedule", convert.json_week_schedule, 21),
    168: TagDefinition("zone-c/schedule", convert.json_week_schedule, 21),
    189: TagDefinition("dhw/schedule", convert.json_week_schedule, 21),
    231: TagDefinition("zone-a/program", convert.unit),
    232: TagDefinition("zone-b/program", convert.unit),
    233: TagDefinition("zone-c/program", convert.unit),
    507: TagDefinition("boiler/start-count", convert.unit_and_ten, 2),
    509: TagDefinition("boiler/hours-count", convert.unit_and_ten, 2),
    601: TagDefinition("outside/temperature", convert.tenth),
    602: TagDefinition("boiler/temperature", convert.tenth),
    607: TagDefinition("boiler/return-temperature", convert.tenth),
    610: TagDefinition("boiler/pressure", convert.tenth),
    614: TagDefinition("zone-a/temperature", convert.tenth),
    615: TagDefinition("zone-a/calculated-temperature", convert.tenth),
    620: TagDefinition("boiler/calculated-temperature", convert.tenth),
    637: TagDefinition("zone-a/active-mode", convert.active_mode),
    638: TagDefinition("zone-b/active-mode", convert.active_mode),
    644: TagDefinition("boiler/active-mode", convert.boiler_mode),
    650: TagDefinition("zone-a/day-target-temperature", convert.tenth),
    651: TagDefinition("zone-a/night-target-temperature", convert.tenth),
    652: TagDefinition("zone-a/antifreeze-target-temperature", convert.tenth),
    653: MultipleTagDefinition([("zone-a/mode", convert.derog_bit),
                                ("zone-a/mode-raw", convert.unit),
                                ("zone-a/mode-simple", convert.derog_bit_simple)]),
    654: TagDefinition("zone-a/sensor-influence", convert.unit),
    655: TagDefinition("zone-a/curve", convert.tenth),
    656: TagDefinition("zone-b/day-target-temperature", convert.tenth),
    657: TagDefinition("zone-b/night-target-temperature", convert.tenth),
    658: TagDefinition("zone-b/antifreeze-target-temperature", convert.tenth),
    659: MultipleTagDefinition([("zone-b/mode", convert.derog_bit),
                                ("zone-b/mode-raw", convert.unit),
                                ("zone-b/mode-simple", convert.derog_bit_simple)]),
    721: TagDefinition("zone-a/antifreeze-duration", convert.unit),
    724: TagDefinition("zone-b/antifreeze-duration", convert.unit)

}

WRITE_TABLE_MODULENS_O = {
    "zone-a/antifreeze-duration/SET": WriteTagDefinition(13, convert.write_unit),
    "zone-a/program/SET": WriteTagDefinition(231, convert.write_unit),
    "zone-a/mode-simple/SET": WriteTagDefinition(653, convert.write_derog_bit_simple),
    "zone-a/mode-raw/SET": WriteTagDefinition(653, convert.write_unit),
    # antifreeze-duration do not work, boiler ignore value
    # "zone-a/antifreeze-duration/SET": WriteTagDefinition(721, convert.write_unit),
    "zone-a/day-target-temperature/SET": WriteTagDefinition(650, convert.write_tenth),
    "zone-a/night-target-temperature/SET": WriteTagDefinition(651, convert.write_tenth),

    "zone-b/program/SET": WriteTagDefinition(232, convert.write_unit),
    "zone-b/mode-simple/SET": WriteTagDefinition(659, convert.write_derog_bit_simple),
    "zone-b/mode-raw/SET": WriteTagDefinition(659, convert.write_unit),
    "zone-b/antifreeze-duration/SET": WriteTagDefinition(724, convert.write_unit),
    "zone-b/day-target-temperature/SET": WriteTagDefinition(656, convert.write_tenth),
    "zone-b/night-target-temperature/SET": WriteTagDefinition(657, convert.write_tenth),
}
