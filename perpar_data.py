# pc端钉钉申请的token
dingding_token = ""
# 填写需要监控的地址
oxdata = {}
#接收方的智能合约地址，方便查阅
contract_list = {
    "0x10ed43c718714eb63d5aa57b78b54704e256024e":"pancake routerV2",
    "0x95c78222b3d6e262426483d42cfa53685a67ab9d":"Venus: vBUSD Token",
    "0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31":"Metamask: Swap Router",
    "0xe9e7cea3dedca5984780bafc599bd69add087d56":"Binance: BUSD Stablecoin",
    "0x8f8dd7db1bda5ed3da8c9daf3bfa471c12d58486":"Dodoex: V2 Proxy"
}
# 当前transfer的方式
method_data = {
    "0x095ea7b3":"Approve",
    "0x7ff36ab5":"Swap Exact ETH For Tokens",
    "0x18cbafe5":"Swap Exact Token For ETH",
    "0x":"Transfer",
    "0xf305d719":"Add Liquiity ETH",
    "0xfb3bdb41":"Swap ETH For Exact Tokens"
}