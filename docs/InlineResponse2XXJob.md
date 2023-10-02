# InlineResponse2XXJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the stem generation job | [optional] 
**client_id** | **str** | Identifier of the client making the request | [optional] 
**created_at** | **str** | Timestamp of when the stem generation job was created | [optional] 
**started_at** | **str** | Timestamp of when the stem generation job was started | [optional] 
**updated_at** | **str** | Timestamp of when the stem generation job was last updated | [optional] 
**request_id** | **str** | Unique identifier of the request that generated this stem generation job | [optional] 
**license_id** | **str** | Identifier of the license used for stem generation | [optional] 
**stem_metadata** | [**InlineResponse2XXJobStemMetadata**](InlineResponse2XXJobStemMetadata.md) |  | [optional] 
**metadata** | [**InlineResponse2XXJobStemMetadata**](InlineResponse2XXJobStemMetadata.md) |  | [optional] 
**callback_url** | **str** | URL for the callback function to receive updates on the stem generation job | [optional] 
**status** | **str** | Current status of the stem generation job | [optional] 
**status_info** | [**InlineResponse2XXJobStatusInfo**](InlineResponse2XXJobStatusInfo.md) |  | [optional] 
**source_asset** | [**InlineResponse2XXJobSourceAsset**](InlineResponse2XXJobSourceAsset.md) |  | [optional] 
**stem_assets** | [**list[InlineResponse2XXJobStemAssets]**](InlineResponse2XXJobStemAssets.md) | Array of assets representing the generated stems | [optional] 
**output_assets** | [**list[InlineResponse2XXJobStemAssets]**](InlineResponse2XXJobStemAssets.md) | Array of assets representing the generated stems | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

