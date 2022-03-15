from subsystems.climbingsubsystem import ClimbingSubsystem
import commands2
 

class coastRotateArm(commands2.CommandBase):
    def __init__(self, isCoast, climb: ClimbingSubsystem, container) -> None:
        super().__init__()
        
        self.climb = climb
        self.container=container
        self.container.isCoast=not self.container.isCoast



    def initialize(self):
        pass

    def execute(self) -> None:

        self.climb.setCoast(isCoast)

        output("Break Mode:",isCoast)

    def end(self, interrupted: bool) -> None:
        self.climb.setCoast(False)
