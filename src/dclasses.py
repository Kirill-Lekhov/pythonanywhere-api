from dataclasses import dataclass
from datetime import datetime


@dataclass
class CPUQuota:
    daily_cpu_limit_seconds: float
    daily_cpu_total_usage_seconds: float
    next_reset_time: datetime

    def __str__(self) -> str:
        return f"""CPU Quota:
Daily CPU limit seconds:\t{self.daily_cpu_limit_seconds}
Daily CPU total usage seconds:\t{self.daily_cpu_total_usage_seconds}
Next reset time:\t\t{self.next_reset_time.isoformat()}
"""

    @classmethod
    def from_json(cls, data: dict) -> "CPUQuota":
        return cls(
            data['daily_cpu_limit_seconds'],
            data['daily_cpu_total_usage_seconds'],
            datetime.fromisoformat(data['next_reset_time']),
        )
