{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n",
      "Hello World\n"
     ]
    }
   ],
   "source": [
    "# 001 print 기초 \n",
    "# 화면에 Hello World 문자열을 출력하세요.\n",
    "\n",
    "print(\"Hello World\")\n",
    "print('Hello World')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mary's cosmetics\n"
     ]
    }
   ],
   "source": [
    "# 002 print 기초 \n",
    "# 화면에 Mary's cosmetics을 출력하세요. (중간에 '가 있음에 주의하세요)\n",
    "\n",
    "print(\"Mary's cosmetics\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "신씨가 소리질렀다. \"도둑이야\".\n"
     ]
    }
   ],
   "source": [
    "# 003 print 기초\n",
    "#화면에 아래 문장을 출력하세요. (중간에 \"가 있음에 주의하세요.)\n",
    "\n",
    "#신씨가 소리질렀다. \"도둑이야\".\n",
    "\n",
    "print('신씨가 소리질렀다. \"도둑이야\".')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "C:\\Windows\n"
     ]
    }
   ],
   "source": [
    "# 004 print 기초\n",
    "# 화면에 \"C:\\Windows\"를 출력하세요.\n",
    "\n",
    "print(\"C:\\Windows\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "안녕하세요.\n",
      "만나서\t\t반갑습니다.\n"
     ]
    }
   ],
   "source": [
    "# 005 print 탭과 줄바꿈\n",
    "# 다음 코드를 실행해보고 \\t와 \\n의 역할을 설명해보세요.\n",
    "\n",
    "print(\"안녕하세요.\\n만나서\\t\\t반갑습니다.\")\n",
    "\n",
    "# \\t: 탭, \\n: 엔터"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "오늘은 일요일\n"
     ]
    }
   ],
   "source": [
    "# 006 print 여러 데이터 출력\n",
    "# print 함수에 두 개의 단어를 입력한 예제입니다. 아래 코드의 출력 결과를 예상해봅시다.\n",
    "\n",
    "print (\"오늘은\", \"일요일\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "naver;kakao;sk;samsung\n"
     ]
    }
   ],
   "source": [
    "# 007 print 기초\n",
    "# print() 함수를 사용하여 다음과 같이 출력하세요.\n",
    "\n",
    "# naver;kakao;sk;samsung\n",
    "\n",
    "print(\"naver\",\"kakao\",\"sk\",\"samsung\", sep=\";\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "naver;kakao;sk;samsung\n"
     ]
    }
   ],
   "source": [
    "# 008 print 기초\n",
    "# print() 함수를 사용하여 다음과 같이 출력하세요.\n",
    "\n",
    "#naver/kakao/sk/samsung\n",
    "\n",
    "print(\"naver\", \"kakao\", \"sk\", \"samsung\", sep=\";\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "firstsecond\n"
     ]
    }
   ],
   "source": [
    "# 009 print 줄바꿈\n",
    "# 다음 코드를 수정하여 줄바꿈이 없이 출력하세요. (힌트: end='') print 함수는 두 번 사용합니다. 세미콜론 (;)은 한줄에 여러 개의 명령을 작성하기 위해 사용합니다.\n",
    "\n",
    "# print(\"first\");print(\"second\")\n",
    "\n",
    "print(\"first\",end='');print(\"second\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1.6666666666666667\n"
     ]
    }
   ],
   "source": [
    "# 010 연산 결과 출력\n",
    "# 5/3의 결과를 화면에 출력하세요.\n",
    "print(5/3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "500000\n"
     ]
    }
   ],
   "source": [
    "# 011 변수 사용하기\n",
    "# 삼성전자라는 변수로 50,000원을 바인딩해보세요.\n",
    "# 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.\n",
    "\n",
    "삼성전자 = 50000\n",
    "총평가금액 = 삼성전자 * 10\n",
    "print(총평가금액)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "298000000000 <class 'int'>\n",
      "50000 <class 'int'>\n",
      "15.79 <class 'float'>\n"
     ]
    }
   ],
   "source": [
    "# 012 변수 사용하기\n",
    "# 다음 표는 삼성전자의 일부 투자정보입니다.\n",
    "# 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.\n",
    "\n",
    "#항목\t값\n",
    "#시가총액\t298조\n",
    "#현재가\t50,000원\n",
    "#PER\t15.79\n",
    "\n",
    "시가총액 = 298000000000\n",
    "현재가 = 50000\n",
    "PER = 15.79\n",
    "\n",
    "print(시가총액, type(시가총액))\n",
    "print(현재가, type(현재가))\n",
    "print(PER, type(PER))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello! python\n"
     ]
    }
   ],
   "source": [
    "# 013 문자열 출력\n",
    "# 변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.\n",
    "\n",
    "# >> s = \"hello\"\n",
    "# >> t = \"python\"\n",
    "# 두 변수를 이용하여 아래와 같이 출력해보세요.\n",
    "\n",
    "# 실행 예:\n",
    "# hello! python\n",
    "\n",
    "s = \"hello\"\n",
    "t = \"python\"\n",
    "\n",
    "print(s+\"!\",t)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 014 파이썬을 이용한 값 계산\n",
    "# 아래 코드의 실행 결과를 예상해보세요.\n",
    "\n",
    "# >> 2 + 2 * 3 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "# 015 type 함수\n",
    "# type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.\n",
    "\n",
    "# >> a = 128\n",
    "# >> print (type(a))\n",
    "# <class 'int'>\n",
    "# 아래 변수에 바인딩된 값의 타입을 판별해보세요.\n",
    "\n",
    "# >> a = \"132\"\n",
    "\n",
    "a = \"132\"\n",
    "print(type(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "# 016 문자열을 정수로 변환\n",
    "# 문자열 '720'를 정수형으로 변환해보세요.\n",
    "\n",
    "# >> num_str = \"720\"\n",
    "\n",
    "num_str = \"720\"\n",
    "num_int = int(num_str)\n",
    "print(type(num_int))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n"
     ]
    }
   ],
   "source": [
    "# 017 정수를 문자열 100으로 변환\n",
    "# 정수 100을 문자열 '100'으로 변환해보세요.\n",
    "\n",
    "# num = 100\n",
    "\n",
    "num = 100\n",
    "num_str = str(100)\n",
    "print(type(num_str))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "<class 'float'>\n"
     ]
    }
   ],
   "source": [
    "# 018 문자열을 실수로 변환\n",
    "# 문자열 \"15.79\"를 실수(float) 타입으로 변환해보세요.\n",
    "\n",
    "num_str = \"15.79\"\n",
    "print(type(num_str))\n",
    "num_float = float(num_str)\n",
    "print(type(num_float))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2017\n",
      "2018\n",
      "2019\n"
     ]
    }
   ],
   "source": [
    "# 019 문자열을 정수로 변환\n",
    "# year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.\n",
    "\n",
    "# year = \"2020\"\n",
    "\n",
    "year = \"2020\"\n",
    "year_int = int(year)\n",
    "\n",
    "print(year_int-3)\n",
    "print(year_int-2)\n",
    "print(year_int-1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1749024\n"
     ]
    }
   ],
   "source": [
    "# 020 파이썬 계산\n",
    "# 에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)\n",
    "\n",
    "월가격 = 48584\n",
    "할부 = 36\n",
    "\n",
    "총금액 = 월가격*할부\n",
    "\n",
    "print(총금액)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "p t\n"
     ]
    }
   ],
   "source": [
    "# 021 문자열 인덱싱\n",
    "# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.\n",
    "\n",
    "# >> letters = 'python'\n",
    "# 실행 예\n",
    "# p t\n",
    "\n",
    "letters = 'python'\n",
    "print(letters[0], letters[2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2210\n"
     ]
    }
   ],
   "source": [
    "# 022 문자열 슬라이싱\n",
    "# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.\n",
    "\n",
    "# >> license_plate = \"24가 2210\"\n",
    "# 실행 예: 2210\n",
    "\n",
    "license_plate = \"24가 2210\"\n",
    "print(license_plate[-4:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "홀홀홀\n"
     ]
    }
   ],
   "source": [
    "# 023 문자열 인덱싱\n",
    "# 아래의 문자열에서 '홀' 만 출력하세요.\n",
    "\n",
    "# >> string = \"홀짝홀짝홀짝\"\n",
    "# 실행 예:\n",
    "# 홀홀홀\n",
    "\n",
    "string = \"홀짝홀짝홀짝\"\n",
    "print(string[::2])\n",
    "\n",
    "# 슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "NOHTYP\n"
     ]
    }
   ],
   "source": [
    "# 024 문자열 슬라이싱\n",
    "# 문자열을 거꾸로 뒤집어 출력하세요.\n",
    "\n",
    "# >> string = \"PYTHON\"\n",
    "# 실행 예:\n",
    "# NOHTYP\n",
    "\n",
    "string = \"PYTHON\"\n",
    "print(string[::-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "010 1111 2222\n"
     ]
    }
   ],
   "source": [
    "# 025 문자열 치환\n",
    "# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.\n",
    "\n",
    "# >> phone_number = \"010-1111-2222\"\n",
    "# 실행 예\n",
    "# 010 1111 2222\n",
    "\n",
    "phone_number = \"010-1111-2222\"\n",
    "phone_number_nohyphen = phone_number.replace(\"-\",\" \")\n",
    "print(phone_number_nohyphen)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "01011112222\n"
     ]
    }
   ],
   "source": [
    "# 026 문자열 다루기\n",
    "# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.\n",
    "\n",
    "# 실행 예\n",
    "# 01011112222\n",
    "\n",
    "phone_number = \"010-1111-2222\"\n",
    "phone_number_nohyphen = phone_number.replace(\"-\",\"\")\n",
    "print(phone_number_nohyphen)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['http://sharebook', 'kr']\n",
      "<class 'list'>\n",
      "kr\n"
     ]
    }
   ],
   "source": [
    "# 027 문자열 다루기\n",
    "# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.\n",
    "\n",
    "# >> url = \"http://sharebook.kr\"\n",
    "# 실행 예:\n",
    "# kr\n",
    "\n",
    "url = \"http://sharebook.kr\"\n",
    "url_split = url.split('.')\n",
    "print(url_split)\n",
    "print(type(url_split))\n",
    "print(url_split[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'str' object does not support item assignment",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m~\\AppData\\Local\\Temp/ipykernel_7332/4062305123.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      8\u001b[0m \u001b[0mlang\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'python'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 9\u001b[1;33m \u001b[0mlang\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m'P'\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     10\u001b[0m \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mlang\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: 'str' object does not support item assignment"
     ]
    }
   ],
   "source": [
    "# 028 문자열은 immutable\n",
    "# 아래 코드의 실행 결과를 예상해보세요.\n",
    "\n",
    "# >> lang = 'python'\n",
    "# >> lang[0] = 'P'\n",
    "# >> print(lang)\n",
    "\n",
    "lang = 'python'\n",
    "lang[0] = 'P'\n",
    "print(lang)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Abcdfe2A354A32A\n"
     ]
    }
   ],
   "source": [
    "# 029 replace 메서드\n",
    "# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.\n",
    "\n",
    "# >> string = 'abcdfe2a354a32a'\n",
    "# 실행 예:\n",
    "# Abcdfe2A354A32A\n",
    "\n",
    "string = 'abcdfe2a354a32a'\n",
    "string_replace = string.replace(\"a\",\"A\")\n",
    "print(string_replace)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "abcd\n"
     ]
    }
   ],
   "source": [
    "# 030 replace 메서드\n",
    "# 아래 코드의 실행 결과를 예상해보세요.\n",
    "\n",
    "# >> string = 'abcd'\n",
    "# >> string.replace('b', 'B')\n",
    "# >> print(string)\n",
    "\n",
    "string = 'abcd'\n",
    "string.replace('b', 'B')\n",
    "print(string)\n",
    "\n",
    "#abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "34\n"
     ]
    }
   ],
   "source": [
    "# 031 문자열 합치기\n",
    "# 아래 코드의 실행 결과를 예상해보세요.\n",
    "\n",
    "# >> a = \"3\"\n",
    "# >> b = \"4\"\n",
    "# >> print(a + b)\n",
    "\n",
    "a = \"3\"\n",
    "b = \"4\"\n",
    "print(a + b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HiHiHi\n"
     ]
    }
   ],
   "source": [
    "# 032 문자열 곱하기\n",
    "# 아래 코드의 실행 결과를 예상해보세요.\n",
    "\n",
    "# >> print(\"Hi\" * 3)\n",
    "\n",
    "print(\"Hi\" * 3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "--------------------------------------------------------------------------------\n"
     ]
    }
   ],
   "source": [
    "# 033 문자열 곱하기\n",
    "# 화면에 '-'를 80개 출력하세요.\n",
    "\n",
    "# 실행 예:\n",
    "# --------------------------------------------------------------------------------\n",
    "\n",
    "hyphen = \"-\"\n",
    "hyphen_80 = hyphen*80\n",
    "print(hyphen_80)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "python java python java python java python java \n"
     ]
    }
   ],
   "source": [
    "# 034 문자열 곱하기\n",
    "# 변수에 다음과 같은 문자열이 바인딩되어 있습니다.\n",
    "\n",
    "# >>> t1 = 'python'\n",
    "# >>> t2 = 'java'\n",
    "\n",
    "t1 = 'python'\n",
    "t2 = 'java'\n",
    "t1t2 = t1 + \" \" + t2 + \" \"\n",
    "print(t1t2*4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름: 김민수 나이: 10\n",
      "이름: 이철희 나이: 13\n"
     ]
    }
   ],
   "source": [
    "# 035 문자열 출력\n",
    "# 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.\n",
    "\n",
    "# name1 = \"김민수\" \n",
    "# age1 = 10\n",
    "# name2 = \"이철희\"\n",
    "# age2 = 13\n",
    "# 이름: 김민수 나이: 10\n",
    "# 이름: 이철희 나이: 13\n",
    "\n",
    "name1 = \"김민수\" \n",
    "age1 = 10\n",
    "name2 = \"이철희\"\n",
    "age2 = 13\n",
    "\n",
    "print(\"이름: %s 나이: %d\" %(name1, age1))\n",
    "print(\"이름: %s 나이: %d\" %(name2, age2))\n",
    "\n",
    "# print 포맷팅에서 %s는 문자열 데이터 타입의 값을 %d는 정수형 데이터 타입 값의 출력을 의미합니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름: 김민수 나이: 10\n",
      "이름: 이철희 나이: 13\n"
     ]
    }
   ],
   "source": [
    "# 036 문자열 출력\n",
    "# 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.\n",
    "\n",
    "name1 = \"김민수\" \n",
    "age1 = 10\n",
    "name2 = \"이철희\"\n",
    "age2 = 13\n",
    "print(\"이름: {} 나이: {}\".format(name1, age1))\n",
    "print(\"이름: {} 나이: {}\".format(name2, age2))\n",
    "\n",
    "문자열의 포맷 메서드는 타입과 상관없이 값이 출력될 위치에 { }를 적어주면 됩니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "이름: 김민수 나이: 10\n",
      "이름: 이철희 나이: 13\n"
     ]
    }
   ],
   "source": [
    "# 037 문자열 출력\n",
    "# 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.\n",
    "\n",
    "name1 = \"김민수\" \n",
    "age1 = 10\n",
    "name2 = \"이철희\"\n",
    "age2 = 13\n",
    "print(f\"이름: {name1} 나이: {age1}\")\n",
    "print(f\"이름: {name2} 나이: {age2}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n"
     ]
    }
   ],
   "source": [
    "# 038 컴마 제거하기\n",
    "# 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.\n",
    "\n",
    "# 상장주식수 = \"5,969,782,550\"\n",
    "\n",
    "상장주식수 = \"5,969,782,550\"\n",
    "상장주식주_str = 상장주식수.replace(\",\",\"\")\n",
    "상장주식주_int = int(상장주식주_str)\n",
    "print(type(상장주식주_int))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2020/03\n"
     ]
    }
   ],
   "source": [
    "# 039 문자열 슬라이싱\n",
    "# 다음과 같은 문자열에서 '2020/03'만 출력하세요.\n",
    "\n",
    "# 분기 = \"2020/03(E) (IFRS연결)\"\n",
    "\n",
    "분기 = \"2020/03(E) (IFRS연결)\"\n",
    "print(분기[:7])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "삼성전자\n"
     ]
    }
   ],
   "source": [
    "# 040 strip 메서드\n",
    "# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.\n",
    "\n",
    "# data = \"   삼성전자    \"\n",
    "\n",
    "data = \"   삼성전자    \"\n",
    "trim_data = data.strip()\n",
    "print(trim_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "BTC_KRW\n"
     ]
    }
   ],
   "source": [
    "# 041 upper 메서드\n",
    "# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.\n",
    "\n",
    "# ticker = \"btc_krw\"\n",
    "\n",
    "ticker = \"btc_krw\"\n",
    "upper_ticker = ticker.upper()\n",
    "print(upper_ticker)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "btc_krw\n"
     ]
    }
   ],
   "source": [
    "# 042 lower 메서드\n",
    "# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.\n",
    "\n",
    "# ticker = \"BTC_KRW\"\n",
    "\n",
    "ticker = \"BTC_KRW\"\n",
    "lower_ticker = ticker.lower()\n",
    "print(lower_ticker)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "HELLO\n"
     ]
    }
   ],
   "source": [
    "# 043 capitalize 메서드\n",
    "# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.\n",
    "\n",
    "str = \"hello\"\n",
    "upper_str = str.upper()\n",
    "print(upper_str)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 044 endswith 메서드\n",
    "# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.\n",
    "\n",
    "# file_name = \"보고서.xlsx\"\n",
    "\n",
    "file_name = \"보고서.xlsx\"\n",
    "file_name.endswith(\"xlsx\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 84,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 045 endswith 메서드\n",
    "# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.\n",
    "\n",
    "# file_name = \"보고서.xlsx\"\n",
    "\n",
    "file_name = \"보고서.xlsx\"\n",
    "file_name.endswith((\"xlsx\",\"xls\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 85,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 046 startswith 메서드\n",
    "# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.\n",
    "\n",
    "# file_name = \"2020_보고서.xlsx\"\n",
    "\n",
    "file_name = \"2020_보고서.xlsx\"\n",
    "file_name.startswith(\"2020\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['hello', 'world']"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 047 split 메서드\n",
    "# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.\n",
    "\n",
    "# a = \"hello world\"\n",
    "\n",
    "a = \"hello world\"\n",
    "a.split(\" \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['btc', 'krw']"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 048 split 메서드\n",
    "# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.\n",
    "\n",
    "# ticker = \"btc_krw\"\n",
    "\n",
    "ticker = \"btc_krw\"\n",
    "ticker.split(\"_\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "039490\n"
     ]
    }
   ],
   "source": [
    "# 050 rstrip 메서드\n",
    "# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.\n",
    "\n",
    "# data = \"039490     \"\n",
    "\n",
    "data = \"039490     \"\n",
    "data_rtrim = data.rstrip()\n",
    "print(data_rtrim)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['닥터 스트레인지', '스플릿', '럭키']\n",
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "# 051 리스트 생성\n",
    "# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다. 영화 제목을 movie_rank 이름의 리스트에 저장해보세요. (순위 정보는 저장하지 않습니다.)\n",
    "\n",
    "# 순위\t영화\n",
    "# 1\t닥터 스트레인지\n",
    "# 2\t스플릿\n",
    "# 3\t럭키\n",
    "\n",
    "movie_rank = [\"닥터 스트레인지\", \"스플릿\", \"럭키\"]\n",
    "print(movie_rank)\n",
    "print(type(movie_rank))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['닥터 스트레인지', '스플릿', '럭키', '배트맨']\n"
     ]
    }
   ],
   "source": [
    "# 052 리스트에 원소 추가\n",
    "# 051의 movie_rank 리스트에 \"배트맨\"을 추가하라.\n",
    "\n",
    "movie_rank = [\"닥터 스트레인지\", \"스플릿\", \"럭키\"]\n",
    "movie_rank.append(\"배트맨\")\n",
    "print(movie_rank)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']\n"
     ]
    }
   ],
   "source": [
    "# 053\n",
    "# movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다. \"슈퍼맨\"을 \"닥터 스트레인지\"와 \"스플릿\" 사이에 추가하라.\n",
    "\n",
    "# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']\n",
    "\n",
    "movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']\n",
    "movie_rank.insert(1,\"슈퍼맨\")\n",
    "print(movie_rank)\n",
    "\n",
    "# 리스트의 insert(인덱스, 원소) 메서드를 사용하면 특정 위치에 값을 끼어넣기 할 수 있습니다."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']\n"
     ]
    }
   ],
   "source": [
    "# 054\n",
    "# movie_rank 리스트에서 '럭키'를 삭제하라.\n",
    "\n",
    "# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']\n",
    "\n",
    "movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']\n",
    "del movie_rank[3]\n",
    "print(movie_rank)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
