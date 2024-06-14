import socket
from threading import Thread
import random

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.2"
port = 7000

server.bind((ip_address, port))
server.listen()

list_of_clients = []

question = [
    "What is the Italian word for PIE? \n a. Mozarella\n b. Pasty\n c. Patty\n d. Pizza",

    "Water boils at 212 Units at which scale? \n a. Fahrenheit \n b. Celsius\n c. Rankine \n d. Kelvin",

    "Which sea creature has three hearts?\n a. Dolphin b. Octopus\n c. Walrus\n d.Seal",

    "Who was the character famous in our childhood rhymes assoiated with a lamb? \n a. Mary \n b. Jack \n c. Johnny d. Mukesh"

    "How many wonders are there in the world? \n a. 7 \n b. 8 \n c. 10 \n d. 4"

]

answer = [ "d", "a", "b", "a", "a", "a", "a", "b", "a", "c", "b", "d", "d", "c", "a", "b", "a"]




def clientthread(conn):
    score = 0
    conn.send("Welcome to this quiz game!".encode('utf-8'))
    conn.send("You will receive a question should be one of a, b, c, d")
    conn.send("Good Luck!\n\n". encode('utf-8'))

    index, question, answer = get_randon_question_answer(conn)
    while True:
        try: 
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == answer:
                    score+=1
                    conn.send(f"Brave! Your score is {score}\n\n".encode('utf-8'))

                else: 
                    conn.send("Incorrect answer! Better luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else: 
                remove(conn)

        except:
            continue

while True:
    conn, = server.accept()
    list_of_clients.append(conn)
    new_thread = Thread(target= clientthread,args=(conn))
    new_thread.start()