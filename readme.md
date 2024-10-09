
Note - 3 members of staff have been created for the purposes of grading the assignment:

    id - 1, username - john, password - johnpass, firstname - John, lastname - Gonzales, department - DCIT
    id - 2, username - james, password - jamespass, firstname - James, lastname - Laurence, department - DCIT
    id - 3, username - jane, password - janepass,firstname - Jane, lastname - Hnederson, department - DCIT


Commands:


App Group - student


    1) add - Adds a new student

       use - flask student add firstname lastname major

       example - flask student add christin beck finance    creates student(christin, beck, finance)
                                                            and adds it to the student table



    2) review - Adds a review to a student by a member of staff

       use - flask student review studentID staffID, text

       example - flask student add 1 1 good     creates review(1, 1, good)               
                                                which is the review "good" for christin beck(1) by John Gonzales(1) 



    3) search - Looks for and returns a specific student

       use - flask student search studentID

       example - flask student search 1     looks for christin beck(1) and returns it 



    4) viewReviews - View all the reviews for a specific student

       use - flask stduent viewReviews studentID

       example - flask student viewReviews 1    displays all the reviews for christin beck(1) along
                                                with the member of staff who reviewed them
