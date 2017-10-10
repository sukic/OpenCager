# -*- coding: utf-8 -*-
def geocode(api_key,input_csv,output_csv,one_result=0,countrycode=0,add_request=1,no_annotations=1,sleep_sec=0):
    import requests, time
    in_file = open(input_csv,"r")
    out_file = open(output_csv,"w")
    out_file.write('id|query|confidence|type|results_count|lng|lat|formatted|components' + "\n")
    for line in in_file:
        time.sleep(sleep_sec)
        print(line)
        pk = line.split("|")[0]
        query = line.split("|")[1]
        parameters = {"key": api_key,"q": query,"countrycode":countrycode,"add_request":add_request,"no_annotations":no_annotations}
        response = requests.get("https://api.opencagedata.com/geocode/v1/json",params=parameters)
        data = response.json()
        confidence_list = []
        for i in range(0,len(data["results"])):
            if len(data["results"]) == 1:    # na dotaz vratil pouze jeden vysledek
                new_line = ""
                new_line = new_line + str(pk) + '|'
                new_line = new_line + str(data["request"]["query"]) + '|'
                new_line = new_line + str(data["results"][i]["confidence"]) + '|'
                new_line = new_line + str(data["results"][i]["components"]["_type"]) + '|'
                new_line = new_line + str(len(data["results"])) + '|'
                new_line = new_line + str(data["results"][i]["geometry"]["lng"]) + '|'
                new_line = new_line + str(data["results"][i]["geometry"]["lat"]) + '|'
                new_line = new_line + str(data["results"][i]["formatted"]) + '|'
                new_line = new_line + str(data["results"][i]["components"]) + "\n"
                out_file.write(new_line)
            if len(data["results"]) >1 and one_result == 0: # na dotaz vratil vice vysledku a beru vsechny + uvadim jejich pocet
                new_line = ""
                new_line = new_line + str(pk) + '|'
                new_line = new_line + str(data["request"]["query"]) + '|'
                new_line = new_line + str(data["results"][i]["confidence"]) + '|'
                new_line = new_line + str(data["results"][i]["components"]["_type"]) + '|'
                new_line = new_line + str(len(data["results"])) + '|'
                new_line = new_line + str(data["results"][i]["geometry"]["lng"]) + '|'
                new_line = new_line + str(data["results"][i]["geometry"]["lat"]) + '|'
                new_line = new_line + str(data["results"][i]["formatted"]) + '|'
                new_line = new_line + str(data["results"][i]["components"]) + "\n"
                out_file.write(new_line)
            if len(data["results"]) >1 and one_result == 1:  # na dotaz vratil vice vysledku, zjistuji max confidence a kolik jich je celkem a kolik s max confidence
                confidence_list.append(int(data["results"][i]["confidence"]))
                confidence_max = max(confidence_list)
                confidence_max_list = []
                for c in confidence_list:
                    if c == confidence_max:
                        confidence_max_list.append(c)
                results_count = str(len(data["results"])) + "/" + str(len(confidence_max_list)) # celkem vraceno/vraceno s max confidence
                looper = 1
        for ii in range(0,len(data["results"])): # pokud mam vice vysledku a chci brat jen jeden
            try:
                if looper == 1:
                    if int(data["results"][ii]["confidence"]) == confidence_max:
                        looper = 0
                        new_line = ""
                        new_line = new_line + str(pk) + '|'
                        new_line = new_line + str(data["request"]["query"]) + '|'
                        new_line = new_line + str(data["results"][ii]["confidence"]) + '|'
                        new_line = new_line + str(data["results"][ii]["components"]["_type"]) + '|'
                        new_line = new_line + results_count + '|'
                        new_line = new_line + str(data["results"][ii]["geometry"]["lng"]) + '|'
                        new_line = new_line + str(data["results"][ii]["geometry"]["lat"]) + '|'
                        new_line = new_line + str(data["results"][ii]["formatted"]) + '|'
                        new_line = new_line + str(data["results"][ii]["components"]) + "\n"
                        out_file.write(new_line)
                    else:
                        pass
            except:
                pass
    in_file.close()
    out_file.close()
        