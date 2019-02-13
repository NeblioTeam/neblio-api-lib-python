# IssueTokenRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_address** | **str** | Address issuing the token | 
**amount** | **float** | Number of tokens to issue | 
**divisibility** | **float** | Number of decimal places the token should be divisble by (0-7) | 
**fee** | **float** | Fee in satoshi to include in the issuance transaction min 1000000000 (10 NEBL) | 
**reissuable** | **bool** | whether the token should be reissuable | 
**flags** | [**IssueTokenRequestFlags**](IssueTokenRequestFlags.md) |  | [optional] 
**transfer** | [**list[IssueTokenRequestTransfer]**](IssueTokenRequestTransfer.md) |  | 
**metadata** | [**IssueTokenRequestMetadata**](IssueTokenRequestMetadata.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


