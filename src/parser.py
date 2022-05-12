import datetime
import subprocess
import re

result = subprocess.Popen("ps aux", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

unique_usernames = set()
unique_usernames_final = set()
list_of = []
list_of2 = {}
memmory_usage = 0.0
cpu_usage = 0.0


def remove_epmty_vals(items):
    for item in items:
        if item == '':
            items.remove('')
    return items


# create list of unique usernames
for elem in str(result).split("\\n"):
    items = elem.split(" ")
    remove_epmty_vals(remove_epmty_vals(remove_epmty_vals(items)))
    list_of.append(items)
    new_name2 = str(elem).replace("   ", "")
    unique_usernames.add(str(re.findall(r"\D+", new_name2)[0]).replace(" ", ""))
list_of.remove(list_of[0])


def calculate_item_in_table(id, listed_array):
    column = 0
    for tempora in listed_array:
        column = round(column, 2) + round(float(tempora[id]), 2)
    return column


def max_val_in_table(id, listed_array):
    max_val = 0.0
    for tempora in listed_array:
        if max_val < float(tempora[id]):
            max_val = float(tempora[id])
    return max_val


def find_proc_by_val(val, id, listed_array):
    for tempora in listed_array:
        if val == float(tempora[id]):
            break
    return listed_array[id][0]


cpu_usage = calculate_item_in_table(2, list_of[:len(list_of) - 2])
cpu_usage_max = max_val_in_table(2, list_of[:len(list_of) - 2])
memmory_usage = calculate_item_in_table(3, list_of[:len(list_of) - 2])
memmory_usage_max = max_val_in_table(3, list_of[:len(list_of) - 2])

print(cpu_usage_max)
print(cpu_usage)
print(memmory_usage_max)
print(memmory_usage)

# get  name of current user in case if needed
current_user = str(subprocess.check_output('whoami', shell=True)).split("\\n")[0]
current_user = current_user.split("'")[1]


# calc processes for current_user
def calc_users_processes(current_user):
    user_process_amount = 0
    for user_pr in list_of[0:len(list_of) - 2]:
        if user_pr[0] == current_user:
            user_process_amount += 1
    return user_process_amount


user_processes_dict = {}

# create set with unique and correct values
for itz in unique_usernames:
    if "b'" not in itz:
        unique_usernames_final.add(itz)

for name in unique_usernames_final:
    user_processes_dict[name] = calc_users_processes(name)

print("Пользователи системы:" + str(unique_usernames_final))
print("Процессов запущено:" + str(max_val_in_table(1, list_of[:len(list_of) - 2])))
print("Пользовательских процессов:" + str(user_processes_dict))

print("Всего памяти используется:" + str(memmory_usage) + '% memmory_usage')
print("Всего CPU используется:" + str(cpu_usage) + '% CPU')
print("Больше всего памяти использует:" + str(find_proc_by_val(memmory_usage_max, 3, list_of[:len(list_of) - 2])))
print("Больше всего CPU использует:" + str(find_proc_by_val(cpu_usage_max, 2, list_of[:len(list_of) - 2])))

filename = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
name = filename + '.txt'
with open(name, "w") as file:
    file.write("Пользователи системы:" + str(unique_usernames_final) + "\n")
    file.write("Процессов запущено:" + str(max_val_in_table(1, list_of[:len(list_of) - 2])) + "\n")
    file.write("Пользовательских процессов:" + str(user_processes_dict) + "\n")
    file.write("Всего памяти используется:" + str(memmory_usage) + '% memmory_usage' + "\n")
    file.write("Всего CPU используется:" + str(cpu_usage) + '% CPU' + "\n")
    file.write("Больше всего памяти использует:" + str(
        find_proc_by_val(memmory_usage_max, 3, list_of[:len(list_of) - 2])) + "\n")
    file.write("Больше всего CPU использует:" + str(find_proc_by_val(cpu_usage_max, 2, list_of[:len(list_of) - 2])))
