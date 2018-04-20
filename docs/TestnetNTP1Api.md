# swagger_client.TestnetNTP1Api

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testnet_broadcast_tx**](TestnetNTP1Api.md#testnet_broadcast_tx) | **POST** /testnet/ntp1/broadcast | Broadcasts a signed raw transaction to the network
[**testnet_burn_token**](TestnetNTP1Api.md#testnet_burn_token) | **POST** /testnet/ntp1/burntoken | Builds a transaction that burns an NTP1 Token
[**testnet_get_address_info**](TestnetNTP1Api.md#testnet_get_address_info) | **GET** /testnet/ntp1/addressinfo/{address} | Information On a Neblio Address
[**testnet_get_token_holders**](TestnetNTP1Api.md#testnet_get_token_holders) | **GET** /testnet/ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token
[**testnet_get_token_id**](TestnetNTP1Api.md#testnet_get_token_id) | **GET** /testnet/ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token
[**testnet_get_token_metadata_of_issuance**](TestnetNTP1Api.md#testnet_get_token_metadata_of_issuance) | **GET** /testnet/ntp1/tokenmetadata/{tokenid} | Get Issuance Metadata of Token
[**testnet_get_token_metadata_of_utxo**](TestnetNTP1Api.md#testnet_get_token_metadata_of_utxo) | **GET** /testnet/ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token
[**testnet_get_transaction_info**](TestnetNTP1Api.md#testnet_get_transaction_info) | **GET** /testnet/ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction
[**testnet_issue_token**](TestnetNTP1Api.md#testnet_issue_token) | **POST** /testnet/ntp1/issue | Builds a transaction that issues a new NTP1 Token
[**testnet_send_token**](TestnetNTP1Api.md#testnet_send_token) | **POST** /testnet/ntp1/sendtoken | Builds a transaction that sends an NTP1 Token


# **testnet_broadcast_tx**
> BroadcastTxResponse testnet_broadcast_tx(body)

Broadcasts a signed raw transaction to the network

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
body = swagger_client.BroadcastTxRequest() # BroadcastTxRequest | Object representing a transaction to broadcast

try:
    # Broadcasts a signed raw transaction to the network
    api_response = api_instance.testnet_broadcast_tx(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_broadcast_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BroadcastTxRequest**](BroadcastTxRequest.md)| Object representing a transaction to broadcast | 

### Return type

[**BroadcastTxResponse**](BroadcastTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_burn_token**
> BurnTokenResponse testnet_burn_token(body)

Builds a transaction that burns an NTP1 Token

Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
body = swagger_client.BurnTokenRequest() # BurnTokenRequest | Object representing the token to be burned

try:
    # Builds a transaction that burns an NTP1 Token
    api_response = api_instance.testnet_burn_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_burn_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BurnTokenRequest**](BurnTokenRequest.md)| Object representing the token to be burned | 

### Return type

[**BurnTokenResponse**](BurnTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_address_info**
> GetAddressInfoResponse testnet_get_address_info(address)

Information On a Neblio Address

Returns both NEBL and NTP1 token UTXOs held at the given address. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
address = 'address_example' # str | Neblio Address to get information on.

try:
    # Information On a Neblio Address
    api_response = api_instance.testnet_get_address_info(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_address_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Neblio Address to get information on. | 

### Return type

[**GetAddressInfoResponse**](GetAddressInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_token_holders**
> GetTokenHoldersResponse testnet_get_token_holders(tokenid)

Get Addresses Holding a Token

Returns the the the addresses holding a token and how many tokens are held 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for

try:
    # Get Addresses Holding a Token
    api_response = api_instance.testnet_get_token_holders(tokenid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_token_holders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenid** | **str**| TokenId to request metadata for | 

### Return type

[**GetTokenHoldersResponse**](GetTokenHoldersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_token_id**
> GetTokenIdResponse testnet_get_token_id(tokensymbol)

Returns the tokenId representing a token

Translates a token symbol to a tokenId if a token exists with that symbol on the network 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
tokensymbol = 'tokensymbol_example' # str | Token symbol

try:
    # Returns the tokenId representing a token
    api_response = api_instance.testnet_get_token_id(tokensymbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_token_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokensymbol** | **str**| Token symbol | 

### Return type

[**GetTokenIdResponse**](GetTokenIdResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_token_metadata_of_issuance**
> GetTokenMetadataResponse testnet_get_token_metadata_of_issuance(tokenid)

Get Issuance Metadata of Token

Returns the metadata associated with a token at time of issuance. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for

try:
    # Get Issuance Metadata of Token
    api_response = api_instance.testnet_get_token_metadata_of_issuance(tokenid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_token_metadata_of_issuance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenid** | **str**| TokenId to request metadata for | 

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_token_metadata_of_utxo**
> GetTokenMetadataResponse testnet_get_token_metadata_of_utxo(tokenid, utxo)

Get UTXO Metadata of Token

Returns the metadata associated with a token for that specific utxo instead of the issuance transaction. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for
utxo = 'utxo_example' # str | Specific UTXO to request metadata for

try:
    # Get UTXO Metadata of Token
    api_response = api_instance.testnet_get_token_metadata_of_utxo(tokenid, utxo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_token_metadata_of_utxo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenid** | **str**| TokenId to request metadata for | 
 **utxo** | **str**| Specific UTXO to request metadata for | 

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_transaction_info**
> GetTransactionInfoResponse testnet_get_transaction_info(txid)

Information On an NTP1 Transaction

Returns detailed information regarding an NTP1 transaction. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
txid = 'txid_example' # str | Neblio txid to get information on.

try:
    # Information On an NTP1 Transaction
    api_response = api_instance.testnet_get_transaction_info(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_transaction_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Neblio txid to get information on. | 

### Return type

[**GetTransactionInfoResponse**](GetTransactionInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_issue_token**
> IssueTokenResponse testnet_issue_token(body)

Builds a transaction that issues a new NTP1 Token

Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
body = swagger_client.IssueTokenRequest() # IssueTokenRequest | Object representing the token to be created

try:
    # Builds a transaction that issues a new NTP1 Token
    api_response = api_instance.testnet_issue_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_issue_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IssueTokenRequest**](IssueTokenRequest.md)| Object representing the token to be created | 

### Return type

[**IssueTokenResponse**](IssueTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_send_token**
> SendTokenResponse testnet_send_token(body)

Builds a transaction that sends an NTP1 Token

Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain. 

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TestnetNTP1Api()
body = swagger_client.SendTokenRequest() # SendTokenRequest | Object representing the token to be sent

try:
    # Builds a transaction that sends an NTP1 Token
    api_response = api_instance.testnet_send_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_send_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendTokenRequest**](SendTokenRequest.md)| Object representing the token to be sent | 

### Return type

[**SendTokenResponse**](SendTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

