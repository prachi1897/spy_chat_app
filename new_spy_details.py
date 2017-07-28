def new_spy():
         new_spy_name=str(raw_input("Enter new spy name"))
         new_spy_salutation=raw_input("What you liked to be called\n1:Mr.\n2:Miss\n3:Mrs\n4:Others")
         new_spy_status=raw_input("Enter\n1:Online\n2:Offline")
         new_spy_rating=float(raw_input("Give ratings to the new spy"))
         new_spy_age=int(raw_input("Enter new spy age"))
         new_spy_list=[new_spy_name,new_spy_salutation,new_spy_status,new_spy_rating,new_spy_age]
         return new_spy_list
