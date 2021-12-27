import json


THRESHOLD = .93


def lambda_handler(event, context):
    
    print(event)
    # Grab the inferences from the event
    inferences = json.loads(event['body'])['inferences']     ## TODO: fill in
    inferences = json.loads(inferences)
    print(f'INFERENCES : {inferences}')
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = (inferences[0]>THRESHOLD or inferences[1]>THRESHOLD)   ## TODO: fill in
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        print("THRESHOLD MET")
        pass
    else:
        print("!!!!!!!     THRESHOLD NOT MET       !!!!!!")
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': json.dumps(event),
        'meets_threshold' : meets_threshold
    }