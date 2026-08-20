{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "f9a36081-8d06-4b57-979f-0e9855c9e95b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['abbas', 'ali', 'saif', 'sajeel', 'ahsan']"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "friends=['abbas','ali','saif','sajeel','ahsan']\n",
    "friends"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "dd521800-d335-4d89-a613-f937c0109e60",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ahsan will pay the bill\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "bill = random.choice(friends)\n",
    "print(f'{bill} will pay the bill')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "5f73afcd-fca5-4433-9c71-7b6e836ca8a7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#2nd option"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "76f0cc3f-a4db-401d-90d9-e6f5af9dde67",
   "metadata": {},
   "outputs": [],
   "source": [
    "random_number=random.randint(0,4)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "8fc131e9-85cb-4b53-b541-11469a29f214",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ali\n"
     ]
    }
   ],
   "source": [
    "print(friends[random_number])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "589c9787-7ee1-4ec1-8af0-d1373da14d58",
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
