# GetTokenMetadataResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_id** | **str** | ID of the token | [optional] 
**divisibility** | **float** | Decimal places the token is divisible to | [optional] 
**lock_status** | **bool** | Whether issuance of more tokens is locked | [optional] 
**aggregation_policy** | **str** | Whether the tokens are aggregatable | [optional] 
**total_supply** | **float** | Total number of tokens in supply | [optional] 
**num_of_holders** | **float** | Total number of addresses this token is held at | [optional] 
**num_of_transfers** | **float** | Total number of transactions of this token | [optional] 
**numof_issuance** | **float** | Total number of times this token has been issued | [optional] 
**num_of_burns** | **float** | Number of times tokens have been burned | [optional] 
**first_block** | **float** | Block number token was issued in | [optional] 
**issuance_txid** | **str** | TXID the token was issued with | [optional] 
**issue_address** | **str** | Address that issued the tokens | [optional] 
**metadata_of_issuance** | [**GetTokenMetadataResponseMetadataOfIssuance**](GetTokenMetadataResponseMetadataOfIssuance.md) |  | [optional] 
**metadata_of_utxo** | [**GetTokenMetadataResponseMetadataOfIssuance**](GetTokenMetadataResponseMetadataOfIssuance.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


