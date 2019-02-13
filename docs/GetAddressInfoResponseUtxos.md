# GetAddressInfoResponseUtxos

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script_pub_key** | [**object**](.md) | Object representing the scruptPubKey of the UTXO | [optional] 
**blocktime** | **float** | Blocktime of the UTXO | [optional] 
**index** | **float** | Index of the UTXO at this address | [optional] 
**txid** | **str** | Txid of this UTXO | [optional] 
**tokens** | [**list[GetAddressInfoResponseTokens]**](GetAddressInfoResponseTokens.md) | Array of NTP1 tokens in this UTXO. | [optional] 
**used** | **bool** | Whether the UTXO has been used | [optional] 
**value** | **float** | Value of the UTXO in NEBL satoshi | [optional] 
**blockheight** | **float** | Blockheight of the UTXO | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

