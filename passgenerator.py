{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "96ab7eda-e993-45fa-b32e-d2e0fad9726c",
   "metadata": {},
   "outputs": [],
   "source": [
    "letters = [\n",
    "    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',\n",
    "    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',\n",
    "    'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',\n",
    "    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',\n",
    "    'U', 'V', 'W', 'X', 'Y', 'Z'\n",
    "]\n",
    "\n",
    "# Numbers\n",
    "numbers = [\n",
    "    '0', '1', '2', '3', '4',\n",
    "    '5', '6', '7', '8', '9'\n",
    "]\n",
    "\n",
    "# Symbols\n",
    "symbols = [\n",
    "    '!', '@', '#', '$', '%', '^', '&', '*',\n",
    "    '(', ')', '-', '_', '=', '+', '[', ']',\n",
    "    '{', '}', '\\\\', '|', ';', ':', \"'\", '\"',\n",
    "    ',', '.', '<', '>', '/', '?', '`', '~'\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "26d23de5-662b-4a30-ae80-f3abdb6b5e8d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "welcome to password generator\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "how many letter would you like to be in you password?\n",
      " 3\n",
      "how many number would you like to be in you password?\n",
      " 2\n",
      "how many symbols would you like to be in you password?\n",
      " 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ruOf95\"\n"
     ]
    }
   ],
   "source": [
    "print('welcome to password generator')\n",
    "nr_letter=int(input('how many letter would you like to be in you password?\\n'))\n",
    "nr_number=int(input('how many number would you like to be in you password?\\n'))\n",
    "nr_symbols=int(input('how many symbols would you like to be in you password?\\n'))\n",
    "\n",
    "password=''\n",
    "for char in range(0,nr_letter):\n",
    "    password += random.choice(letters)\n",
    "password+=random_char\n",
    "for n in range(0,nr_number):\n",
    "    password += random.choice(numbers)\n",
    "for s in range(0,nr_symbols):\n",
    "    password += random.choice(symbols)\n",
    "print(password)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "abf0945f-65db-4125-818c-32ad40f31744",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "welcome to password generator\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "how many letter would you like to be in you password?\n",
      " 3\n",
      "how many number would you like to be in you password?\n",
      " 4\n",
      "how many symbols would you like to be in you password?\n",
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['o', 'Q', 'u', '5', '8', '9', '5', '_', '-', '<']\n",
      "['9', 'u', '5', '5', '8', '-', '_', '<', 'Q', 'o']\n",
      "9u558-_<Qo\n",
      "your passord is 9u558-_<Qo\n"
     ]
    }
   ],
   "source": [
    "#hard level\n",
    "print('welcome to password generator')\n",
    "nr_letter=int(input('how many letter would you like to be in you password?\\n'))\n",
    "nr_number=int(input('how many number would you like to be in you password?\\n'))\n",
    "nr_symbols=int(input('how many symbols would you like to be in you password?\\n'))\n",
    "\n",
    "password_list=[]\n",
    "for char in range(0,nr_letter):\n",
    "    password_list.append(random.choice(letters))\n",
    "password+=random_char\n",
    "for n in range(0,nr_number):\n",
    "    password_list.append(random.choice(numbers))\n",
    "for s in range(0,nr_symbols):\n",
    "    password_list.append(random.choice(symbols))\n",
    "print(password_list)\n",
    "random.shuffle(password_list)\n",
    "print(password_list)\n",
    "password=''\n",
    "for char in password_list:\n",
    "    password+=char\n",
    "print(f'your passord is {password}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9269a16-9e9e-4475-8c50-8a47cf3caab8",
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
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
