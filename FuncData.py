import json,os
from perpar_data import apikey_MATIC,apikey_FTM,apikey_ETH,apikey_BSC,apikey_AVAX
data_path = os.getcwd()+ "/storage_data.json"

class FuncData:
    '''封装json读写操作'''
    def __init__(self):
        pass


    def _get_json_data(self):
        '''读取json文件'''
        tmp_json = {}
        with open(data_path, 'r') as f:
            tmp_json = json.load(f)
            f.close()
        return tmp_json


    def _modify_json_data(self,data):
        '''修改json文件'''
        with open(data_path, "w") as f:
            f.write(json.dumps(data))
        f.close()

    ####------下面为输出函数--------####

    def get_block_list(self,type):
        data_json = self._get_json_data()
        if type == apikey_AVAX:
            return data_json["block_list_avax"]
        elif type == apikey_ETH:
            return data_json['block_list_eth']
        elif type == apikey_BSC:
            return data_json["block_list_bsc"]
        elif type == apikey_MATIC:
            return data_json["block_list_matic"]
        elif type == apikey_FTM:
            return data_json["block_list_ftm"]



    def modify_block_list(self,block_number,type):
        '''

        :param type: bsc、ftm、matic
        :return:
        '''
        data_json = self._get_json_data()
        if type == apikey_BSC:
            data_json['block_list_bsc'].append(block_number)
        elif type == apikey_FTM:
            data_json['block_list_ftm'].append(block_number)
        elif type == apikey_MATIC:
            data_json['block_list_matic'].append(block_number)
        elif type == apikey_ETH:
            data_json['block_list_eth'].append(block_number)
        elif type == apikey_AVAX:
            data_json['block_list_avax'].append(block_number)

        self._modify_json_data(data_json)



