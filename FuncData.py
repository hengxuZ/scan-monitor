import json,os

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

    def get_block_list_bsc(self):
        data_json = self._get_json_data()
        return data_json["block_list_bsc"]

    def get_block_list_ftm(self):
        data_json = self._get_json_data()
        return data_json["block_list_ftm"]

    def get_block_list_matic(self):
        data_json = self._get_json_data()
        return data_json["block_list_matic"]

    def get_block_list_eth(self):
        data_json = self._get_json_data()
        return data_json["block_list_eth"]

    def modify_block_list(self,block_number,type):
        '''

        :param type: bsc、ftm、matic
        :return:
        '''
        data_json = self._get_json_data()
        if type == 'bsc':
            data_json['block_list_bsc'].append(block_number)
        elif type == 'ftm':
            data_json['block_list_ftm'].append(block_number)
        elif type == "matic":
            data_json['block_list_matic'].append(block_number)
        elif type == "eth":
            data_json['block_list_eth'].append(block_number)


        self._modify_json_data(data_json)

    def get_hash_list_eth(self):
        data_json = self._get_json_data()
        return data_json["hash_list_eth"]

    def get_hash_list_bsc(self):
        data_json = self._get_json_data()
        return data_json["hash_list_bsc"]

    def get_hash_list_ftm(self):
        data_json = self._get_json_data()
        return data_json["hash_list_ftm"]

    def get_hash_list_matic(self):
        data_json = self._get_json_data()
        return data_json["hash_list_matic"]

    def modify_hash_list(self,hash_number,type):
        '''

        :param type: bsc、ftm、matic
        :return:
        '''
        data_json = self._get_json_data()
        if type == 'bsc':
            data_json['hash_list_bsc'].append(hash_number)
        elif type == 'ftm':
            data_json['hash_list_ftm'].append(hash_number)
        elif type == "matic":
            data_json['hash_list_matic'].append(hash_number)
        elif type == "eth":
            data_json['hash_list_eth'].append(hash_number)

        self._modify_json_data(data_json)

