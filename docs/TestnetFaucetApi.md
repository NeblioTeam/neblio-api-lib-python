# neblio-api.TestnetFaucetApi

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testnet_get_faucet**](TestnetFaucetApi.md#testnet_get_faucet) | **GET** /testnet/faucet | Withdraws testnet NEBL to the specified address


# **testnet_get_faucet**
> GetFaucetResponse testnet_get_faucet(address, amount=amount)

Withdraws testnet NEBL to the specified address

Withdraw testnet NEBL to your Neblio Testnet address. By default amount is 1500000000 or 15 NEBL and has a max of 50 NEBL. Only 2 withdrawals allowed per 24 hour period. 

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetFaucetApi()
address = 'address_example' # str | Your Neblio Testnet Address
amount = 3.4 # float | Amount of NEBL to withdrawal in satoshis (optional)

try:
    # Withdraws testnet NEBL to the specified address
    api_response = api_instance.testnet_get_faucet(address, amount=amount)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetFaucetApi->testnet_get_faucet: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Your Neblio Testnet Address | 
 **amount** | **float**| Amount of NEBL to withdrawal in satoshis | [optional] 

### Return type

[**GetFaucetResponse**](GetFaucetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

