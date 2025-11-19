""" Configuration models for signals."""

class SignalConfig(BaseModel):
    readback: str
    setpoint: Optional[str] = None