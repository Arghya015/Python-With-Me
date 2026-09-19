def check_for_word():
    word="learning"
    with open("demo.txt","r") as f:
        data=f.read()
        if(word in data):
            print("found")
        else:
            print("not found")
check_for_word()

def check_for_line():
    word="learning"
    data=True
    line_no = 1
    with open("demo.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
            line_no += 1
    return -1
check_for_line()
