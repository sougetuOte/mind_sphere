# c:\work2\mind_sphere\first_test.py

import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain.schema import HumanMessage, AIMessage

# .envファイルから環境変数を読み込む
load_dotenv()

class Chat:
    def __init__(self):
        # Claude-3.5-Sonnetモデルを使用してChatAnthropicを初期化
        self.llm = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.7)
        self.conversation_history = []

    def get_response(self, user_input):
        # ユーザーの入力を会話履歴に追加
        self.conversation_history.append(HumanMessage(content=user_input))
        
        # LLMに会話履歴を渡して応答を生成
        response = self.llm(self.conversation_history)
        
        # AIの応答を会話履歴に追加
        self.conversation_history.append(AIMessage(content=response.content))
        
        return response.content

def main():
    chat = Chat()
    print("簡単なチャットボットです。終了するには 'quit' と入力してください。")
    
    while True:
        user_input = input("あなた: ")
        if user_input.lower() == 'quit':
            print("チャットを終了します。")
            break
        
        response = chat.get_response(user_input)
        print(f"AI: {response}")

if __name__ == "__main__":
    main()
