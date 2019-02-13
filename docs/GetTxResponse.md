# GetTxResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**txid** | **str** | TXID of transaction | [optional] 
**version** | **float** | Transaction version | [optional] 
**locktime** | **float** | Transaction locktime | [optional] 
**vin** | [**list[GetTxResponseVin]**](GetTxResponseVin.md) | Array of transaction inputs | [optional] 
**vout** | [**list[GetTxResponseVout]**](GetTxResponseVout.md) | Array of transaction outputs | [optional] 
**blocktime** | **float** | Block time of this transaction | [optional] 
**blockheight** | **float** | Block height of this transaction | [optional] 
**totalsent** | **float** | Total NEBL sent in this transaction in satoshis | [optional] 
**fee** | **float** | Total NEBL used as fee for this transcation in satoshis | [optional] 
**blockhash** | **str** | Hash of the block this transaction is in | [optional] 
**time** | **float** | Transaction time | [optional] 
**confirmations** | **float** | Number of transaction confirmations | [optional] 
**value_out** | **float** | Total NEBL output in this transaction | [optional] 
**value_in** | **float** | Total NEBL input in this transaction | [optional] 
**fees** | **float** | Total NEBL used in fees for this transaction | [optional] 
**size** | **float** | Transcation size in bytes | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


