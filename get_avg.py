class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def from_string(cls, string_params):
        user = string_params.strip(',')
        self.name = user[0]
        self.email = user[1]
        self.password = user[2]

    @classmethod
    def from_list(cls, list_params):
        # 여기에 코드를 작성하세요
        pass

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)