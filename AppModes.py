import backend.backend_SQL as sql
import backend.backend_PDF as pdf

def AddADishMode():

    print('Add a Dish: ')

    dishname = input('enter dish name: ')

    print('b : breakfast\nl : lunch\nd : dinner')
    dishtype = input('enter dish type (b, l or d): ')

    print('adding dish in the database....')
    sql.AddDishInDatabase(dishname, dishtype)

    print('process successful!')
    print('what do you want to do now?\n(a): add another dish\n(b): go back\n(e): exit the program')

    choice = input('please enter your choice (a,b or e): ')

    if choice == 'a':
        AddADishMode()
    elif choice == 'b':
        return 'go back!'
    elif choice == 'e':
        return 'exit'
    else:
        print('incorrect choice!')

def MakeAMenuMode():
    '''this is supposed to be the whole process of how the menu making function goes to work hehehehe!!!'''
    #heading
    print('Make a menu:')

    #days of the week all in an immutable tuple
    daysOfWeek = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

    #all the meals of a day in an immutable tuple
    courses = {"b":'Breakfast', 'l':'Lunch', 'd':'Dinner'}

    #this is where we store all the data for the menu which will be delivered to the pdf making function
    menu_dict = dict()

    #user input for all the shit
    for i in daysOfWeek:
        print(i,':')
        
        #for storing all the intermediat values temporarily until we finally update them in menu_dict
        courses_dict = dict()

        for j in courses:

            print('\t', courses[j], ':')

            #loop for user input
            while True:

                #give the user a choice to randomize it from the database or just write it on their own
                choice = input("\t\tpress 'r' for something random from the "+ courses[j] + " category to be added or press 't' to type something on your own: ")

                if choice == 'r':

                    #add in the random dish into the dictionary
                    courses_dict[j] = sql.randomizeDish(j, menu_dict)

                    print('randomly chosen', courses_dict[j])
                    break
                elif choice == 't':
                    
                    #let the user type in their preference
                    courses_dict[j] = input('add in the dish name: ')

                    print('dish', courses_dict[j], 'added!')
                    break
                else:
                    print('wrong input!')
                    continue
            #end of user input loop
        #end of courses loop

        menu_dict[i] = courses_dict
    #end of the week loop
    print(menu_dict)
    #now for the pdf magic to happen!
    print('the menu has been successfully made!')

    print('arranging data in a table....')
    print('printing table onto pdf format....')

    if pdf.createpdf(menu_dict):
        return 'exit'
    else:
        return 'no work!'

