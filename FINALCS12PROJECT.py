import pickle
import random
import os



def menu(open="\n1.Add Questions\n2.Generate paper\n3.Display paper\n4.Exit",error="Enter a number between 1 to 4"):
    print(open)
    while True:
        try:
            n = int(input("Enter funtion: "))
        except ValueError:
            print(error)
        if n <= 4 and n >0:
            return n
        else:
            print(error)
def login():
    
    while True:
        userid=input("enter username:")
        passwd=input("enter password:")
        if userid!="xiics":
            print("Enter userid correctly")
            
        elif passwd!="s3v212cs":
            print("Enter password correctly")
        else:
            break
            
        
            
    
def namegenerator():
    
    while True:
      print("Physics-1, chemistry-2, CS-3")
      y=int(input("enter subject number:"))
      if y==1:
          x="physics"
          sname=x
          break
      elif y==2:
          x="chemistry"
          sname=x
          break
      elif y==3:
          x="CS"
          sname=x
          break 
    
    y=int(input("enter how many marks(1/2/3/5) : "))
    if y==1 or y==2 or y==3 or y==5:
        s1=x+str(y)+".dat"
    
    print(s1)
    return s1

def namegenerator1():
    
    while True:
      print("Physics-1, chemistry-2, CS-3")
      y=int(input("enter subject number:"))
      if y==1:
          x="physics"
          sname=x
          break
      elif y==2:
          x="chemistry"
          sname=x
          break
      elif y==3:
          x="CS"
          sname=x
          break 
    
    return sname

def letadd(fname):
    f=open(fname,"ab")
    while True:
        q=input("enter questions: ")
        l=[q]
        pickle.dump(l,f)
        ch=input("More(Y/N):")
        if ch in"Nn":
            break
    f.close()
        

Q1=Q2=Q3=Q5=0
def totalmarks(sname):
    
    global Q1,Q2,Q3,Q5
    while True:
        Total_marks=int(input("Enter total marks="))
        Q1=int(input("Enter total number of 1 mark question="))
        Q2=int(input("Enter total number of 2 mark question="))
        Q3=int(input("Enter total number of 3 mark question="))
        Q5=int(input("Enter total number of 5 mark question="))
        check=Q1*1+Q2*2+Q3*3+Q5*5
        if check!=Total_marks:
            print("Enter Marks correctly") 
        else:
            break
    generate_paper(sname,Q1,Q2,Q3,Q5)
        
    
    
def generate(sname, no_ques, fileno):
    Lt=[]
    count=1
    fname=sname+str(fileno)+".dat"
    fn=open(fname,"rb")
    try:
        while True:
            p=pickle.load(fn)
            count=count+1
            
    except EOFError:
        fn.close()

    while len(Lt)<=no_ques:
        num=random.randint(1,count)
        if num not in Lt:
            Lt.append(num)
    return Lt


def generate_paper(sname,Q1,Q2,Q3,Q5):
    
        
    
    
    list_q= generate(sname,Q1,1)
    write_ques(sname,list_q,1)
    list_q= generate(sname,Q2,2)
    write_ques(sname,list_q,2)
    list_q= generate(sname,Q3,3)
    write_ques(sname,list_q,3)
    list_q= generate(sname,Q5,5)
    write_ques(sname,list_q,5)

def write_ques(sname,list_q,fileno):
    fname=sname+str(fileno)+".dat"
    f=open(fname,"rb")
    f1=open("qpaper.dat","ab")
    list_q.sort()
    count=0
    try:
        while True:
            ques=pickle.load(f)
            k=list_q[0]
            if k==count:
                list_q.pop(0)
                pickle.dump(ques,f1)
            count=count+1
            if len(list_q)==0:
                break
    except EOFError:
        f.close()
        f1.close()

def display(fname,Q1,Q2,Q3,Q5):
    count=1
    f=open(fname,"rb")
    subject_name=input("enter subject name again=")
    s=subject_name.upper()
    
        
    print("                                                         CLASS: XII Session: 2022-2023                                                     ")
    print("                                                               ",s,"                                                                       ")
    print("                                                         Sample Question Paper(Theory)                                                     ")
    
                                                                                         

    print("GENERAL INSTRUCTIONS:")
    print("        1. Please read the Question Paper carefully.")
    print("        2. 15 minutes are alloted for reading the Question Paper.")
    print("        3. Do not write anything on the Question Paper.")
    if Q1>0 and Q1>1:
        print("        4. Question 1 to ",Q1,"are of 1 marks questions.")
    if Q2>0 and Q2>1:
        print("        5. Question",Q1+1,"to",Q1+Q2,"are of 2 marks questions.")
    if Q3>0 and Q3>1:
        print("        6. Question",Q1+Q2+1,"to",Q1+Q2+Q3,"are of 3 marks question.")

    if Q5>0 and Q5>1:
        print("        7. Question",Q1+Q2+Q3+1,"to",Q1+Q2+Q3+Q5,"are of 5 marks questions")
    print(" ___________________________________________________________________________________________________________________________________________ ")
          
          
    try:
        while True:
            ques=pickle.load(f)
            print(count,ques[0],sep='.')
            count=count+1
                   
    except EOFError:
        f.close()
    remove=input("Is this paper okay?(Y/N)=")
    if remove in 'yY':
        os.remove("qpaper.dat")
    else:
        start()
def start():
    
   
    while True:
        n=menu()
        if n==1:
            call=namegenerator() 
            letadd(call)
        elif n==2:
            sname=namegenerator1() 
            totalmarks(sname)
        elif n==3:
            display("qpaper.dat",Q1,Q2,Q3,Q5)          
        elif n==4:
            break
login()
start()
