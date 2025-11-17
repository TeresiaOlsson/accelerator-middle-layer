"""
Example for MLS.
This code should eventually go in it's own repository.
"""

"""Example file for generating the configuration for MLS."""

from accelerator_middle_layer.config import (
    AcceleratorConfig,
    EPICSConfig,
    SimulatorConfig,
    MagnetConfig,
    EPICSType
)

from accelerator_middle_layer.registry.accelerator import Accelerator
from accelerator_middle_layer.registry.utils import WildcardDict

# Facility and machine name
facility = 'MLS'
machine = 'storage_ring'

# Backends
live = EPICSConfig(name = 'live', access_type=EPICSType.CA)
twin = EPICSConfig(name = 'twin', access_type=EPICSType.CA,pv_prefix='twin')
design = SimulatorConfig(name = 'design', type='pyat',model='design_lattice.json')
error = SimulatorConfig(name = 'error', type='pyat',model='error_lattice.json')
measured = SimulatorConfig(name = 'measured', type='pyat',model='measured_lattice.json')

# Quadrupoles
quads = []
families = ['Q1','Q2','Q3']
cells = ['1','2']
sections = ['K1','L2','K3','L4']

for quad in families:
    for cell in cells:
        for section in sections:
            quads.append(MagnetConfig(name=f'{quad}M{cell}{section}RP',type='quadrupole',power_supply=f'{quad}P{cell}{section}RP'))

# Generate a dictionary of the quadrupole configurations
quads_by_name = {q.name: q for q in quads}

# Families

Q1 = [device.name for device in WildcardDict(quads_by_name)['Q1*']]
Q2 = [device.name for device in WildcardDict(quads_by_name)['Q2*']]
Q3 = [device.name for device in WildcardDict(quads_by_name)['Q3*']]
TuneCorrectors = Q1 + Q3

families = {'Q1': Q1,
            'Q2': Q2,
            'Q3': Q3,
            'TuneCorrectors': TuneCorrectors}

# Accelerator

config = AcceleratorConfig(facility=facility, machine=machine,
                           backends = {'live': live,
                                       'twin': twin,
                                        'design': design,
                                         'error': error,
                                         'measured': measured
                                         },
                           devices = quads_by_name,
                           families = families
                           )

mls = Accelerator(config)