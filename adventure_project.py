{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9ab6bfce-2449-4560-8c03-3fd2858e639d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "welocome to treasure island. your mission is to find the treasure\n"
     ]
    }
   ],
   "source": [
    "print('welocome to treasure island. your mission is to find the treasure')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1c24e155-9958-4e10-8fa5-9b3b8bcfa0b8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "where you want to go left or right?choose \"Left\" or \"Right left\n",
      "where you want to swim or wait?choose \"swim\" or \"wait\" swim\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "you are attacked by angry trout.game over\n"
     ]
    }
   ],
   "source": [
    "choice1=input('where you want to go left or right?choose \"Left\" or \"Right').lower()\n",
    "if choice1=='left':\n",
    "    choice2=input('where you want to swim or wait?choose \"swim\" or \"wait\"').lower()\n",
    "    if choice2=='wait':\n",
    "        choice3=input('from which door you want to enter?\"Red\" or \"blue\" or \"yellow?\"').lower()\n",
    "        if choice3=='yellow':\n",
    "                print('congrats! you find the treasure..')\n",
    "        elif choice3=='Blue':\n",
    "                print('you enter room of beasts...game over')\n",
    "        elif choice3=='Red':\n",
    "                print('you enter in a room full of fire.. game over')\n",
    "        else:\n",
    "                print('you chose wrong door')\n",
    "    else:\n",
    "        print('you are attacked by angry trout.game over')\n",
    "else:\n",
    "    print('you choose wrong way...game over')                              "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46657bc6-4ad7-40bd-8fef-2076d5a2e635",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n"
   ]
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
