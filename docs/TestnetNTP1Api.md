# neblioapi.TestnetNTP1Api

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testnet_broadcast_tx**](TestnetNTP1Api.md#testnet_broadcast_tx) | **POST** /testnet/ntp1/broadcast | Broadcasts a signed raw transaction to the network
[**testnet_burn_token**](TestnetNTP1Api.md#testnet_burn_token) | **POST** /testnet/ntp1/burntoken | Builds a transaction that burns an NTP1 Token
[**testnet_get_address_info**](TestnetNTP1Api.md#testnet_get_address_info) | **GET** /testnet/ntp1/addressinfo/{address} | Information On a Neblio Address
[**testnet_get_token_holders**](TestnetNTP1Api.md#testnet_get_token_holders) | **GET** /testnet/ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token
[**testnet_get_token_id**](TestnetNTP1Api.md#testnet_get_token_id) | **GET** /testnet/ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token
[**testnet_get_token_metadata**](TestnetNTP1Api.md#testnet_get_token_metadata) | **GET** /testnet/ntp1/tokenmetadata/{tokenid} | Get Metadata of Token
[**testnet_get_token_metadata_of_utxo**](TestnetNTP1Api.md#testnet_get_token_metadata_of_utxo) | **GET** /testnet/ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token
[**testnet_get_transaction_info**](TestnetNTP1Api.md#testnet_get_transaction_info) | **GET** /testnet/ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction
[**testnet_issue_token**](TestnetNTP1Api.md#testnet_issue_token) | **POST** /testnet/ntp1/issue | Builds a transaction that issues a new NTP1 Token
[**testnet_send_token**](TestnetNTP1Api.md#testnet_send_token) | **POST** /testnet/ntp1/sendtoken | Builds a transaction that sends an NTP1 Token


# **testnet_broadcast_tx**
> BroadcastTxResponse testnet_broadcast_tx(broadcast_tx_request)

Broadcasts a signed raw transaction to the network

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example

```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
broadcast_tx_request = neblioapi.BroadcastTxRequest() # BroadcastTxRequest | Object representing a transaction to broadcast

try:
    # Broadcasts a signed raw transaction to the network
    api_response = api_instance.testnet_broadcast_tx(broadcast_tx_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_broadcast_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **broadcast_tx_request** | [**BroadcastTxRequest**](BroadcastTxRequest.md)| Object representing a transaction to broadcast | 

### Return type

[**BroadcastTxResponse**](BroadcastTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_burn_token**
> BurnTokenResponse testnet_burn_token(burn_token_request)

Builds a transaction that burns an NTP1 Token

Builds an unsigned raw transaction that burns an NTP1 token on the Neblio blockchain. 

### Example

```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
burn_token_request = neblioapi.BurnTokenRequest() # BurnTokenRequest | Object representing the token to be burned

try:
    # Builds a transaction that burns an NTP1 Token
    api_response = api_instance.testnet_burn_token(burn_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_burn_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **burn_token_request** | [**BurnTokenRequest**](BurnTokenRequest.md)| Object representing the token to be burned | 

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
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
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

 - **Content-Type**: Not defined
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
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
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

 - **Content-Type**: Not defined
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
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_token_metadata**
> GetTokenMetadataResponse testnet_get_token_metadata(tokenid, verbosity=verbosity)

Get Metadata of Token

Returns the metadata associated with a token. 

### Example

```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for
verbosity = 3.4 # float | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses (optional)

try:
    # Get Metadata of Token
    api_response = api_instance.testnet_get_token_metadata(tokenid, verbosity=verbosity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_token_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenid** | **str**| TokenId to request metadata for | 
 **verbosity** | **float**| 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses | [optional] 

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_token_metadata_of_utxo**
> GetTokenMetadataResponse testnet_get_token_metadata_of_utxo(tokenid, utxo, verbosity=verbosity)

Get UTXO Metadata of Token

Returns the metadata associated with a token for that specific utxo instead of the issuance transaction. 

### Example

```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for
utxo = 'utxo_example' # str | Specific UTXO to request metadata for
verbosity = 3.4 # float | 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses (optional)

try:
    # Get UTXO Metadata of Token
    api_response = api_instance.testnet_get_token_metadata_of_utxo(tokenid, utxo, verbosity=verbosity)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_get_token_metadata_of_utxo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokenid** | **str**| TokenId to request metadata for | 
 **utxo** | **str**| Specific UTXO to request metadata for | 
 **verbosity** | **float**| 0 (Default) is fastest, 1 contains token stats, 2 contains token holding addresses | [optional] 

### Return type

[**GetTokenMetadataResponse**](GetTokenMetadataResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
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
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_issue_token**
> IssueTokenResponse testnet_issue_token(issue_token_request)

Builds a transaction that issues a new NTP1 Token

Builds an unsigned raw transaction that issues a new NTP1 token on the Neblio blockchain. 

### Example

```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
issue_token_request = neblioapi.IssueTokenRequest() # IssueTokenRequest | Object representing the token to be created

try:
    # Builds a transaction that issues a new NTP1 Token
    api_response = api_instance.testnet_issue_token(issue_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_issue_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_token_request** | [**IssueTokenRequest**](IssueTokenRequest.md)| Object representing the token to be created | 

### Return type

[**IssueTokenResponse**](IssueTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_send_token**
> SendTokenResponse testnet_send_token(send_token_request)

Builds a transaction that sends an NTP1 Token

Builds an unsigned raw transaction that sends an NTP1 token on the Neblio blockchain. 

### Example

```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblioapi.TestnetNTP1Api()
send_token_request = neblioapi.SendTokenRequest() # SendTokenRequest | Object representing the token to be sent

try:
    # Builds a transaction that sends an NTP1 Token
    api_response = api_instance.testnet_send_token(send_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetNTP1Api->testnet_send_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_token_request** | [**SendTokenRequest**](SendTokenRequest.md)| Object representing the token to be sent | 

### Return type

[**SendTokenResponse**](SendTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

