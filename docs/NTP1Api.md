# neblioapi.NTP1Api

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcast_tx**](NTP1Api.md#broadcast_tx) | **POST** /ntp1/broadcast | Broadcasts a signed raw transaction to the network
[**burn_token**](NTP1Api.md#burn_token) | **POST** /ntp1/burntoken | Builds a transaction that burns an NTP1 Token
[**get_address_info**](NTP1Api.md#get_address_info) | **GET** /ntp1/addressinfo/{address} | Information On a Neblio Address
[**get_token_holders**](NTP1Api.md#get_token_holders) | **GET** /ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token
[**get_token_id**](NTP1Api.md#get_token_id) | **GET** /ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token
[**get_token_metadata**](NTP1Api.md#get_token_metadata) | **GET** /ntp1/tokenmetadata/{tokenid} | Get Metadata of Token
[**get_token_metadata_of_utxo**](NTP1Api.md#get_token_metadata_of_utxo) | **GET** /ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token
[**get_transaction_info**](NTP1Api.md#get_transaction_info) | **GET** /ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction
[**issue_token**](NTP1Api.md#issue_token) | **POST** /ntp1/issue | Builds a transaction that issues a new NTP1 Token
[**send_token**](NTP1Api.md#send_token) | **POST** /ntp1/sendtoken | Builds a transaction that sends an NTP1 Token


# **broadcast_tx**
> BroadcastTxResponse broadcast_tx(broadcast_tx_request)

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
api_instance = neblioapi.NTP1Api()
broadcast_tx_request = neblioapi.BroadcastTxRequest() # BroadcastTxRequest | Object representing a transaction to broadcast

try:
    # Broadcasts a signed raw transaction to the network
    api_response = api_instance.broadcast_tx(broadcast_tx_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->broadcast_tx: %s\n" % e)
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

# **burn_token**
> BurnTokenResponse burn_token(burn_token_request)

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
api_instance = neblioapi.NTP1Api()
burn_token_request = neblioapi.BurnTokenRequest() # BurnTokenRequest | Object representing the token to be burned

try:
    # Builds a transaction that burns an NTP1 Token
    api_response = api_instance.burn_token(burn_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->burn_token: %s\n" % e)
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

# **get_address_info**
> GetAddressInfoResponse get_address_info(address)

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
api_instance = neblioapi.NTP1Api()
address = 'address_example' # str | Neblio Address to get information on.

try:
    # Information On a Neblio Address
    api_response = api_instance.get_address_info(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->get_address_info: %s\n" % e)
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

# **get_token_holders**
> GetTokenHoldersResponse get_token_holders(tokenid)

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
api_instance = neblioapi.NTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for

try:
    # Get Addresses Holding a Token
    api_response = api_instance.get_token_holders(tokenid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->get_token_holders: %s\n" % e)
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

# **get_token_id**
> GetTokenIdResponse get_token_id(tokensymbol)

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
api_instance = neblioapi.NTP1Api()
tokensymbol = 'tokensymbol_example' # str | Token symbol

try:
    # Returns the tokenId representing a token
    api_response = api_instance.get_token_id(tokensymbol)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->get_token_id: %s\n" % e)
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

# **get_token_metadata**
> GetTokenMetadataResponse get_token_metadata(tokenid)

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
api_instance = neblioapi.NTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for

try:
    # Get Metadata of Token
    api_response = api_instance.get_token_metadata(tokenid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->get_token_metadata: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_metadata_of_utxo**
> GetTokenMetadataResponse get_token_metadata_of_utxo(tokenid, utxo)

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
api_instance = neblioapi.NTP1Api()
tokenid = 'tokenid_example' # str | TokenId to request metadata for
utxo = 'utxo_example' # str | Specific UTXO to request metadata for

try:
    # Get UTXO Metadata of Token
    api_response = api_instance.get_token_metadata_of_utxo(tokenid, utxo)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->get_token_metadata_of_utxo: %s\n" % e)
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

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_info**
> GetTransactionInfoResponse get_transaction_info(txid)

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
api_instance = neblioapi.NTP1Api()
txid = 'txid_example' # str | Neblio txid to get information on.

try:
    # Information On an NTP1 Transaction
    api_response = api_instance.get_transaction_info(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->get_transaction_info: %s\n" % e)
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

# **issue_token**
> IssueTokenResponse issue_token(issue_token_request)

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
api_instance = neblioapi.NTP1Api()
issue_token_request = neblioapi.IssueTokenRequest() # IssueTokenRequest | Object representing the token to be created

try:
    # Builds a transaction that issues a new NTP1 Token
    api_response = api_instance.issue_token(issue_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->issue_token: %s\n" % e)
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

# **send_token**
> SendTokenResponse send_token(send_token_request)

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
api_instance = neblioapi.NTP1Api()
send_token_request = neblioapi.SendTokenRequest() # SendTokenRequest | Object representing the token to be sent

try:
    # Builds a transaction that sends an NTP1 Token
    api_response = api_instance.send_token(send_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NTP1Api->send_token: %s\n" % e)
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

