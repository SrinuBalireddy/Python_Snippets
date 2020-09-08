# Prodigi Python Dev Technical Test Solution
## Execution

``` 
env\Scripts\activate.bat 
pip install -r requirements.txt
hypercorn main:app --reload
```

- `Open http://127.0.0.1:8000/docs`
- `POST Request`
- ` Request Body{
  "image_url": "https://pwintyimages.blob.core.windows.net/samples/stars/test-sample-grey.png"
  }`
 
 **Response**

- `200 OK` on success
- ``` grey ```
 
**Definition**

`POST /image`

**Arguments**

- `"image_url":string`

**Response**

- `200 OK` on success
- ``` color Name ```
