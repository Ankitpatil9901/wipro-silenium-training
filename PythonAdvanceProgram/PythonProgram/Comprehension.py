#comprehensions - create this using a single line of a code instead of loops
#sntax
# expression for item in iterable if condition]

# square of a num
sq = [x**2 for x in range(1-6)]
print(sq)

#with condition

even_no=[x for x in range(10) if x%2 ==0 ]
print(even_no)

#dict
# k and v are key and value

salary = {"A":50000, "B":80000, "C": 548422}
update_sal={k : v+0.1 * v for k , v in salary.items()}
print(update_sal)

#filtering of dict

emp={
    "Ankit":"Active",
    "Amit":"InActive"
}
act_emp={ k : v for k, v in emp.items() if v=="Active"}
print(act_emp)

# set comprehensions
sqs = {x**2 for x in range(1,6) }
print(sqs)

#with the condition

even_no = { x for x in range(10) if x%2 ==0}
print(even_no)
