### Login

#### Request

```
POST http://docker:32774/api/dataset/user/login
Accept: application/json
Content-Length: 29
Content-Type: application/x-www-form-urlencoded

username=admin&password=admin
```

#### Response

```json
{
    "sessid": "OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk",
    "session_name": "SESSd14344a17ca11d13bda8baf612c0efa5",
    "token": "C2dfCUcN4hjgt6u2Xmv15mc1nkj5uv1Iqpa8QE3d7E8",
    "user": {
        "access": "1492546345",
        "created": "1488377334",
        "data": false,
        "field_about": [],
        "init": "admin@example.com",
        "language": "",
        "login": 1492546519,
        "mail": "admin@example.com",
        "name": "admin",
        "og_user_node": {
            "und": [
                {
                    "target_id": "1"
                },
                {
                    "target_id": "2"
                },
                {
                    "target_id": "3"
                }
            ]
        },
        "picture": null,
        "roles": {
            "2": "authenticated user"
        },
        "signature": "",
        "signature_format": null,
        "status": "1",
        "theme": "",
        "timezone": "UTC",
        "uid": "1",
        "uuid": "5eb4da39-cfba-4d43-bb45-691ebcde8f70"
    }
}
```

### Retrieve session token

#### Request
```
POST http://docker:32774/services/session/token
Accept: application/json
Cookie: SESSd14344a17ca11d13bda8baf612c0efa5=OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk
Content-Length: 0
```

#### Response

```
XBWI44XD33XBIANLpyK-rtvRa0N5OcaC03qLx0VQsP4
```


### Create dataset

#### Request

```
POST http://docker:32774/api/dataset/node
Content-Type: application/json
Accept: application/json
X-CSRF-Token: XBWI44XD33XBIANLpyK-rtvRa0N5OcaC03qLx0VQsP4
Cookie: SESSd14344a17ca11d13bda8baf612c0efa5=OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk
Content-Length: 44

{"type": "dataset", "title": "Test Dataset"}
```

#### Response

```json
{
    "nid": "75",
    "uri": "http://docker:32774/api/dataset/node/75"
}
```

### Create resource

#### Request

```
POST http://docker:32774/api/dataset/node
Content-Type: application/json
Accept: application/json
X-CSRF-Token: XBWI44XD33XBIANLpyK-rtvRa0N5OcaC03qLx0VQsP4
Cookie: SESSd14344a17ca11d13bda8baf612c0efa5=OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk
Content-Length: 97

{"type": "resource", "field_dataset_ref": {"und": {"target_id": "75"}}, "title": "Test Resource"}
```

#### Response

```json
{
    "nid": "76",
    "uri": "http://docker:32774/api/dataset/node/76"
}
```

### Retrieve parent dataset to check resource reference

#### Request
```
GET http://docker:32774/api/dataset/node/75
Accept: application/json
X-CSRF-Token: XBWI44XD33XBIANLpyK-rtvRa0N5OcaC03qLx0VQsP4
Cookie: SESSd14344a17ca11d13bda8baf612c0efa5=OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk
```

#### Response

```json
{
    "body": [],
    "changed": "1492544349",
    "comment": "0",
    "created": "1492544348",
    "data": "b:0;",
    "field_additional_info": [],
    "field_author": [],
    "field_conforms_to": [],
    "field_contact_email": [],
    "field_contact_name": [],
    "field_data_dictionary": [],
    "field_data_dictionary_type": [],
    "field_frequency": [],
    "field_granularity": [],
    "field_harvest_source_ref": [],
    "field_is_part_of": [],
    "field_landing_page": [],
    "field_language": [],
    "field_license": {
        "und": [
            {
                "format": null,
                "safe_value": "notspecified",
                "value": "notspecified"
            }
        ]
    },
    "field_modified_source_date": [],
    "field_orphan": {
        "und": [
            {
                "value": "0"
            }
        ]
    },
    "field_pod_theme": [],
    "field_public_access_level": {
        "und": [
            {
                "value": "public"
            }
        ]
    },
    "field_related_content": [],
    "field_resources": {
        "und": [
            {
                "target_id": "76"
            }
        ]
    },
    "field_rights": [],
    "field_spatial": [],
    "field_spatial_geographical_cover": [],
    "field_tags": [],
    "field_temporal_coverage": [],
    "field_topic": [],
    "language": "und",
    "log": "",
    "name": "admin",
    "nid": "75",
    "og_group_ref": [],
    "path": "http://docker:32774/dataset/test-dataset-16",
    "picture": "0",
    "promote": "0",
    "revision_timestamp": "1492544349",
    "revision_uid": "1",
    "status": "1",
    "sticky": "0",
    "title": "Test Dataset",
    "tnid": "0",
    "translate": "0",
    "type": "dataset",
    "uid": "1",
    "uuid": "d53881b3-d80f-49c2-8815-897321fe926e",
    "vid": "117",
    "vuuid": "c4663ada-0162-4780-8ee5-347c6c037429"
}
```

