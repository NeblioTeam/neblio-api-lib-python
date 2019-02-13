# BurnTokenRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee** | **float** | Fee in satoshi to include in the issuance transaction min 10000 (0.0001 NEBL) | 
**_from** | **list[str]** | Array of addresses to send the token from | [optional] 
**transfer** | [**list[SendTokenRequestTo]**](SendTokenRequestTo.md) |  | [optional] 
**burn** | [**list[BurnTokenRequestBurn]**](BurnTokenRequestBurn.md) | Array of objects representing tokens to be burned | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


