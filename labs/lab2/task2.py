#   (II)In a company ,worker efficiency is determined on the basis of the time required for a worker 
#   to complete a particular job.If the time taken by the worker is between 2-3 hours then the worker 
#   is said to be highly efficient. If the time required by the worker is between 3-4hours,then the worker 
#   is ordered to improve speed. If the time taken is between 4-5 hours ,the worker is given training to 
#   improve his speed ,and if the time taken by the worker is more than 5 hours ,then the worker haas 
#   to leave the company, If the time taken by the worker is input through the keyboard,find the 
#   efficiency of the worker.


time = float(input("Enter your time to complete that particular task: "))

statement=""



if(time>=2 and time<3):
    statement="wow! you're highly efficient!"

elif(time>=3 and time<4):
    statement=" you're good! but you need to improve your speed!"

elif(time>=4 and time<=5):
    statement="you're slow!  you would be given training to improve your speed! "

elif(time>5):
    statement="Sorry to say but you have to leave this company!"

print(statement)
