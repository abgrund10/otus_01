import datetime
import json
import re


class ParceFile:
    parced_dictionary = {}
    parced_dictionary_final = []

    def parsing_file(filename):
        methods_and_amount = {}
        methods = ("GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE")
        # parsing file
        with open(filename, 'r') as f_in:
            for line in f_in.readlines():
                try:
                    s = line.split('"')
                    ParceFile.parced_dictionary.update(
                        {'ip_time': s[0], "request_header_endpoint": s[1], "response_bytes": s[2],
                         "endpoint_full": s[3],
                         "User_Agent": s[5], "duration": s[6]})
                    ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", s[0]).group()
                    try:
                        date = re.search("\d\d\d\d:\d\d:\d\d:\d\d \+\d\d\d\d", s[0]).group()
                    except AttributeError as ex:
                        date = None
                    try:
                        method = re.search(r'(.*?) ', s[1]).group(1)
                    except AttributeError as ex:
                        method = None
                    try:
                        endpoint = re.search(r'/(.*?)HTTP', s[1]).group(1)
                    except AttributeError as ex:
                        endpoint = None
                    try:
                        endpoint_full = s[3]
                    except AttributeError as ex:
                        endpoint_full = None
                    try:
                        duration = s[6].split('\n')[0]
                    except AttributeError as ex:
                        duration = None
                    ParceFile.parced_dictionary_final.append(
                        {'ip': ip, 'date': date, "method": method, "endpoint": endpoint,
                         "endpoint_full": endpoint_full, "duration": duration})
                except IndexError as ex:
                    print(ex)

            ##### shared function to calc item in parsed dict
            def calc_amount_of_item(key, value):
                request_amount = 0
                for single_line in ParceFile.parced_dictionary_final:
                    if single_line[key] == value:
                        request_amount += 1
                return request_amount

            # calc amount of requests per its name:
            for row in methods:
                methods_and_amount[row] = calc_amount_of_item("method", row)

            # sort list of methods by its occurrence
            requests_sorted = sorted(methods_and_amount, key=methods_and_amount.get, reverse=True)
            methods_and_amount_sorted = {}
            for line in requests_sorted:
                methods_and_amount_sorted[line] = methods_and_amount[line]

            # print("Amount of request headers are : " + str(methods_and_amount))

            # calc total_requests
            total_requests = sum(value for value in methods_and_amount.values())

        calc_list_ip = {}
        top_3_ip = []

        for single_line in ParceFile.parced_dictionary_final:
            dd = calc_amount_of_item("ip", single_line["ip"])
            calc_list_ip.update({single_line["ip"]: dd})

        sorted_keys = sorted(calc_list_ip, key=calc_list_ip.get, reverse=True)
        for i in range(3):
            top_3_ip.append({sorted_keys[i]: calc_list_ip[sorted_keys[i]]})

        def sort_key(parced_dictionary_final):
            return parced_dictionary_final['duration']

        top_3_duration = []
        ParceFile.parced_dictionary_final.sort(key=sort_key, reverse=True)
        for i in range(3):
            top_3_duration.append({"ip": top_3_ip[i],
                                   "date": ParceFile.parced_dictionary_final[i]["date"],
                                   "method": ParceFile.parced_dictionary_final[i]["method"],
                                   "url": ParceFile.parced_dictionary_final[i]["endpoint"],
                                   "duration": ParceFile.parced_dictionary_final[i]["duration"]})

        new_json = {"top_ips": top_3_ip, "top_longest": top_3_duration,
                    "total_stat": methods_and_amount_sorted, "total_requests": total_requests}
        print(json.dumps(new_json, indent=4))

        new_filename = str(filename).replace('.log', '') + '_' + datetime.datetime.now().strftime(
            '%d-%m-%Y_%H.%M.%S')
        with open(f"results_of_{new_filename}.json".format(filename=new_filename), "w") as f:
            f.write(json.dumps(new_json, indent=4))
