# neblio-api.TestnetInsightApi

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**testnet_get_address**](TestnetInsightApi.md#testnet_get_address) | **GET** /testnet/ins/addr/{address} | Returns address object
[**testnet_get_address_balance**](TestnetInsightApi.md#testnet_get_address_balance) | **GET** /testnet/ins/addr/{address}/balance | Returns address balance in sats
[**testnet_get_address_total_received**](TestnetInsightApi.md#testnet_get_address_total_received) | **GET** /testnet/ins/addr/{address}/totalReceived | Returns total received by address in sats
[**testnet_get_address_total_sent**](TestnetInsightApi.md#testnet_get_address_total_sent) | **GET** /testnet/ins/addr/{address}/totalSent | Returns total sent by address in sats
[**testnet_get_address_unconfirmed_balance**](TestnetInsightApi.md#testnet_get_address_unconfirmed_balance) | **GET** /testnet/ins/addr/{address}/unconfirmedBalance | Returns address unconfirmed balance in sats
[**testnet_get_address_utxos**](TestnetInsightApi.md#testnet_get_address_utxos) | **GET** /testnet/ins/addr/{address}/utxo | Returns all UTXOs at a given address
[**testnet_get_block**](TestnetInsightApi.md#testnet_get_block) | **GET** /testnet/ins/block/{blockhash} | Returns information regarding a Neblio block
[**testnet_get_block_index**](TestnetInsightApi.md#testnet_get_block_index) | **GET** /testnet/ins/block-index/{blockindex} | Returns block hash of block
[**testnet_get_raw_tx**](TestnetInsightApi.md#testnet_get_raw_tx) | **GET** /testnet/ins/rawtx/{txid} | Returns raw transaction hex
[**testnet_get_status**](TestnetInsightApi.md#testnet_get_status) | **GET** /testnet/ins/status | Utility API for calling several blockchain node functions
[**testnet_get_sync**](TestnetInsightApi.md#testnet_get_sync) | **GET** /testnet/ins/sync | Get node sync status
[**testnet_get_tx**](TestnetInsightApi.md#testnet_get_tx) | **GET** /testnet/ins/tx/{txid} | Returns transaction object
[**testnet_get_txs**](TestnetInsightApi.md#testnet_get_txs) | **GET** /testnet/ins/txs | Get transactions by block or address
[**testnet_send_tx**](TestnetInsightApi.md#testnet_send_tx) | **POST** /testnet/ins/tx/send | Broadcasts a signed raw transaction to the network (not NTP1 specific)


# **testnet_get_address**
> GetAddressResponse testnet_get_address(address)

Returns address object

Returns NEBL address object containing information on a specific address

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
address = 'address_example' # str | Address

try:
    # Returns address object
    api_response = api_instance.testnet_get_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_address: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

[**GetAddressResponse**](GetAddressResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_address_balance**
> float testnet_get_address_balance(address)

Returns address balance in sats

Returns NEBL address balance in satoshis

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
address = 'address_example' # str | Address

try:
    # Returns address balance in sats
    api_response = api_instance.testnet_get_address_balance(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_address_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_address_total_received**
> float testnet_get_address_total_received(address)

Returns total received by address in sats

Returns total NEBL received by address in satoshis

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
address = 'address_example' # str | Address

try:
    # Returns total received by address in sats
    api_response = api_instance.testnet_get_address_total_received(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_address_total_received: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_address_total_sent**
> float testnet_get_address_total_sent(address)

Returns total sent by address in sats

Returns total NEBL sent by address in satoshis

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
address = 'address_example' # str | Address

try:
    # Returns total sent by address in sats
    api_response = api_instance.testnet_get_address_total_sent(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_address_total_sent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_address_unconfirmed_balance**
> float testnet_get_address_unconfirmed_balance(address)

Returns address unconfirmed balance in sats

Returns NEBL address unconfirmed balance in satoshis

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
address = 'address_example' # str | Address

try:
    # Returns address unconfirmed balance in sats
    api_response = api_instance.testnet_get_address_unconfirmed_balance(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_address_unconfirmed_balance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

**float**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_address_utxos**
> list[object] testnet_get_address_utxos(address)

Returns all UTXOs at a given address

Returns information on each Unspent Transaction Output contained at an address

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
address = 'address_example' # str | Address

try:
    # Returns all UTXOs at a given address
    api_response = api_instance.testnet_get_address_utxos(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_address_utxos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_block**
> GetBlockResponse testnet_get_block(blockhash)

Returns information regarding a Neblio block

Returns blockchain data for a given block based upon the block hash

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
blockhash = 'blockhash_example' # str | Block Hash

try:
    # Returns information regarding a Neblio block
    api_response = api_instance.testnet_get_block(blockhash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_block: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockhash** | **str**| Block Hash | 

### Return type

[**GetBlockResponse**](GetBlockResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_block_index**
> GetBlockIndexResponse testnet_get_block_index(blockindex)

Returns block hash of block

Returns the block hash of a block at a given block index

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
blockindex = 3.4 # float | Block Index

try:
    # Returns block hash of block
    api_response = api_instance.testnet_get_block_index(blockindex)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_block_index: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blockindex** | **float**| Block Index | 

### Return type

[**GetBlockIndexResponse**](GetBlockIndexResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_raw_tx**
> GetRawTxResponse testnet_get_raw_tx(txid)

Returns raw transaction hex

Returns raw transaction hex representing a NEBL transaction

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
txid = 'txid_example' # str | Transaction ID

try:
    # Returns raw transaction hex
    api_response = api_instance.testnet_get_raw_tx(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_raw_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GetRawTxResponse**](GetRawTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_status**
> object testnet_get_status(q=q)

Utility API for calling several blockchain node functions

Utility API for calling several blockchain node functions - getInfo, getDifficulty, getBestBlockHash, getLastBlockHash

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
q = 'q_example' # str | Function to call, getInfo, getDifficulty, getBestBlockHash, or getLastBlockHash (optional)

try:
    # Utility API for calling several blockchain node functions
    api_response = api_instance.testnet_get_status(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| Function to call, getInfo, getDifficulty, getBestBlockHash, or getLastBlockHash | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_sync**
> GetSyncResponse testnet_get_sync()

Get node sync status

Returns information on the node's sync progress

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()

try:
    # Get node sync status
    api_response = api_instance.testnet_get_sync()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_sync: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSyncResponse**](GetSyncResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_tx**
> GetTxResponse testnet_get_tx(txid)

Returns transaction object

Returns NEBL transaction object representing a NEBL transaction

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
txid = 'txid_example' # str | Transaction ID

try:
    # Returns transaction object
    api_response = api_instance.testnet_get_tx(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **txid** | **str**| Transaction ID | 

### Return type

[**GetTxResponse**](GetTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_get_txs**
> GetTxsResponse testnet_get_txs(address=address, block=block, page_num=page_num)

Get transactions by block or address

Returns all transactions by block or address

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
address = 'address_example' # str | Address (optional)
block = 'block_example' # str | Block Hash (optional)
page_num = 3.4 # float | Page number to display (optional)

try:
    # Get transactions by block or address
    api_response = api_instance.testnet_get_txs(address=address, block=block, page_num=page_num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_get_txs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| Address | [optional] 
 **block** | **str**| Block Hash | [optional] 
 **page_num** | **float**| Page number to display | [optional] 

### Return type

[**GetTxsResponse**](GetTxsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **testnet_send_tx**
> BroadcastTxResponse testnet_send_tx(body)

Broadcasts a signed raw transaction to the network (not NTP1 specific)

Broadcasts a signed raw transaction to the network. If successful returns the txid of the broadcast trasnaction. 

### Example

```python
from __future__ import print_function
import time
import neblio-api
from neblio-api.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = neblio-api.TestnetInsightApi()
body = neblio-api.SendTxRequest() # SendTxRequest | Object representing a transaction to broadcast

try:
    # Broadcasts a signed raw transaction to the network (not NTP1 specific)
    api_response = api_instance.testnet_send_tx(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TestnetInsightApi->testnet_send_tx: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SendTxRequest**](SendTxRequest.md)| Object representing a transaction to broadcast | 

### Return type

[**BroadcastTxResponse**](BroadcastTxResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

