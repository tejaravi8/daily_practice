class onlineExam:
    def __init__(self):
        self.__questions={
            "who is the president of India":"murumu",
            "what is the capital of india":"New delhi",
            "what is the current pythion":3
            
        }
        self.__marks=0
        self.__isloggedin=False
        
    def loginExam(self,id):
        if id== id:
            print("successfully loggedin to exam ")
            self.__isloggedin=True
            
    def startExam(self):
        if self.__isloggedin:
            print("exam started")
            for q in self.__questions.keys():
                print(q)
        else:
            print("plz login to start the exam")
            
    def marks(self,answers):
        for q,a in self.__questions.items():
            # prrint(self.__questions[q])
            if self.__questions[q]==answers[q]:
                self.__marks+=1
        print(self.__marks,"marks")
        
        
durva=onlineExam()
S_id=input("enter student id:")
durva.loginExam(S_id)
durva.startExam()
durva.marks({"who is the president of India":"modi","what is the capital of india":"New delhi","what is the current pythion":3})



