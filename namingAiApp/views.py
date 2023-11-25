from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
import os
import json
import openai
from openai import OpenAI

client = OpenAI(
  api_key=os.environ.get('OPENAI_API_KEY'),
  timeout=15.0,
)

# Create your views here.
class Recommendations(APIView):

  def request_json_teamnames(self, messages):
    # 주어진 messages로 OpenAI에 팀명을 요청한다.
    # OpenAI의 응답값은 반드시 JSON 형식의 문자열이어야 한다.
    try:
      chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
      )
    except openai.APITimeoutError as e:
      raise ParseError("시간 초과")
    except openai.APIConnectionError as e:
      raise ParseError("OpenAI 서버에 접근 불가")
    except openai.APIError as e:
      raise ParseError("서버 내 오류")

    response = chat_completion.choices[0].message.content

    # OpenAI의 응답값을 문자열에서 파이썬 객체로 역직렬화한다.
    try:
      data = json.loads(response)
    except json.JSONDecodeError as e:
      raise ParseError("올바르지 않은 OpenAI 응답")

    return data

  def post(self, request):
    keywords = request.data.get("keywords");

    prompt = """
    우리 팀을 나타내는 키워드는 다음과 같아. 
    ```""" + ','.join(keywords) + """``` 
    이 키워드를 바탕으로 우리 팀의 팀명 5개를 추천해줘. 
    추천된 결과는 다음 키로 JSON 형식으로 제공해줘: 팀명 리스트-teamnames
    """

    messages=[
      {"role": "system", "content": "You are an assistant skilled in naming team name."},
      {"role": "user", "content": prompt}
    ]

    data = self.request_json_teamnames(messages)

    return Response({
      "teamnames": data['teamnames']
    })
