import sys
import datetime
def help():
    sa = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
    sys.stdout.buffer.write(sa.encode('utf8'))


def add(p,s):
    
    f = open('task.txt', 'a')
    f.write(s+" "+p)
    #f.write(p)
    #f.write("%s %d" %(s,p))
    f.write("\n")
    f.close()
    s = '"'+s+'"'
    print(f"Added task: {s} with priority {p}")

def ls():
    try:
        nec()
        l=len(d)
        k=l
        dict1 = {}
        for i in d:
            prior = d[i]
            dict1[prior[:-1]] = prior[-1]
        a = sorted(dict1.items(), key=lambda x: x[1])
        count=1
        for i,v in a:
            sys.stdout.buffer.write(f"{count}. {i}[{v}]".encode('utf8'))
            sys.stdout.buffer.write("\n".encode('utf8'))
            count+=1

    except Exception as e:
        raise e 

def done(no):
    try:
  
        nec()
        no = int(no)
        f = open('completed.txt', 'a')
        st =d[no]
          
        f.write(st)
        f.write("\n")
        f.close()
        print(f"Marked item as done.")
          
        with open("task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
              
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
    except:
        print(f"Error: no incomplete item with index #{no} exists.")

def report():
    nec()
    try:
  
        nf = open('completed.txt', 'r')
        c = 1
          
        for line in nf:
            line = line.strip('\n')
            don.update({c: line})
            c = c+1
        print(f'Pending : {len(d)}')
        
        l = len(d)
        k = l
  
        for i in d:
            prior = d[i]
            print(f"{i}. {prior[:-1]}[{prior[-1]}]")
        
        print(f'\nCompleted : {len(don)}')

        nef()
   
    except:
        print(
            f'Pending : {len(d)} Completed : {len(don)}')

def deL(no):
    try:
        no = int(no)
        nec()
  
        
        with open("task.txt", "r+") as f:
            lines = f.readlines()
            f.seek(0)
              
            for i in lines:
                if i.strip('\n') != d[no]:
                    f.write(i)
            f.truncate()
        print(f"Deleted task #{no}")
  
    except Exception as e:
        
        print(f"Error: task with index #{no} does not exist. Nothing deleted.")

def nec():
  
    try:
        f = open('task.txt', 'r')
        c = 1
        for line in f:
            line = line.strip('\n')
            d.update({c: line})
            c = c+1
    except:
        sys.stdout.buffer.write("There are no pending tasks!".encode('utf8'))

def nef():
    
    d1 = {}
    try:
        f1 = open('completed.txt', 'r')
        c1 = 1
        for line1 in f1:
            line1 = line1.strip('\n')
            d1.update({c1: line1})
            c1 = c1+1
    except:
        sys.stdout.buffer.write("All tasks completed".encode('utf8'))
    
    l1 = len(d1)
    k1 = l1
  
    for i in d1:
            prior1 = d1[i]
            print("{}. {}".format(i,prior1[:-2]))
if __name__ == '__main__':
    try:
        d = {}
        don = {}
        args = sys.argv
          
        if(args[1] == 'del'):
            args[1] = 'deL'
              
        if(args[1] == 'add' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing tasks string. Nothing added!".encode('utf8'))
  
        elif(args[1] == 'done' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for marking tasks as done.".encode('utf8'))
  
        elif(args[1] == 'deL' and len(args[2:]) == 0):
            sys.stdout.buffer.write(
                "Error: Missing NUMBER for deleting tasks.".encode('utf8'))
        else:
            globals()[args[1]](*args[2:])
  
    except Exception as e:
  
        s = """Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics"""
        sys.stdout.buffer.write(s.encode('utf8'))
