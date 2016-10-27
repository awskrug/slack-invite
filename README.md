
# Automatic Slack Invitation Page by AWS Lambda & API Gateway
This page is a small web application to invite a user into your slack team via Amazon API Gateway and AWS Lambda functions. You can make it with serverless arhcitecture including Amazon S3 static web hosting.

## Main Page `

You can set variables for your own purpose in `config.js` or environment variables.

## Settings
You can set variables for your own purpose in `index.html`, `config.js` or environment variables.

### Make a your invitation webpage in Amazon S3 
Please add `index.html` and `milligram.min.css` to your Amazon S3 bucket as a static webpage. Fill out `index.html` as your infomation.
```
            $.ajax({
              type: "POST",
              url: "https://956uxyx6ej.execute-api.ap-northeast-1.amazonaws.com/prod/slack", // PLEASE CHANGE
              data: JSON.stringify(pl),
              contentType: "application/json",
              dataType: "json",
              crossDomain: true,
              headers: {
                  'x-api-key': "kMupZ06nx12GSGSM36Hpc7e984bHBvBDwAlAIWY7" // PLEASE CHANGE
              }
```
* `url`: your API endpoint URL
* `headers` : your API Key


### Deploy your API backedn to Amazon API Gateway
You can deploy your API Gateway endpoints using `backend/apigateway.yaml` file and make a lambda function using `backend/f_invite.py`.

## Implemented site
You can check out http://slack.awskr.org!
