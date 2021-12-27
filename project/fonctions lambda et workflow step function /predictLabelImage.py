import json
#import sagemaker
import base64

import boto3
client = boto3.client('sagemaker-runtime')


# Fill this in with the name of your deployed model
ENDPOINT = 'scone-endpoint' ## TODO: fill in

def lambda_handler(event, context):

    # print(f' --------- INDICE --------- / {event.keys()}')
    # Decode the image data
    image = base64.b64decode(event['image_data']) ## TODO: fill in


    ###########             NOT USED           ##############
    # Instantiate a Predictor ----> NOT USED
    # predictor = Predictor(ENDPOINT) 
    #
    # NEED A LINUX MACHINE OR A VM LINUX IN WINDOWS, OR CLOUD9+CLI TO PACKAGE SAGEMAKER  
    # LOCALLY ( WITH "LINUX DEPENDENCIES") TO BE UPLOADED TO LAMBDA
    #
    # -->> better fastly use a solution found in forum : https://knowledge.udacity.com/questions/767689
    # Use of 'runtime.sagemaker' client in boto3, imported natively, rather than importing sagemaker
    
    
    # For this model the IdentitySerializer needs to be "image/png"
    # predictor.serializer = IdentitySerializer("image/png")



    # Make a prediction:
    #inferences = predictor.predict(event['s3_bucket'] + event['s3_key'])## TODO: fill in
    ############################################################   
    
    # print(f'ENDPOINT: {ENDPOINT}')

    response = client.invoke_endpoint( EndpointName = ENDPOINT, ContentType = 'image/png', Body=image)

    # Make a prediction:
    inferences = response['Body'].read()
    
    # We return the data back to the Step Function    
    event['inferences'] = inferences.decode('utf-8')
    
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
    
    
