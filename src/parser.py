import datetime
import subprocess
import functools

stdout, stderr = subprocess.Popen("ps aux", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
result = stdout.decode()

get_users_check, stderr2 = subprocess.Popen("awk -F: '{ print $1}' /etc/passwd", shell=True, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE).communicate()
get_users_check = get_users_check.decode()

unique_usernames = set()
unique_usernames_final = set()
list_of = []
list_of2 = {}
memmory_usage = 0.0
cpu_usage = 0.0
list_of_users_check = []
user_processes_dict = {}

# create list of processes per user without first and last rows
for elem in str(result).split("\n"):
    items = elem.split()
    list_of.append(items)
list_of.remove(list_of[0])
list_of.remove(list_of[len(list_of) - 1])

""" calc processes for current_user """


def calc_users_processes(user):
    user_process_amount = 0
    for user_pr in list_of:
        if user_pr[0] == user:
            user_process_amount += 1
    return user_process_amount


"""fill dictionary of users & amount of their processes """
for row in list_of:
    unique_usernames.add(row[0])
    user_processes_dict[row[0]] = calc_users_processes(row[0])

""" create list of users from get_users_check  to compare in future """
for elem2 in str(get_users_check).split("\\n"):
    items = elem2.split()
    list_of_users_check.append(items)
    new_name2 = str(elem2).replace("   ", "")

"""
check if users are in the list_of_users_check list
if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, list_of_users_check, unique_usernames), True):
    print("The lists l1 and l2 are the same")
else:
            print("The lists l1 and l2 are not the same")
"""


def calculate_item_in_table(item_id, listed_array):
    column = 0
    for tempora in listed_array:
        column = round(column, 2) + round(float(tempora[item_id]), 2)
    return column


def max_val_in_table(item_id, listed_array):
    max_val = 0.0
    for tempora in listed_array:
        if max_val < float(tempora[item_id]):
            max_val = float(tempora[item_id])
    return max_val


def find_proc_by_val(val, item_id, listed_array):
    for tempora in listed_array:
        if val == float(tempora[item_id]):
            break
    return listed_array[item_id][0]


cpu_usage = calculate_item_in_table(2, list_of[:len(list_of) - 2])
cpu_usage_max = max_val_in_table(2, list_of[:len(list_of) - 2])
memmory_usage = calculate_item_in_table(3, list_of[:len(list_of) - 2])
memmory_usage_max = max_val_in_table(3, list_of[:len(list_of) - 2])

""" get  name of current user in case if needed """
current_user = str(subprocess.check_output('whoami', shell=True)).split("\\n")[0]
current_user = current_user.split("'")[1]

print("Пользователи системы:" + str(unique_usernames))
print("Процессов запущено:" + str(len(list_of)))
print("Пользовательских процессов:" + str(user_processes_dict))

print("Всего памяти используется:" + str(memmory_usage) + '% memmory_usage')
print("Всего CPU используется:" + str(cpu_usage) + '% CPU')
print("Больше всего памяти использует:" + str(memmory_usage_max))
print("Больше всего CPU использует:" + str(cpu_usage_max))

filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
name = filename + '.txt'
with open(name, "w") as file:
    file.write("Пользователи системы:" + str(unique_usernames_final) + "\n" +
               "Процессов запущено:" + str(max_val_in_table(1, list_of[:len(list_of) - 2])) + "\n" +
               "Пользовательских процессов:" + str(user_processes_dict) + "\n" +
               "Всего памяти используется:" + str(memmory_usage) + '% memmory_usage' + "\n" +
               "Всего CPU используется:" + str(cpu_usage) + '% CPU' + "\n" +
               "Больше всего памяти использует:" + str(memmory_usage_max) + "\n" +
               "Больше всего CPU использует:" + str(cpu_usage_max))
