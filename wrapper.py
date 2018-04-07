from timeit import default_timer

helper_content = {}
solutions = {}


def check(i):
    global helper_content
    if i in list(helper_content):
        return True
    if int(i) < 1:
        print("\nPlease enter a positive integer.")
    else:
        print("\nThis problem was not yet solved and described.")
    return False


def run(i):
    if check(i):
        loaded_problem = __import__("Problem" + i)
        start = default_timer()
        solution = loaded_problem.run()
        time_needed = default_timer() - start
        correct = True
        if i not in solutions:
            solutions[i] = solution
            with open("wrapper_solutions.txt", "a") as f:
                f.write(i + "||" + str(solution) + "\n")
        if solution != solutions[i]:
            print("\nThe solution file was somehow changed. Please, download the files again.")
            correct = False
        if not correct:
            if not input("Type anything and press enter to display the result anyway: "):
                print("\nSkipping...")
                return None
        print("\n Solution:", solution)
        print(" Duration:", time_needed)
        if not correct:
            print("\nWARNING: The solution was not saved!")
    return None


def help(i):
    if check(i):
        print("\n", helper_content[i], sep="")
    return None


def retrieve_solution(i):
    if check(i):
        if i in solutions:
            print("\n Solution:", solutions[i])
        else:
            print("\nThis problem was solved and described, but the solution has not yet been saved.")
            print("Input the same number without the exclamation mark in order to calculate the solution.")
    return None


def prep_the_list():
    global helper_content, solutions
    with open("wrapper_descriptions.txt", "r") as f:
        content = f.read()[:-1].split("||\n\n")
        for i in content:
            i = i.split("|")
            helper_content[i[0]] = i[1]
    with open("wrapper_solutions.txt", "r") as g:
        content = g.read().splitlines()
        for i in content:
            i = i.split("||")
            solutions[i[0]] = int(i[1])
    return None


prep_the_list()
print("""\nEnter the problem number if you want to run the program and see its solution.
If you want to see my written description of the algorithm instead, add the '?' sign after the number.
If you only want to see the solution without calculating it on your machine, add the '!' sign after the number.\n""")
while True:
    print("===============================================")
    vnos = input("Enter the problem number: ")
    if vnos == "exit" or vnos == "":
        break
    elif vnos[-1] == "?":
        help(vnos[:-1].zfill(3))
    elif vnos[-1] == "!":
        retrieve_solution(vnos[:-1].zfill(3))
    else:
        run(vnos.zfill(3))

    print("\nDone!")
    print("===============================================\n")
