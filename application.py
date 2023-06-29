from flask import Flask,request,Response,json
import boto3
application = Flask(__name__)

@application.route('/getTranslation',methods=['POST'])
def getTranslation():
    payload = request.get_json()
    s3 = boto3.client(aws_access_key_id='AKIAYN2KW7RDLUAMLSCE',
    aws_secret_access_key='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',region_name='us-east-1',service_name="translate"
)
    # aws_mag_con=boto3.session.Session(profile_name='demo_user')
    # client=aws_mag_con.client(service_name='translate',region_name='us-east-1') 
    response=s3.translate_text(Text=payload['text'],SourceLanguageCode=payload['from_lang'],TargetLanguageCode=payload['to_lang'])
    # print("Translated Text : "+response.get('TranslatedText'))
    data = {'translated_text':response.get('TranslatedText')}
    res = Response(json.dumps(data), status=200, mimetype='application/json')
    return res

if __name__=="__main__":
    application.run(debug=True)