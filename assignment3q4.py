# assignment3print("\nQuestion 4")

grade_point=int(input("enter grade point:"))
dic={10:"your grade is 'A+' and oustanding performance.",
     9:"your grade is 'A' and excellent performnace.",
     8:"your grade is 'B+' and very good performance.",
     7:"your grade is 'B' and good performance.",
     6:"your grade is 'C+' and average performance.",
     5:"your grade is 'C' and below average performance.",
     4:"your grade is 'D' and poor performance.",}
#Applying conditions for correct grade range
if 4<=grade_point<=10:
          statement=dic.get(grade_point)
          print(statement)
else:
         print("\nError\nPlease enter grade in range [4,10]") 
     
