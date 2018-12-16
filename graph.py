#Graph
import matplotlib.pyplot as plt

emp_ages=[22,23,24,25,20,60,19,22,87,54,32,41,33,25,56,19]
no_emp=[0,10,20,30,40,50,60]

plt.hist(emp_ages,no_emp,histtype="bar",rwidth=0.8,color="red")
plt.xlabel("employee ages")
plt.ylabel("no.of employees")
plt.title("sathyabama start up")
plt.legend()
plt.show()