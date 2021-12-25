import requests,json,time
from perpar_data import oxdata,method_data,dingding_token,contract_list,apikey_MATIC,apikey_FTM,apikey_ETH,apikey_BSC,apikey_AVAX

from FuncData import FuncData
funcdata = FuncData()

class Exercises:
    '''基于各大scan的api开发的监控地址预警系统'''

    def __init__(self):
        self.BASE_URL_BSC = "https://api.bscscan.com/api"
        self.BASE_URL_ETH = "https://api.etherscan.io/api"
        self.BASE_URL_FTM = "https://api.ftmscan.com/api"
        self.BASE_URL_MATIC = "https://api.polygonscan.com/api"
        self.BASE_URL_AVAX = "https://api.snowtrace.io/api"
        self.apikey_FTM = apikey_FTM
        self.apikey_MATIC = apikey_MATIC
        self.wei = 1000000000000000000
        self.apikey_BSC = apikey_BSC
        self.apikey_ETH = apikey_ETH
        self.apikey_AVAX = apikey_AVAX
        self.eth_dingding_token = "" # 可不填



    def split_msg(self,dict):
        '''钉钉拼接格式消息'''

        # 支持debank、bscscan
        debank_link = "https://debank.com/profile/"+ dict['from'] + "/history?chain=bsc&token="
        bscscan_hash_link = "https://bscscan.com/tx/" + dict['hash']
        transfer_link = "https://bscscan.com/address/" + dict['from']
        # 传输的方法的文本
        if dict['method'] in method_data:
            dict['method'] = method_data[dict['method']]

        if  dict['to'] in contract_list.keys():
            dict['to'] = contract_list[dict['to']]

        if  dict['from'] in oxdata.keys():
            dict['from'] = oxdata[dict['from']]


        return "发送方:{send}\n\n to:{recive}。\n\n 方式：{method} \n\n 价值：{value} BNB。\n\n [debank]({link}) \n [区块transfer]({transfer}) \t [区块hash]({hash_link}) \n\n 时间：{time}".\
            format(method=dict['method'],transfer=transfer_link,hash_link=bscscan_hash_link,link=debank_link,value=float(dict['value']) / self.wei,time=self.stampTransformTime(int(dict['time'])), send=dict['from'],recive=dict['to'])

    def split_msg_eth(self,dict):
        '''拼接消息'''

        # self.error_checkout(dict)
        debank_link = "https://debank.com/profile/"+ dict['from'] + "/history?chain=eth&token="
        bscscan_hash_link = "https://etherscan.io/tx/" + dict['hash']
        transfer_link = "https://etherscan.io/address/" + dict['from']
        opensea_link = "https://opensea.io/" + dict['from'] + "?tab=activity"
        # 传输的方法的文本
        if dict['method'] in method_data:
            dict['method'] = method_data[dict['method']]

        if  dict['to'] in contract_list.keys():
            dict['to'] = contract_list[dict['to']]

        if  dict['from'] in oxdata.keys():
            dict['from'] = oxdata[dict['from']]

        return "发送方:{send}\n\n to:{recive}。\n\n 方式：{method} \n\n 价值：{value} ETH。\n\n [debank]({link}) \n [区块transfer]({transfer}) \t [区块hash]({hash_link}) \t [opensea]({open_link}) \n\n 时间：{time}".\
            format(method=dict['method'],transfer=transfer_link,hash_link=bscscan_hash_link,link=debank_link,open_link=opensea_link,value=float(dict['value']) / self.wei,time=self.stampTransformTime(int(dict['time'])), send=dict['from'],recive=dict['to'])



    def split_msg_ftm(self,dict):
        '''拼接消息'''
        cur_from = ''
        cur_to = ''
        # self.error_checkout(dict)
        debank_link = "https://debank.com/profile/"+ dict['from'] + "/history?chain=ftm&token="
        bscscan_hash_link = "https://ftmscan.com/tx/" + dict['hash']
        transfer_link = "https://ftmscan.com/address/" + dict['from']
        if  dict['to'] in oxdata.keys():
            cur_to = oxdata[dict['to']]
        else:
            cur_to = dict['to']

        if  dict['from'] in oxdata.keys():
            cur_from = oxdata[dict['from']]
        else:
            cur_from = dict['from']


        return "操作方:{send}\n\n 操作:{recive}。\n\n 价值：{value} FTM。\n\n [debank]({link})\t [区块transfer]({transfer}) \t [区块hash]({hash_link}) \n\n 时间：{time}".format(transfer=transfer_link,hash_link=bscscan_hash_link,link=debank_link,value=float(dict['value']) / self.wei,time=self.stampTransformTime(int(dict['time'])),send=cur_from,recive=cur_to)

    def split_msg_matic(self,dict):
        '''拼接消息'''
        cur_from = ''
        cur_to = ''
        # self.error_checkout(dict)
        debank_link = "https://debank.com/profile/"+ dict['from'] + "/history?chain=matic&token="
        bscscan_hash_link = "https://polygonscan.com/tx/" + dict['hash']
        transfer_link = "https://polygonscan.com/address/" + dict['from']
        if  dict['to'] in oxdata.keys():
            cur_to = oxdata[dict['to']]
        else:
            cur_to = dict['to']

        if  dict['from'] in oxdata.keys():
            cur_from = oxdata[dict['from']]
        else:
            cur_from = dict['from']


        return "操作方:{send}\n\n 操作:{recive}。\n\n 价值：{value} Matic。\n\n [debank]({link})\t [区块transfer]({transfer}) \t [区块hash]({hash_link}) \n\n 时间：{time}".format(transfer=transfer_link,hash_link=bscscan_hash_link,link=debank_link,value=float(dict['value']) / self.wei,time=self.stampTransformTime(int(dict['time'])),send=cur_from,recive=cur_to)

    def split_msg_avax(self,dict):
        '''拼接消息'''
        cur_from = ''
        cur_to = ''
        # self.error_checkout(dict)
        debank_link = "https://debank.com/profile/"+ dict['from'] + "/history?chain=avax&token="
        bscscan_hash_link = "https://snowtrace.io/tx/" + dict['hash']
        transfer_link = "https://snowtrace.io/address/" + dict['from']
        if  dict['to'] in oxdata.keys():
            cur_to = oxdata[dict['to']]
        else:
            cur_to = dict['to']

        if  dict['from'] in oxdata.keys():
            cur_from = oxdata[dict['from']]
        else:
            cur_from = dict['from']


        return "操作方:{send}\n\n 操作:{recive}。\n\n 价值：{value} AVAX。\n\n [debank]({link})\t [区块transfer]({transfer}) \t [区块hash]({hash_link}) \n\n 时间：{time}".format(transfer=transfer_link,hash_link=bscscan_hash_link,link=debank_link,value=float(dict['value']) / self.wei,time=self.stampTransformTime(int(dict['time'])),send=cur_from,recive=cur_to)


    def dingding_warn(self,dict,tag=None):
        '''钉钉消息推送'''
        headers = {'Content-Type': 'application/json;charset=utf-8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36'}
        api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % dingding_token
        eth_dingding_token = dingding_token if self.eth_dingding_token == "" else self.eth_dingding_token
        if tag == self.apikey_FTM:
            final_text = self.split_msg_ftm(dict)
        elif tag == "error":
            final_text = dict
        elif tag == self.apikey_MATIC:
            final_text = self.split_msg_matic(dict)
        elif tag == self.apikey_ETH:
            api_url = "https://oapi.dingtalk.com/robot/send?access_token=%s" % eth_dingding_token
            final_text = self.split_msg_eth(dict)
        elif tag == self.apikey_BSC:
            final_text = self.split_msg(dict)
        elif tag == self.apikey_AVAX:
            final_text = self.split_msg_avax(dict)

        json_text = {
            "msgtype": "markdown",
            "at": {
                "atMobiles": [
                    "11111"
                ],
                "isAtAll": False
            },
            "markdown": {
                "title": "预警",
                "text":final_text
            }
        }
        res = requests.post(api_url, json.dumps(json_text), headers=headers).content
        return res

    def stampTransformTime(self,timestamp):
        '''10位时间戳转为时间'''
        time_local = time.localtime(timestamp)
        return time.strftime("%Y-%m-%d %H:%M:%S", time_local)




    def _get_txlist_api(self,offset,address,type_api):
        '''封装scan中 txlist接口
            @param int offset：当前地址最近几条信息
            @param address ：监控的地址
            @param type_api: 关于链的类型。传入对应链的api_key。例如 apikey_BSC
        '''
        params = {
            'module': 'account',
            'action': 'txlist',
            "startblock":0,
            "endblock":99999999,
            "page":1,
            "offset":offset,
            "sort":'desc',
            'address': address,
            'apikey': type_api
        }
        url = ""
        if type_api == self.apikey_BSC:
            url = self.BASE_URL_BSC
        elif type_api == self.apikey_ETH:
            url = self.BASE_URL_ETH
        elif type_api == self.apikey_FTM:
            url = self.BASE_URL_FTM
        elif type_api == self.apikey_MATIC:
            url = self.BASE_URL_MATIC
        elif type_api == self.apikey_AVAX:
            url = self.BASE_URL_AVAX
        try:
            res = requests.get(url, params)
            return res.json()
        except Exception as e:
            if str(e).find("443") != -1:  # 网络错误不用报错
                return 443
            
    # ---- API接口封装  ------

    def get_recent_tx(self,address,rotate_count=0):
        '''获取最新交易信息'''
        apikey_list = [self.apikey_ETH,self.apikey_BSC,self.apikey_FTM,self.apikey_MATIC,self.apikey_AVAX]
        for item in apikey_list:
            res = self._get_txlist_api(2, address,item)
            if res == 443 and rotate_count < 10:  # 网络问题并且20次都访问都是443则报错停止运行
                rotate_count += 1
                time.sleep(2)
                self.get_recent_tx(address,rotate_count)

            elif 'status' in res and res['status'] == '1' and len(res['result']) > 1:

                first_mes = res['result'][0]
                second_mes = res['result'][1]
                if first_mes['blockNumber'] not in funcdata.get_block_list(item) and time.time() - float(first_mes['timeStamp'])  < 3600 and float(first_mes['timeStamp']) - float(second_mes['timeStamp']) > 300:
                    method = first_mes['input'][0:10]
                    self.dingding_warn({"time":first_mes['timeStamp'],"hash":first_mes['hash'],"value":first_mes['value'],"from":first_mes['from'],"to":first_mes['to'],'method':method},item)
                    funcdata.modify_block_list(str(first_mes['blockNumber']),item)


if __name__ == "__main__":
    ins = Exercises()
    while(True):
        for key in oxdata:
            ins.get_recent_tx(key)
            time.sleep(1)




