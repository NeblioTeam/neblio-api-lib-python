# neblioapi.JSONRPCApi

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**r_pc**](JSONRPCApi.md#r_pc) | **POST** / | Send a JSON-RPC call to a localhost neblio-Qt or nebliod node


# **r_pc**
> RpcResponse r_pc(rpc_request)

Send a JSON-RPC call to a localhost neblio-Qt or nebliod node

Call any Neblio RPC command from the Neblio API libraries. Useful for signing transactions with a local node and other functions. Will not work from this page due to CORS restrictions. Requires a node to be running locally at 127.0.0.1 - Use port 16326 for testnet.

### Example

* Basic Authentication (rpcAuth):
```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint
configuration = neblioapi.Configuration()
# Configure HTTP basic authorization: rpcAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = neblioapi.JSONRPCApi(neblioapi.ApiClient(configuration))
rpc_request = neblioapi.RpcRequest() # RpcRequest | 

try:
    # Send a JSON-RPC call to a localhost neblio-Qt or nebliod node
    api_response = api_instance.r_pc(rpc_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JSONRPCApi->r_pc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rpc_request** | [**RpcRequest**](RpcRequest.md)|  | 

### Return type

[**RpcResponse**](RpcResponse.md)

### Authorization

[rpcAuth](../README.md#rpcAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