### Update dataset

#### Request

```
PUT http://docker:32774/api/dataset/node/75
Content-Type: application/json
Accept: application/json
X-CSRF-Token: XBWI44XD33XBIANLpyK-rtvRa0N5OcaC03qLx0VQsP4
Cookie: SESSd14344a17ca11d13bda8baf612c0efa5=OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk
Content-Length: 34

{"title": "Updated dataset title"}
```

#### Response

```json
{
    "nid": "75",
    "uri": "http://docker:32774/api/dataset/node/75"
}
```

### Add a file to a resource

```
POST http://docker:32774/api/dataset/node/76/attach_file
Accept: application/json
X-CSRF-Token: XBWI44XD33XBIANLpyK-rtvRa0N5OcaC03qLx0VQsP4
Cookie: SESSd14344a17ca11d13bda8baf612c0efa5=OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk
Content-Length: 474
Content-Type: multipart/form-data; boundary=5f8b431c36a24c828044cd876b3aa669

--5f8b431c36a24c828044cd876b3aa669
Content-Disposition: form-data; name="attach"

0
--5f8b431c36a24c828044cd876b3aa669
Content-Disposition: form-data; name="field_name"

field_upload
--5f8b431c36a24c828044cd876b3aa669
Content-Disposition: form-data; name="files[1]"; filename="tension_sample_data.csv"

tension,current,timestamp
220,10,2016-05-27T19:56:41.870Z
50,15,2016-05-27T19:51:21.794Z
230,10,2016-05-27T19:56:41.870Z
--5f8b431c36a24c828044cd876b3aa669--
```

#### Response

```json
[
    {
        "fid": "38",
        "uri": "http://docker:32774/api/dataset/file/38"
    }
]
```


### Retrieve the resource to check the file field

#### Request

```
GET http://docker:32774/api/dataset/node/76
Accept: application/json
X-CSRF-Token: XBWI44XD33XBIANLpyK-rtvRa0N5OcaC03qLx0VQsP4
Cookie: SESSd14344a17ca11d13bda8baf612c0efa5=OBoeXKMQx3zmaZrS_v3FOP7_Ze66fYA61TGhtm9s0Qk

None
```

#### Response
```json
{
    "body": [],
    "changed": "1492544350",
    "comment": "0",
    "created": "1492544349",
    "data": "b:0;",
    "field_dataset_ref": {
        "und": [
            {
                "target_id": "75"
            }
        ]
    },
    "field_datastore_status": {
        "und": [
            {
                "value": "2"
            }
        ]
    },
    "field_format": {
        "und": [
            {
                "tid": "32"
            }
        ]
    },
    "field_link_api": [],
    "field_link_remote_file": [],
    "field_orphan": {
        "und": [
            {
                "value": "0"
            }
        ]
    },
    "field_upload": {
        "und": [
            {
                "alt": "",
                "delimiter": null,
                "embed": null,
                "fid": "38",
                "filemime": "text/csv",
                "filename": "tension_sample_data.csv",
                "filesize": "120",
                "graph": null,
                "grid": null,
                "map": null,
                "metadata": [],
                "service_id": null,
                "status": "1",
                "timestamp": "1492544350",
                "title": "",
                "type": "undefined",
                "uid": "1",
                "uri": "public://tension_sample_data.csv",
                "uuid": "87019111-7ef0-48e5-b8a4-ea2c392f2e56"
            }
        ]
    },
    "language": "und",
    "log": "",
    "name": "admin",
    "nid": "76",
    "og_group_ref": [],
    "path": "http://docker:32774/dataset/updated-dataset-title/resource/34b45055-bc10-416f-a8ba-8b9f27718362",
    "picture": "0",
    "promote": "0",
    "revision_timestamp": "1492544350",
    "revision_uid": "1",
    "status": "1",
    "sticky": "0",
    "title": "Test Resource",
    "tnid": "0",
    "translate": "0",
    "type": "resource",
    "uid": "1",
    "uuid": "34b45055-bc10-416f-a8ba-8b9f27718362",
    "vid": "118",
    "vuuid": "ac1c1aa3-f6ee-4f76-a2f9-6510d9504680"
}
```

