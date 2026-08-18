"""
file_read
"""
from OOP_Advanced_data_practice1 import Record
import json
from typing import List
class FileReader:
    def read_data(self):
        pass
class txtFileReader(FileReader):
    def __init__(self,path):
        self.path = path
    def read_data(self) -> List[Record]:
        record_list : List[Record] = []
        f = open(self.path,"r",encoding="utf-8")
        for line in f.readlines():
            line = line.strip()
            line = line.split(",")
            record = Record(line[0],line[1],int(line[2]),line[3])
            record_list.append(record)
        f.close()
        return record_list


class jsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path
    def read_data(self) -> List[Record]:
        f = open(self.path,"r",encoding="utf-8")
        record_list : List[Record] = []
        for line in f.readlines():
            line = json.loads(line)
            record = Record(line["date"], line["order_id"], int(line["money"]), line["province"])
            record_list.append(record)
        f.close()
        return record_list


if __name__ =="__main__":
    txt = txtFileReader("2011年1月销售数据.txt")
    res = txt.read_data()
    for record in res:
        print(record)
    print("-----------------")
    js = jsonFileReader("2011年2月销售数据JSON.txt")
    res = js.read_data()
    for record in res:
        print(record)




