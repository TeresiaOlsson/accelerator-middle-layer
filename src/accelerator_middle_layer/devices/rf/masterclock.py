""" Module for masterclock. """

from pydantic import BaseModel
from typing import Optional
from ...config import SignalConfig
from ophyd_async.core._signal_backend import SignalBackend, SignalDatatypeT
from ophyd_async.core._signal import SignalRW
from ophyd_async.core import StandardReadable


class MasterclockConfig(BaseModel):
    frequency: SignalConfig

class MasterClock(StandardReadable):

    def __init__(self, backend: SignalBackend[SignalDatatypeT], readback: str, setpoint: Optional[str] = None):

        name = "masterclock"

        #frequency = SignalRW(backend)

        # self._readback = readback
        # if setpoint:
        #     self._setpoint = setpoint

        with self.add_children_as_readables():
            self.frequency = epics_signal_rw(float, read_pv= self._readback_pv,
#                                              write_pv= self._setpoint_pv, name='frequency')
#         super().__init__(name=config.name)

    @DeviceFactory.register(MasterclockConfig)
    def create_masterclock(config: MasterclockConfig) -> MasterClock:
        return MasterClock(readback=config.readback, setpoint=config.setpoint)
    

#     @AsyncStatus.wrap
#     async def set(self, new_value: float, timeout: CalculatableTimeout = CALCULATE_TIMEOUT):
#         logging.debug(f"set() called with new_value={new_value}")

#         old_value = await self.frequency.get_value()
#         logging.debug(f"Old value = {old_value}")

#         # Calculate the time to wait based on the ramp rate
#         change = abs(new_value - old_value)
#         wait_time = change / self._ramp_rate
#         logging.debug(f"Calculated wait time = {wait_time}")

#         # Define the timeout based on the ramp rate
#         if timeout == CALCULATE_TIMEOUT:
#             timeout = wait_time + DEFAULT_TIMEOUT
#             logging.debug(f"Calculated timeout = {timeout}")

#         # Set the value
#         await self.frequency.set(new_value)
#         await asyncio.sleep(wait_time)

#         # Compare so readback and setpoint is within some tolerance
#         current_values = await self.frequency.locate()
#         diff = abs(current_values['readback'] - current_values['setpoint'])

#         logging.debug(f"Compare setpoint = {current_values['setpoint']} and readback = {current_values['readback']}")
#         logging.debug(f"Absolute difference is = {diff}")

#         if diff > self._tolerance:
#             raise Exception('The difference between the readback and setpoint is larger than the tolerance.')



# import asyncio
# from pydantic import BaseModel
# from typing import Optional
# # from ophyd_async.core import (
# #     StandardReadable,
# #     AsyncStatus,
# #     CALCULATE_TIMEOUT,
# #     DEFAULT_TIMEOUT,
# #     CalculatableTimeout,
# # )

# # from ophyd_async.epics.core import epics_signal_rw


# class MasterClockConfig(BaseModel):

#     name: 'masterclock'
#     setpoint_pv: str
#     readback_pv: str
#     ramp_rate: float # Unit should be in kHz/s
#     tolerance: float # Unit should be in Hz
#     # TODO: Units needs to be generalised and handled better


# class MasterClock(StandardReadable):

#     def __init__(self, config: MasterClockConfig, prefix: Optional[str] = None) -> None:

#         # TODO: this needs to be generalised so can also incude ca and pva.
#         if prefix:
#             self._setpoint_pv = prefix + ':' + config.setpoint_pv
#             self._readback_pv = prefix + ':' + config.readback_pv
#         else:
#             self._setpoint_pv = config.setpoint_pv
#             self._readback_pv = config.readback_pv

#         self._ramp_rate = config.ramp_rate
#         self._tolerance = config.tolerance

#         with self.add_children_as_readables():
#             self.frequency = epics_signal_rw(float, read_pv= self._readback_pv,
#                                              write_pv= self._setpoint_pv, name='frequency')
#         super().__init__(name=config.name)

#     @property
#     def setpoint_pv(self):
#         return self._setpoint_pv

#     @property
#     def readback_pv(self):
#         return self._readback_pv

#     @property
#     def ramp_rate(self):
#         return self._ramp_rate

#     @property
#     def tolerances(self):
#         return self._tolerance


#     @AsyncStatus.wrap
#     async def set(self, new_value: float, timeout: CalculatableTimeout = CALCULATE_TIMEOUT):
#         logging.debug(f"set() called with new_value={new_value}")

#         old_value = await self.frequency.get_value()
#         logging.debug(f"Old value = {old_value}")

#         # Calculate the time to wait based on the ramp rate
#         change = abs(new_value - old_value)
#         wait_time = change / self._ramp_rate
#         logging.debug(f"Calculated wait time = {wait_time}")

#         # Define the timeout based on the ramp rate
#         if timeout == CALCULATE_TIMEOUT:
#             timeout = wait_time + DEFAULT_TIMEOUT
#             logging.debug(f"Calculated timeout = {timeout}")

#         # Set the value
#         await self.frequency.set(new_value)
#         await asyncio.sleep(wait_time)

#         # Compare so readback and setpoint is within some tolerance
#         current_values = await self.frequency.locate()
#         diff = abs(current_values['readback'] - current_values['setpoint'])

#         logging.debug(f"Compare setpoint = {current_values['setpoint']} and readback = {current_values['readback']}")
#         logging.debug(f"Absolute difference is = {diff}")

#         if diff > self._tolerance:
#             raise Exception('The difference between the readback and setpoint is larger than the tolerance.')
