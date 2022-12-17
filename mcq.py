class questions:
    def __init__(self,prompt,answer):
        self.prompt=prompt
        self.answer=answer
qp=[
    "What colour is the sky?\n(a)Blue\n(b)Green\n(c)Grey\n",
    "What colour is an apple?\n(a)Blue\n(b)Red\n(c)Pink\n",
    "What colour is a banana?\n(a)Blue\n(b)Red\n(c)Yellow\n",
]
question=[
    questions(qp[0],"a"),
    questions(qp[1],"b"),
    questions(qp[2],"c"),
]
def rt(question):
    score=0
    for q in question:
        a=input(q.prompt)
        if a==q.answer:
            score+=1
    print("You got "+str(score)+" questions right out of "+str(len(question))+"!")
rt(question)