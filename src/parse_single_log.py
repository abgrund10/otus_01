import datetime
import json
import os
import re
import subprocess
import functools


class Parsing_file:
    def __int__(self, filename):
        filename = filename


    #filename = 'access1.log'
    methods_and_amount = {}
    methods = ("GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE")

    # parsing file
    parced_dictionary = {}
    parced_dictionary_final = []



    with open(f'{filename}'.format(filename=Parsing_file().filename), 'r') as f_in:
            for line in f_in.readlines():
                try:
                    s = line.split('"')
                    parced_dictionary.update(
                        {'ip_time': s[0], "request_header_endpoint": s[1], "response_bytes": s[2], "endpoint_full": s[3],
                         "User_Agent": s[5], "duration": s[6]})
                    ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s[0]).group()
                    date = re.search("\d\d\d\d:\d\d:\d\d:\d\d \+\d\d\d\d", s[0]).group()
                    method = re.search(r'(.*?) ', s[1]).group(1)
                    endpoint = re.search(r'/(.*?)HTTP', s[1]).group(1)
                    endpoint_full = s[3]
                    duration = s[6].split('\n')[0]
                    parced_dictionary_final.append({'ip': ip, 'date': date, "method": method, "endpoint": endpoint,
                                                    "endpoint_full": endpoint_full, "duration": int(duration)})
                except IndexError as ex:
                    print(ex)


        # calc amount of requests per its name

        ##### shared function to calc item in parsed dict
        def calc_amount_of_item(key, value):
            request_amount = 0
            for single_line in parced_dictionary_final:
                if single_line[key] == value:
                    request_amount += 1
            return request_amount


        for row in methods:
            methods_and_amount[row] = calc_amount_of_item("method", row)

        # sort list of methods by its occurance
        requests_sorted = sorted(methods_and_amount, key=methods_and_amount.get, reverse=True)
        methods_and_amount_sorted = {}
        for line in requests_sorted:
            methods_and_amount_sorted[line] = methods_and_amount[line]

        # print("Amount of request headers are : " + str(methods_and_amount))

        # calc total_requests
        total_requests = sum(value for value in methods_and_amount.values())

        # calc top 3 addresses
        calc_list_ip = {}
        top_3_ip = []

        for single_line in parced_dictionary_final:
            dd = calc_amount_of_item("ip", single_line["ip"])
            calc_list_ip.update({single_line["ip"]: dd})

        sorted_keys = sorted(calc_list_ip, key=calc_list_ip.get, reverse=True)
        for i in range(3):
            top_3_ip.append({sorted_keys[i]: calc_list_ip[sorted_keys[i]]})

        # print("List of top 3 ip : " + str(top_3_ip))

        # calc 3 lognest requests
        top_3_duration = []


        def sort_key(parced_dictionary_final):
            return parced_dictionary_final["duration"]


        parced_dictionary_final.sort(key=sort_key, reverse=True)

        for i in range(3):
            top_3_duration.append({"ip": sorted_keys[i], "date": parced_dictionary_final[i]["date"],
                                   "method": parced_dictionary_final[i]["method"],
                                   "url": parced_dictionary_final[i]["endpoint"],
                                   "duration": parced_dictionary_final[i]["duration"]})

        # print("3 longest requests : " + str(top_3_duration))

        new_json = {"top_ips": top_3_ip, "top_longest": top_3_duration, "total_stat": methods_and_amount_sorted,
                "total_requests": total_requests}
        # print(json.dumps(file, indent=4))

        new_filename = filename.replace('.log', '') + '_' + datetime.datetime.now().strftime('%d-%m-%Y_%H.%M.%S')
        with open(f"results_of_{new_filename}.json".format(filename=new_filename), "w") as f:
            f.write(json.dumps(new_json, indent=4))
