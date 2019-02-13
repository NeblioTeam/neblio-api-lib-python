# neblio-api.InsightApi

All URIs are relative to *https://ntp1node.nebl.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_address**](InsightApi.md#get_address) | **GET** /ins/addr/{address} | Returns address object
[**get_address_balance**](InsightApi.md#get_address_balance) | **GET** /ins/addr/{address}/balance | Returns address balance in sats
[**get_address_total_received**](InsightApi.md#get_address_total_received) | **GET** /ins/addr/{address}/totalReceived | Returns total received by address in sats
[**get_address_total_sent**](InsightApi.md#get_address_total_sent) | **GET** /ins/addr/{address}/totalSent | Returns total sent by address in sats
[**get_address_unconfirmed_balance**](InsightApi.md#get_address_unconfirmed_balance) | **GET** /ins/addr/{address}/unconfirmedBalance | Returns address unconfirmed balance in sats
[**get_address_utxos**](InsightApi.md#get_address_utxos) | **GET** /ins/addr/{address}/utxo | Returns all UTXOs at a given address
[**get_block**](InsightApi.md#get_block) | **GET** /ins/block/{blockhash} | Returns information regarding a Neblio block
[**get_block_index**](InsightApi.md#get_block_index) | **GET** /ins/block-index/{blockindex} | Returns block hash of block
[**get_raw_tx**](InsightApi.md#get_raw_tx) | **GET** /ins/rawtx/{txid} | Returns raw transaction hex
[**get_status**](InsightApi.md#get_status) | **GET** /ins/status | Utility API for calling several blockchain node functions
[**get_sync**](InsightApi.md#get_sync) | **GET** /ins/sync | Get node sync status
[**get_tx**](InsightApi.md#get_tx) | **GET** /ins/tx/{txid} | Returns transaction object
[**get_txs**](InsightApi.md#get_txs) | **GET** /ins/txs | Get transactions by block or address
[**send_tx**](InsightApi.md#send_tx) | **POST** /ins/tx/send | Broadcasts a signed raw transaction to the network (not NTP1 specific)


# **get_address**
> GetAddressResponse get_address(address)

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
api_instance = neblio-api.InsightApi()
address = 'address_example' # str | Address

try:
    # Returns address object
    api_response = api_instance.get_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address: %s\n" % e)
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

# **get_address_balance**
> float get_address_balance(address)

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
api_instance = neblio-api.InsightApi()
address = 'address_example' # str | Address

try:
    # Returns address balance in sats
    api_response = api_instance.get_address_balance(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address_balance: %s\n" % e)
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

# **get_address_total_received**
> float get_address_total_received(address)

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
api_instance = neblio-api.InsightApi()
address = 'address_example' # str | Address

try:
    # Returns total received by address in sats
    api_response = api_instance.get_address_total_received(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address_total_received: %s\n" % e)
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

# **get_address_total_sent**
> float get_address_total_sent(address)

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
api_instance = neblio-api.InsightApi()
address = 'address_example' # str | Address

try:
    # Returns total sent by address in sats
    api_response = api_instance.get_address_total_sent(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address_total_sent: %s\n" % e)
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

# **get_address_unconfirmed_balance**
> float get_address_unconfirmed_balance(address)

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
api_instance = neblio-api.InsightApi()
address = 'address_example' # str | Address

try:
    # Returns address unconfirmed balance in sats
    api_response = api_instance.get_address_unconfirmed_balance(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address_unconfirmed_balance: %s\n" % e)
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

# **get_address_utxos**
> list[object] get_address_utxos(address)

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
api_instance = neblio-api.InsightApi()
address = 'address_example' # str | Address

try:
    # Returns all UTXOs at a given address
    api_response = api_instance.get_address_utxos(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address_utxos: %s\n" % e)
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

# **get_block**
> GetBlockResponse get_block(blockhash)

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
api_instance = neblio-api.InsightApi()
blockhash = 'blockhash_example' # str | Block Hash

try:
    # Returns information regarding a Neblio block
    api_response = api_instance.get_block(blockhash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_block: %s\n" % e)
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

# **get_block_index**
> GetBlockIndexResponse get_block_index(blockindex)

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
api_instance = neblio-api.InsightApi()
blockindex = 3.4 # float | Block Index

try:
    # Returns block hash of block
    api_response = api_instance.get_block_index(blockindex)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_block_index: %s\n" % e)
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

# **get_raw_tx**
> GetRawTxResponse get_raw_tx(txid)

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
api_instance = neblio-api.InsightApi()
txid = 'txid_example' # str | Transaction ID

try:
    # Returns raw transaction hex
    api_response = api_instance.get_raw_tx(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_raw_tx: %s\n" % e)
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

# **get_status**
> object get_status(q=q)

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
api_instance = neblio-api.InsightApi()
q = 'q_example' # str | Function to call, getInfo, getDifficulty, getBestBlockHash, or getLastBlockHash (optional)

try:
    # Utility API for calling several blockchain node functions
    api_response = api_instance.get_status(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_status: %s\n" % e)
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

# **get_sync**
> GetSyncResponse get_sync()

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
api_instance = neblio-api.InsightApi()

try:
    # Get node sync status
    api_response = api_instance.get_sync()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_sync: %s\n" % e)
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

# **get_tx**
> GetTxResponse get_tx(txid)

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
api_instance = neblio-api.InsightApi()
txid = 'txid_example' # str | Transaction ID

try:
    # Returns transaction object
    api_response = api_instance.get_tx(txid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_tx: %s\n" % e)
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

# **get_txs**
> GetTxsResponse get_txs(address=address, block=block, page_num=page_num)

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
api_instance = neblio-api.InsightApi()
address = 'address_example' # str | Address (optional)
block = 'block_example' # str | Block Hash (optional)
page_num = 3.4 # float | Page number to display (optional)

try:
    # Get transactions by block or address
    api_response = api_instance.get_txs(address=address, block=block, page_num=page_num)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_txs: %s\n" % e)
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

# **send_tx**
> BroadcastTxResponse send_tx(body)

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
api_instance = neblio-api.InsightApi()
body = neblio-api.SendTxRequest() # SendTxRequest | Object representing a transaction to broadcast

try:
    # Broadcasts a signed raw transaction to the network (not NTP1 specific)
    api_response = api_instance.send_tx(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->send_tx: %s\n" % e)
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

