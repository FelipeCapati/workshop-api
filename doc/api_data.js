define({ "api": [
  {
    "type": "post",
    "url": "/api/v1/example",
    "title": "Verify data input",
    "group": "Example",
    "name": "Verify_data",
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "Authorization",
            "description": "<p>Basic auth with user and password.</p>"
          }
        ]
      }
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "bool",
            "description": "<p>Boolean data [True or False]</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "number",
            "description": "<p>Integer number data [-inf, +inf]</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"data\": \"The number is less than 10 and bool is True\",\n    \"status\": true\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "src/infra/http/api/example.py",
    "groupTitle": "Example"
  }
] });
