# neblioapi
APIs for Interacting with NTP1 Tokens & The Neblio Blockchain

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.2.2
- Package version: 1.2.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/NeblioTeam/neblio-api-lib-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/NeblioTeam/neblio-api-lib-python.git`)

Then import the package:
```python
import neblioapi 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import neblioapi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import neblioapi
from neblioapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = neblioapi.InsightApi(neblioapi.ApiClient(configuration))
address = 'address_example' # str | Address

try:
    # Returns address object
    api_response = api_instance.get_address(address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InsightApi->get_address: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://ntp1node.nebl.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*InsightApi* | [**get_address**](docs/InsightApi.md#get_address) | **GET** /ins/addr/{address} | Returns address object
*InsightApi* | [**get_address_balance**](docs/InsightApi.md#get_address_balance) | **GET** /ins/addr/{address}/balance | Returns address balance in sats
*InsightApi* | [**get_address_total_received**](docs/InsightApi.md#get_address_total_received) | **GET** /ins/addr/{address}/totalReceived | Returns total received by address in sats
*InsightApi* | [**get_address_total_sent**](docs/InsightApi.md#get_address_total_sent) | **GET** /ins/addr/{address}/totalSent | Returns total sent by address in sats
*InsightApi* | [**get_address_unconfirmed_balance**](docs/InsightApi.md#get_address_unconfirmed_balance) | **GET** /ins/addr/{address}/unconfirmedBalance | Returns address unconfirmed balance in sats
*InsightApi* | [**get_address_utxos**](docs/InsightApi.md#get_address_utxos) | **GET** /ins/addr/{address}/utxo | Returns all UTXOs at a given address
*InsightApi* | [**get_block**](docs/InsightApi.md#get_block) | **GET** /ins/block/{blockhash} | Returns information regarding a Neblio block
*InsightApi* | [**get_block_index**](docs/InsightApi.md#get_block_index) | **GET** /ins/block-index/{blockindex} | Returns block hash of block
*InsightApi* | [**get_raw_tx**](docs/InsightApi.md#get_raw_tx) | **GET** /ins/rawtx/{txid} | Returns raw transaction hex
*InsightApi* | [**get_status**](docs/InsightApi.md#get_status) | **GET** /ins/status | Utility API for calling several blockchain node functions
*InsightApi* | [**get_sync**](docs/InsightApi.md#get_sync) | **GET** /ins/sync | Get node sync status
*InsightApi* | [**get_tx**](docs/InsightApi.md#get_tx) | **GET** /ins/tx/{txid} | Returns transaction object
*InsightApi* | [**get_txs**](docs/InsightApi.md#get_txs) | **GET** /ins/txs | Get transactions by block or address
*InsightApi* | [**send_tx**](docs/InsightApi.md#send_tx) | **POST** /ins/tx/send | Broadcasts a signed raw transaction to the network (not NTP1 specific)
*JSONRPCApi* | [**json_rpc**](docs/JSONRPCApi.md#json_rpc) | **POST** / | Send a JSON-RPC call to a localhost neblio-Qt or nebliod node
*NTP1Api* | [**broadcast_tx**](docs/NTP1Api.md#broadcast_tx) | **POST** /ntp1/broadcast | Broadcasts a signed raw transaction to the network
*NTP1Api* | [**burn_token**](docs/NTP1Api.md#burn_token) | **POST** /ntp1/burntoken | Builds a transaction that burns an NTP1 Token
*NTP1Api* | [**get_address_info**](docs/NTP1Api.md#get_address_info) | **GET** /ntp1/addressinfo/{address} | Information On a Neblio Address
*NTP1Api* | [**get_token_holders**](docs/NTP1Api.md#get_token_holders) | **GET** /ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token
*NTP1Api* | [**get_token_id**](docs/NTP1Api.md#get_token_id) | **GET** /ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token
*NTP1Api* | [**get_token_metadata**](docs/NTP1Api.md#get_token_metadata) | **GET** /ntp1/tokenmetadata/{tokenid} | Get Metadata of Token
*NTP1Api* | [**get_token_metadata_of_utxo**](docs/NTP1Api.md#get_token_metadata_of_utxo) | **GET** /ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token
*NTP1Api* | [**get_transaction_info**](docs/NTP1Api.md#get_transaction_info) | **GET** /ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction
*NTP1Api* | [**issue_token**](docs/NTP1Api.md#issue_token) | **POST** /ntp1/issue | Builds a transaction that issues a new NTP1 Token
*NTP1Api* | [**send_token**](docs/NTP1Api.md#send_token) | **POST** /ntp1/sendtoken | Builds a transaction that sends an NTP1 Token
*TestnetFaucetApi* | [**testnet_get_faucet**](docs/TestnetFaucetApi.md#testnet_get_faucet) | **GET** /testnet/faucet | Withdraws testnet NEBL to the specified address
*TestnetInsightApi* | [**testnet_get_address**](docs/TestnetInsightApi.md#testnet_get_address) | **GET** /testnet/ins/addr/{address} | Returns address object
*TestnetInsightApi* | [**testnet_get_address_balance**](docs/TestnetInsightApi.md#testnet_get_address_balance) | **GET** /testnet/ins/addr/{address}/balance | Returns address balance in sats
*TestnetInsightApi* | [**testnet_get_address_total_received**](docs/TestnetInsightApi.md#testnet_get_address_total_received) | **GET** /testnet/ins/addr/{address}/totalReceived | Returns total received by address in sats
*TestnetInsightApi* | [**testnet_get_address_total_sent**](docs/TestnetInsightApi.md#testnet_get_address_total_sent) | **GET** /testnet/ins/addr/{address}/totalSent | Returns total sent by address in sats
*TestnetInsightApi* | [**testnet_get_address_unconfirmed_balance**](docs/TestnetInsightApi.md#testnet_get_address_unconfirmed_balance) | **GET** /testnet/ins/addr/{address}/unconfirmedBalance | Returns address unconfirmed balance in sats
*TestnetInsightApi* | [**testnet_get_address_utxos**](docs/TestnetInsightApi.md#testnet_get_address_utxos) | **GET** /testnet/ins/addr/{address}/utxo | Returns all UTXOs at a given address
*TestnetInsightApi* | [**testnet_get_block**](docs/TestnetInsightApi.md#testnet_get_block) | **GET** /testnet/ins/block/{blockhash} | Returns information regarding a Neblio block
*TestnetInsightApi* | [**testnet_get_block_index**](docs/TestnetInsightApi.md#testnet_get_block_index) | **GET** /testnet/ins/block-index/{blockindex} | Returns block hash of block
*TestnetInsightApi* | [**testnet_get_raw_tx**](docs/TestnetInsightApi.md#testnet_get_raw_tx) | **GET** /testnet/ins/rawtx/{txid} | Returns raw transaction hex
*TestnetInsightApi* | [**testnet_get_status**](docs/TestnetInsightApi.md#testnet_get_status) | **GET** /testnet/ins/status | Utility API for calling several blockchain node functions
*TestnetInsightApi* | [**testnet_get_sync**](docs/TestnetInsightApi.md#testnet_get_sync) | **GET** /testnet/ins/sync | Get node sync status
*TestnetInsightApi* | [**testnet_get_tx**](docs/TestnetInsightApi.md#testnet_get_tx) | **GET** /testnet/ins/tx/{txid} | Returns transaction object
*TestnetInsightApi* | [**testnet_get_txs**](docs/TestnetInsightApi.md#testnet_get_txs) | **GET** /testnet/ins/txs | Get transactions by block or address
*TestnetInsightApi* | [**testnet_send_tx**](docs/TestnetInsightApi.md#testnet_send_tx) | **POST** /testnet/ins/tx/send | Broadcasts a signed raw transaction to the network (not NTP1 specific)
*TestnetNTP1Api* | [**testnet_broadcast_tx**](docs/TestnetNTP1Api.md#testnet_broadcast_tx) | **POST** /testnet/ntp1/broadcast | Broadcasts a signed raw transaction to the network
*TestnetNTP1Api* | [**testnet_burn_token**](docs/TestnetNTP1Api.md#testnet_burn_token) | **POST** /testnet/ntp1/burntoken | Builds a transaction that burns an NTP1 Token
*TestnetNTP1Api* | [**testnet_get_address_info**](docs/TestnetNTP1Api.md#testnet_get_address_info) | **GET** /testnet/ntp1/addressinfo/{address} | Information On a Neblio Address
*TestnetNTP1Api* | [**testnet_get_token_holders**](docs/TestnetNTP1Api.md#testnet_get_token_holders) | **GET** /testnet/ntp1/stakeholders/{tokenid} | Get Addresses Holding a Token
*TestnetNTP1Api* | [**testnet_get_token_id**](docs/TestnetNTP1Api.md#testnet_get_token_id) | **GET** /testnet/ntp1/tokenid/{tokensymbol} | Returns the tokenId representing a token
*TestnetNTP1Api* | [**testnet_get_token_metadata**](docs/TestnetNTP1Api.md#testnet_get_token_metadata) | **GET** /testnet/ntp1/tokenmetadata/{tokenid} | Get Metadata of Token
*TestnetNTP1Api* | [**testnet_get_token_metadata_of_utxo**](docs/TestnetNTP1Api.md#testnet_get_token_metadata_of_utxo) | **GET** /testnet/ntp1/tokenmetadata/{tokenid}/{utxo} | Get UTXO Metadata of Token
*TestnetNTP1Api* | [**testnet_get_transaction_info**](docs/TestnetNTP1Api.md#testnet_get_transaction_info) | **GET** /testnet/ntp1/transactioninfo/{txid} | Information On an NTP1 Transaction
*TestnetNTP1Api* | [**testnet_issue_token**](docs/TestnetNTP1Api.md#testnet_issue_token) | **POST** /testnet/ntp1/issue | Builds a transaction that issues a new NTP1 Token
*TestnetNTP1Api* | [**testnet_send_token**](docs/TestnetNTP1Api.md#testnet_send_token) | **POST** /testnet/ntp1/sendtoken | Builds a transaction that sends an NTP1 Token


## Documentation For Models

 - [BroadcastTxRequest](docs/BroadcastTxRequest.md)
 - [BroadcastTxResponse](docs/BroadcastTxResponse.md)
 - [BurnTokenRequest](docs/BurnTokenRequest.md)
 - [BurnTokenRequestBurn](docs/BurnTokenRequestBurn.md)
 - [BurnTokenResponse](docs/BurnTokenResponse.md)
 - [Error](docs/Error.md)
 - [GetAddressInfoResponse](docs/GetAddressInfoResponse.md)
 - [GetAddressInfoResponseTokens](docs/GetAddressInfoResponseTokens.md)
 - [GetAddressInfoResponseUtxos](docs/GetAddressInfoResponseUtxos.md)
 - [GetAddressResponse](docs/GetAddressResponse.md)
 - [GetBlockIndexResponse](docs/GetBlockIndexResponse.md)
 - [GetBlockResponse](docs/GetBlockResponse.md)
 - [GetFaucetResponse](docs/GetFaucetResponse.md)
 - [GetFaucetResponseData](docs/GetFaucetResponseData.md)
 - [GetRawTxResponse](docs/GetRawTxResponse.md)
 - [GetSyncResponse](docs/GetSyncResponse.md)
 - [GetTokenHoldersResponse](docs/GetTokenHoldersResponse.md)
 - [GetTokenHoldersResponseHolders](docs/GetTokenHoldersResponseHolders.md)
 - [GetTokenIdResponse](docs/GetTokenIdResponse.md)
 - [GetTokenMetadataResponse](docs/GetTokenMetadataResponse.md)
 - [GetTokenMetadataResponseMetadataOfIssuence](docs/GetTokenMetadataResponseMetadataOfIssuence.md)
 - [GetTokenMetadataResponseMetadataOfIssuenceData](docs/GetTokenMetadataResponseMetadataOfIssuenceData.md)
 - [GetTokenMetadataResponseMetadataOfIssuenceDataUserData](docs/GetTokenMetadataResponseMetadataOfIssuenceDataUserData.md)
 - [GetTokenMetadataResponseMetadataOfIssuenceDataUserDataMeta](docs/GetTokenMetadataResponseMetadataOfIssuenceDataUserDataMeta.md)
 - [GetTransactionInfoResponse](docs/GetTransactionInfoResponse.md)
 - [GetTransactionInfoResponsePreviousOutput](docs/GetTransactionInfoResponsePreviousOutput.md)
 - [GetTransactionInfoResponseScriptSig](docs/GetTransactionInfoResponseScriptSig.md)
 - [GetTransactionInfoResponseTokens](docs/GetTransactionInfoResponseTokens.md)
 - [GetTransactionInfoResponseVin](docs/GetTransactionInfoResponseVin.md)
 - [GetTransactionInfoResponseVout](docs/GetTransactionInfoResponseVout.md)
 - [GetTxResponse](docs/GetTxResponse.md)
 - [GetTxResponseVin](docs/GetTxResponseVin.md)
 - [GetTxResponseVout](docs/GetTxResponseVout.md)
 - [GetTxsResponse](docs/GetTxsResponse.md)
 - [IssueTokenRequest](docs/IssueTokenRequest.md)
 - [IssueTokenRequestFlags](docs/IssueTokenRequestFlags.md)
 - [IssueTokenRequestMetadata](docs/IssueTokenRequestMetadata.md)
 - [IssueTokenRequestMetadataEncryptions](docs/IssueTokenRequestMetadataEncryptions.md)
 - [IssueTokenRequestMetadataRules](docs/IssueTokenRequestMetadataRules.md)
 - [IssueTokenRequestMetadataRulesExpiration](docs/IssueTokenRequestMetadataRulesExpiration.md)
 - [IssueTokenRequestMetadataRulesFees](docs/IssueTokenRequestMetadataRulesFees.md)
 - [IssueTokenRequestMetadataRulesFeesItems](docs/IssueTokenRequestMetadataRulesFeesItems.md)
 - [IssueTokenRequestMetadataRulesHolders](docs/IssueTokenRequestMetadataRulesHolders.md)
 - [IssueTokenRequestMetadataUrls](docs/IssueTokenRequestMetadataUrls.md)
 - [IssueTokenRequestTransfer](docs/IssueTokenRequestTransfer.md)
 - [IssueTokenResponse](docs/IssueTokenResponse.md)
 - [RpcRequest](docs/RpcRequest.md)
 - [RpcResponse](docs/RpcResponse.md)
 - [SendTokenRequest](docs/SendTokenRequest.md)
 - [SendTokenRequestTo](docs/SendTokenRequestTo.md)
 - [SendTokenResponse](docs/SendTokenResponse.md)
 - [SendTxRequest](docs/SendTxRequest.md)


## Documentation For Authorization


## rpcAuth

- **Type**: HTTP basic authentication


## Author




