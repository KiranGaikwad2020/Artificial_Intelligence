from experta import *
class StudentFacts(Fact):
    pass
class CareerExpertSystem(KnowledgeEngine):
    @Rule(StudentFacts(likes='Maths'), StudentFacts(likes='Physics'))
    def bachelor(self):
        print("Suggested Career Path: B.Sc, Physics Mastery, You Nerd!")
    @Rule(StudentFacts(likes= 'Biology'), StudentFacts(likes= 'Chemistry'))
    def mbbs(self):
        print("Suggested Career Path: Become a Doctor, Save Lives!")
    @Rule(StudentFacts(likes='Programming'), StudentFacts(likes='Maths'))
    def computer(self):
        print("Suggested Career Path: Computer Engineering, You Future IT Worker!")
    @Rule(StudentFacts(likes='Programming'),StudentFacts(likes='AI'))
    def AIDS(self):
    	print("Suggested Career Path: Artifical Intelligence and Data Science, You Aspiring Data Scientist!")
    @Rule(StudentFacts(likes='Maths'),StudentFacts(likes= 'Mechanics'))
    def mechanical(self):
    	print("Suggested Career Path: Mechanical Engineering,  Build Some Machines Bro!")
    @Rule(StudentFacts(likes='Graphics'),StudentFacts(likes='Maths'))
    def Civil(self):
    	print("Suggested Career Path: Civil Engineering, Get construct those skyscrapers.")
    @Rule(StudentFacts(likes='Design'),StudentFacts(likes='Machine Learning'))
    def Ro_AI(self):
    	print("Suggested Career Path: Robotics and Artificial Intelligence, Go and Design you Teeny Weeny Robots")
def main():
    engine = CareerExpertSystem()
    engine.reset()
    print("Welcome to the Career Path Expert System!\n")
    print("Select the subjects you are interested in\n")
    print(" 1.Maths\n", "2.Physics\n","3.Graphics\n","4.Mechanics\n","5.Programming\n","6.Chemistry\n","7.Biology\n","8.Circuits\n","9.AI\n","10.Design\n","11.Machine learning\n")
    interests = input("Enter your any 2 of the above subjects as your interests separated by commas (e.g., Maths, Programming): ").split(',')
    for interest in interests:
        engine.declare(StudentFacts(likes=interest.strip()))
    engine.run()
if __name__ == "__main__":
    main()


# Execute the following steps to execute the program
# 1. $ sudo apt update
# 2. $ sudo apt install python3-pip
# 3. $ python3 -m pip install experta
# 4. $ python3 -m pip install frozendict==2.3.4
