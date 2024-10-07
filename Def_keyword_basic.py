def answer(ans):
    if ans == 78:
        return True
    else:
        return False

def get_user_ans():
    while True:
        try:
            user_ans = int(input("what is sveenty-eight?"))
            return user_ans

        except ValueError:
            print("enter you answer properly")
        
    
def main():
    print("welcome to our QUiz")

    user_ans = get_user_ans()
    user_answerr = answer(user_ans)

    if user_answerr:
        print("you are right")

    else:
        print("No, you are wrong")

if __name__=="__main__":
    main()

    
    

