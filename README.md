# loremIpsum
As part of the #NoServerNovember challenge of 2018, I'm sharing my solution using Python and Serverless Framework.

I'm using [lorem](https://pypi.org/project/lorem/) project to generate random text.

You can play with it on: https://ij2umnilc1.execute-api.us-east-1.amazonaws.com/dev/

### Exercise

Build a Serverless Ipsum generator.

Build a simple serverless-backed web app that displays Serverless Ipsum when it is loaded. Or Tony Danza Ipsum. Or The Office Ipsum. Or Reasons-I-Can’t-Take-Out-The-Trash Ipsum.

As long as it looks like Lorem Ipsum, but uses different words, we’re good. The page doesn’t have to look fancy, and you can do this even if you’ve never coded anything in your life!


### Installation

Install Serverless:

    $ yarn install -g serverless
    

Install the dependencies to handle pip requirements easily
    
    $ pip install -r requirements.txt
    
    
### Test

To test it locally, you can just run invoke function on your command line
    
    $ sls invoke local --function lorem-ipsum
    
### Deploy

Assuming you have your AWS credentials set to use the API:

    $ sls deploy -v 
    
