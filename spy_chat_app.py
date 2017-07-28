import default_spy_details
from new_spy_details import new_spy
import new_spy_details
from default_spy_details import default_spy_dict
# encode a text message behind an image
from steganography.steganography import Steganography
#from new_spy_details import new_spy_name,new_spy_age,new_spy_rating,new_spy_salutation,new_spy_status

#chat dictionary
chat={
    'Prachi':"Hey!! How are you",
    'Ritu':"I am fine",
    'James Bond':"Hey ssup",
    'Xx01':'Welcome'
}

#defining friends name
friend_name=['Ritu','XX01','James Bond','Prachi']
#defining friends status
friend_status=[]
#defining friend_rating
friend_rating=[]
#defining friend_age
friend_age=[]
#defining status list
spy_status_list=[]
#defining status list
status_list=["Hello", "Have a wonderful day","Hey ssup"]



#status function
def new_status():
    default_status = raw_input("Enter \n1:Add a new status\n2:Older status")
    if default_status=='1':
        current_status = raw_input("Display the new status")
        if current_status == None:
                print "You don't have any current status"
        elif current_status != None:
                print "Your status" + current_status
                spy_status_list.append(current_status)
                print spy_status_list

#selection of friend
def select_a_friend():
    print friend_name
    choose_friend = raw_input("Choose friend name")
    print choose_friend


#add a friend
def add_a_friend():
    str=new_spy()
    print str
    if str[0] > 0 and str[4] > 12 and str[0] > default_spy_details.default_spy_dict['Prachi'][
        'rating']:
        friend_name.append(str[0])
        friend_age.append(str[4])
        friend_rating.append(str[3])
        return len(friend_name)

#send a message
def send_a_message():
    select_a_friend()
    name_encoded_image = raw_input("Enter the name for the encoded image")
    path = "C:\\Users\\hp\\Pictures\\Screenshots\\Screenshot1.png"
    out_path = "C:\\Users\\hp\\Pictures\\Screenshots\\secret.png"
    msg = raw_input("Enter the secret message you want to hide")
    # encode a text message behind an image
    Steganography.encode(path, out_path, msg)
    # read secret text from image
    secret_text = Steganography.decode(out_path)




#read chat
def read_chat():
    choose_frnd=raw_input("Enter the friend name")
    if choose_frnd in friend_name:
        read_c = chat[choose_frnd]
        print read_c



#menu function
def menu():
    choice = raw_input("Enter what do you want to do\n1:Update the status\n2:Add a friend\n3:Send a secret message\n4:Send a message\n5:Read chats from the user\n6:Close application")
    while True:
        if choice == '1':
            status = raw_input("Enter\n 1:Add a status update.\n 2:Choose from older status")
            if status == '1':
                new_status()
            elif status == '2':
                print status_list
                old_status = raw_input("Enter the previous status")
                if old_status in status_list:
                    print "Status is present in status list and is "" " + old_status
                else:
                    print "Status is not present in the older status list"
                    status_input=raw_input("Enter 1:If you want to input the status in spy list 2:if you dont wanna add the status to spy list")
                    if status_input=='1':
                        status_list.append(old_status)
                        print status_list
                    elif status_input=='2':
                        print "Thankyou"

                menu()
        elif choice == '2':
            add_a_friend()
            menu()
        elif choice=='3':
            send_a_message()
            menu()
        elif choice=='4':
            send_a_message()
            menu()
        elif choice=='5':
            read_chat()
            menu()

        elif choice=='6':
            print "Bye-Bye"
            quit()


#welcome the spy
default_spy_name=raw_input("Enter the default spy name")
if default_spy_name in default_spy_details.default_spy_dict:
    print" Spy name is present in the list\n Welcome" "  " + default_spy_name
elif default_spy_name not in default_spy_dict:
    print "Spy name is not present in the list"
    if len(default_spy_name) >0:
        print "Spy name is valid"
        default_spy_dict[default_spy_name]={
            "salutation":'Miss',
            "age":20,
            "status":'Online',
            "rating":9
        }
    elif len(default_spy_name) < 0:
        print "Invalid spy name"


choose_spy=raw_input("Enter\n 1:If you want to continue with the default spy \n 2:If you want to add a new spy")

if choose_spy=='1':
    print "You choose to continue with the default spy"  "  "+ default_spy_name
    menu()
 #new spy details
elif choose_spy=='2':
    print new_spy_details.new_spy()
   # print new_spy_name
    menu()
