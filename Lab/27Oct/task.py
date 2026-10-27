import random
from abc import ABC, abstractmethod


# ==========================================
# 1. ENVIRONMENT CLASS
#    Encapsulation & Properties
# ==========================================
class Environment:
    """Represents the world/room the agents interact with."""

    def __init__(self, initial_temp: float):
        self.__temperature = initial_temp
        self.__ac_on = False
        self.__motion_detected = False

    # Temperature property
    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        self.__temperature = round(value, 2)

    # AC status property
    @property
    def ac_on(self) -> bool:
        return self.__ac_on

    @ac_on.setter
    def ac_on(self, status: bool):
        self.__ac_on = status

    # Motion detection property
    @property
    def motion_detected(self) -> bool:
        return self.__motion_detected

    @motion_detected.setter
    def motion_detected(self, value: bool):
        self.__motion_detected = value

    def simulate_weather(self):
        """Randomly changes the room temperature."""
        change = random.choice([0.5, 1.0, -0.5])
        self.temperature = self.temperature + change

    def simulate_intruder(self):
        """Randomly simulates motion detection."""
        self.motion_detected = random.choice([True, False])


# ==========================================
# 2. BASE AGENT CLASS
#    Abstraction
# ==========================================
class Agent(ABC):
    """A generic blueprint for software agents."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def perceive(self, environment: Environment) -> float | bool:
        """Senses environmental data."""
        raise NotImplementedError

    @abstractmethod
    def think(self, perception_data: float | bool) -> str:
        """Processes perception and determines an action."""
        raise NotImplementedError

    @abstractmethod
    def act(self, action: str, environment: Environment):
        """Executes the chosen action."""
        raise NotImplementedError


# ==========================================
# 3. SMART AC AGENT
#    Inheritance & Polymorphism
# ==========================================
class SmartACAgent(Agent):
    """Controls room temperature using a simple reflex strategy."""

    def __init__(self, name: str, threshold_temp: float):
        super().__init__(name)
        self.threshold = threshold_temp

    def perceive(self, environment: Environment) -> float:
        current_temp = environment.temperature
        print(
            f"[{self.name}] Sensed Room Temperature: "
            f"{current_temp}°C"
        )
        return current_temp

    def think(self, current_temp: float) -> str:
        if current_temp > self.threshold:
            return "TURN_ON_AC"
        elif current_temp < (self.threshold - 2.0):
            return "TURN_OFF_AC"
        return "DO_NOTHING"

    def act(self, action: str, environment: Environment):
        if action == "TURN_ON_AC":
            if not environment.ac_on:
                environment.ac_on = True
                print(
                    f"[{self.name}] Action: "
                    "🟢 Turning ON the AC."
                )

            # AC lowers the room temperature
            environment.temperature = (
                environment.temperature - 1.5
            )

        elif action == "TURN_OFF_AC":
            if environment.ac_on:
                environment.ac_on = False
                print(
                    f"[{self.name}] Action: "
                    "🔴 Turning OFF the AC."
                )

        else:
            print(
                f"[{self.name}] Action: "
                "💤 Maintaining status quo."
            )


# ==========================================
# 4. SMART SECURITY AGENT
#    Inheritance & Polymorphism
# ==========================================
class SmartSecurityAgent(Agent):
    """Detects motion and controls the security alarm."""

    def __init__(self, name: str):
        super().__init__(name)
        self.__alarm_triggered = False

    # Alarm state property
    @property
    def alarm_triggered(self) -> bool:
        return self.__alarm_triggered

    @alarm_triggered.setter
    def alarm_triggered(self, value: bool):
        self.__alarm_triggered = value

    def perceive(self, environment: Environment) -> bool:
        """Checks whether motion is detected."""
        motion_status = environment.motion_detected
        print(
            f"[{self.name}] Motion detected: "
            f"{motion_status}"
        )
        return motion_status

    def think(self, motion_status: bool) -> str:
        """Decides whether to trigger the alarm."""
        if motion_status:
            return "TRIGGER_ALARM"
        return "STANDBY"

    def act(self, action: str, environment: Environment):
        """Triggers the alarm or keeps it on standby."""
        if action == "TRIGGER_ALARM":
            self.alarm_triggered = True
            print(
                "🚨 ALERT! Intruder detected! "
                "Alarm sounding!"
            )

        elif action == "STANDBY":
            self.alarm_triggered = False
            print("🔒 Room is secure.")


# ==========================================
# 5. EXECUTION LOOP
#    Multi-Agent Simulation
# ==========================================
if __name__ == "__main__":

    # Create the environment
    living_room = Environment(initial_temp=26.0)

    # Instantiate both agents
    climate_agent = SmartACAgent(
        name="ThermoAgent",
        threshold_temp=25.0
    )

    security_agent = SmartSecurityAgent(
        name="GuardAgent"
    )

    print("--- Starting Multi-Agent Simulation ---")

    # Run the simulation for five steps
    for step in range(1, 6):
        print(f"\n--- Hour {step} ---")

        # Simulate environmental changes
        living_room.simulate_weather()
        living_room.simulate_intruder()

        # 1. Climate Agent Cycle
        temp_reading = climate_agent.perceive(living_room)
        ac_decision = climate_agent.think(temp_reading)
        climate_agent.act(ac_decision, living_room)

        # 2. Security Agent Cycle
        motion_reading = security_agent.perceive(living_room)
        sec_decision = security_agent.think(motion_reading)
        security_agent.act(sec_decision, living_room)

        # Display final room status
        print(
            f"Room Status -> "
            f"AC On: {living_room.ac_on}, "
            f"Real Temp: {living_room.temperature}°C, "
            f"Alarm Triggered: "
            f"{security_agent.alarm_triggered}"
        )
