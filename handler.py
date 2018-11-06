from lorem.text import TextLorem

WORDS = [
    'API Gateway',
    'auto-scaling',
    'AWS',
    'Azure',
    'cloud',
    'event',
    'function',
    'Google Cloud',
    'handler',
    'Lambda',
    'microservices',
    'monitoring',
    'NoOps',
    'pay-per-execution',
    'serverdeath',
    'SNS',
    'zero-maintenance',
]

lorem = TextLorem(wsep=' ', srange=(10, 20), words=WORDS)


def lorem_ipsum(event, _):
    response = {
        "statusCode": 200,
        "body": lorem.sentence()
    }

    return response
